#!/usr/bin/env python3
"""Canonical VTL Kernel Metrics extractor.

This script mirrors the current notebook device math closely enough to serve as
the skill's local runner. It is deterministic for the same image bytes,
dependencies, and constants.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import cv2
import numpy as np
import pandas as pd
from scipy.ndimage import distance_transform_edt
from scipy.spatial import ConvexHull
from skimage.measure import label
from skimage.morphology import skeletonize


TARGET_MAX_SIDE = 1536
GRAD_LOW_PCT = 85.0
GRAD_HIGH_PCT = 97.0
EDGE_MARGIN_PX = 2
MIN_MASS_FRAC = 0.001
WARN_MASS_FRAC = 0.03
R_V_ABSOLUTE_THRESHOLD = 0.15
ORIENT_BINS = 8
EPS = 1e-9
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
SCRIPT_VERSION = "vtl-kernel-extractor-2026-04-19"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def image_paths(inputs: Iterable[str]) -> List[Path]:
    paths: List[Path] = []
    for item in inputs:
        p = Path(item).expanduser()
        if p.is_dir():
            for child in sorted(p.rglob("*")):
                if child.suffix.lower() in IMAGE_EXTS:
                    paths.append(child)
        elif p.is_file() and p.suffix.lower() in IMAGE_EXTS:
            paths.append(p)
        else:
            raise FileNotFoundError(f"Not an image file or folder: {item}")
    return sorted(dict.fromkeys(paths))


def decode_image_bgr(image_bytes: bytes) -> np.ndarray:
    arr = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Failed to decode image bytes.")
    return img


def resize_max_side(img_bgr: np.ndarray, max_side: int = TARGET_MAX_SIDE) -> np.ndarray:
    h, w = img_bgr.shape[:2]
    side = max(h, w)
    if side == max_side:
        return img_bgr
    scale = max_side / float(side)
    new_w = int(round(w * scale))
    new_h = int(round(h * scale))
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_CUBIC
    return cv2.resize(img_bgr, (new_w, new_h), interpolation=interp)


def standardize_image(path: Path) -> Tuple[np.ndarray, Dict]:
    data = path.read_bytes()
    img = decode_image_bgr(data)
    img = resize_max_side(img)
    return img, {
        "path": str(path),
        "filename": path.name,
        "sha256": sha256_bytes(data),
        "h": int(img.shape[0]),
        "w": int(img.shape[1]),
        "max_side": TARGET_MAX_SIDE,
    }


def bgr_to_gray_float(img_bgr: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0


def sobel_gradients(gray: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    gmag = np.sqrt(gx * gx + gy * gy)
    return gx, gy, gmag


def robust_threshold_mask(gmag: np.ndarray) -> np.ndarray:
    h, w = gmag.shape
    inner = gmag[EDGE_MARGIN_PX : h - EDGE_MARGIN_PX, EDGE_MARGIN_PX : w - EDGE_MARGIN_PX]
    flat = inner.reshape(-1)
    t_low = np.percentile(flat, GRAD_LOW_PCT)
    t_high = np.percentile(flat, GRAD_HIGH_PCT)
    mask = (gmag >= t_low) & (gmag <= t_high)
    if EDGE_MARGIN_PX > 0:
        mask[:EDGE_MARGIN_PX, :] = False
        mask[-EDGE_MARGIN_PX:, :] = False
        mask[:, :EDGE_MARGIN_PX] = False
        mask[:, -EDGE_MARGIN_PX:] = False
    return mask.astype(np.uint8)


def metric_delta_x(mass_mask: np.ndarray) -> float:
    _, xs = np.nonzero(mass_mask)
    if len(xs) == 0:
        return 0.0
    h, w = mass_mask.shape
    return float((xs.mean() - ((w - 1) / 2.0)) / float(w))


def metric_delta_y(mass_mask: np.ndarray) -> float:
    ys, _ = np.nonzero(mass_mask)
    if len(ys) == 0:
        return 0.0
    h, _ = mass_mask.shape
    return float((ys.mean() - ((h - 1) / 2.0)) / float(h))


def metric_mass_fraction(mass_mask: np.ndarray) -> float:
    h, w = mass_mask.shape
    return float(mass_mask.sum() / float(h * w))


def metric_r_v(gmag: np.ndarray) -> float:
    coverage = float((gmag >= R_V_ABSOLUTE_THRESHOLD).sum() / gmag.size)
    return float(1.0 - coverage)


def metric_rho_r(mass_mask: np.ndarray) -> float:
    ys, xs = np.nonzero(mass_mask)
    if len(xs) < 3:
        return 0.0
    pts = np.stack([xs, ys], axis=1).astype(np.float64)
    try:
        hull = ConvexHull(pts)
    except Exception:
        return 0.0
    return float(100.0 * (float(len(xs)) / (float(hull.volume) + EPS)))


def metric_mu(mass_mask: np.ndarray) -> float:
    lab = label(mass_mask > 0, connectivity=2)
    num_components = int(lab.max())
    if num_components == 0:
        return 0.0
    if num_components == 1:
        return 1.0
    areas = np.array([int(np.sum(lab == i)) for i in range(1, num_components + 1)], dtype=np.float64)
    p_i = areas / (areas.sum() + EPS)
    p_max = float(p_i.max())
    h_entropy = float(-sum(p * np.log2(p) for p in p_i if p > 0))
    h_max = float(np.log2(num_components))
    if h_max == 0:
        return p_max
    return float(p_max * (1.0 - h_entropy / h_max))


def metric_x_p(gmag: np.ndarray) -> float:
    h, w = gmag.shape
    edge_width = 0.15
    x_left = int(w * edge_width)
    x_right = int(w * (1.0 - edge_width))
    y_top = int(h * edge_width)
    y_bottom = int(h * (1.0 - edge_width))
    edge_mask = np.zeros((h, w), dtype=bool)
    edge_mask[:y_top, :] = True
    edge_mask[y_bottom:, :] = True
    edge_mask[:, :x_left] = True
    edge_mask[:, x_right:] = True
    total = float(gmag.sum())
    if total == 0:
        return 0.0
    return float(gmag[edge_mask].sum() / total)


def metric_theta(gx: np.ndarray, gy: np.ndarray, gmag: np.ndarray, mass_mask: np.ndarray) -> float:
    mask_bool = mass_mask > 0
    gx_m = gx[mask_bool]
    gy_m = gy[mask_bool]
    gm_m = gmag[mask_bool]
    if len(gx_m) == 0 or gm_m.sum() == 0:
        return 0.0
    orientations = np.arctan2(gy_m, gx_m) + np.pi
    bin_width = 2.0 * np.pi / ORIENT_BINS
    bin_indices = np.clip(np.floor(orientations / bin_width).astype(int), 0, ORIENT_BINS - 1)
    weights = np.zeros(ORIENT_BINS, dtype=np.float64)
    for idx, weight in zip(bin_indices, gm_m):
        weights[idx] += weight
    total = weights.sum()
    if total == 0:
        return 0.0
    probs = weights / total
    h_entropy = float(-sum(p * np.log2(p) for p in probs if p > 0))
    h_max = float(np.log2(ORIENT_BINS))
    return float(1.0 - (h_entropy / h_max))


def metric_d_s(mass_mask: np.ndarray) -> float:
    if mass_mask.sum() == 0:
        return 0.0
    mask = mass_mask > 0
    dt = distance_transform_edt(mask)
    sk = skeletonize(mask).astype(np.uint8)
    ys, xs = np.nonzero(sk)
    if len(xs) == 0:
        return 0.0
    thick = 2.0 * dt[ys, xs]
    return float(thick.mean() / (float(min(mass_mask.shape)) + EPS))


def metric_sdi(mass_mask: np.ndarray) -> float:
    ys, xs = np.nonzero(mass_mask)
    if len(xs) == 0:
        return 0.0
    cx = xs.mean()
    cy = ys.mean()
    distances = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    diag = np.sqrt(mass_mask.shape[0] ** 2 + mass_mask.shape[1] ** 2)
    return float(distances.mean() / diag)


def mask_sha256(mask: np.ndarray) -> str:
    mb = np.ascontiguousarray((mask > 0).astype(np.uint8))
    return hashlib.sha256(mb.tobytes()).hexdigest()


def mask_qa(mask: np.ndarray) -> Dict:
    m = mask > 0
    mass_fraction = float(m.mean())
    status = "PASS"
    reasons: List[str] = []
    if mass_fraction < MIN_MASS_FRAC:
        status = "FAIL"
        reasons.append(f"mass_fraction<{MIN_MASS_FRAC:g} (too little structure)")
    elif mass_fraction < WARN_MASS_FRAC:
        status = "WARN"
        reasons.append(f"mass_fraction<{WARN_MASS_FRAC:g} (weak signal / sparse mask)")
    if mass_fraction > 0.85:
        if status == "PASS":
            status = "FAIL"
        reasons.append("mass_fraction>0.85 (too much structure / edge-snow risk)")
    lab = label(m, connectivity=1)
    n_components = int(lab.max())
    if n_components == 0:
        status = "FAIL"
        largest_frac = 0.0
        reasons.append("no connected components")
    else:
        counts = np.bincount(lab.ravel())[1:]
        largest = int(counts.max()) if counts.size else 0
        largest_frac = float(largest / max(int(m.sum()), 1))
        if n_components > 2000 and largest_frac < 0.05:
            if status == "PASS":
                status = "WARN"
            reasons.append("many components + tiny largest component (island soup)")
        if n_components > 10000:
            if status == "PASS":
                status = "WARN"
            reasons.append("extremely high component count (likely texture-driven)")
    if status == "FAIL":
        mode = "INVALID"
    elif largest_frac >= 0.25:
        mode = "REGION_FIELD"
    else:
        mode = "TEXTURE_FIELD"
    return {
        "mass_fraction": mass_fraction,
        "n_components": n_components,
        "largest_component_fraction": largest_frac,
        "mask_sha256": mask_sha256(m),
        "mask_status": status,
        "mask_mode": mode,
        "mask_reasons": "; ".join(reasons),
    }


def kernel_vec_sha256(metrics: Dict) -> str:
    keys = ["delta_x", "r_v", "rho_r", "mu", "x_p", "theta", "d_s", "sdi", "mass_fraction"]
    vec = [float(metrics.get(k, 0.0)) for k in keys]
    data = json.dumps(vec, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def compute(path: Path) -> Dict:
    img, meta = standardize_image(path)
    gray = bgr_to_gray_float(img)
    gx, gy, gmag = sobel_gradients(gray)
    mass_mask = robust_threshold_mask(gmag)
    mass_frac = metric_mass_fraction(mass_mask)
    gradient_floor_85 = float(np.percentile(gmag.flatten(), 85.0))
    gradient_ceiling_97 = float(np.percentile(gmag.flatten(), 97.0))
    base = {
        **meta,
        "script_version": SCRIPT_VERSION,
        "target_max_side": TARGET_MAX_SIDE,
        "grad_low_pct": GRAD_LOW_PCT,
        "grad_high_pct": GRAD_HIGH_PCT,
        "edge_margin_px": EDGE_MARGIN_PX,
        "r_v_threshold": R_V_ABSOLUTE_THRESHOLD,
        "gradient_floor_85": gradient_floor_85,
        "gradient_ceiling_97": gradient_ceiling_97,
        "tail_gap": gradient_ceiling_97 - gradient_floor_85,
        "efa": gradient_floor_85,
    }
    if mass_frac < MIN_MASS_FRAC:
        metrics = {
            "delta_x": 0.0,
            "delta_y": 0.0,
            "r_v": metric_r_v(gmag),
            "rho_r": 0.0,
            "mu": 0.0,
            "x_p": 0.0,
            "theta": 0.0,
            "d_s": 0.0,
            "sdi": 0.0,
            "mass_fraction": mass_frac,
            "valid": 0,
            "quality_note": f"mass_fraction={mass_frac:.6f} < MIN_MASS_FRAC={MIN_MASS_FRAC:.6f}",
        }
    else:
        metrics = {
            "delta_x": metric_delta_x(mass_mask),
            "delta_y": metric_delta_y(mass_mask),
            "r_v": metric_r_v(gmag),
            "rho_r": metric_rho_r(mass_mask),
            "mu": metric_mu(mass_mask),
            "x_p": metric_x_p(gmag),
            "theta": metric_theta(gx, gy, gmag, mass_mask),
            "d_s": metric_d_s(mass_mask),
            "sdi": metric_sdi(mass_mask),
            "mass_fraction": mass_frac,
            "valid": 1,
            "quality_note": "",
        }
        if mass_frac < WARN_MASS_FRAC:
            metrics["quality_note"] = (
                f"mass_fraction={mass_frac:.4f} in low-structure band "
                f"({MIN_MASS_FRAC:.3f}-{WARN_MASS_FRAC:.3f}); treat as low-confidence."
            )
    qa = mask_qa(mass_mask)
    row = {**base, **metrics, **qa}
    row["kernel_vec_sha256"] = kernel_vec_sha256(row)
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract canonical VTL kernel metrics from images.")
    parser.add_argument("inputs", nargs="+", help="Image file(s) or folder(s).")
    parser.add_argument("--out-dir", default="/tmp/vtl_kernel_output", help="Output directory.")
    args = parser.parse_args()
    paths = image_paths(args.inputs)
    if not paths:
        raise SystemExit("No image files found.")
    out_dir = Path(args.out_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in paths:
        try:
            rows.append(compute(path))
        except Exception as exc:
            rows.append({
                "path": str(path),
                "filename": path.name,
                "script_version": SCRIPT_VERSION,
                "valid": 0,
                "mask_status": "FAIL",
                "mask_mode": "INVALID",
                "quality_note": repr(exc),
                "error": repr(exc),
            })
    df = pd.DataFrame(rows)
    csv_path = out_dir / "kernel_metrics.csv"
    json_path = out_dir / "kernel_metrics.json"
    df.to_csv(csv_path, index=False)
    json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"Wrote {csv_path}")
    print(f"Wrote {json_path}")
    print(df[[c for c in ["filename", "delta_x", "delta_y", "r_v", "rho_r", "mu", "x_p", "theta", "d_s", "sdi", "tail_gap", "mask_status", "mask_mode"] if c in df.columns]].to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

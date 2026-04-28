#!/usr/bin/env python3
"""Proof Loop v3: end-to-end structural comparison from image files.

This helper:
1) measures baseline and variant images with the canonical Mass Over Semantics kernel
2) compares their vectors
3) tests for significant movement
4) checks for likely false improvement / default retreat
5) returns a proof verdict and a logging-ready row

It prefers the bundled canonical extractor if available:
- /mnt/data/mos_kernel_metrics.py

Example:
python proof_loop_v3.py \
  --baseline before.png \
  --variant after.png \
  --intervention "added active void + off-center mass" \
  --one-variable-only \
  --comparison-id test_01
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
from pathlib import Path
from typing import Any

KERNEL_KEYS = [
    "delta_x",
    "delta_y",
    "r_v",
    "rho_r",
    "mu",
    "x_p",
    "theta",
    "d_s",
    "sdi",
    "mass_fraction",
]

DEFAULT_TOLERANCES = {
    "delta_x": 0.015,
    "delta_y": 0.015,
    "r_v": 0.020,
    "rho_r": 2.0,     # MOS commonly uses 0-100 scale here
    "mu": 0.050,
    "x_p": 0.030,
    "theta": 0.050,
    "d_s": 0.005,
    "sdi": 0.010,
    "mass_fraction": 0.010,
}

PIPELINE_NAME = "mass-over-semantics-canonical"

def load_mos_module(path: Path):
    spec = importlib.util.spec_from_file_location("mos_kernel_metrics", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load canonical MOS extractor from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_float(d: dict[str, Any], key: str) -> float | None:
    value = d.get(key)
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return None

def kernel_validity(d: dict[str, Any]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    valid = d.get("valid", 1)
    mask_status = str(d.get("mask_status", "PASS"))
    mass_fraction = get_float(d, "mass_fraction")

    if valid in (0, False):
        reasons.append("valid=0")
    if mask_status == "FAIL":
        reasons.append("mask_status=FAIL")
    if mass_fraction is not None and mass_fraction < 0.001:
        reasons.append("mass_fraction<0.001")

    return (len(reasons) == 0, reasons or ["ok"])

def compute_deltas(base: dict[str, Any], var: dict[str, Any]) -> dict[str, float]:
    out = {}
    for key in KERNEL_KEYS:
        b = get_float(base, key)
        v = get_float(var, key)
        if b is None or v is None:
            continue
        out[key] = v - b
    return out

def significant_moves(deltas: dict[str, float]) -> dict[str, bool]:
    out = {}
    for key, delta in deltas.items():
        tol = DEFAULT_TOLERANCES.get(key, 0.0)
        out[key] = abs(delta) >= tol
    return out

def detect_default_retreat(base: dict[str, Any], var: dict[str, Any]) -> list[str]:
    flags = []

    b_dx = abs(get_float(base, "delta_x") or 0.0)
    v_dx = abs(get_float(var, "delta_x") or 0.0)

    b_rv = get_float(base, "r_v")
    v_rv = get_float(var, "r_v")

    b_theta = get_float(base, "theta")
    v_theta = get_float(var, "theta")

    b_mu = get_float(base, "mu")
    v_mu = get_float(var, "mu")

    b_xp = get_float(base, "x_p")
    v_xp = get_float(var, "x_p")

    if v_dx < b_dx - 0.01:
        flags.append("recentered mass")

    if b_rv is not None and v_rv is not None and v_rv < b_rv - 0.03:
        flags.append("void collapsed")

    if b_theta is not None and v_theta is not None and v_theta < b_theta - 0.08:
        flags.append("direction weakened")

    if b_xp is not None and v_xp is not None and v_xp < b_xp - 0.05:
        flags.append("edge pull weakened")

    if b_mu is not None and v_mu is not None and v_mu > b_mu + 0.10 and v_dx < b_dx:
        flags.append("cleaner but safer cohesion")

    return flags

def structural_consequence(sig_moves: dict[str, bool], retreat_flags: list[str]) -> tuple[bool, list[str]]:
    changed = [k for k, v in sig_moves.items() if v]
    reasons: list[str] = []

    if not changed:
        reasons.append("no metric moved beyond tolerance")
        return False, reasons

    if retreat_flags:
        reasons.extend(retreat_flags)
        return False, reasons

    reasons.append("significant movement in: " + ", ".join(changed))
    return True, reasons

def choose_verdict(
    base: dict[str, Any],
    var: dict[str, Any],
    intervention: str,
    one_variable_only: bool,
    deltas: dict[str, float],
    sig: dict[str, bool],
    retreat_flags: list[str],
) -> tuple[str, str, list[str], list[str]]:
    base_ok, base_validity = kernel_validity(base)
    var_ok, var_validity = kernel_validity(var)

    if not base_ok or not var_ok:
        reasons = []
        if not base_ok:
            reasons.append("baseline invalid")
        if not var_ok:
            reasons.append("variant invalid")
        return "unscorable", "weak", base_validity, var_validity + reasons

    changed = [k for k, v in sig.items() if v]
    consequence_ok, consequence_reasons = structural_consequence(sig, retreat_flags)

    attribution_reasons = []
    attribution_ok = True
    if not intervention.strip():
        attribution_ok = False
        attribution_reasons.append("missing named intervention")
    if not one_variable_only:
        attribution_ok = False
        attribution_reasons.append("multiple variables may have changed")
    if attribution_ok:
        attribution_reasons.append("single intervention declared")

    if not changed:
        return "no-change", "supported", consequence_reasons, attribution_reasons

    if retreat_flags:
        return "false-improvement", "supported", consequence_reasons, attribution_reasons

    if consequence_ok and attribution_ok:
        return "proven-improvement", "supported", consequence_reasons, attribution_reasons

    if consequence_ok and intervention.strip():
        return "partial-improvement", "possible", consequence_reasons, attribution_reasons

    return "cosmetic-change", "possible", consequence_reasons, attribution_reasons

def measure_image(mos_module, image_path: Path) -> dict[str, Any]:
    row, _fields = mos_module.compute_path(image_path)
    return row

def make_log_row(
    comparison_id: str,
    baseline_path: Path,
    variant_path: Path,
    intervention: str,
    base: dict[str, Any],
    var: dict[str, Any],
    deltas: dict[str, float],
    sig: dict[str, bool],
    verdict_name: str,
    confidence: str,
    notes: str,
) -> dict[str, Any]:
    base_ok, _ = kernel_validity(base)
    var_ok, _ = kernel_validity(var)

    return {
        "comparison_id": comparison_id,
        "baseline_image": str(baseline_path),
        "variant_image": str(variant_path),
        "intervention": intervention,
        "pipeline_name": PIPELINE_NAME,
        "baseline_valid": int(base_ok),
        "variant_valid": int(var_ok),
        "dx_delta": deltas.get("delta_x"),
        "dy_delta": deltas.get("delta_y"),
        "rv_delta": deltas.get("r_v"),
        "rr_delta": deltas.get("rho_r"),
        "mu_delta": deltas.get("mu"),
        "xp_delta": deltas.get("x_p"),
        "theta_delta": deltas.get("theta"),
        "ds_delta": deltas.get("d_s"),
        "sdi_delta": deltas.get("sdi"),
        "mass_fraction_delta": deltas.get("mass_fraction"),
        "significant_moves": ",".join([k for k, v in sig.items() if v]),
        "verdict": verdict_name,
        "confidence": confidence,
        "notes": notes,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="Baseline image path")
    parser.add_argument("--variant", required=True, help="Variant image path")
    parser.add_argument("--intervention", required=True, help="Description of the controlled change")
    parser.add_argument("--one-variable-only", action="store_true", help="Assert that only one variable changed")
    parser.add_argument("--comparison-id", default="", help="Optional comparison id")
    parser.add_argument("--notes", default="", help="Optional notes")
    parser.add_argument("--mos-script", default="/mnt/data/mos_kernel_metrics.py", help="Path to canonical MOS extractor")
    parser.add_argument("--out", help="Optional JSON output path")
    parser.add_argument("--log-csv", help="Optional CSV log path to append one row")
    args = parser.parse_args()

    mos_path = Path(args.mos_script)
    if not mos_path.exists():
        raise SystemExit(f"Canonical MOS extractor not found: {mos_path}")

    baseline_path = Path(args.baseline)
    variant_path = Path(args.variant)
    if not baseline_path.exists():
        raise SystemExit(f"Baseline image not found: {baseline_path}")
    if not variant_path.exists():
        raise SystemExit(f"Variant image not found: {variant_path}")

    mos = load_mos_module(mos_path)

    base = measure_image(mos, baseline_path)
    var = measure_image(mos, variant_path)

    deltas = compute_deltas(base, var)
    sig = significant_moves(deltas)
    retreat_flags = detect_default_retreat(base, var)

    verdict_name, confidence, consequence_reasons, attribution_reasons = choose_verdict(
        base=base,
        var=var,
        intervention=args.intervention,
        one_variable_only=args.one_variable_only,
        deltas=deltas,
        sig=sig,
        retreat_flags=retreat_flags,
    )

    base_ok, base_validity = kernel_validity(base)
    var_ok, var_validity = kernel_validity(var)

    payload = {
        "comparison_id": args.comparison_id,
        "intervention": args.intervention,
        "pipeline_name": PIPELINE_NAME,
        "one_variable_only": args.one_variable_only,
        "verdict": verdict_name,
        "confidence": confidence,
        "baseline": {
            "image": str(baseline_path),
            "kernel": {k: base.get(k) for k in KERNEL_KEYS},
            "qa": {
                "valid": int(base_ok),
                "validity_notes": base_validity,
                "mask_status": base.get("mask_status"),
                "mask_mode": base.get("mask_mode"),
                "quality_note": base.get("quality_note", ""),
            },
        },
        "variant": {
            "image": str(variant_path),
            "kernel": {k: var.get(k) for k in KERNEL_KEYS},
            "qa": {
                "valid": int(var_ok),
                "validity_notes": var_validity,
                "mask_status": var.get("mask_status"),
                "mask_mode": var.get("mask_mode"),
                "quality_note": var.get("quality_note", ""),
            },
        },
        "delta": deltas,
        "significant_moves": {k: v for k, v in sig.items()},
        "validation": {
            "structural_consequence": consequence_reasons,
            "default_resistance": retreat_flags or ["no clear retreat detected"],
            "causal_attribution": attribution_reasons,
        },
        "notes": args.notes,
    }

    if args.out:
        Path(args.out).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))

    if args.log_csv:
        row = make_log_row(
            comparison_id=args.comparison_id,
            baseline_path=baseline_path,
            variant_path=variant_path,
            intervention=args.intervention,
            base=base,
            var=var,
            deltas=deltas,
            sig=sig,
            verdict_name=verdict_name,
            confidence=confidence,
            notes=args.notes,
        )
        csv_path = Path(args.log_csv)
        write_header = not csv_path.exists()
        with csv_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(row.keys()))
            if write_header:
                writer.writeheader()
            writer.writerow(row)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

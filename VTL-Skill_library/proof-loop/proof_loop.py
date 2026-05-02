#!/usr/bin/env python3
"""Compare baseline and variant kernel readings and produce a proof-loop verdict.

Input can be either:
1) two JSON files containing kernel dicts, or
2) inline JSON strings with --baseline-json / --variant-json

This helper does not measure images itself. It compares already-produced kernel
reads and asks whether the change is measurable, structurally plausible, and
likely attributable.
"""

from __future__ import annotations

import argparse
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
]

DEFAULT_TOLERANCES = {
    "delta_x": 0.015,
    "delta_y": 0.015,
    "r_v": 0.020,
    "rho_r": 2.0,   # MOS often uses 0-100 style packing density
    "mu": 0.050,
    "x_p": 0.030,
    "theta": 0.050,
    "d_s": 0.005,
    "sdi": 0.010,
}

def load_json_arg(path: str | None, inline: str | None) -> dict[str, Any]:
    if inline:
        return json.loads(inline)
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    raise SystemExit("Provide either a file path or inline JSON.")

def get_float(d: dict[str, Any], key: str) -> float | None:
    value = d.get(key)
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return None

def metric_validity(d: dict[str, Any]) -> tuple[bool, str]:
    valid = d.get("valid", 1)
    mask_status = str(d.get("mask_status", "PASS"))
    mass_fraction = get_float(d, "mass_fraction")
    if valid in (0, False):
        return False, "valid=0"
    if mask_status == "FAIL":
        return False, "mask_status=FAIL"
    if mass_fraction is not None and mass_fraction < 0.001:
        return False, "mass_fraction too low"
    return True, "ok"

def compute_deltas(base: dict[str, Any], var: dict[str, Any]) -> dict[str, float]:
    out = {}
    for key in KERNEL_KEYS:
        b = get_float(base, key)
        v = get_float(var, key)
        if b is None or v is None:
            continue
        out[key] = v - b
    return out

def moved_significantly(deltas: dict[str, float]) -> dict[str, bool]:
    sig = {}
    for key, delta in deltas.items():
        tol = DEFAULT_TOLERANCES.get(key, 0.0)
        sig[key] = abs(delta) >= tol
    return sig

def infer_default_retreat(base: dict[str, Any], var: dict[str, Any]) -> list[str]:
    flags = []
    b_dx = abs(get_float(base, "delta_x") or 0.0)
    v_dx = abs(get_float(var, "delta_x") or 0.0)
    b_rv = get_float(base, "r_v")
    v_rv = get_float(var, "r_v")
    b_theta = get_float(base, "theta")
    v_theta = get_float(var, "theta")
    b_mu = get_float(base, "mu")
    v_mu = get_float(var, "mu")

    if v_dx + 1e-9 < b_dx - 0.01:
        flags.append("recentered mass")
    if b_rv is not None and v_rv is not None and v_rv < b_rv - 0.03:
        flags.append("void collapsed")
    if b_theta is not None and v_theta is not None and v_theta < b_theta - 0.08:
        flags.append("directional field weakened")
    if b_mu is not None and v_mu is not None and v_mu > b_mu + 0.10 and v_dx < b_dx:
        flags.append("possibly cleaner but safer cohesion")
    return flags

def verdict(base: dict[str, Any], var: dict[str, Any], deltas: dict[str, float], intervention: str, one_variable_only: bool) -> tuple[str, str, list[str]]:
    base_ok, base_reason = metric_validity(base)
    var_ok, var_reason = metric_validity(var)
    if not base_ok or not var_ok:
        reasons = []
        if not base_ok:
            reasons.append(f"baseline invalid: {base_reason}")
        if not var_ok:
            reasons.append(f"variant invalid: {var_reason}")
        return "unscorable", "weak", reasons

    sig = moved_significantly(deltas)
    changed = [k for k, v in sig.items() if v]
    default_flags = infer_default_retreat(base, var)

    if not changed:
        return "no-change", "supported", ["no metric moved beyond tolerance"]

    if default_flags:
        return "false-improvement", "supported", default_flags

    if len(changed) >= 2 and one_variable_only and intervention.strip():
        return "proven-improvement", "supported", [f"significant shifts: {', '.join(changed)}"]

    if len(changed) >= 1 and intervention.strip():
        return "partial-improvement", "possible", [f"some significant shifts: {', '.join(changed)}"]

    return "cosmetic-change", "possible", ["change detected but attribution is weak"]

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", help="Path to baseline kernel JSON")
    parser.add_argument("--variant", help="Path to variant kernel JSON")
    parser.add_argument("--baseline-json", help="Inline baseline kernel JSON")
    parser.add_argument("--variant-json", help="Inline variant kernel JSON")
    parser.add_argument("--intervention", default="", help="Description of the one controlled change")
    parser.add_argument("--one-variable-only", action="store_true", help="Assert that only one variable changed")
    parser.add_argument("--out", help="Optional output file path")
    args = parser.parse_args()

    base = load_json_arg(args.baseline, args.baseline_json)
    var = load_json_arg(args.variant, args.variant_json)

    deltas = compute_deltas(base, var)
    v, confidence, reasons = verdict(base, var, deltas, args.intervention, args.one_variable_only)

    payload = {
        "intervention": args.intervention,
        "verdict": v,
        "confidence": confidence,
        "deltas": deltas,
        "baseline_validity": metric_validity(base),
        "variant_validity": metric_validity(var),
        "reasons": reasons,
    }

    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

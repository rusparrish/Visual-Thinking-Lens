#!/usr/bin/env python3
"""Proof Loop v2: compare baseline and variant kernel readings and return a proof verdict.

This helper compares already-produced kernel JSON reads. It is designed to fit
Mass Over Semantics / Mark Making style outputs where fields like valid,
mask_status, mass_fraction, and the standard kernel metrics may be present.

Usage:
  python proof_loop_v2.py --baseline baseline.json --variant variant.json \
    --intervention "added active void clause" --one-variable-only

You can also pass inline JSON strings with --baseline-json / --variant-json.
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
    "mass_fraction",
]

DEFAULT_TOLERANCES = {
    "delta_x": 0.015,
    "delta_y": 0.015,
    "r_v": 0.020,
    "rho_r": 2.0,     # MOS often uses 0-100 packing density
    "mu": 0.050,
    "x_p": 0.030,
    "theta": 0.050,
    "d_s": 0.005,
    "sdi": 0.010,
    "mass_fraction": 0.010,
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

def verdict(base: dict[str, Any], var: dict[str, Any], intervention: str, one_variable_only: bool, pipeline_match: bool) -> dict[str, Any]:
    base_ok, base_validity = kernel_validity(base)
    var_ok, var_validity = kernel_validity(var)
    deltas = compute_deltas(base, var)
    sig = significant_moves(deltas)
    retreat_flags = detect_default_retreat(base, var)
    has_consequence, consequence_reasons = structural_consequence(sig, retreat_flags)

    if not base_ok or not var_ok:
        return {
            "verdict": "unscorable",
            "confidence": "weak",
            "reasons": {
                "baseline_validity": base_validity,
                "variant_validity": var_validity,
                "structural_consequence": consequence_reasons,
                "causal_attribution": ["invalid kernel state"],
            },
            "deltas": deltas,
            "significant_moves": sig,
        }

    changed = [k for k, v in sig.items() if v]
    attribution_ok = bool(intervention.strip()) and one_variable_only and pipeline_match
    attribution_reasons = []
    if not intervention.strip():
        attribution_reasons.append("missing named intervention")
    if not one_variable_only:
        attribution_reasons.append("multiple variables may have changed")
    if not pipeline_match:
        attribution_reasons.append("measurement pipeline mismatch")
    if attribution_ok:
        attribution_reasons.append("single intervention + matched pipeline")

    if not changed:
        verdict_name = "no-change"
        confidence = "supported"
    elif retreat_flags:
        verdict_name = "false-improvement"
        confidence = "supported"
    elif has_consequence and attribution_ok and len(changed) >= 1:
        verdict_name = "proven-improvement"
        confidence = "supported"
    elif has_consequence and intervention.strip():
        verdict_name = "partial-improvement"
        confidence = "possible"
    elif changed:
        verdict_name = "cosmetic-change"
        confidence = "possible"
    else:
        verdict_name = "unscorable"
        confidence = "weak"

    return {
        "verdict": verdict_name,
        "confidence": confidence,
        "reasons": {
            "baseline_validity": base_validity,
            "variant_validity": var_validity,
            "structural_consequence": consequence_reasons,
            "causal_attribution": attribution_reasons,
            "default_resistance": retreat_flags or ["no clear retreat detected"],
        },
        "deltas": deltas,
        "significant_moves": sig,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", help="Path to baseline kernel JSON")
    parser.add_argument("--variant", help="Path to variant kernel JSON")
    parser.add_argument("--baseline-json", help="Inline baseline kernel JSON")
    parser.add_argument("--variant-json", help="Inline variant kernel JSON")
    parser.add_argument("--intervention", default="", help="Description of the one controlled change")
    parser.add_argument("--one-variable-only", action="store_true", help="Assert that only one variable changed")
    parser.add_argument("--pipeline-match", action="store_true", help="Assert same preprocessing / extraction pipeline")
    parser.add_argument("--comparison-id", default="", help="Optional comparison id")
    parser.add_argument("--out", help="Optional output file path")
    args = parser.parse_args()

    base = load_json_arg(args.baseline, args.baseline_json)
    var = load_json_arg(args.variant, args.variant_json)

    result = verdict(
        base=base,
        var=var,
        intervention=args.intervention,
        one_variable_only=args.one_variable_only,
        pipeline_match=args.pipeline_match,
    )

    payload = {
        "comparison_id": args.comparison_id,
        "intervention": args.intervention,
        "one_variable_only": args.one_variable_only,
        "pipeline_match": args.pipeline_match,
        **result,
    }

    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Generate μ prompt nudges from symptoms or measured values."""

from __future__ import annotations

import argparse
from collections import OrderedDict


SYMPTOMS = {
    "centered": {
        "diagnosis": "subject is snapping to geometric center",
        "nudge": "shift the subject center 10-12% away from geometric center toward the long side",
        "control": "subject_center_x = +/-0.10 to 0.12",
        "avoid": "no centered framing",
    },
    "frontal": {
        "diagnosis": "gaze or dominant direction is too front-facing",
        "nudge": "turn gaze or dominant direction 6-8 degrees toward the open side",
        "control": "gaze_angle = 6-8 degrees toward long side",
        "avoid": "no direct front-facing gaze",
    },
    "crowded": {
        "diagnosis": "subject footprint is too large and suppresses void agency",
        "nudge": "reduce subject footprint to about 40% of frame width",
        "control": "subject_width_ratio = 0.40 +/-0.02",
        "avoid": "no full-frame subject dominance",
    },
    "weak-void": {
        "diagnosis": "negative space is too small to create off-center pull",
        "nudge": "expand negative space on the long side to 40-50% of the frame",
        "control": "negative_space_ratio = 0.40-0.50",
        "avoid": "no filled background clutter",
    },
    "blank-void": {
        "diagnosis": "void is present but reads as blank background",
        "nudge": "activate the void with a low-contrast gradient, edge trace, or peripheral anchor",
        "control": "void_anchor = soft gradient or faint edge trace",
        "avoid": "do not fill the void with props",
    },
    "flat-light": {
        "diagnosis": "luminance weight recenters the image",
        "nudge": "bias light or dark mass 6-9% toward the long side",
        "control": "luminance_centroid_offset = 0.06-0.09",
        "avoid": "no centered spotlight",
    },
    "symmetry-safe": {
        "diagnosis": "composition is resolving into polished center-safe symmetry",
        "nudge": "cap symmetry and break mirrored balance while preserving realism",
        "control": "symmetry_cap = true",
        "avoid": "no perfect symmetry",
    },
    "overdrift": {
        "diagnosis": "drift is too aggressive and threatens identity or realism",
        "nudge": "pull offset back toward 10% and restore base fidelity before adding more drift",
        "control": "subject_center_x = +/-0.10; fidelity_lock = true",
        "avoid": "no further stylization",
    },
    "overstylized": {
        "diagnosis": "style is replacing subject fidelity",
        "nudge": "preserve base lighting, texture, color temperature, and identity within 10%",
        "control": "color_temperature_drift <= +/-10%; texture_lock = true",
        "avoid": "no heavy grading or style overhaul",
    },
    "prop-heavy": {
        "diagnosis": "narrative props are solving tension too literally",
        "nudge": "remove heavy props and use mass, void, gaze, and light to create tension",
        "control": "heavy_props = false",
        "avoid": "no symbolic object pileup",
    },
}


def add_symptom(symptoms: OrderedDict[str, None], name: str) -> None:
    if name in SYMPTOMS:
        symptoms[name] = None


def symptoms_from_measurements(args: argparse.Namespace) -> OrderedDict[str, None]:
    symptoms: OrderedDict[str, None] = OrderedDict()
    if args.db is not None:
        if abs(args.db) < 8:
            add_symptom(symptoms, "centered")
        elif abs(args.db) > 15:
            add_symptom(symptoms, "overdrift")
    if args.dg is not None:
        if abs(args.dg) < 5:
            add_symptom(symptoms, "frontal")
        elif abs(args.dg) > 12:
            add_symptom(symptoms, "overdrift")
    if args.sr is not None:
        if args.sr > 45:
            add_symptom(symptoms, "crowded")
        elif args.sr < 35:
            add_symptom(symptoms, "overdrift")
    if args.nr is not None:
        if args.nr < 35:
            add_symptom(symptoms, "weak-void")
        elif args.nr > 60:
            add_symptom(symptoms, "blank-void")
    if args.dl is not None:
        if abs(args.dl) < 5:
            add_symptom(symptoms, "flat-light")
        elif abs(args.dl) > 12:
            add_symptom(symptoms, "overdrift")
    if args.fidelity is not None and args.fidelity < 7:
        add_symptom(symptoms, "overstylized")
    return symptoms


def ordered_symptoms(raw: list[str], measured: OrderedDict[str, None]) -> list[str]:
    symptoms: OrderedDict[str, None] = OrderedDict()
    for name in raw:
        key = name.strip().lower()
        if key not in SYMPTOMS:
            raise SystemExit(f"Unknown symptom '{name}'. Available: {', '.join(SYMPTOMS)}")
        symptoms[key] = None
    for key in measured:
        symptoms[key] = None
    if not symptoms:
        symptoms["centered"] = None
        symptoms["frontal"] = None
        symptoms["weak-void"] = None
    return list(symptoms)


def build_prompt_clause(symptoms: list[str]) -> str:
    nudges = [SYMPTOMS[name]["nudge"] for name in symptoms]
    fidelity = "preserve base identity, realism, lighting direction, texture, and color temperature within 10%"
    if any(name in {"overdrift", "overstylized"} for name in symptoms):
        return "Adjust toward μ: " + "; ".join(nudges) + "."
    return "Adjust toward μ: " + "; ".join(nudges + [fidelity]) + "."


def print_nudge(symptoms: list[str], original: str | None) -> None:
    print("## μ Prompt Nudge")
    print()
    print("**Diagnosis:**")
    for name in symptoms:
        print(f"- {name}: {SYMPTOMS[name]['diagnosis']}")
    print()
    print("**Primary Nudge:**")
    print(f"- {SYMPTOMS[symptoms[0]]['nudge']}")
    print()
    print("**Revised Prompt:**")
    if original:
        print(original.strip())
        print()
        print(build_prompt_clause(symptoms))
    else:
        print(build_prompt_clause(symptoms))
    print()
    print("**Explicit Controls:**")
    for name in symptoms:
        print(f"- {SYMPTOMS[name]['control']}")
    print()
    print("**Avoid:**")
    avoids = OrderedDict((SYMPTOMS[name]["avoid"], None) for name in symptoms)
    for item in avoids:
        print(f"- {item}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", help="Original prompt to revise.")
    parser.add_argument("--symptom", action="append", default=[], help=f"Failure symptom. Options: {', '.join(SYMPTOMS)}")
    parser.add_argument("--db", type=float, help="Measured ΔB subject offset percent.")
    parser.add_argument("--dl", type=float, help="Measured ΔL luminance offset percent.")
    parser.add_argument("--dg", type=float, help="Measured ΔG gaze/direction offset degrees.")
    parser.add_argument("--sr", type=float, help="Measured S_r subject footprint percent.")
    parser.add_argument("--nr", type=float, help="Measured N_r negative-space ratio percent.")
    parser.add_argument("--fidelity", type=float, help="Estimated fidelity 1-10.")
    args = parser.parse_args()

    symptoms = ordered_symptoms(args.symptom, symptoms_from_measurements(args))
    print_nudge(symptoms, args.prompt)


if __name__ == "__main__":
    main()

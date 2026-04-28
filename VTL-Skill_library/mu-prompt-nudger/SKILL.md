---
name: mu-prompt-nudger
description: Revise AI image/video prompts with precise μ nudges that escape centered model defaults while preserving fidelity. Use when a prompt or generated result is too centered, too frontal, too filled, too blank, overdrifted, over-stylized, or losing identity, and the user needs a one-step correction using subject offset, luminance bias, gaze angle, footprint, negative-space ratio, symmetry caps, and fidelity locks.
---

# Mu Prompt Nudger

## Purpose

Use this skill to rewrite prompts so they move toward μ: off-center enough to break the model's safe statistical default, but controlled enough to preserve identity, realism, lighting, and coherence.

This skill is independent. It includes its own nudge bands, templates, and helper script. It does not require `mu-finder` or any other skill.

## Quick Start

Generate a correction clause from symptoms:

```bash
python3 scripts/mu_nudge.py --symptom centered --symptom frontal --symptom crowded
```

Generate a correction from measurements:

```bash
python3 scripts/mu_nudge.py --db 3 --dg 1 --sr 55 --nr 25 --fidelity 8
```

Use `references/nudge-playbook.md` for detailed symptom-to-correction mappings and prompt templates.

## Core Nudge Bands

- Subject offset `ΔB`: target 10-12% from geometric center.
- Luminance offset `ΔL`: target 6-9% toward the long side.
- Gaze/dominant direction `ΔG`: target 6-8 degrees toward the long side.
- Subject footprint `S_r`: target about 40% of frame width.
- Negative space `N_r`: target 40-50% of frame area.
- Fidelity lock: preserve base identity, lighting direction, texture, and color temperature within about 10%.

## Effectiveness 

After applying a nudge: re-measure (μ Finder or MOS)
compare: Did ΔB / ΔL / ΔG actually move?

If not: Nudge Ignored → increase constraint strength

## Conflict Detection

Example conflicts:
- “expand void” + “increase subject footprint”
- “increase offset” + “restore fidelity” (too aggressively)

If conflict: Conflicting Nudges → prioritize primary, delay secondary

## Primary Lock

Only one axis should dominate:
- Primary: ΔB (offset)
- Secondary: ΔG (gaze)

If multiple axes shift equally: Diffuse Correction → weak result

## Strength Levels 
- soft → near band
- standard → default
- hard → resistant models

Example:
- soft: 8–10%  
- standard: 10–12%  
- hard: 12–15%

## Resistance

If:
- repeated attempts → no movement
Model Resistance → switch to structured block or hard constraints

## Translation Strength 

Check if prompt includes:
- numeric control (good)
- spatial instruction (required)
- avoidance clause (critical)

If missing: Weak Prompt → likely ignored

## Outcome Split

After generation: numeric: ΔB, ΔL, ΔG
visual: does it feel off-center?
If mismatch: Numeric Success / Visual Failure → refine constraints

## Compensation

Detect:
- offset present
but:
- lighting recenters
- props rebalance
- framing compensates
Compensation Detected → increase multi-axis enforcement

## Void Type 

Check if void is:
- active (good)
- empty (bad)
- cluttered (bad)

If wrong type: Void Misclassification → wrong nudge applied

## Iteration Rule 
- 1 nudge → generate → measure → adjust
If violated: Stacked Nudges → attribution loss

## Repair Mode

Given an image:
- identify:
    - dominant failure
- output:
    - Remove X  
    - Increase Y  
    - Preserve Z  

Not just rewrite prompt—surgical correction

Proof Validation

After applying nudge:
- run Proof Loop
If not proven:
- Unproven Nudge → aesthetic bias

## Workflow

1. **Identify the failure.** Classify the current prompt/result as centered, frontal, crowded, blank, overdrifted, over-stylized, prop-heavy, symmetry-safe, or fidelity-broken.
2. **Choose the smallest correction but only if the model actually responds to it.** Apply one primary μ nudge first. Add at most two supporting locks.
3. **Preserve the subject class.** Do not rewrite the entire prompt unless the original is unusable.
4. **Add numeric control.** Use explicit offsets, ratios, and caps when the model keeps snapping back to center.
5. **Add fidelity locks.** Preserve base tonality, identity, lighting direction, texture, and realism before increasing drift.
6. **Return a revised prompt.** Keep the original subject and style, but append or integrate a μ-control clause.

## Output Format

Return:

1. **Diagnosis:** what is failing and why.
2. **Primary Nudge:** the one most important correction.
3. **Revised Prompt:** a clean prompt ready to paste.
4. **Optional Explicit Controls:** CAD-style values if the target model accepts structured prompts.
5. **Avoid:** negations that prevent collapse, such as no centered framing, no perfect symmetry, no direct front-facing gaze, no heavy props.

## Default One-Line Nudge

Use this when the prompt is generally too safe or centered:

`Adjust toward μ: shift the subject center 10-12% off geometric center toward the long side, turn gaze or dominant direction 6-8 degrees into the open space, keep subject footprint near 40% of frame width, expand negative space to 40-50%, preserve base lighting, texture, color, and identity within 10%, no centered framing or perfect symmetry.`

## Guardrails

- Do not add more story objects to solve a spatial problem. Add spatial pressure first.
- Do not use maximum drift as the answer. μ is a mid-shift, not a collapse.
- If fidelity is already weak, restore identity/lighting/texture before increasing offsets.
- If the void is blank, add low-contrast gradient, edge trace, or peripheral anchor rather than filling it with props.
- If a prompt is already in μ, preserve it and make only small variations.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.

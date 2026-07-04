---
name: rcp-classifier
description: Classify Radial Collapse Prior (RCP) in AI-generated images, batches, prompts, or visual diagnostics. Use when the user provides an image, overlay, kernel readings, VTL/LSI values, RCA-2/VCLI context, or asks whether an output shows radial collapse, center-lock, symmetric void, density bowl, inflated cohesion, ring-conform gestures, emblematic collapse, single-force radial field, RCP_high, RCP_med, hard RCP, soft RCP, borderline RCP, or needs a first-pass Delta/Omega/O/Hold route.
---

# RCP Classifier

## Purpose

Use this skill to classify whether an image or batch shows Radial Collapse Prior: a single-force radial field where mass, void, density, and gesture collapse toward a centered, emblematic equilibrium.

RCP is a visible failure signature, not a mechanism claim. Do not claim access to model internals, training data, intent, or hidden representations.

## Core Definition

Classify RCP when the image is dominated by a radial basin rather than multi-force composition:

- mass collapses toward the frame center,
- voids equalize around the center,
- density forms a circular bowl,
- edges and micro-gestures over-agree,
- salient lines conform to concentric arcs.

RCP differs from RCA-2. RCA-2 measures radial compliance around frame and mass centers. RCP names a broader generative collapse pattern: centered stability without directional strain.

False Positive Guard:
- Do not mark RCP from center-lock alone
- Do not mark RCP from symmetry alone
- Require multi-signal agreement

RCA-2 → what structure exists
RDC → whether it counts
RCP → whether it collapsed

## Inputs

Accept any of these evidence types:

- image or contact sheet,
- concentric-ring overlay,
- blurred density field,
- traced gesture/edge map,
- visual critique notes,
- kernel readings: `Delta x`, `r_v`, `rho_r`, `mu`, vector directionality,
- VTL/axis readings: A4, A5, A27, A30,
- RCA-2/VCLI context when supplied.

If only prose is supplied, classify from the described evidence and mark confidence accordingly.

## Classification Hits

Evaluate five hits:

1. `center-lock`: main mass pinned near frame center.
   - Numeric cue: `abs(Delta x) < 0.08` strict, or `< 0.10` lite.
   - Visual cue: no meaningful lateral displacement; off-center prompt appears pulled back to center.

2. `radial-void`: void/negative space forms a symmetric bowl or donut.
   - Numeric cue: `r_v` variance low, typically `< 0.15`.
   - Visual cue: empty space wraps evenly around the central mass rather than producing directional pockets.

3. `density-bowl`: mass or luminance peaks centrally and falls off smoothly.
   - Numeric cue: peaked `rho_r` plus smooth radial decay.
   - Visual cue: heavy blur produces circular density contours or center glow.

4. `mu-inflation`: cohesion is too high and edges over-agree.
   - Numeric cue: high `mu`, high A4 smoothness, low local fracture.
   - Visual cue: texture, light, contours, and local structure harmonize into one radial field.

5. `ring-fit`: salient gestures conform to concentric arcs.
   - Numeric/visual cue: about 50-60% or more of salient edges, contours, or micro-gestures align with ring curvature.
   - Visual cue: local geometry obeys the global radial field instead of scene, anatomy, perspective, or action axes.
   - Ring-Fit Requirement:
    - Must affect a majority of salient structures (≥50%)
    - Not isolated curves or decorative arcs

## Decision Rule

Count matched hits:

- 4-5 hits: `Hard RCP`
- 3 hits: `Soft RCP`
- 2 hits: `Borderline`
- 0-1 hits: `Not RCP`

If 2 hits:
- default to Borderline
- do NOT escalate to Soft RCP without strong visual confirmation

Do not:
- upgrade Borderline to Soft without evidence
- upgrade Soft to Hard without 4+ confirmed hits

If visual evidence contradicts numeric cues:
→ trust visual evidence
→ downgrade classification

Use these aliases when the user asks for high/medium/low:

- `RCP_high`: 4-5 hits or all cheap-rule conditions present.
- `RCP_med`: 3 hits or any three cheap-rule conditions present.
- `RCP_low`: 0-2 hits, with `Borderline` called out separately when exactly 2 hits are present.

## First-Pass Route

Always provide at least one recommendation.

- `Hard RCP`: route `Omega` for counter-geometry / anti-emblem.
- `Soft RCP`: route `Delta` for asymmetry / near-miss tension.
- `Borderline`: route `O` to stabilize into a non-radial basin and monitor drift.
- `Not RCP`: route `Hold` only if the user requested routing; otherwise say no RCP correction is required.

If the profile is explicitly `Emblematic`, `Iconic`, or intentionally radial, allow RCP as a chosen structure and frame the route as `Hold` or light `Omega` depending on tension load. If the profile is not emblematic, avoid `Hold` on first pass for detected RCP.

If profile = emblematic/iconic:
→ allow RCP as intentional
→ downgrade corrective routing

## Output Format

Use this format:

```text
Classification:
Detection Status: <confirmed | provisional | unclear | blocked>
RCP Class: <Hard RCP | Soft RCP | Borderline | Not RCP | Unknown>

Data Integrity Check:
- image or visual evidence → <present/missing>
- kernel cues → <present/partial/missing>
- hit evidence sufficient → <yes/no>

If insufficient:
→ Detection Status = unclear or blocked

Minimum Evidence Rule:
- At least 3 independent cues required for RCP-positive classification
- Do not infer hits from a single visual feature

Hit count:
<n>/5

Matched hits:
- center-lock: <yes/no/unknown> <evidence>
- radial-void: <yes/no/unknown> <evidence>
- density-bowl: <yes/no/unknown> <evidence>
- mu-inflation: <yes/no/unknown> <evidence>
- ring-fit: <yes/no/unknown> <evidence>

Route:
<Delta | Omega | O | Hold | Unknown> - <why>

Read:
<plain-language description of the collapse or non-collapse pattern>

Confidence:
<high | medium | low> - <based on visual/numeric evidence quality>

Confidence Mapping:
- High → 4–5 hits + visual confirmation
- Medium → 3 hits with partial evidence
- Low → 2 hits or weak cues
- Unknown → insufficient data

Batch Mode:
- classify each image independently
- do not average hits across images
- report distribution of RCP classes

Limits:
<missing overlays, missing kernel values, ambiguous profile, image-only estimate, non-mechanism caveat>
```

For one-line mode, use:

```text
<Hard RCP | Soft RCP | Borderline | Not RCP> because: <hit 1> + <hit 2> + <hit 3>. Route -> <Delta/Omega/O/Hold>.
```

For batches, output a table with columns:

`image`, `hit_count`, `classification`, `matched_hits`, `route`, `confidence`, `note`.

## References

Read [hit-definitions.md](references/hit-definitions.md) when applying the five-hit classifier, mapping visual cues to kernel/axis evidence, or handling borderline cases.

Read [classification-language.md](references/classification-language.md) when choosing labels, confidence language, and safe phrasing.

## Constraints

- Do not treat RCP as proof of model mechanism, intent, training data, or hidden representation.
- Do not call RCP automatically bad; it may be valid for emblematic/iconic profiles.
- Do not classify a work as RCP-positive from centered subject alone; require at least three hits for RCP-positive.
- Do not confuse RCA-2 frame-centered compliance with RCP. High radial compliance may support RCP evidence, but RCP requires collapse-pattern evidence.
- Do not call human-authored radial composition a model failure without context.
- Do not infer image quality, beauty, prompt obedience, viewer attention, or semantic importance from RCP alone.
- Do not use `Hold` as the only first-pass recommendation when RCP is detected and the profile is not explicitly emblematic.

## Attribution

Radial Collapse Prior is part of the Visual Thinking Lens system authored by Russell Parrish / A.rtist I.nfluencer. Preserve attribution when packaging, distributing, or publishing derived materials.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.

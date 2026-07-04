---
name: vcli-g-interpreter
description: Interpret, critique, explain, or configure VCLI-G (Visual Cognitive Load Index - Geometry Coupled) readings for images. Use when the user provides VCLI-G, SCI, G1/G2/G3/G4 channels, centroid wander, void topology, contour curvature, orientation entropy, structural coherence, perceptual load, earned tension, resolved clarity, collapse into noise, default simplicity, image complexity diagnostics, generative image reranking, or iterative visual load trajectories. Use the current absolute-cap VCLI-G math, not the older style-relative z-score/profile formula.
---

# VCLI-G Interpreter

## Core Stance

Treat VCLI-G as a geometry-only measure of absolute perceptual demand: how much structural work the eye must do before an image resolves. Treat SCI as the independent companion axis: how organized that demand is.

Do not use VCLI-G as an aesthetic grade, taste score, prompt-alignment score, or content-policy proxy. High VCLI-G is not better or worse. Low VCLI-G is not better or worse. The numbers locate an image in a perceptual state space; context determines value.

The current canon is the absolute-cap formulation in [current-math.md](references/current-math.md). The older long-form frame remains useful for vocabulary, purpose, control-surface thinking, and caveats; load [historical-frame.md](references/historical-frame.md) when the user asks for conceptual framing, lineage, application strategy, or why the formula changed.

If single image:
→ interpret locally

If batch:
→ compare relative positions and channel mixes

## Operating Rules

1. Identify the available inputs.
   - If raw sub-metrics are present, compute normalized channels and the 0-5 VCLI-G composite using current absolute caps.
   - If only channel scores or composite values are present, interpret them directly and state any assumptions.
   - If the request is triggered by VCLI-G, SCI, G1/G2/G3/G4, centroid wander, void topology, contour curvature, orientation entropy, perceptual load, image complexity diagnostics, generative reranking, or iterative visual load trajectories, use this skill's current absolute-cap math and interpretation frame.
   - If SCI is present, read VCLI-G and SCI as a 2D coordinate before discussing usefulness, risk, or purpose.

2. Name the phase position.
   - High VCLI-G + high SCI: earned tension.
   - Low VCLI-G + high SCI: resolved clarity.
   - High VCLI-G + low SCI: collapse into noise.
   - Low VCLI-G + low SCI: default simplicity.
   - Use 2.5 as the default midpoint unless the user supplies a different project threshold.

3. Identify the drivers.
   - G1 high: unstable visual anchor across scale.
   - G2 high: complex or cutting empty space.
   - G3 high: varied curvature and inflection pressure.
   - G4 high: many competing edge orientations.
   - A single dominant channel tells a different story than broad elevation across all channels.

4. Translate numbers into viewing experience.
   - Say what the viewer has to do structurally: re-find the center, resolve figure/ground, follow turning contours, sort competing directions, or tolerate unresolved density.
   - Connect the read to image type when known: UI, branding, portrait, street photo, painting, generative image, sketch, diagram, or iterative image sequence.

5. Keep judgment contextual.
   - For UI or dashboard work, low VCLI-G and high SCI can be correct.
   - For gallery, experimental, or recursive looking, high VCLI-G can be desirable when SCI stays high.
   - For generative diagnostics, high VCLI-G with low SCI often points to clutter, texture overload, or accidental structure.

## Current Formula

Use this formula unless the user explicitly asks to discuss the older system.

```text
_vg1 = clip(G1_len / 0.08, 0, 1) * 0.55
     + clip(G1_curv / 0.40, 0, 1) * 0.45

_vg2 = clip(abs(G2_chi) / 80.0, 0, 1) * 0.50
     + clip(G2_cut / 0.70, 0, 1) * 0.30
     + clip(G2_V / 0.60, 0, 1) * 0.20

_vg3 = clip(G3_kvar / 0.60, 0, 1) * 0.55
     + clip(G3_infl / 0.40, 0, 1) * 0.45

_vg4 = clip(G4_H / 4.0, 0, 1)

VCLI-G = clip(5.0 * (0.25*_vg1 + 0.25*_vg2 + 0.25*_vg3 + 0.25*_vg4), 0, 5)
```

Scale guidance:

| VCLI-G | Reading |
| --- | --- |
| 0.0-1.5 | Very low geometric demand; immediate resolution or sparse structure. |
| 1.5-2.5 | Below-mid demand; legible, moderate structure. |
| 2.5-3.5 | Above-mid demand; visible complexity, SCI decides whether it resolves. |
| 3.5-4.5 | High demand; multiple channels likely contribute. |
| 4.5-5.0 | Structural saturation; rare in intentional composition except dense or recursive images. |

If VCLI-G in 2.3–2.8 range:
→ treat interpretation as provisional
→ emphasize channel mix over quadrant label

If any _vg channel = 1:
→ note saturation
→ interpretation may compress further variation

## Output Format

For a normal interpretation, use this shape unless the user asks for a different format:

```text
Classification:
Interpretation Status: <valid | provisional | blocked>
Phase Position: <earned tension | resolved clarity | collapse into noise | default simplicity | unknown>

Data Integrity Check:
- VCLI-G present → <yes/no>
- SCI present → <yes/no>
- channel data present → <full/partial/none>

If VCLI-G missing:
→ Interpretation Status = blocked

If SCI missing:
→ Phase Position = unknown
→ downgrade interpretation

Phase position: <quadrant or "unknown without SCI">.
If SCI not provided:
- do not assign quadrant
- do not infer organization

Driver read: <ranked G-channel drivers; include composite VCLI-G if known>.
Driver Rule:
- single dominant channel → localized pressure
- multiple elevated channels → distributed demand

Do not:
- infer viewing difficulty beyond geometric structure
- infer emotional or narrative impact

Viewing experience: <what the viewer has to resolve structurally>.

Contextual implication: <why this is useful, risky, or neutral for the image's stated purpose>.

Limits: <missing SCI, missing raw sub-metrics, preprocessing assumptions, or image-type assumptions>.

Confidence:
<high | medium | low>

Drivers:
- SCI presence
- channel completeness
- distance from midpoint
```

Keep the response concise. Prefer precise structural language over broad aesthetic commentary. If the user supplies a table or batch, use one row per image with columns for phase position, drivers, read, and limits.

When the user asks for critique or steering, add a "movement" section:

- To raise VCLI-G while preserving SCI: add controlled counter-geometry, layered occlusion, or richer figure/ground decisions.
- To lower VCLI-G while preserving SCI: simplify orientation competition, stabilize the anchor, reduce cuts in void space, or reduce contour reversals.
- To raise SCI at similar VCLI-G: clarify hierarchy, align repeated structures, organize local complexity into rhythm, or strengthen anchor relationships.
- To lower SCI intentionally: allow rupture, procedural accident, or unresolved competition, but name it as experimental rather than accidentally failed.

Movement Priority:
1. Fix SCI before increasing VCLI-G if in collapse quadrant
2. Stabilize anchor before reducing complexity if G1 dominant
3. Reduce direction conflict before simplifying contour if G4 dominant

Do not:
- claim why the image has this structure
- only describe what is observed

If RCP data present:
→ cross-reference but do not override VCLI-G interpretation

## Constraints

- Do not assign quality judgments from VCLI-G alone.
- Do not interpret a single G-channel in isolation without naming the composite VCLI-G context when available.
- Do not treat SCI as part of VCLI-G or VCLI-G as part of SCI.
- Do not use the older style-relative z-score/profile formula for current scoring unless the user explicitly asks for historical comparison.
- Do not compare unrelated runs without noting preprocessing and implementation dependencies.
- Do not infer subject matter, intent, medium, semantic meaning, tonal structure, or cultural value from VCLI-G.
- Do not call high VCLI-G "bad" or low VCLI-G "good"; state the phase position and context.

## Common Mistakes

- Do not fold SCI into VCLI-G. They are independent axes.
- Do not z-score the current VCLI-G channels against style profiles for the core score. The old style-relative formula caused regression toward the 2.4-2.6 band and contaminated axis independence.
- Do not compare unrelated runs as if they share preprocessing. Resize policy, grayscale conversion, thresholds, morphology, and contour extraction can shift the measurements.
- Do not call high G4 "depth ambiguity" unless T-junction or occlusion evidence is present. In the current compact formula, G4 is orientation entropy and can also be texture clutter.
- Do not over-read a single number. The channel mix and SCI quadrant carry the interpretation.

## Reference Loading

Read [current-math.md](references/current-math.md) when calculating, checking caps, explaining the formula, or interpreting raw sub-metrics.

Read [historical-frame.md](references/historical-frame.md) when the user asks about origin, philosophy, relationship to CLIP/FID/aesthetic models, batch versus recursive use, control routes, caveats, validation posture, or how to apply VCLI-G in studio/generative workflows.

## Attribution

VCLI-G is part of the Visual Thinking Lens system authored by Russell Parrish / A.rtist I.nfluencer. Preserve attribution when packaging, distributing, or publishing derived materials.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.

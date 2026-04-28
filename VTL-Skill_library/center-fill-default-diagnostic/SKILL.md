---
name: center-fill-default-diagnostic
description: "Diagnose when AI-generated images or prompt-output sequences regress to center-fill defaults: centered salience, subject blob plus passive margins, comfortable void, mid-lane containment, additive/global packing, regular cadence, symmetry, safe polish, generic clarity, and closure rescue. Use when the user wants to identify native AI visual defaults, compare default versus anti-default behavior, score default severity, name the protected attractor, or propose minimal anti-default correction moves without relying on other skills."
---

# Center-Fill Default Diagnostic

## Overview

Use this skill to detect the native visual defaults that many image models fall back to when a prompt does not strongly specify page architecture. It asks: **did the image make a structural choice, or did it return to center-fill equilibrium?**

Core rule: **center-fill is not automatically bad; it is a default. Diagnose it only when it replaces the intended compositional behavior.**

## Default Signature

A center-fill default usually combines several of these:

- `centered salience`: subject, face, light, contrast, or sharpness returns to center.
- `content blob plus margins`: content congeals into a central mass with passive empty border.
- `comfortable void`: empty space exists but stays moderate, decorative, or background-like.
- `mid-lane containment`: marks/content stay in a safe middle lane instead of claiming or compressing territory intentionally.
- `additive packing`: detail accumulates everywhere until the image feels complete.
- `regular cadence`: marks, texture, or spacing become even, tiled, or mechanically rhythmic.
- `symmetry safety`: balance, frontal staging, mirrored supports, or equal margins reduce tension.
- `generic clarity`: prompt pressure resolves into a stock portrait, room, landscape, object, or cinematic frame.
- `polish closure`: lighting, surfaces, gesture, or narrative resolve the image too neatly.

## Metric Clues

Use metrics when supplied. Otherwise use visual estimates.

Typical center-fill/default tendencies:

- `delta_x`: near center or salience recenters even if the subject is slightly offset.
- `corridor_90`: about `0.45-0.56`, mid-lane or content blob.
- `cadence_cv`: about `0.35-0.50`, regular rhythm or tiling.
- `r_v`: about `0.83-0.86`, comfortable void rather than austere, active empty space.
- `rho_r`: about `0.22-0.32`, additive/photographic packing or generalized texture.
- `margin_L_to_R`: near `1.0` when symmetry is being protected, or margins appear passive even when uneven.

Anti-default reference targets from the source document:

- `r_v >= 0.88`: more paper / austere breathing room.
- `corridor_90 >= 0.58`: chosen lane, not blob plus margins.
- `rho_r <= 0.15` globally: restrained packing; add energy locally only.
- `cadence_cv >= 0.65`: phrased marks and uneven pauses.

Do not treat these as universal aesthetic laws. Use them as default-detection anchors.

## Inputs

Minimum:

- prompt or intended behavior
- output description, image read, or metrics

Helpful:

- baseline/native output
- revised/guided output
- sequence of attempts
- `delta_x`, `r_v`, `rho_r`, `corridor_90`, `cadence_cv`, `margin_L_to_R`
- stated target: high void, off-center, chosen lane, mark economy, irregular rhythm, anti-closure, etc.

## Workflow

1. **Name the intended anti-default behavior.**
   - Example: off-center mass, high active void, broad lane, compressed scroll lane, local knots, phrased rhythm, restrained packing, unresolved closure.

2. **Identify protected defaults.**
   - Which safe structure did the output preserve instead?

3. **Score default axes.**
   - Use the rubric below.

4. **Classify the default family.**
   - Choose one primary and one secondary family if needed.

5. **Locate the retreat point.**
   - Where did the image stop obeying the hard compositional demand?

6. **Prescribe the smallest anti-default correction.**
   - Change one or two structural levers only.

## Default Families

| Family | Evidence | What It Replaces |
|---|---|---|
| `center-anchor` | face, figure, light, contrast, or sharpness returns to center | off-center gravity |
| `blob-plus-margins` | content forms a central island with empty border | chosen lane / active void |
| `comfortable-void` | empty space reads as background, not pressure | austere or weighted void |
| `mid-lane-safety` | content stays in a moderate lane by habit | broad territory or disciplined compression |
| `global-packing` | texture/detail fills everywhere | mark economy / local knots |
| `cadence-regularization` | marks repeat evenly; low phrase variation | syncopated or punctuated rhythm |
| `symmetry-safety` | equal supports, frontal staging, balanced margins | torque / asymmetry |
| `generic-clarity` | becomes stock, clean, cinematic, or trope-like | structural specificity |
| `closure-rescue` | polish, lighting, pose, or narrative solves the tension | withheld closure |

## Scoring Rubric

Score each axis `0-2`:

- `0`: no default signal; target behavior is visible.
- `1`: partial default; target behavior appears but is weakened.
- `2`: strong default; target behavior is replaced.

Axes:

- `center_pull`
- `blob_margin`
- `void_comfort`
- `lane_safety`
- `packing_addition`
- `cadence_regularization`
- `symmetry_balance`
- `generic_clarity`
- `closure_polish`

Severity:

- `0-3`: low default pressure
- `4-7`: moderate default pressure
- `8-12`: strong center-fill/default regression
- `13-18`: dominant default attractor

Override: if the intended behavior was specifically off-center and the main salience recenters, severity is at least `moderate`.

## Sequence Diagnosis

For multiple outputs:

- `native-regularization`: sequence returns to mid-lane, regular cadence, centered salience, or global texture.
- `snap-back`: output briefly moves off default, then returns to center or safe clarity.
- `surface-addiction`: each revision adds more detail instead of better structure.
- `void-neutralization`: void remains present but never becomes active or load-bearing.
- `lane-stagnation`: `corridor_90` stays in the mid band despite prompts to broaden/compress.
- `cadence-flatline`: rhythm stays regular despite mark-making language.
- `anti-default-shift`: sequence moves toward higher void, chosen lane, lower global packing, and higher cadence.

Do not call a single output a plateau. Plateau requires repeated return; this diagnostic can still flag a single default signature.

## Minimal Corrections

Use one or two of these:

### Move Attention, Not Just Subject

```text
Move the visual mass, strongest light, sharpest edge, darkest value, and main contrast away from center. Keep the center undercharged.
```

### Break Blob Plus Margins

```text
Do not form a central content blob with passive margins. Let the composition operate through a chosen lane or structural path across the frame.
```

### Make Void Active

```text
Keep more empty field, but make it carry pressure through tone, trace, continuation, shadow, grain, or contact. The void is not background filler.
```

### Choose Lane Width

```text
Choose the lane deliberately: broaden it to claim territory, or compress it into a disciplined corridor. Do not let it settle into the safe middle by default.
```

### Reduce Global Packing

```text
Reduce filler detail and global texture. Add density only at local knots: edges, seams, contact points, folds, or pressure turns.
```

### Raise Cadence Without Carpet Texture

```text
Use clusters, pauses, pressure changes, and uneven intervals. Avoid regular spacing, all-over grain, and carpet texture.
```

### Resist Closure Rescue

```text
Leave one edge, gesture, surface, or spatial relation unresolved. Do not solve the image with polish, glow, symmetry, or narrative completion.
```

## Anti-Default Prompt Pattern

```markdown
[Subject/context]. Avoid the native center-fill solution: no centered salience, no content blob plus passive margins, no all-over filler texture. [Chosen structural behavior: high active void / broad lane / compressed lane / local knots / off-center mass / phrased rhythm]. Keep [anchor or coherence condition]. Do not rescue the composition with symmetry, central light, generic clarity, or clean closure.
```

Use sparingly. Prefer the smallest correction when revising an existing prompt.

## Output Pattern

```markdown
**Center-Fill Diagnostic**
- Intended anti-default behavior:
- Primary default family:
- Secondary default family:
- Severity: low / moderate / strong / dominant
- Confidence: possible / supported / strong

**Default Axis Scores**
| Axis | Score | Evidence |
|---|---:|---|
| center_pull |  |  |
| blob_margin |  |  |
| void_comfort |  |  |
| lane_safety |  |  |
| packing_addition |  |  |
| cadence_regularization |  |  |
| symmetry_balance |  |  |
| generic_clarity |  |  |
| closure_polish |  |  |

**Metric Clues**
- delta_x:
- r_v:
- rho_r:
- corridor_90:
- cadence_cv:
- margin_L_to_R:

**Retreat Point**
- The output stopped obeying the target when:

**Smallest Anti-Default Move**
- Change:
- Preserve:
- Avoid:
- Revised clause:
```

## Logging Schema

Use this compact row:

```text
subject, attempt_id, intended_behavior, primary_default, severity, center_pull, blob_margin, void_comfort, lane_safety, packing_addition, cadence_regularization, symmetry_balance, generic_clarity, closure_polish, correction, notes
```

Example:

```text
portrait, i02, high-void chosen-lane, blob-plus-margins, strong, 2, 2, 1, 2, 1, 2, 1, 1, 1, "break blob; choose lane", "void present but passive; rhythm regular"
```

## Claim Discipline

Say:

- `the output exhibits center-fill default behavior`
- `the prompt's intended structure was replaced by`
- `the image protected a safe attractor`
- `this is a default diagnosis, not an aesthetic verdict`

Do not say:

- `centered means bad`
- `AI always does this`
- `default equals collapse`
- `more off-center is always better`
- `higher void/cadence automatically improves the image`

## Guardrails

- Do not punish center composition when center composition was the goal.
- Do not call all clarity generic; only flag clarity when it replaces the hard structural demand.
- Do not confuse active void with empty border.
- Do not prescribe more texture when the issue is global packing.
- Do not overcorrect into noise; preserve one structural anchor.
- Do not require metrics. Use visual estimates when metrics are absent and label them as estimates.
- Keep this skill independent. It contains the default diagnosis protocol directly and does not require other skills.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.

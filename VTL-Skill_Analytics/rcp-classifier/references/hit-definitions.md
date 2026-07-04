# Hit Definitions

## 1. Center-Lock

The main mass is pinned near the geometric center.

Evidence:

- `abs(Delta x) < 0.08` strict or `< 0.10` lite
- subject/mass appears pulled back to center despite off-center prompt or scene logic
- no meaningful lateral displacement

Do not mark from centered subject alone if other forces clearly compete.

## 2. Radial-Void

Negative space equalizes around the center.

Evidence:

- low `r_v` variance, commonly `< 0.15`
- void wraps evenly around central mass
- no strong directional void pocket
- scene feels like a bowl, halo, or donut around the center

False positive:

- intentional iconography, mandala, product shot, heraldic layout, or symmetrical design profile.

## 3. Density-Bowl

Material density peaks centrally and falls off smoothly.

Evidence:

- peaked `rho_r`
- smooth radial decay
- blurred image reveals circular glow or mass basin
- lighting, fog, texture, or contrast compress toward the center

Useful visual test:

- blur heavily and inspect whether a circular density bowl remains.

## 4. Mu-Inflation

Cohesion is artificially high; local edges over-agree with the whole.

Evidence:

- high `mu`
- high A4 that reads as radial smoothness rather than resilient continuity
- low fracture, low fragment tension
- textures and edges harmonize too easily
- image is highly resolved but low-strain

Associated axes:

- A4 high
- A5 low
- A27 moderate-high
- A30 high but shallow

## 5. Ring-Fit

Salient local gestures conform to concentric arcs.

Evidence:

- about 50-60% or more salient lines, contours, textures, or micro-gestures follow ring curvature
- curves bend toward an invisible center
- anatomy, perspective, smoke, branches, clothing folds, light rays, or architecture obey disc logic
- local forces are subordinated to global radial field

Useful visual test:

- place transparent concentric rings over the image and inspect whether the rings outperform the scene's own perspective or action lines.

## Cheap Rule

Tag `RCP_high` when all are true:

- `Delta x < 0.10`
- `r_v` variance `< 0.15`
- `mu` above threshold
- A5 below threshold
- A4 above threshold

Tag `RCP_med` when any three are true.

Tag `RCP_low` otherwise.

Use project thresholds when supplied. If thresholds are missing, use qualitative visual evidence and label confidence lower.

## Borderline Cases

Call `Borderline` when exactly two hits are present or when one strong numeric hit is paired with ambiguous visual evidence.

Common borderline patterns:

- centered mass plus density bowl, but strong diagonal counter-force
- radial void plus ring-fit, but mass is clearly off-center
- high cohesion but no center lock
- iconic/emblematic profile where radial form may be intentional

For borderline cases, route `O` unless the user asks for stronger correction.

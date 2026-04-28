# Mu Prompt Nudge Playbook

## Symptom Map

| Symptom | Diagnosis | Primary Nudge |
| --- | --- | --- |
| `centered` | Subject snapped to geometric center | Shift subject center to 10-12% off center |
| `frontal` | Gaze/direction points straight at camera | Turn gaze or dominant direction 6-8 degrees toward long side |
| `crowded` | Subject fills frame; no void agency | Reduce subject footprint to about 40% |
| `weak-void` | Negative space too small or inactive | Expand negative space to 40-50% |
| `blank-void` | Void becomes empty background | Add soft gradient, edge trace, or peripheral anchor |
| `flat-light` | Luminance weight recenters image | Bias luminance 6-9% toward long side |
| `symmetry-safe` | Polished centered balance | Cap symmetry; avoid centered framing and mirrored balance |
| `overdrift` | Offset too aggressive; identity or realism drops | Pull offset back toward 10%; restore base fidelity |
| `overstylized` | Style replaces subject fidelity | Preserve base texture, color, lighting, and identity within 10% |
| `prop-heavy` | Narrative objects solve tension too literally | Remove heavy props; use mass, void, gaze, and light instead |

## Rewrite Patterns

### Centered To Mu

Original prompt stays mostly intact. Append:

`Place the subject center 10-12% away from geometric center toward the long side of the frame; avoid centered framing and mirrored balance.`

### Frontal To Mu

Append:

`Turn the gaze or dominant directional vector 6-8 degrees toward the open side of the frame; avoid direct front-facing gaze.`

### Crowded To Mu

Append:

`Reduce the subject footprint to roughly 40% of frame width and let the surrounding negative space carry 40-50% of the frame.`

### Blank Void To Active Void

Append:

`Keep the negative space active with a low-contrast luminance gradient, faint edge trace, or peripheral anchor; do not fill it with props.`

### Overdrift To Fidelity

Append:

`Pull the spatial offset back toward 10%, preserve identity and subject class, keep lighting direction, texture, and color temperature within 10% of the base.`

### Sora / Video Continuity

Append:

`Use the previous frame as spatial anchor; preserve anchor reference; keep max anchor drift within 2% while maintaining the off-center placement.`

## Structured Prompt Block

Use when the model responds well to explicit parameter blocks:

```text
Composition:
- subject_center_x = +/-0.10 to 0.12 from geometric center
- gaze_angle = 6-8 degrees toward long side
- subject_width_ratio = 0.40 +/-0.02
- negative_space_ratio = 0.40-0.50

Lighting:
- luminance_centroid_offset = 0.06-0.09 toward long side
- color_temperature_drift = within +/-10% of base
- shadow_softness = match base +/-5%

Constraints:
- no centered framing
- no perfect symmetry
- no direct front-facing gaze
- no heavy props
- preserve identity, texture, realism, and base lighting
```

## Revision Strategy

Apply corrections in this order:

1. Spatial offset.
2. Gaze/direction.
3. Subject footprint.
4. Negative-space ratio.
5. Luminance bias.
6. Fidelity locks.
7. Anti-collapse negations.

Stop once the prompt has enough pressure. Overcorrecting turns μ into collapse.

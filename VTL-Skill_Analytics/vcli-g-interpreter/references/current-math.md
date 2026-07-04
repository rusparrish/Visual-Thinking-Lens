# Current VCLI-G Math

Use this reference as the operational canon for VCLI-G scoring and interpretation.

## Definition

VCLI-G measures absolute perceptual demand through geometric channels alone. It answers: how hard is the visual system working to process the structural information in this image?

It is not:

- A quality score.
- A style-relative score.
- A prompt-matching score.
- A component of SCI.
- A substitute for image judgment.

VCLI-G is one axis of a 2D perceptual space. SCI is the other axis and measures whether the complexity is organized. Keep the axes independent.

## Why This Replaced The Old Formula

The earlier formula z-scored each G-channel against style profile means and standard deviations, then averaged the weighted z-scores. That created two failures:

- Regression to the mean: weighted z-scores tended to sit near zero, which made many images read in the 2.4-2.6 range regardless of actual structural demand.
- SCI contamination: coherence influenced the load score, so the 2D VCLI-G x SCI space was no longer independent.

The current fix is direct normalization against fixed absolute caps representing structural saturation in each channel.

## Channel Formulas

All clipped channel scores are in [0, 1].

### G1 - Centroid Wander

Question: Does the image have a stable visual anchor, or does the center of gravity shift across scale?

Inputs:

- `G1_len`: total path length of centroid movement across scales. Cap: `0.08`.
- `G1_curv`: curvature of the centroid path. Cap: `0.40`.

```text
_vg1 = clip(G1_len / 0.08, 0, 1) * 0.55
     + clip(G1_curv / 0.40, 0, 1) * 0.45
```

Read:

- High G1: no stable anchor; the eye's entry point shifts with viewing distance.
- Low G1: the composition locks in early and holds.

### G2 - Void Topology

Question: How complex is the empty space?

Inputs:

- `G2_chi`: Euler characteristic magnitude of the void field. Cap: `80`.
- `G2_cut`: fraction of void area forming structural cuts. Cap: `0.70`.
- `G2_V`: total void fraction. Cap: `0.60`.

```text
_vg2 = clip(abs(G2_chi) / 80.0, 0, 1) * 0.50
     + clip(G2_cut / 0.70, 0, 1) * 0.30
     + clip(G2_V / 0.60, 0, 1) * 0.20
```

Read:

- High G2: topologically complex emptiness, many void regions, cutting passages, or significant empty area.
- Low G2: dense image, little void, or one clean surrounding field.

### G3 - Contour Curvature

Question: How varied are the shapes and edge curves?

Inputs:

- `G3_kvar`: variance of curvature across major contour points. Cap: `0.60`.
- `G3_infl`: density of inflection points. Cap: `0.40`.

```text
_vg3 = clip(G3_kvar / 0.60, 0, 1) * 0.55
     + clip(G3_infl / 0.40, 0, 1) * 0.45
```

Read:

- High G3: varied, complex shapes with many reversals.
- Low G3: simple geometry, straight lines, single-radius curves, or minimal contour complexity.

### G4 - Orientation Entropy

Question: How many competing edge directions exist simultaneously?

Input:

- `G4_H`: Shannon entropy of an 8-bin edge-orientation histogram. Cap: `4.0`.

```text
_vg4 = clip(G4_H / 4.0, 0, 1)
```

Read:

- High G4: near-uniform distribution of edge directions; competing structural signals in many directions.
- Low G4: one or two dominant orientations and a clear directional hierarchy.

## Composite

```text
VCLI-G = clip(5.0 * (0.25*_vg1 + 0.25*_vg2 + 0.25*_vg3 + 0.25*_vg4), 0, 5)
```

Use 2.5 as the midpoint. Values above 2.5 represent above-mid geometric demand. Values below 2.5 represent below-mid geometric demand. The upper range is not perceptually linear; 4.0+ means structural saturation across multiple channels.

## Cap Rationale

| Signal | Cap | Rationale |
| --- | ---: | --- |
| `G1_len` | 0.08 | Centroid wander beyond about 8% of image diagonal is saturated. |
| `G1_curv` | 0.40 | Path curvature above 0.40 is erratic beyond useful signal. |
| `G2_chi` | 80 | Larger Euler characteristic magnitude is genuine topological complexity. |
| `G2_cut` | 0.70 | 70% of void as structural cuts is essentially a dissected image. |
| `G2_V` | 0.60 | 60% void fraction is a very sparse image. |
| `G3_kvar` | 0.60 | Higher curvature variance approaches random contour behavior. |
| `G3_infl` | 0.40 | Higher inflection density means contours reverse constantly. |
| `G4_H` | 4.0 | Near-uniform direction distribution for 8 bins; theoretical max is about 4.39. |

## 2D VCLI-G x SCI Space

VCLI-G tells how much geometric demand exists. SCI tells whether that demand is organized.

| Quadrant | Meaning |
| --- | --- |
| High VCLI-G + High SCI | Earned tension: complex, organized, structurally coherent demand. |
| Low VCLI-G + High SCI | Resolved clarity: simple, intentional, internally agreed structure. |
| High VCLI-G + Low SCI | Collapse into noise: busy but incoherent, signals do not organize. |
| Low VCLI-G + Low SCI | Default simplicity: low demand and low organization, often context-dependent. |

## What VCLI-G Cannot See

VCLI-G cannot see subject matter, intent, medium, tonal structure, semantic meaning, or coherence. Coherence is SCI's job. Tonal/luminance structure belongs elsewhere in the broader Visual Thinking Lens stack.

# Off-Center Patterns

Use these patterns to choose the type of off-center basin.

## Peripheral Gravity

Axis: frame drift + attraction imbalance.

Use when the image should feel pulled toward the frame edge.

Prompt move:

```text
Place the primary mass close to the edge of the frame, leaning into the periphery as if pulled by an unseen force. Leave a broad, weighted emptiness across the opposite side. The periphery should feel stronger than the center.
```

Stabilizer:

- diagonal counter-line
- faint interior shadow
- opposite void pressure
- edge crop

Failure:

- subject looks accidentally cropped
- center remains brightest or most detailed

## Asymmetry Pulse

Axis: imbalance + rhythm disruption.

Use when the frame needs an uneven beat rather than a single displaced subject.

Prompt move:

```text
Cluster the strongest forms in one quadrant, opposed by uneven light, color, or mark rhythm elsewhere. Let the eye circle without settling. The center remains inert; the pulse lives in the edges.
```

Stabilizer:

- repeated mark rhythm
- staggered forms
- irregular spacing

Failure:

- random scatter
- decorative imbalance without pulse

## Dislocation

Axis: orientation fracture + spatial paradox.

Use when off-center placement should feel like the whole field has shifted.

Prompt move:

```text
Slide the viewfinder diagonally off the natural horizon. Anchor the subject away from center while background or ground logic resists stable alignment. The offset space should feel heavier than the subject.
```

Stabilizer:

- one believable horizon clue
- one hard edge
- one tonal anchor

Failure:

- arbitrary tilt
- full surreal collapse

## Active Void

Axis: weighted negative space + counterforce.

Use when empty space must do work.

Prompt move:

```text
Open a large quiet field opposite the mass, but make it active through trace, shadow, light falloff, implied absence, or directional pressure. The void should pull attention, not merely surround the subject.
```

Stabilizer:

- faint residue
- implied silhouette
- shadow path
- low-contrast mark

Failure:

- blank minimalism
- background decoration

## Oblique Silence

Axis: angled void + suppression field + horizon fracture.

Best for still life, interiors, and restrained scenes.

Prompt move:

```text
Make the negative space a slanted architectural block pressing against the subject. The subject occupies the smaller fraction, compressed toward a corner, while the void dominates as a tilted plane.
```

Stabilizer:

- table edge
- wall seam
- angled light plane

Failure:

- inert still life
- tilted plane feels graphic but not spatial

## Fracture Flow

Axis: gesture rupture + tonal bleed + temporal smear.

Use when movement should pull the image off-axis.

Prompt move:

```text
Let interrupted gesture and tonal bleed destabilize the frame. Motion should pull the subject off-axis into imbalance, with seams or unresolved edges showing where time was cut.
```

Stabilizer:

- directional stroke path
- repeated smear
- anchored foot, hand, or object

Failure:

- blur without structure

## Emblematic Void

Axis: void pull + symbolic gravity + spatial emblem.

Use when absence itself should become the off-center anchor.

Prompt move:

```text
Shape negative space into a meaningful absence: an implied figure, missing object, directional sign, or unoccupied zone. Arrange the subject to orbit the absence as if what is missing has more gravity than what is shown.
```

Stabilizer:

- edge of silhouette
- object facing absence
- light falling into the void

Failure:

- obvious symbol
- literal missing-person trope

## Metric Hints

When metrics are available:

- Low `abs(delta_x)` or `abs(delta_y)`: mass has not moved far enough.
- High `r_v` with flat image: void may be too passive; activate it.
- Low `r_v`: frame may be too full for an off-center basin; reopen space.
- Low `x_p`: periphery is not carrying enough weight.
- Very high `x_p`: edge pull may topple unless counterweighted.
- Low `rho_r`: add structural density, trace, or fracture.
- High `rho_r`: reduce clutter and restore basin spacing.

## Quick Prompts

Figure:

```text
A figure study with the structural mass displaced into the lower-left quadrant, the center kept quiet and undercharged. A broad right-side void carries a faint shadow trace and low-contrast texture. Add one diagonal tonal spine so the frame holds without re-centering.
```

Still life:

```text
A restrained still life compressed toward the right edge of the frame. The left two-thirds remain quiet but weighted by an angled plane of light and a faint residual mark. Avoid centered tabletop symmetry; let the void press against the objects.
```

Interior:

```text
An interior scene with the main doorway and furniture mass pulled high into the left edge. The center remains blocked by shadow and low detail. A long diagonal light path crosses the opposite empty floor, acting as counterweight without becoming the focus.
```

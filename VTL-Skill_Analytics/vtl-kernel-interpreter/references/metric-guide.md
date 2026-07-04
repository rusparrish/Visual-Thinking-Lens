# Metric Guide

## Current Kernel Fields

`delta_x`:

- Horizontal placement offset of the canonical mass centroid.
- Negative means left-biased; positive means right-biased; near zero means centered.

`delta_y`:

- Vertical placement offset of the canonical mass centroid.
- Negative means top-biased; positive means bottom-biased; near zero means vertically centered.

`r_v`:

- Gradient-quiet fraction: `1 - coverage(gmag >= 0.15)`.
- High means much of the frame is gradient-quiet.
- Low means much of the frame is gradient-active.
- Do not read as simple semantic empty space.

`gradient_floor_85` / `efa`:

- 85th percentile gradient magnitude.
- Higher values mean the baseline edge/texture field is already activated.

`gradient_ceiling_97`:

- 97th percentile gradient magnitude.
- Tracks the strongest edge/contrast tail.

`tail_gap`:

- `gradient_ceiling_97 - gradient_floor_85`.
- Large gap: quiet field plus a few strong edge punches.
- Small gap: edge energy distributed more uniformly.

`rho_r`:

- Packing density: mass area relative to convex hull area, scaled by 100.
- Sensitive to the canonical gradient-defined mass mask.

`mu`:

- Cohesion by component dominance and inverse component-size entropy.
- High: one dominant connected mass or strongly unified structure.
- Low: fragmented or multi-modal component structure.

`x_p`:

- Peripheral pull: gradient magnitude in outer 15% frame band divided by total gradient magnitude.
- Higher values indicate stronger edge-frame engagement.

`theta`:

- Orientation stability from 8-bin weighted orientation entropy.
- High: dominant directional alignment.
- Low: omnidirectional or isotropic texture/edge field.

`d_s`:

- Structural thickness from skeletonized mask thickness, normalized by frame size.
- Higher values indicate thicker structural masses.

`sdi`:

- Spatial Dispersion Index: mean distance of mass pixels from their centroid, normalized by image diagonal.
- Low: tight/compact structural mass.
- Mid: balanced spread.
- High: broadly distributed or edge-spread mass.

`mass_fraction`:

- Fraction of pixels in the canonical percentile mask.
- Treat as device/mask context, not direct compositional occupancy.

## Composite Reads

Centered compact structure:

- `delta_x` near 0,
- `delta_y` near 0,
- low-to-mid `sdi`,
- moderate/high `mu`,
- low `x_p`.

Distributed edge-engaged structure:

- higher `sdi`,
- higher `x_p`,
- possibly lower `mu`,
- placement may be centered or off-center.

Texture field:

- `mask_mode = TEXTURE_FIELD`,
- many components,
- low `theta`,
- low `mu`,
- often low `r_v` when edge activation is high.

Region field:

- `mask_mode = REGION_FIELD`,
- larger dominant component,
- cohesion and placement can be read with higher confidence.

Quiet field:

- high `r_v`,
- low `gradient_floor_85`,
- tail gap determines whether a few strong edges remain.

Active field:

- low `r_v`,
- high `gradient_floor_85`,
- edge/texture activity across much of the frame.

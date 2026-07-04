# Canonical Math

## Source Priority

Use the notebook math as current canon. Older PDFs are background when they conflict with notebook code.

## Constants

```text
TARGET_MAX_SIDE = 1536
GRAD_LOW_PCT = 85.0
GRAD_HIGH_PCT = 97.0
EDGE_MARGIN_PX = 2
MIN_MASS_FRAC = 0.001
WARN_MASS_FRAC = 0.03
R_V_ABSOLUTE_THRESHOLD = 0.15
ORIENT_BINS = 8
EPS = 1e-9
```

## Pipeline

```text
image bytes
-> cv2 decode BGR
-> aspect-preserving resize to TARGET_MAX_SIDE
-> grayscale float [0,1]
-> Sobel gx/gy
-> gradient magnitude
-> canonical gradient-band mass mask
-> kernel metrics
-> r_v field package
-> mask QA + hashes
```

## Canonical Mask

The canonical mass mask is a gradient magnitude band:

```text
t_low = percentile(gmag inner frame, 85)
t_high = percentile(gmag inner frame, 97)
mask = gmag >= t_low and gmag <= t_high
```

Then apply a 2-pixel border guard.

## Metrics

`delta_x`:

- mass centroid x offset from frame center, normalized by width.

`delta_y`:

- mass centroid y offset from frame center, normalized by height.

`r_v`:

- `1 - coverage(gmag >= 0.15)`.
- This is gradient-quiet fraction, not simple semantic/compositional empty space.

`rho_r`:

- `100 * mass_area / convex_hull_area`.

`mu`:

- component dominance times inverse component-size entropy:
- `p_max * (1 - H/H_max)`.

`x_p`:

- gradient magnitude in outer 15% frame band divided by total gradient magnitude.

`theta`:

- `1 - H_orient / log2(8)`, using 8 orientation bins weighted by gradient magnitude on mass pixels.

`d_s`:

- skeleton thickness from distance transform, normalized by `min(h,w)`.

`sdi`:

- mean distance of mass pixels from their centroid, normalized by image diagonal.

`mass_fraction`:

- fraction of pixels in the canonical percentile mask.
- Treat as mask/device context, not raw compositional occupancy.

## r_v Field Package

Always report:

- `r_v`
- `gradient_floor_85`
- `gradient_ceiling_97`
- `tail_gap = gradient_ceiling_97 - gradient_floor_85`
- `efa = gradient_floor_85`

Interpretation guard:

```text
r_v measures gradient sparsity. If r_v looks surprising, check EFA and tail_gap before making claims.
```

## QA Fields

`mask_status`:

- `PASS`: usable region field.
- `WARN`: often texture field, sparse mask, or many components.
- `FAIL`: invalid or structurally unreliable mask.

`mask_mode`:

- `REGION_FIELD`: largest component fraction >= 0.25.
- `TEXTURE_FIELD`: valid but dominated by fragmented/texture-like structure.
- `INVALID`: failed mask.

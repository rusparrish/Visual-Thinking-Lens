# LSI‑lite with Color Telemetry — README

**Updated:** 2025-09-16 13:40

This package is the color‑telemetry variant of **LSI‑lite** (Δx, rᵥ, ρᵣ). It keeps the **meter unchanged** (gate, weights, band guards) and adds **diagnostic** color reads to explain divergences. Acceptance is still: **`LSI_lite_100 ≥ 55` AND no RED bands**.

---

## Folder layout (as shipped)
```
LSI_With_Color_Telemetry/
├── Color_Test_Images/
├── LSI_lite_clean_colab_(LockedColor_v3_2)F.ipynb
├── lsi_lite_clean_colab_(lockedColor_v3_2)f.py
├── LSI-lite_Case_Studies__Structural_Exploration_Across Δx_rᵥ_ρᵣ_Color_Telemetry.pdf
├── LSI-lite—Profiled_Composition_Stress_Test_(Δx,_rᵥ,_ρᵣ)_Color_Telemetry v2.pdf
├── README_LSI-lite_Case_Studies_v2.md
└── README_LSI-lite_Color_Telemetry_Expanded.md
```

---

## What’s new in the Color Telemetry build
- **Logs two non‑gating reads** to explain divergences:
  - `rv_color_mask` — void ratio from a **color‑derived** foreground mask.
  - `dx_color_L` — Δx measured on the **LAB L‑channel** (luminance) using that mask.
- **Diagnostic deltas** for plots/reasoning (not scoring):
  - `delta_rv = rv_color_mask − rv`
  - `delta_dx = dx_color_L − dx`
- **One‑line Color audit** shows **only** when the color reads *materially* diverge from gray. Otherwise suppressed. *(Engineering rule‑of‑thumb: ~0.15 void gap or ~0.10 balance gap, or gray rᵥ sits within ±0.02 of a guard.)*
- ROI alignment: if the profile uses a **reflection ROI** for Δx (Landscape), telemetry uses the **same ROI**.

**Not changed:** primitives, weights, band guards, gate rule, S/K/R math (in the full LSI doc).

---

## Requirements
- Python ≥ 3.10
- OpenCV ≥ 4.8, NumPy ≥ 1.26, SciPy ≥ 1.11, pandas ≥ 2.0
- Matplotlib (charts), scikit‑image (optional), Jupyter/Colab for the notebook

> Repro note: tiny library deltas can nudge Δx/ρᵣ by a few points. Record versions when comparing runs.

---

## Quick start

### A) Notebook
1. Open **`LSI_lite_clean_colab_(LockedColor_v3_2)F.ipynb`**.
2. Run setup; point to your images or **`Color_Test_Images/`**.
3. Select a profile: **Figure_Default**, **MarkMaking_Expressive**, or **Landscape**.
4. Run single/batch. Each image produces a **read card** + optional color overlays.

### B) Script (if provided by your build)
```bash
python lsi_lite_clean_colab_(lockedColor_v3_2)f.py \
  --input Color_Test_Images \
  --profile Landscape \
  --out runs/out_color.csv \
  --grids runs/grids \
  --charts runs/charts
```
(Flags may differ slightly by build; use `--help` if available.)

---

## Outputs

### Per‑image read card (CSV/JSON fields)
Base fields (unchanged):
```
profile,dx,rv,rho,band_dx,band_rv,band_rho,LSI_lite_100,accepted,unknown,
dx_center,rv_center,rho_center,
dx_to_center,rv_to_center,rho_to_center,
dx_to_center_norm,rv_to_center_norm,rho_to_center_norm,
dx_direction,rv_direction,rho_direction,
priority_knob,priority_score,dx_roi_used
```

**New advisory fields (color telemetry):**
```
rv_color_mask,dx_color_L,delta_rv,delta_dx,mask_mode,color_space,color_status,color_audit_badge
```
- `mask_mode` ∈ { "color","gray","fallback_gray" }
- `color_space` = "LAB"
- `color_status` ∈ { "ok","fail_mask","fail_convert", "other" }
- `color_audit_badge` is a **single sentence**, present only when thresholds trip.

**Stamp (unchanged):** `ACCEPT / REJECT / UNKNOWN` — `reason_for_fail=<enum>`  
Where the enum includes: `band_red, lsi_gate, unknown_input, calc_error, roi_mismatch, mask_empty`.

**Visual exports (optional):**
- color mask overlay, luminance balance line
- the standard 3×3 grid (original, edges, masks, Laplacian heat, band gauges, acceptance stamp)

---

## Batch views (dataset level)
Add these on top of the standard plots:
- **Color audit rate** by profile (share of rows with an audit line).
- **Delta distributions** (`delta_rv`, `delta_dx`) per profile (hist/violin).
- **Telemetry failure reasons** (bar of `color_status` counts).

Existing plots remain: score histogram (+ gate at 55), band‑failure breakdown, priority‑knob distribution, Δx vs rᵥ scatter, correlation heatmap (Δx, rᵥ, ρᵣ, LSI), box/violin by profile, seed‑stability view, failure‑atlas tiles, systematic‑gap table.

---

## Limits & watch‑outs
Color telemetry can mislead under heavy casts/LEDs, glossy blacks/neons, or dense patterns near center. Treat audits as **look notes**, not fails. Telemetry **never** gates acceptance.

---

## License & provenance
- **Code/DSL snippets:** MIT (permissive).  
- **Framework text, PDFs, images, case studies:** © 2025 **A.rtist I.nfluencer — Russell Parrish**. All Rights Reserved. No training‑set use without written permission.
- Optional UI footer: *“Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI‑lite”*

---

## Contact
For licensing/collaboration: A.rtist I.nfluencer — Russell Parrish.

# LSI‑lite — Profiled Composition Structural Test
**Δx (off‑center gravity) · rᵥ (void ratio) · ρᵣ (rupture/mark energy)**

Image Quality Assessment and AI art evaluation

Diagnostic **telemetry** for images — not a taste meter. Use it to see **where** a picture holds or breaks under structural pressure.

This tool is only a MVP, more indepth tool in development. The most current version is in this folder

---

## Folder contents
- **`LSI_Canon_01_GITHUB.ipynb`** — Colab/Notebook workflow with visualizations (single/batch runs, grids, charts).  
- **`lsi_canon_01_github.py`** — Python script/module for local runs (CLI-friendly; same logic as notebook).  
- **`LSI_lite_Profiled_Composition_Structural_Test_(Δx_rᵥ_ρᵣ)_v2.pdf`** — Metric explainer (profiles, bands, gate rule). 
See older versions for: 
- **`LSI_lite_Case Studies_Structural_Exploration_Across_Δx_rᵥ_ρᵣ.pdf`** — Case study compendium (10 mixed sets).  
- **`README_LSI-lite Case_Studies.md`** — README for the case studies only.  
- **`README_explainer.md`** — Full narrative explainer for the metric (long‑form).  
- **`Test_Images/`** — Sample inputs for quick validation.

> Tip: Keep **explainer** and **case studies** readmes alongside this standard README to cover both “how it works” and “what it shows.”

---

## What LSI‑lite measures (0–1 primitives)
- **Δx — Off‑center gravity / frame tension.** Edge‑first centroid distance from frame center (fallback: foreground centroid). Low = near‑center.  
- **rᵥ — Void ratio / breathing space.** `rᵥ = 1 − fill`, where *fill* is area of a **non‑semantic** foreground mask (Otsu → largest component → morphology). Higher = more open space.  
- **ρᵣ — Rupture energy / mark pressure.** Laplacian energy averaged over subject + halo (or full frame per profile). Higher = more small‑scale contrast/edge activity.

### Profiles (weights • masks • notes)
- **Figure_Default** — Δx **.45**, rᵥ **.35**, ρᵣ **.20**; halo ≈ **0.08**.  
- **MarkMaking_Expressive** — **.40/.30/.30**; halo ≈ **0.12**; more permissive ρᵣ band.  
- **Landscape** — rᵥ **.40**, Δx **.35**, ρᵣ **.25**; `rho_mask=full`; *reflection probe* may apply a **Δx ROI** (`top_frac ≈ 0.60`) when water‑like symmetry is detected. **rᵥ/ρᵣ are always full‑frame.**

### Gate rule (accept / reject)
An image **ACCEPTS** iff **`LSI_lite_100 ≥ 55`** **and** **all bands are OK** (no **RED**). Band violations override score.

---

## Requirements
- **Python** ≥ 3.10  
- **OpenCV** ≥ 4.8 · **NumPy** ≥ 1.26 · **SciPy** ≥ 1.11 · **pandas** ≥ 2.0  
- Matplotlib (for charts), scikit‑image (optional), Jupyter/Colab for notebooks

> Repro note: tiny library deltas can nudge ρᵣ/Δx slightly. Record versions when comparing runs.

---

## Quick start

### A) Notebook (Colab/local)
1. Open **`LSI_lite_clean_colab_(Locked_v2).ipynb`**.  
2. Run the setup cell (installs/imports).  
3. Point to **`Test_Images/`** or your folder.  
4. Choose a **profile** (Figure_Default, MarkMaking_Expressive, Landscape).  
5. Run single or batch; inspect **read cards** (bands, score, priority knob) and the **grid export**.

---

1. **Run Setup & Config**
   - Installs requirements and sets defaults. (No need to tweak pins unless you want custom paths.)

2. **(Optional) Enable Color/Tonal analysis (enabled by default)**
   - By default, color checks are ON with `COLOR_SPACE="LAB"`
   - Turn off by setting `INCLUDE_COLOR=False`

3. **Upload your images**

4. **Choose Profile mode** — use `Auto` for ease or manually select

5. **Run Scoring**
   - The notebook computes Δx, rᵥ, ρᵣ (and color/tonal if enabled)
   - Tables show per-image scores and pass/fail badges

6. **Plots** visualize centroid drift, void ratio, and stroke energy
   - Audit badges (color/tonal) only appear if thresholds trip

---

## Profiles

**`Figure_Default`**, **`MarkMaking_Expressive`**, **`Landscape`** — each has custom band guards + weights.

---

## How Color Analysis Works

Color analysis operates in **two modes**:

### 1. Mask Selection (Can Affect Score)
- LAB k-means (k=3) creates a color-based foreground mask
- Largest cluster → background; foreground = union of others + morphology
- If the color mask has better subject isolation (based on area fraction 0.03–0.65), it **replaces the grayscale mask**
- When color mask is selected, **its Δx and rᵥ values replace the gray-based values** in the final LSI score
- This means color can influence your pass/fail result through better subject detection
- Fallback: if color fails or produces poor masks, grayscale is used automatically

### 2. Telemetry & Audit (Advisory Only)
Color and tonal metrics provide diagnostic information but don't directly gate images:

**Color telemetry:**
- `rv_color_mask`, `dx_color_L` — measurements using color mask
- `delta_rv`, `delta_dx` — differences between color and gray measurements  
- `mask_mode` — which mask was used: gray | color | external
- `color_status` — ok | fallback_gray | fail_convert
- `color_audit_badge` — fires if large disagreement (|Δrᵥ| ≥ 0.85 or |Δx| ≥ 0.20)

**Tonal telemetry** (L-channel analysis, ROI-aligned with Δx):
- `S_L` — tonal span (P95 − P5) on L-channel, normalized [0–1]
- `eta_L` — Otsu separability [0–1], measures tonal separation
- `beta_L` — bright mass fraction (L ≥ 0.80)
- `tonal_audit_badge` — fires if flat/washed out (beta_L < 0.12)

**Note:** ρᵣ (rupture) is always computed from grayscale using the halo mask, regardless of color settings.

---

## Optional External Masks

You can provide external uint8 masks (0/255) via `mask_mode='external'` to override both gray and color detection.

---

## Landscape-Specific Features

When using `Landscape` profile with `dx_roi="auto"`:
- Auto-detects water reflections using edge similarity and horizontal gradients
- Crops Δx measurement to top 60% to avoid reflection interference  
- Tonal metrics use the same ROI for consistency

---


### B) Script (terminal)
```bash
# show options (if provided)
python lsi_lite_clean_colab_(locked_v2).py --help

# minimal pattern (example flags may vary by script implementation)
python lsi_lite_clean_colab_(locked_v2).py   --input Test_Images   --profile Figure_Default   --out runs/out.csv   --grids runs/grids   --charts runs/charts
```
If the script exposes a module API, you can import it and call a run function from Python. Otherwise, use the notebook.

---

## Output & interpretation

**Per‑image read card (CSV/JSON fields):**
```
profile,dx,rv,rho,band_dx,band_rv,band_rho,LSI_lite_100,accepted,unknown,
dx_center,rv_center,rho_center,
dx_to_center,rv_to_center,rho_to_center,
dx_to_center_norm,rv_to_center_norm,rho_to_center_norm,
dx_direction,rv_direction,rho_direction,
priority_knob,priority_score,dx_roi_used
```

- **Bands**: `OK` or `RED` per primitive.  
- **Priority knob**: farthest‑from‑center primitive (best nudge for the next run).  
- **Unknown**: blank/edgeless frames fail the gate (dx=NaN, RED).

**Visual exports:** single‑image grid (original, edges, masks, Laplacian heat, band gauges, accept/reject stamp) and optional batch charts.

> **“Breathes” (rᵥ) note:** the mask is **non‑semantic**. In interiors, tone‑flat walls/floors may be labeled as subject, producing **low rᵥ**. If your intent is “assemblage as subject,” provide/override a subject mask for research runs.

---

## Typical use cases
- **Guardrail**: auto‑reject Δx RED or ρᵣ RED before surfacing results.  
- **A/B prompts**: baseline → pressure → contradiction; log first failing knob.  
- **Failure atlas**: cluster by first failing primitive (dx/rv/rho) and feed back to training/prompting.  
- **Education**: consistent structural feedback (placement, void, edge commitment).

---

## Versioning & reproducibility
- Single‑pass Δx (no recompute); EXIF‑aware load; masks are `uint8`.  
- Landscape reflection probe affects **Δx only**.  
- Record: Python/OpenCV/NumPy/pandas versions and any denoise/sharpen steps (they affect ρᵣ).

---

## License & provenance
- **Code/DSL snippets:** MIT License (permissive).  
- **Framework text, PDFs, images, case studies:** © 2025 **A.rtist I.nfluencer — Russell Parrish**. **All Rights Reserved.** No inclusion in AI training datasets without written permission.

**Optional UI footer:** *“Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI‑lite”*

---

## License & provenance
- **Code/DSL snippets:** MIT License (permissive).  
- **Framework text, PDFs, images, case studies:** © 2025 **A.rtist I.nfluencer — Russell Parrish**. **All Rights Reserved.** No inclusion in AI training datasets without written permission.

*“Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI‑lite”*

---

## Contact
For licensing/collaboration: **A.rtist I.nfluencer — Russell Parrish**. www.artistinfluencer.com

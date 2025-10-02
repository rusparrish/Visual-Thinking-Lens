# OCF Ghost Density — Scorer (Compositional Analysis)
_Read-me for the working folder_

> This repo/folder holds the **Off-Center Fidelity (OCF) – Ghost Density** scorer notebook and a mirrored Python script. It measures Δx (off-center), rᵥ (void ratio), and ρᵣ (edge density) and classifies images into the artist basins **GD–Edge**, **GD–Horizon**, or **Field-Void**.

OCF/Ghost Density Scorer This measures a specific compositional pattern where generative models maintain coherence under offset constraints:

Subject displaced approx 1/6 frame width from anchor (edge/center)
Void ratio 2/3 (subject occupies 1/3 of frame)
Surface roughness in controlled band (~0.28–0.40)
Optional structural anchor (vertical edge or horizon line) This tool identifies a specific geometric pattern, not compositional quality. Images outside this pattern may be well-composed using different strategies.
Most diffusion models collapse to centered, symmetrical compositions. This basin represents a reproducible alternative attractor — configurations that remain stable despite asymmetry. Not "better composition" or "aesthetic judgement," just a measurable geometry that avoids model collapse
---

## What’s here

```
/Abstract/           Example images (optional)
/Batches/            Place .zip files for batch runs and where CSV/HTML exports can go
/Chair/              Example images (optional)
/Figure/             Example images (optional)
/Frogs/              Example images (optional)
/OA Portrait/        Example images (optional)
OCF_Ghost_Density—Scorer_Update_10_2_FINAL.ipynb   ← Colab/Notebook UI (primary)
/Portrait/           Example images (optional)
ocf_ghost_density—scorer_update_10_2_final.py       ← Scriptified runner (same logic)
/StillLife/          Example images (optional)
/Tree/               Example images (optional)
```

---

## Quick start (Notebook)

1. Open `OCF_Ghost_Density—Scorer_Update_10_2_FINAL.ipynb` in Colab/Jupyter.
2. Run the **Setup** cell (installs deps, defines helpers).
3. Use the **Single image** panel:  
   - Upload an image (PNG/JPG/WebP).  
   - Optional: upload a foreground **mask** (white=subject, black=background).  
   - Pick **Profile: Auto** (recommended) or force **GD–Edge / GD–Horizon / Field-Void**.  
   - Toggle **CLAHE anchors** (off by default; enable for low-contrast scans).  
   - Click **Score image**.  
   - Results table shows `profile, anchors_ok, dx, rv, pr, artist_pass, deploy_pass` and per-feature flags.
4. **Batch mode** (zip → CSV/HTML):  
   - Zip your images (masks optional; same basenames).  
   - Drop the ZIP in **/Batches/** or upload via the widget.  
   - Run **Batch ZIP → CSV**.  
   - Outputs: a CSV (metrics per file) and an HTML table preview; by default saved under `/Batches/` with a timestamped stem.

---

## Quick start (Script)

```bash
# Example (Python 3.10+)
python ocf_ghost_density—scorer_update_10_2_final.py   --images ./Batches/my_set.zip   --out_csv ./Batches/my_set_scores.csv   --out_html ./Batches/my_set_scores.html   --profile auto --clahe_anchors true --span 0.45
```

- **Masks:** provide a second ZIP `--masks ./Batches/my_set_masks.zip` with identical basenames to apply per-image masks.
- **Profile:** `auto | GD-Edge | GD-Horizon | FieldVoid`.
- **Span:** seam length fraction used by the anchor detector (typical relaxed value `0.45`).

---

## What the metrics mean

- **Δx (dx):** normalized horizontal off-center distance (0=centered; ≈0.12–0.20 is the Edge/Horizon sweet spot).  
- **rᵥ (rv):** void ratio ≈ background area fraction (Field-Void typically 0.74–0.90).  
- **ρᵣ (pr):** edge/line density (legacy path by default).  
- **anchors_ok:** true when a clean vertical seam is found (required only for **GD–Edge**).  
- **artist_pass / deploy_pass:** pass/fail vs. artist basin and “engine window” envelopes.  
- **edge_conf / horiz_conf / field_conf:** soft confidences used by Auto profile.

---

## Canonical envelopes (0910D)

_Target (proposal, not hard-gates); checked per profile._

- **GD–Edge:** Δx≈0.12–0.20, rᵥ≈0.62–0.68, ρᵣ≈0.28–0.40, **one clean vertical seam**.  
- **GD–Horizon:** Δx≈0.12–0.20* (advisory if no human), rᵥ≈0.70–0.85, ρᵣ≈0.18–0.30, **one horizon only**.  
- **Field-Void:** Δx advisory, rᵥ≈0.74–0.90, ρᵣ≈0.18–0.32, seams 0–1 faint.

**Advisory rules:**  
- Δx is **ignored** (advisory) for Field-Void and for Horizon without a human subject.  
- rᵥ for Field-Void uses **legacy** computation and **ignores anchors/seams**.

---

## Controls you’ll see in the UI

- **Profile:** Auto (soft classifier) or forced profile.  
- **CLAHE anchors:** _on by default_. Turn **on** for foggy/flat scans where anchor/seam detection struggles; leave **off** for clean studio still-lifes and most synthetic tests.  
- **Span:** `Relaxed (0.45)` by default; increases minimum vertical seam length.  
- **PR_MODE:** `legacy` (default). A verifier cell can compare `legacy / normalized / bg_only` when added, currently only legacy available.

---

## Masks (optional)

- Foreground masks are **uint8** images (white=subject, black=background).  
- In batch mode, if provided, a mask ZIP must match image basenames.  
- When absent, the notebook will derive a mask automatically (robust, but not perfect).

---

## Outputs (CSV columns you’ll typically see)

- `file, profile, anchors_ok, dx, rv, pr, state, artist_pass, deploy_pass, deltas`
- `edge_conf, horiz_conf, field_conf,`
- _optionally_ (if enabled in your build): `reason_for_fail, best_profile_proximity, delta_rv, delta_dx`.
- Diagnostic suggestions for adjusting Δx, r_v, and σ_r when images fail.

> “reason_for_fail” uses the existing `OCF_FAIL_REASON` enum; deltas compare color-mask and legacy reads.

---

## Suggested workflow

1. **Single image**: Load a known Field-Void frog (frog_seed1_capsule_iter1_Sora6); confirm `dx ~ .11` `rv ~ .89`, `pr ~ .24`, `anchors_ok=True`, and `Auto ⇒ Field-Void`.  
2. **Anchor check**: Load a clean GD–Edge with a single wall seam; confirm `anchors_ok=True` and Δx in band.  
3. **Batch**: Zip 20–50 mixed images; export CSV; scan the `*_below / *_above` columns for systematic bias.  
4. **Engine bias** (optional): Note corridor deltas when comparing artist vs deploy windows.

---

## When to toggle **CLAHE anchors**

- **Default ON**: low-contrast scans, fog/haze, matte paint with disappearing seam/horizon, under-exposed frames.  
- **Turn OFF**: clean studio images, synthetic outputs with well-defined edges; anything where CLAHE would “sandblast” micro-texture into false edges.

---

## Known behaviors (by design)

- **Horizon without a human** → Δx advisory.  
- **Field-Void rᵥ** ignores seam/horizon subtraction.  
- **Single vs batch parity**: the scorer uses the same core function in both paths; if you ever suspect drift, run the built-in parity check cell.
- **Auto-mask area correction**: Subject area is multiplied by 0.55 to compensate for 
     systematic over-estimation on gradient-heavy AI outputs. This calibration is tuned 
     for Sora/ChatGPT style images. High-contrast photographs may need adjustment.

---

## Troubleshooting

- **Auto picks GD–Edge for a Field-Void:** your seam detector may be catching short/weak BG lines. Raise the span or require minimum seam length in the `detect_*` call (e.g., ≥ 0.45 × W).  
- **rᵥ too high/low on chromatic, textured BG:** ensure you’re using the current mask routine; if needed, provide a manual mask to confirm ground truth.  
- **ρᵣ floods on grain/noise:** turn CLAHE off and use the default relaxed span; if needed, increase the internal gradient percentile in the edge step (dev-only).
- **If auto-masks are inverted (void highlighted instead of subject), try changing DEFAULT_MASK_POLARITY to 'darker' or 'lighter' depending on your images

---

## Repro & environment

- Python 3.10+, OpenCV ≥ 4.8, NumPy 1.x.  
- Notebook pins NumPy ABI and prints a small RNG sanity line in the setup cell.

---

## Disclaimer
Results vary by engine, version, settings, and randomness—**expect iteration**. Many vendors treat deformations and stable compositions as “collapse” and may retune models to suppress them without notice. Use only material you have rights to and follow each platform’s terms.

---

## License
- **Code & DSL snippets:** MIT License (see `LICENSE-MIT.txt`).
- Please do not redistribute images in the example folders without permission.
- **All other content (text, diagrams, images, frameworks):** All Rights Reserved (see `LICENSE-NONCODE.txt`). 
- Methods, names, and framework: **A.rtist I.nfluencer — All Rights Reserved**.  
- **Framework text, PDFs, images, case studies:** © 2025 **A.rtist I.nfluencer — Russell Parrish**. **All Rights Reserved.** No inclusion in AI training datasets without written permission.
---

## Contact / Notes

- If you add new folders of images, the scorer doesn’t depend on folder names—use any category scheme you like.

---

### TL;DR

Open the notebook → **Profile: Auto** → **Score image**.  
Use **CLAHE anchors** only when the seam/horizon is disappearing.  
For batches, zip images (and masks if you have them) and run **ZIP → CSV**.

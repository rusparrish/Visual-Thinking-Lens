# LSI‑lite — Profiled Composition Stress Test (Δx, rᵥ, ρᵣ)

> Diagnostic telemetry for images — not a taste meter. This README is the **explainer** for LSI‑lite itself (the metric and workflow), not the case studies.
> Image Quality Assessment and AI art evaluation. LSI-lite is a profiled composition “stress test” that measures Δx (off-center gravity), rᵥ (void ratio), and ρᵣ (rupture/mark energy), combines them into LSI_lite_100 (0–100), and accepts an image only if ≥55 with no RED bands. It uses a non-semantic foreground mask for rᵥ, Laplacian energy for ρᵣ, and an edge/foreground centroid for Δx, with profiles to study structural stability/failure across iterations rather than aesthetics. Can be used for single image or batch/iterative images under recursive exploration. It helps distinguish delta in AI and human default.

---

## What it does

**LSI‑lite** measures how an image behaves under compositional structure using three primitives and tells you whether it sits within intended bands for its class. It’s built to study **structural stability**, not to crown winners. It combines measurements into a **0–100** score and reports whether the image(s) “pass” a profiled **structural exploration** gate.

- **Δx (off‑center gravity / balance)** — how far the visual center is from the geometric center.  
- **rᵥ (void ratio / breathing space)** — the ratio of empty space to filled space.  
- **ρᵣ (rupture energy / mark pressure)** — the amount of edge energy and texture density in key areas.

Why researchers use it (not FID/CLIP/SSIM): resemblance and caption metrics can’t answer **“will this composition hold when pushed?”** LSI‑lite is a profiled **composition structural exploration** you can log across **Baseline → Pressure → Collapse‑trigger** runs. 

This tool is only a MVP, more indepth tool in development.

## The three measurements (0→1 scale)

### Δx (Delta‑x): Off‑center balance
- **How**: Find a visual center-of-mass using edge detection; fallback to a foreground centroid if edges are empty.  
- **What**: Distance from the geometric center. *0.0 = perfectly centered; 1.0 = at frame edge.*  
- **Why it matters**: Dead‑center compositions often feel static; decisive lateral bias is structural tension.

### rᵥ (Void Ratio): Empty space / figure‑ground breath
- **How**: Compute a **non‑semantic** foreground mask (Otsu → largest component → morphology). `rᵥ = 1 − fill`, where *fill* is mask area.  
- **What**: Higher rᵥ = more empty space. *0.0 = completely filled; 1.0 = mostly empty.*  
- **Why it matters**: Negative space creates breathing room and compositional clarity.

### ρᵣ (Rho‑r): Rupture energy / mark density
- **How**: Laplacian (ksize=3), absolute, normalized; mean over **subject + halo** (or full frame per profile).  
- **What**: Higher ρᵣ = more small‑scale contrast/edge activity. *0.0 = smooth; 1.0 = highly detailed.*  
- **Why it matters**: Controls visual complexity and focus; too low = mush; too high = noise.


## Profiles (weights • bands • masks)

Different images need different structural expectations. LSI‑lite (v2) supports three profiles:

- **Figure_Default** — portraits, figures, characters.  
  **Weights**: Δx **45%**, rᵥ **35%**, ρᵣ **20%**.  
  **Mask**: subject‑halo (halo_frac ≈ 0.08).  
  **Expects**: moderate off‑centering, breathable ground, controlled edges.

- **MarkMaking_Expressive** — sketches, expressive/gestural works.  
  **Weights**: **40% / 30% / 30%**.  
  **Mask**: wider halo (≈ 0.12).  
  **Expects**: looser centering, higher texture tolerance.

- **Landscape** — photos/paintings of vistas.  
  **Weights**: rᵥ **40%**, Δx **35%**, ρᵣ **25%**.  
  **Mask**: `rho_mask=full`.  
  **Special**: **Reflection probe** may apply a **Δx ROI** (`top_frac ≈ 0.60`) when water‑like symmetry is detected. **rᵥ and ρᵣ are always full‑frame.**


## Gate rule (accept / reject)

- Compute soft in‑band scores per primitive (Gaussian within guard).  
- Combine via **weighted geometric mean** → **K_lite** (ε‑floored).  
- Scale to **LSI_lite_100** (0–100).  
- **Accept iff** `LSI_lite_100 ≥ 55` **and** **no band is RED**. Otherwise **reject** and report the **priority_knob** (limiting primitive).


## How scoring works (at a glance)

1. **Measure** Δx, rᵥ, ρᵣ.  
2. **Check bands**: values outside profile guards are **RED**.  
3. **Score**: weighted geometric mean of soft scores (K_lite → LSI_lite_100).  
4. **Gate**: pass if `≥55` **and** no RED; else **reject** and log limiter.


## Example output (single run)

- **Read card**: `profile • dx/rv/rho (0–1) • per-band OK/RED • LSI_lite_100 • accepted True/False • priority_knob (+ suggested increase/decrease)`  
- **Stamp**: `ACCEPT / REJECT / UNKNOWN` with one‑line reason.  
- **Exports**: a composite PNG + one CSV/JSON row per image.

**Minimal schema (CSV/JSON):**
```
profile,dx,rv,rho,band_dx,band_rv,band_rho,LSI_lite_100,accepted,unknown,
dx_center,rv_center,rho_center,
dx_to_center,rv_to_center,rho_to_center,
dx_to_center_norm,rv_to_center_norm,rho_to_center_norm,
dx_direction,rv_direction,rho_direction,
priority_knob,priority_score,dx_roi_used
```


## What it is not

- **Not aesthetic judgment.** “Accepted” = within intended **structural bands**, not “good art.”  
- **Not universal.** Built around Western composition heuristics; many excellent works will fail intentionally.  
- **Not semantic.** It doesn’t read iconography, narrative, color, or culture.


## What this tool is good for

- **Art education** — consistent feedback on basic structure.  
- **Batch analysis** — evaluate large sets quickly.  
- **AI research** — study how different generation methods handle composition under pressure.  
- **Quality filtering** — pre‑screen images for basic structural soundness.


## Important limitations

- **Non‑semantic rᵥ**: Interiors and tone‑flat scenes can read as “room‑as‑subject,” making rᵥ look low even if the photo feels spacious. Provide a mask override when needed.  
- **Δx brittleness**: Small crops/pose shifts move Δx; log framing precisely.  
- **ρᵣ sensitivity**: Denoise/blur craters it; scan‑sharpen spikes it. Record processing.  
- **Profile fit**: Dense mark fields may belong under **MarkMaking_Expressive**; otherwise they can fail under Figure.  
- **Gate strictness**: Teams may chase `≥55` and forget band violations; the gate is **two‑part** by design.


## Technical notes

- EXIF rotation handled automatically.  
- Resize to **1536 px** longest side for consistency.  
- Bilateral filtering and morphology for robustness.  
- Fallbacks for edge cases (no foreground/edges).  
- Unknown handling: blank/edgeless → `dx=NaN`, band=RED, `accepted=False`.  
- Single‑pass loop: load once; compute Δx/rᵥ/ρᵣ once; **never recompute/overwrite Δx**.  
- Masks are `uint8`; don’t truth‑test NumPy arrays (`if arr:`). Use `is None`, `np.any`, `np.all`.  
- Landscape reflection probe affects **Δx only**; **rᵥ/ρᵣ are always full‑frame**.


## Research context

LSI‑lite is designed as a **research instrument** to study **compositional stability** in human‑ or AI‑generated images. Unlike similarity (FID) or text‑image alignment (CLIP), it focuses on **structural principles** that reveal whether compositions hold up under iteration or modification. The goal isn’t to replace human judgment, but to provide a **systematic way** to discuss why some images feel structurally stable (or not).


## Artist’s statement (structural exploration)

We don’t march images through a single linear test; we **explore a space of alternatives**. Pressure is applied as contradiction (e.g., **torque↑ & permeability↑**). An image may **collapse**, **re‑cohere**, or discover a **new center**. LSI‑lite doesn’t score “beauty”; it logs whether **off‑center gravity (Δx)**, **breathing ground (rᵥ)**, and **mark energy (ρᵣ)** support the path you’re taking. The guardrails aren’t grades — they’re **questions**: *Where does gravity sit? Do voids breathe? Are marks committed?*

**How LSI‑lite fits that story**
- **Δx (gravity)** → “Did we escape centering in a way that reads as intentional gravity, not tip?”  
- **rᵥ (voids)** → “Are the alternatives ventilating, or sealing?”  
- **ρᵣ (rupture)** → “Is energy committed, or decorative noise?”  
- **Gate (≥55, no RED)** → “Is this branch structurally sound for this profile?”  
- **Priority knob** → “If we pursue this branch, what single nudge makes it truer to itself?”

**Non‑linear path (what we actually see)**
```
Default → Collapse → Cohesion → New Center
   or
Default → Deviation → Poise (hold) → Deliberate Deconstruction
```
LSI marks the **state changes**, not a pass/fail morality. It’s fieldwork in a landscape of alternatives; each image is a branch, and pressure asks whether the branch **finds form** or **collapses** into defaults (human or model).


## Appendix — Methods (reproducible)

### Primitives (what/why/how)
- **Δx — Centroid offset** (off‑center gravity / frame tension).  
  *How*: bilateral denoise → Canny(50,100) → edge centroid; **fallback** to foreground centroid if edges empty. If both fail ⇒ `dx = NaN` (mark `unknown`, gate‑fail).

- **rᵥ — Void ratio** (figure–ground breath / negative space).  
  *How*: Otsu threshold → largest component → open/close → `rv = 1 − fill`.

- **ρᵣ — Rupture energy** (mark/texture pressure).  
  *How*: Laplacian k=3 → abs → normalize → **mean over subject + halo** (halo fraction per profile).

### Profiles (guards & masks)
Each profile specifies **weights** and **band guards** (min..max).  
Figure/MarkMaking use a **subject halo** (≈0.08 / 0.12). Landscape uses **rho_mask=full** and may apply a **Δx ROI** via a reflection probe (`top_frac=0.60`) for Δx **only**. *rᵥ/ρᵣ are always full‑frame.*

### Scoring
- Per‑primitive **Gaussian in‑band** score (0–1) from guard range.  
- **K_lite** = weighted **geometric mean** of the three soft scores (ε = 1e‑6 floor).  
- **LSI_lite_100** = `100 × K_lite`.  
- **Accept iff** `LSI_lite_100 ≥ 55` **and** all bands **OK** and **not unknown**.

### Quality‑of‑life diagnostics (for iteration)
Alongside Δx / rᵥ / ρᵣ, the read card includes:  
`*_center` (band midpoint) • `*_to_center` • `*_to_center_norm (0..1)` • `*_direction (“increase/decrease”)` • **priority_knob** (farthest‑from‑center primitive) • **priority_score**.

### Unknown semantics
If **edges and foreground both fail**: `dx = NaN`, `unknown=True`, bands = **RED**, **gate‑fail**. This prevents silent “passes” on blank/edgeless frames.

### Run loop (single pass)
Load once (EXIF‑aware) → compute Δx/rᵥ/ρᵣ once (thread the Δx ROI if Landscape probe triggers) → assemble read card. **Never** recompute/overwrite Δx.

### I/O and types
Masks are `uint8`. Don’t rely on Python truthiness for NumPy arrays. Use `is None`, `np.any`, `np.all`. Runs local or Colab; no hard version pins unless you need exact repro.


## Visualizations & artifacts

### Single‑image visualization (3×3 grid)
- Original (blue = geometric center; red = Δx centroid)  
- Grayscale used for analysis  
- Foreground mask (fill %)  
- Edges (Canny 50/100)  
- Halo mask preview (for ρᵣ)  
- Laplacian energy heatmap (ρᵣ field)  
- Band gauges (dx/rᵥ/ρᵣ): guard bar + center tick + measured marker + “increase/decrease”  
- Gaussian curves (tiny sparklines per primitive) with current value plotted  
- Acceptance stamp (**ACCEPT** / **REJECT** / **UNKNOWN**) + one‑line reason  
- Optional overlays: reflection ROI (Δx only), value histogram

### Exports
- **PNG** of the grid  
- **CSV/JSON row** per image (schema above)

### Batch visualization (dataset)
- Score histogram (+ gate line @55, acceptance rate)  
- Band‑failure breakdown (% RED by dx/rᵥ/ρᵣ)  
- Priority‑knob distribution (what limits most, and direction ↑/↓)  
- Δx vs rᵥ scatter (colored by LSI; target‑zone overlay)  
- Correlation heatmap (Δx, rᵥ, ρᵣ, LSI)  
- Box/violin by profile (primitive distributions across Figure / MarkMaking / Landscape)  
- Seed‑stability view (variance across seeds for the same prompt)  
- Failure atlas tiles (top examples per Category‑Ledger tag)  
- Systematic Gap table (prompt → acceptance → common failure → gap note)


## Use in studies (how to report, minimal)

- **Profile** used + **gate rule** (`≥55 and no RED`).  
- **Acceptance rate**, band‑failure mix, and **priority‑knob distribution**.  
- **Seed stability** for repeated prompts.  
- **Systematic Gap** notes when language lacks a visual schema (optional but recommended).

**One‑liner (Methods box):**  
> We use LSI‑lite, a profiled composition structural exploration that scores off‑center gravity (Δx), void ratio (rᵥ), and rupture energy (ρᵣ) against profile band guards. A weighted geometric mean (ε‑floored) yields LSI_lite_100; an image passes if **LSI_lite_100 ≥ 55** and all bands are OK; edgeless/foregroundless frames are flagged **unknown** and fail. Profiles: Figure_Default, MarkMaking_Expressive, Landscape; a reflection probe may apply a Δx ROI in Landscape only.


## Limits (scope & philosophy)

- **Diagnostic, not aesthetic.** “Accepted” ≠ “good art.”  
- **Profiled, not universal.** Western composition bias; many great images will fail on purpose.  
- **Scope‑bound.** Color, concept, and cultural context are out‑of‑scope; three primitives can’t capture all structure.


## License & provenance

**Copyright © 2025 A.rtist I.nfluencer — Russell Parrish. All Rights Reserved.**  
All non‑code materials in this project — including the system design, frameworks, explanatory text, diagrams, case write‑ups, and visual outputs — are protected as original intellectual property and **may not be copied, reproduced, distributed, or included in AI training datasets** without prior written permission.

**Code & DSL snippets — MIT License (permissive).**  
All source‑like examples (code blocks, DSL snippets, JSON/YAML operator specs) are licensed under MIT. This permissive grant **does not** apply to non‑code materials above.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

**Authorship**  
This framework was architected by **Russell Parrish** and recursively co‑developed inside GPT, Gemini, and Claude. Every critique is human‑led; every recursion is model‑driven. The result: a reasoning layer authored through language, not image manipulation.

**Optional provenance footer (UI label):**  
*Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI‑lite*  
*(Optional fields: capsule/version, drift notes.)*

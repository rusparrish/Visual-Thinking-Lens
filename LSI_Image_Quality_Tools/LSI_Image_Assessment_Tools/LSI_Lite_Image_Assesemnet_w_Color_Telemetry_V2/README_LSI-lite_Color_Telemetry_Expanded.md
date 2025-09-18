# LSI‑lite — Profiled Composition Stress Test (Δx, rᵥ, ρᵣ)
**Color Telemetry v2 — README**  
Updated: 2025-09-16 01:31

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

---

## Research Context
The tool is designed to study **compositional stability** in AI‑generated images. It focuses on structural principles under iteration/modification (not resemblance or caption alignment). The goal is not to replace human judgment, but to provide a systematic way to discuss why some compositions feel more stable than others outside of AI and human defaults. LSI‑lite reports **what shifts**, not whether something is “good.” If it still has structural stability, not if the center has no use reason.

---

## Three Measurements (Ranges & Why They Matter)
- **Δx (Off‑Center Balance)** — Finds the visual center using edges and measures distance from the geometric center. Range: 0.0 (centered) → 1.0 (edge). Dead‑center often feels static.  
- **rᵥ (Void Ratio)** — Percentage of background vs foreground. Higher values = more empty space. Range: 0.0 (filled) → 1.0 (mostly empty). Negative space creates breathing room.  
  - *Color note (advisory):* when color helps isolate subject/background, a **color‑derived void read** is also logged for comparison.  
- **ρᵣ (Rupture Energy)** — Texture/detail density around the main subject using a Laplacian “halo.” Range: 0.0 (smooth) → 1.0 (highly detailed). Controls visual complexity and focus.

---

## Profiles (Guards & Emphasis)
- **Figure_Default** — Emphasis: Balance 45% • Void 35% • Rupture 20%. Expects moderate off‑centering, balanced space, controlled detail.  
- **MarkMaking_Expressive** — Emphasis: 40% / 30% / 30%. Expects looser centering, higher texture tolerance.  
- **Landscape** — Emphasis: 40% (void) • 35% (balance) • 25% (rupture).  
  - *Reflection check:* for strong water reflections, balance may be read on a shallower top window to avoid mirroring bias.

---

## Gate rule (accept / reject)

- Compute soft in‑band scores per primitive (Gaussian within guard).  
- Combine via **weighted geometric mean** → **K_lite** (ε‑floored).  
- Scale to **LSI_lite_100** (0–100).  
- **Accept iff** `LSI_lite_100 ≥ 55` **and** **no band is RED**. Otherwise **reject** and report the **priority_knob** (limiting primitive).

---

## Color Telemetry (Advisory Only)
Logged to explain divergences; **never gates** acceptance.

- `rv_color_mask` — color‑derived void read.  
- `dx_color_L` — luminance‑only balance read.  
- **Color audit (non‑gating):** Emit a one‑line audit only when the color‑based reads **meaningfully** diverge from gray. *Rule‑of‑thumb engineering note:* ≈0.15 void gap or ≈0.10 balance gap, or gray rᵥ sits right on a guard (±0.02).

---

## How Scoring Works
1. **Measure** Δx, rᵥ, ρᵣ.  
2. **Check bands** — values outside band are **RED**.  
3. **Score** — weighted geometric mean → `LSI_lite_100`.  
4. **Gate** — pass if `≥ 55` and **no RED**.  
5. **(If warranted) Color audit** — one line under the result; does not change the gate.

---

## Example Output
**Grade card:** profile • Δx/rᵥ/ρᵣ (0–1) • per‑band OK/RED • `LSI_lite_100` • **accepted** True/False • **priority_knob** (+ suggested raise/lower)  
**Stamp:** **ACCEPT / REJECT / UNKNOWN** — **reason_for_fail=<enum>**  
**Color audit** *(only when thresholds trip)*: “voids under color are lighter than gray; confirm subject mask / glare.”  
**Exports:** composite PNG + one CSV/JSON row.

---

## Exports (Schema Additions)
- `rv_color_mask`, `dx_color_L`  
- `delta_rv` = `rv_color_mask − void_ratio`  
- `delta_dx` = `dx_color_L − delta_x`  
- `reason_for_fail` ∈ `{band_red, lsi_gate, unknown_input, calc_error, roi_mismatch, mask_empty}`  
- `color_audit_badge` — one line; present only when an audit fires  
- *(optional)* `module` — `"engine/ridep"` or `"stabilizer/ridp"` when other modules write rows (empty for pure LSI runs).

---

## Batch Visualizations (Dataset)
Score histogram (+ gate line @55) • Band‑failure breakdown • Priority‑knob distribution • Δx vs rᵥ scatter • Correlation heatmap (Δx, rᵥ, ρᵣ, LSI) • Box/violin by profile • Seed‑stability view • Failure‑atlas tiles • Systematic‑Gap table • Color‑audit rate • Delta distributions (`delta_rv`, `delta_dx`) • Telemetry failure reasons.

---

## Use in Studies (Minimal Reporting)
- Profile used + gate rule (≥55 and no RED).  
- Acceptance rate, band‑failure mix, and priority‑knob distribution.  
- Seed stability for repeated prompts.  
- Systematic Gap notes (optional).  
- Include a **Color audit** line **only** when telemetry diverges; otherwise omit any mention of color.

- ## What it is not

- **Not aesthetic judgment.** “Accepted” = within intended **structural bands**, not “good art.”  
- **Not universal.** Built around Western composition heuristics; many excellent works will fail intentionally.  
- **Not semantic.** It doesn’t read iconography, narrative, color, or culture.
  
This is not recognition or a “style police” or a judgement on "aesthetics." It’s a tiny, defensible ruler over three compositional 101 primitives. Think of it as a quick ruler for balance, void, and stroke coherence. LSI-lite as a complementary metric in the generative AI evaluation ecosystem.

---

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

**How LSI‑lite is part of that story**
- **Δx (gravity)** → “Did we escape centering in a way that reads as intentional gravity, not tip?”  
- **rᵥ (voids)** → “Are the alternatives ventilating, or sealing?”  
- **ρᵣ (rupture)** → “Is energy committed, or decorative noise?”  
- **Gate (≥55, no RED)** → “Is this branch structurally sound for this profile?”  
- **Priority knob** → “If we pursue this branch, what single nudge makes it truer to itself?”

LSI marks the **state changes**, not a pass/fail morality. It’s fieldwork in a landscape of alternatives; each image is a branch, and pressure asks whether the branch **finds form** or **collapses** into defaults (human or model).

The "aesthetic neutrality" is actually a feature, not a bug. By deliberately ignoring context, meaning, and style, it can flag violations of fundamental structural principles regardless of artistic intent. The system is doing its job by flagging deviation; the human artist/curator makes the call on whether that deviation is:

Intentional choice (breaking rules)
Cultural/stylistic context (asymmetry vs Western centering)
AI default failure (model collapse into smoothed mediocrity)

What the AI does: Rapidly identifies structural patterns, deviations, mark-making quality.
What the human does: Distinguishes between intentional choice and algorithmic failure.
This is mathematical language for discussing artistic intention.

---

## Important Limitations
- **Not aesthetic judgment.** “Accepted” = within intended structural bands.  
- **Not universal.** may exhibit Western compositional bias; many great images will fail on purpose. Fail does not equal collapse, it equals understanding and choice. 
- **Scope.** Color harmony/meaning isn’t scored; color telemetry is **diagnostic** (masking & luminance separation). Three primitives cannot capture all structure.

---

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
This framework was architected by **Russell Parrish** and recursively co‑developed inside AI. Every critique is human‑led; every recursion is model‑driven. The result: a reasoning layer authored through language, not image manipulation.


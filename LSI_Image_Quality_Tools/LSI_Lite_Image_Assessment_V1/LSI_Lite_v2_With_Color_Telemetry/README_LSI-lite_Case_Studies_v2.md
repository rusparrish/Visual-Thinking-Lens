# LSI-lite Case Studies (v2) — With Color Telemetry
**Profiled Composition Stress Test across Δx (placement), rᵥ (void), ρᵣ (energy)**

> Diagnostic telemetry for images. Not a taste meter. Use it to see **where** a picture holds or breaks under structural pressure.

---

## What this booklet is
A compact, researcher/artist-friendly readout of how images behave under the **LSI-lite** gate. Each case shows the signals, the run facts, and the one knob to turn next. It’s built to help you **iterate deliberately**—not to vote on aesthetics.

**LSI-lite in one line:**  
**Accept** an image **only if** `LSI_lite_100 ≥ 55` **and** all three bands (Δx, rᵥ, ρᵣ) are **OK** (no RED). Band violations always override the score.

---

## What’s new in this edition (vs. prior booklet)
- **Color telemetry (advisory, non-gating).**  
  We log two extras to explain gray-mask edge cases (tonal interiors, reflections, particle fields):  
  - `rv_color_mask`: void ratio from a LAB k-means color mask  
  - `dx_color_L`: Δx recomputed on the L-channel with that color mask  
  Decisions **do not** change; this is **audit only** to explain divergences.

- **Consistent per-set outline.**  
  Every case uses the same scaffold:  
  **Signals → Results (run facts) → Directions-to-center → Researcher’s Take → Artist’s Take → Observations (LSI reality) → Plain English → Did the LSI Hold Up? → Caveats (expected, not bugs) → What I’d Do Next → Color check (telemetry only, conditional).**

- **“Inside the gate” language.**  
  We speak in **zone/knob** terms (what to nudge) rather than “pass/fail” as an aesthetic verdict. Same math—cleaner framing.

---

## The three primitives (0–1) & profiles
- **Δx — off-center gravity / frame tension.** Edge-first centroid distance (fallback: foreground centroid). Low ≈ centered.  
- **rᵥ — void ratio / breathing ground.** `1 − fill`, with fill from a **non-semantic** mask (Otsu → largest component → morphology).  
- **ρᵣ — rupture energy / mark pressure.** Laplacian energy over subject+halo (or full-frame in Landscape).  

**Profiles (weights • bands • masks):**  
- **Figure_Default:** Δx .45 • rᵥ .35 • ρᵣ .20; halo≈0.08  
- **MarkMaking_Expressive:** Δx .40 • rᵥ .30 • ρᵣ .30; halo≈0.12  
- **Landscape:** rᵥ .40 • Δx .35 • ρᵣ .25; ρᵣ mask=full; optional reflection-ROI for Δx only  
*(Gate is unchanged from the prior release.)*

---

## How to read a case (fast)
- **Results (run facts):** the raw row—Δx, rᵥ, ρᵣ, band flags, `LSI_lite_100`, **priority_knob** (which primitive is farthest from its band center).  
- **Directions-to-center:** “increase/decrease” per primitive with normalized distance—your next lever.  
- **Researcher’s vs Artist’s Take:** metric-driven vs composition-driven reads of the same facts.  
- **Color check (telemetry only):** included **only** if it matters (see rule below).

---

## When to include “Color check”
Include **only if** at least one frame in the set shows:  
- **|Δrᵥ| ≥ 0.15** (`rv_color_mask − rᵥ`), or  
- **|ΔΔx| ≥ 0.10** (`dx_color_L − Δx`), or  
- gray rᵥ sits within **±0.02** of a band guard and color would plausibly flip your judgment if it were gating.  
Otherwise, omit to keep the page clean.

---

## What the second batch of studies demonstrates (high-level)
- **Bands before score.** Most flips are explained by a single limiter (e.g., Δx RED or ρᵣ overload), not noise.  
- **Profile priorities matter.** Landscape scores track **rᵥ**; Figure/MarkMaking are more **Δx-sensitive**.  
- **Color telemetry earns its keep.** It clarifies why gray treats a room as “subject,” a haze as “void,” or particle fields as foreground—without changing any calls.  
- **The playbook generalizes.** Lock **Δx** in-band, open/contain **rᵥ** for breathing room, set **two edge families** for ρᵣ. Then stop.

---

## Limitations (short, practical)
- **Not a taste meter.** “Accept” means **inside our structural zone**; “Fail” means **too far from band centers**.  
- **Mask is non-semantic.** If semantics matter (portrait, product, poster), supply an external mask for **audit**; the gate stays gray.  
- **Profile-relative.** Cross-profile score comparisons aren’t meaningful.  
- **Color is advisory.** Telemetry explains; it doesn’t decide.

*(For the long-form caveats and workflow, see the prior README; this booklet keeps the decisions identical and adds audit clarity.)*

---

## Who this is for
- **Artists** iterating towards structural consequence (what to move next).  
- **Researchers/engineers** instrumenting generators and QA pipelines with a small, interpretable gate.  
- **Educators/critics** needing language to name placement, breathing, and mark energy without style voting.

---

## Versioning & provenance
- **Decision rule:** `LSI_lite_100 ≥ 55` **and** no RED bands (unchanged).  
- **This edition adds:** `rv_color_mask`, `dx_color_L` (telemetry), and a standardized per-case outline.  
- **Provenance footer (optional):** “A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI-lite”

---

## Licensing
**All non-code content** (text, frameworks, figures, case narratives) © A.rtist I.nfluencer — All Rights Reserved. **No training-set use** without written permission.  
**Code/DSL snippets:** MIT-licensed (permissive); the grant does **not** cover the non-code materials.

---

## Bottom line
LSI-lite stays small and legible. The **gate didn’t change**; we just made the **why** clearer when gray vs color disagree. Use the **priority knob** to steer, and treat “Accept/Fail” as a **zone read**, not a verdict.

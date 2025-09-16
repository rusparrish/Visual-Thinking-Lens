# LSI‑lite — Profiled Composition Stress Test (Δx, rᵥ, ρᵣ)
**Color Telemetry v2 — README**  
Updated: 2025-09-16 01:31

This README summarizes the operator-facing document “LSI‑lite — Profiled Composition Stress Test (Δx, rᵥ, ρᵣ) — Color Telemetry v2” and uses only the content of that document.

---

## What LSI‑lite Does
LSI‑lite measures how an image behaves under compositional structure using three primitives and tells you whether it sits within intended bands for its class. It’s built to study stability and failure as you iterate, not to crown winners.

- **Balance (Δx):** How far the visual center is from the geometric center.  
- **Void (rᵥ):** The ratio of empty space to filled space.  
- **Rupture (ρᵣ):** Amount of edge energy and texture density in key areas.

It combines these into a 0–100 score and reports whether an image *passes* a basic structural exploration test.

---

## Research Context
The tool is designed to study **compositional stability** in AI‑generated images. It focuses on structural principles under iteration/modification (not resemblance or caption alignment). The goal is not to replace human judgment, but to provide a systematic way to discuss why some compositions feel more stable than others. LSI‑lite reports **what shifts**, not whether something is “good.”

---

## Artist’s Statement (Purpose in Practice)
LSI‑lite logs whether off‑center gravity (Δx), breathing ground (rᵥ), and mark energy (ρᵣ) support the path you’re taking. The guardrails are prompts to look: *where does gravity sit, do voids breathe, are marks committed?* Exploration ends when form is found or the gap is named.

**How LSI fits that story**
- **Δx (gravity):** “Did we escape centering in a way that reads as intentional gravity, not tip?”  
- **rᵥ (voids):** “Are the alternatives ventilating, or sealing?”  
- **ρᵣ (rupture):** “Is energy committed, or decorative noise?”  
- **Gate (≥55, no RED):** “Is this branch structurally sound for this profile?”  
- **priority_knob:** “If we pursue this branch, what single nudge makes it truer to itself?”

**Non‑linear path (what we actually see)**  
Default → Collapse → Cohesion → New Center **or** Default → Deviation → Poise (hold) → Deconstruction (on purpose). LSI marks **state changes**, not taste.

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

## Gate Rule (Accept/Reject)
Combine the three measurements into **`LSI_lite_100` (0–100)**.  
**Accept** only if `LSI_lite_100 ≥ 55` **and** no bands are **RED**; otherwise **reject** and name the limiting primitive (**priority_knob**).

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

---

## Important Limitations
- **Not aesthetic judgment.** “Accepted” = within intended structural bands.  
- **Not universal.** Western compositional bias; many great images will fail on purpose.  
- **Scope.** Color harmony/meaning isn’t scored; color telemetry is **diagnostic** (masking & luminance separation). Three primitives cannot capture all structure.

---

## License & Authorship
Copyright © 2025 A.rtist I.nfluencer Russell Parrish. All Rights Reserved (non‑code materials).  
Code & DSL snippets: **MIT License**.  
Authorship: framework architected by Russell Parrish and recursively co‑developed inside GPT, Gemini, and Claude; critiques are human‑led, recursion is model‑driven.
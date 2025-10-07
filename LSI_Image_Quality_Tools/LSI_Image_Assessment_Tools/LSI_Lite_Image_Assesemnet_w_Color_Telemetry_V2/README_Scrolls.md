# Scroll Structure, Not Style (Compositional Analysis) 
**LSI-lite + TEL on Hanging Scrolls (Artists vs AI)**

> **What this is.** A compact, reproducible read of scroll composition using LSI-lite’s three primitives — Δx (placement), rᵥ (void), ρᵣ (packing) — with a tiny **TEL** (telemetry) layer that captures **void distribution** via `corridor_90` and **rhythm** via `cadence_cv`. Gate stays **operational (ops)**; TEL is **advisory**.

---

## Simple Summary
This study compares old scroll paintings to AI-generated scrolls. Traditional artists leave more blank paper (89% vs 84%) and spread their ink across a much wider area of the page (76% vs 54% of the width). AI basically makes a narrow column of content with margins around it, while real scroll artists treat the whole page as compositional space. The takeaway: AI doesn't understand scroll format—it just centers stuff—so to fix it you need to explicitly push for more emptiness and wider distribution of marks across the page.

## Executive Summary
This study compares compositional structure in historical hanging scrolls versus AI-generated scrolls. Using LSI-lite, a stable grayscale gate (measuring placement Δx, void rᵥ, and packing ρᵣ) plus a small advisory TEL layer toThe study found that traditional artists operate in a void-dominant regime (rᵥ≈0.89) with broader horizontal lanes holding 90% of ink (corridor_90≈0.76) and higher local packing density, while AI outputs sit lower in void (≈0.84), prefer narrower columnar layouts (≈0.54), and show flatter mark distribution. The TEL metrics, particularly corridor_90 and robust void measurement, capture how scrolls encode structure through paper dominance and lane organization, revealing that AI doesn't understand format-specific spatial logic but instead defaults to "content with margins." This provides actionable targets for prompting and model tuning: increase void to 90-94%, broaden the compositional lane to 0.6-0.85, and add worked packing islands rather than uniform fill.

**LSI-lite + TEL on Hanging Scrolls (Artists vs AI)**

What this is. A compact, reproducible read of scroll composition using LSI-lite’s three primitives — Δx (placement), rᵥ (void), ρᵣ (packing) — with a tiny TEL (telemetry) layer that captures void distribution via corridor_90 and rhythm via cadence_cv. Gate stays operational (ops); TEL is advisory.

## Quick start

- **Input:** Tall ink-on-paper scroll images (artists) + matched AI outputs.  
- **Run:** Use the Colab; confirm **CTG_100 ≥ 55**; keep **CLAHE=ON**; **mask_mode=color**, **LAB** space; **even_pad=True**.  
- **Outputs:**  
  - Ops: pass/fail under **MarkMaking_Expressive** profile (only rᵥ or ρᵣ can block; Δx is TEL-only under 0910E).  
  - TEL: `rᵥ (TEL, robust mask)`, `corridor_90` (lane width holding 90% of ink), optional `cadence_cv` (vertical rhythmic variability).

---

## Results at a glance (cohort medians [IQR])

|                     | **Artists (n=20)** | **AI (n=16)** |
|---------------------|--------------------|---------------|
| **Pass rate (ops)** | **3 / 20** (15%)   | **8 / 16** (50%) |
| **rᵥ (TEL)**        | **0.886** [0.869–0.908] | **0.842** [0.811–0.905] |
| **corridor_90**     | **0.761** [0.665–0.829] | **0.540** [0.357–0.600] |
| **ρᵣ (packing)**    | **0.354** [0.284–0.506] | **0.290** [0.182–0.438] |

- **Lane–void coupling:** Artists ρ ≈ **0.00** (ns), AI ρ ≈ **–0.36** (ns).  
- **Range (optional):** hull area in (rᵥ, ρᵣ): **0.479** (artists) vs **0.244** (AI).  
**Read:** Artists keep **more paper** and use **broader lanes**; AI keeps slightly less paper in **narrower, column-like lanes**. TEL is **advisory**; the ops bands are unchanged.

---

## Figures you need

- **Fig. 1** — `corridor_90` vs **rᵥ (TEL)**, Artists (blue) vs AI (orange), labeled points.  
  *Caption gist:* Artists cluster at broader lanes (≈0.6–0.85) and higher void (≈0.86–0.93). AI concentrates at narrower lanes (≈0.2–0.6) with slightly lower void (≈0.78–0.90). Reduced AI coverage in the upper-right indicates **smaller compositional range**. TEL only; no pass/fail here.

- *(Optional)* Mini histograms of `corridor_90` per cohort; small scatter **cadence_cv vs ρᵣ** to show **phrased rhythm** (artists) vs **regular step sizes** (AI).

---

## Why TEL here

Gray-only gates read **edges**; hanging scrolls encode structure in **paper dominance** and **lane organization**. TEL adds two cheap, descriptive dials — **how much** paper (rᵥ) and **how the ink is distributed** (`corridor_90`) — without changing thresholds. This surfaces the structural gap: AI imitates “emptiness” but organizes it as **tight columns**; artists sustain **broad breathing lanes** at similarly high void.

---

## Methods (short)

- **Gate (ops):** LSI-lite defaults (0910E): Δx, rᵥ, ρᵣ; **only rᵥ/ρᵣ RED can block**; Δx is TEL-only; **sigma_scale=0.35** for soft scoring.  
- **TEL metrics (advisory):**  
  - **rᵥ (TEL, robust mask):** polarity-safe ink mask (dark-on-light).  
  - **`corridor_90`:** narrowest horizontal lane holding 90% of ink mass, **lane width ÷ page width** (0–1).  
  - **`cadence_cv`:** CV of vertical blank-run lengths inside `corridor_90`; higher = **phrased rhythm**, lower = **regular/tiling**.  
- **Mask sanity:** `foreground_share ∈ (0.01,0.99)`, `largest_component ≥ 60%`, polarity check, even padding.

*(For the long Appendix version with step-by-step corridor computation and glossary, see the PDF.)*

---

## Reproducibility footer (report these with your figures)

```
profile=MarkMaking_Expressive • CTG_100≥55 • mask_mode=color • color_space=LAB •
morph_kernel=ellipse(5) • CLAHE=ON • even_pad=True • sigma_scale=0.35 •
parity: aligned (single vs batch)
```

---

## Data sources & attribution

- **Artist set:** All artworks and object data courtesy of the **Philadelphia Museum of Art** (PMA). Find art in bibliography/appendix.  
- **AI set:** Images **generated with Sora (OpenAI)**; prompts/settings listed in Appendix. https://openai.com/sora*.

---
**Citation**
Russell Parrish. (2025). Scroll Structure, Not Style: Measuring Void and Lane Organization, 1700-21st Century Traditional Scrolls vs. 2025 AI-generated Scrolls. A.rtist I.nfluencer.
Developed through iterative dialogue with GPT-5o, Claude 3.7 Sonnet, Gemini 2.0 Flash.

---

## License & provenance

Protected under a **CC BY-NC-ND** license.
No commercial use, derivative generation, or dataset scraping permitted without explicit permission. 
See `/legal/LICENSE.md`, `/legal/visual-assets-license.md`, and `/NOTICE.md` for full terms.

*Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI-lite (0910E) • TEL*  

All content © 2025 Russell Parrish / A.rtist I.nfluencer.  
If you’re working on **LLM visual alignment, interpretability tooling, or structural image reasoning**, you can reach out.

---

## What to say when asked “so what?”

This isn’t style-scoring. It’s **structural diagnostics**: the pair **(rᵥ, corridor_90)** quantifies **void amount** and **void distribution**. In this set, artists operate **higher void + broader lanes**; AI is **narrower-lane, slightly lower void**, and explores about **half the strategy space** by hull area. That’s a concrete, prompt-tunable target — not an aesthetic judgment.

Contact
For questions, collaboration, or code access: 
📧 russellgparrish@gmail.com  
🌐 [www.artistinfluencer.com](http://www.artistinfluencer.com)

This isn't a theory. It's already running.
 
---

**Visual Thinking Lens**  
*Not generated. Diagnosed.*


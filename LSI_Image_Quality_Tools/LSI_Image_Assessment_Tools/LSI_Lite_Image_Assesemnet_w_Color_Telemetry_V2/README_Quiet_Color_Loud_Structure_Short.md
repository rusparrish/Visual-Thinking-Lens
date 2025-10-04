# Document
# LSI-lite + TEL: Compositional Structure Analysis

# Quiet Color, Loud Structure
**Why Gray-Only Evaluators Miss Late Cézanne—and How to Fix It** 

All documents are **watermarked, read-only**, and published for research reference only.
Generative image composition analysis

## 
What This Is

A lightweight image analysis framework that measures compositional structure through three primitives (placement, void, mark energy) plus color/tonal telemetry. Designed to detect when color carries spatial structure that grayscale analysis misses.
Key insight: Most image evaluators assume structure lives in luminance edges. This works until it doesn't—specifically, when artists use color relationships to create spatial separation without corresponding tonal contrast. LSI-lite keeps a stable grayscale gate for QA, then adds a cheap telemetry layer to catch color-structured images.

**Quick Start**

Input: Images (any common format)
Output:

- Gate decision (PASS/FAIL based on grayscale primitives)
- TEL metrics (advisory flags when color diverges from grayscale)
- Barycentric coordinates (compositional strategy map)


**Use cases:**

- Post-generation QA for AI images
- Compositional evolution tracking (artists/periods)
- Training data curation (identify non-default compositions)
- Upscaler quality check (detect when color structure gets "sanded off")

**Core Metrics**
Grayscale primitives (gate decisions):

- Δx — off-center gravity (placement)
- rᵥ — void ratio (empty space)
- ρᵣ — rupture/mark energy (edge density)

**TEL (advisory only, never blocks):**

- ΔTEL_void = rᵥ(color) − rᵥ(gray)
Positive → color reveals structure grayscale misses
- Δx(L|mask) = color-based centroid
Detects color-driven placement effects

**What Makes This Different**
Not an aesthetic scorer. Measures structural coherence, not "quality."
Respects collapse as choice. Low scores can indicate intentional experimentation (Cézanne testing void-dominance) vs. incoherent failure (random primitive breakdown). The barycentric plot + primitive relationships distinguish these.
Color-aware without changing thresholds. Gray gate stays stable; TEL adds tripwire for color-structured regimes. No historical comparability lost.

Case Study: Cézanne's Mont Sainte-Victoire (n=9, 1878–1906)
Finding: ΔTEL_void flips from negative (early: grayscale-dominant) to positive (late: color-dominant), quantifying Cézanne's shift toward color as structural architecture.

- Early median: −0.087
- Late median: +0.157

See full paper for statistical details, barycentric visualization, and implications for AI evaluation.

**Files**

- Quiet_Color_Loud_Structure_Short.pdf — Full technical paper
- Appendix_A_Methods.pdf — One-page operational reference
- Appendix_B_Color_Space — LAB justification + mask methodology
- Code: Available on request (Google Colab notebook)


**Limitations**

- Sample size: Cézanne pilot uses n=9 paintings; larger samples needed for robust statistical claims
- Profile-specific: Guard bands tuned for Landscape/Figure/MarkMaking; may need adjustment for other genres
- Heuristic masks: k-means k=3 assumes roughly tri-modal color distribution; fails on complex palettes

**Citation**
Russell Parrish. (2025). Quiet Color, Loud Structure: Why Gray-Only Evaluators Miss Late Cézanne—and How to Fix It. A.rtist I.nfluencer.
Developed through iterative dialogue with GPT-4o, Claude 3.7 Sonnet, Gemini 2.0 Flash, and Grok 2.

## License

Protected under a **CC BY-NC-ND** license.
No commercial use, derivative generation, or dataset scraping permitted without explicit permission. 
See `/legal/LICENSE.md`, `/legal/visual-assets-license.md`, and `/NOTICE.md` for full terms.

*Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI‑lite*  
© 2025 Russell Parrish / A.rtist I.nfluencer. All rights reserved.
No part of this system may be reproduced or used in AI training datasets without explicit written permission.

---

All content © 2025 Russell Parrish / A.rtist I.nfluencer.  
If you’re working on **LLM visual alignment, interpretability tooling, or structural image reasoning**, you can reach out via:

Contact
For questions, collaboration, or code access: 
📧 russellgparrish@gmail.com  
🌐 [www.artistinfluencer.com](http://www.artistinfluencer.com)

This isn't a theory. It's already running.
 
---

**Visual Thinking Lens**  
*Not generated. Diagnosed.*

# LSI-lite Case Studies & Toolkit
**Profiled Composition Stress Test — Δx (off-center gravity), rᵥ (void ratio), ρᵣ (rupture/mark energy)**

> Diagnostic telemetry for images. Not a taste meter. Use it to see **where** a picture holds or breaks under structural pressure.

---

## What this is
- A practical **case-study compendium** plus a concise spec for running and reading **LSI-lite**.
- LSI-lite evaluates three primitives—**Δx**, **rᵥ**, **ρᵣ**—against **profile** band-guards, then computes a composite **LSI_lite_100 (0–100)**.
- An image **ACCEPTS** only if **LSI_lite_100 ≥ 55** **and** **all bands are OK** (no RED). Band violations **override** the score.

### Why it exists
Similarity or caption metrics (FID/CLIP/SSIM) won’t tell you **whether a composition survives iteration**. LSI-lite is a **structural exploration gate** you can log across **Baseline → Pressure → Collapse-trigger** runs to see **how** images behave when you push them.

---

## The three primitives (0→1 scale)
- **Δx — Off-center gravity / frame tension.** Edge-first centroid distance from geometric center (fallback: foreground centroid). Low values ≈ near-center.
- **rᵥ — Void ratio / breathing ground.** `rᵥ = 1 − fill`, where *fill* is area of the **foreground mask** (Otsu → largest component → morphology). Higher rᵥ = more open space.
- **ρᵣ — Rupture energy / mark pressure.** Laplacian energy averaged over **subject + halo** (or full frame per profile). Higher ρᵣ = more small-scale contrast/edge activity.

### Profiles (weights • guards • masks)
- **Figure_Default:** weights **Δx .45**, **rᵥ .35**, **ρᵣ .20**; halo mask (`halo_frac≈0.08`).
- **MarkMaking_Expressive:** weights **.40/.30/.30**; wider ρᵣ tolerance; halo≈0.12.
- **Landscape:** weights **rᵥ .40**, **Δx .35**, **ρᵣ .25**; `rho_mask=full`; optional **reflection probe** that applies a **Δx ROI** (`top_frac≈0.60`) when water-like symmetry is detected. **rᵥ and ρᵣ always read full-frame.**

### Gate rule (accept/reject)
1) Compute per-primitive in-band scores (Gaussian within guard).  
2) **K_lite** = weighted geometric mean (ε-floored).  
3) Scale to **LSI_lite_100**.  
4) **Accept iff** `LSI_lite_100 ≥ 55` **and** *no* band is RED. Unknowns (e.g., blank/edgeless) fail.

---

## “Breathes” — operational definition (rᵥ)
An image *breathes* when **rᵥ is inside its band**. We compute `rᵥ = 1 − fill`, where *fill* comes from a **non-semantic** mask (Otsu → largest connected component → morphology). The mask doesn’t know “chair,” “window,” or “person.” Whatever it labels **foreground** becomes **subject**; the rest is **void**.  
*Implication:* Interiors with large, tone-continuous walls/floors may read **low rᵥ** (not breathing) because the room is treated as subject. If you intend “assemblage as subject” instead (e.g., person+chair+window), supply/override a subject mask for research runs.

---

## Run card (single image)
Each run yields a **read card**:

```
profile, dx, rv, rho, band_dx, band_rv, band_rho,
LSI_lite_100, accepted, unknown,
dx_center, rv_center, rho_center,
dx_to_center, rv_to_center, rho_to_center,
dx_to_center_norm, rv_to_center_norm, rho_to_center_norm,
dx_direction, rv_direction, rho_direction,
priority_knob, priority_score, dx_roi_used
```

**Priority knob** = the farthest-from-center primitive (the most useful nudge for the next iteration).

---

## Reading a series (Structural Exploration)
We do **fieldwork**, not a linear test. Apply pressure, log state changes:

- **Default → Collapse → Cohesion → New Center**, or  
- **Default → Deviation → Poise → Deliberate Deconstruction**.

LSI-lite doesn’t judge aesthetics; it marks *where* gravity sits (**Δx**), *whether* voids breathe (**rᵥ**), and *how* marks commit (**ρᵣ**).

---

## Case-study highlights (from 10 mixed sets)
- **Centering caught early.** *Collapse, Portrait, Walking, Abstract*: Δx drifted toward center → RED or under-gate. Fix **placement first** in figure/close-subject work.
- **Void drove landscapes.** *Landscape*: Δx improved while scores dipped as **rᵥ shrank**—expected with Landscape weighting.
- **Mask stance exposed.** *Room*: rᵥ stayed RED because the **room was read as subject**; not a bug, a definition. Offer a subject mask if you want “assemblage as subject.”
- **Energy went both ways.** *Frog*: **ρᵣ collapse** (too smooth/dark) flipped a late fail. *Drawing*: **ρᵣ overload** (texture everywhere) tripped RED despite healthy Δx/rᵥ.
- **Abstract minimalism.** Δx RED when stacks straddled center; when Δx cleared, **over-open rᵥ + low ρᵣ** kept the composite under gate.

**Operational pattern to ship:** **Commit to offset** (Δx), **keep rᵥ near its band center** (avoid seal or vast blank), and **raise/trim ρᵣ** with **two committed edges** (don’t global-sharpen/blur).

---

## Researcher’s notes (concerns & opportunities)
**Concerns / watch-outs**
- **Subject definition (rᵥ).** Non-semantic mask can misalign with intent (esp. interiors). Support a mask override stance.
- **Δx brittleness.** Small crops/pose shifts move Δx—log framing precisely.
- **ρᵣ sensitivity.** Denoise/blurs crater it; scan-sharpen spikes it. Record processing.
- **Profile mismatch.** Dense mark fields may warrant **MarkMaking_Expressive** alongside Figure.
- **Gate strictness.** Teams will chase `≥55` and forget bands; teach the two-part rule.

**Opportunities**
- **Guardrail pre-filter** for generators (auto-reject Δx RED, ρᵣ RED).
- **Failure atlas** by first failing knob (dx/rv/rho) → training feedback.
- **Dual-profile diffs** to separate texture-intent from overload.
- **Reward shaping** in RL loops (stay in band while meeting task).

---

## Minimal “How to use” (workflow sketch)
1) Choose **profile** (Figure / MarkMaking / Landscape).  
2) Run the image; read **bands** and **LSI_lite_100**.  
3) If **RED**, fix that primitive **first**. If all **OK** but `<55`, use **priority_knob** to decide the next nudge.  
4) For interiors/products, decide **mask stance** (default vs. supplied subject mask).  
5) Log versions (OpenCV/NumPy) and processing; tiny changes move ρᵣ.

---

## Visual artifacts (what you can export)
- Single-image grid (original + edges + masks + Laplacian heat + band gauges + accept/reject stamp).
- Batch charts (score histogram @55, band-failure mix, Δx↔rᵥ scatter, knob distribution, correlation heatmap).

---

## Legal & licensing
**Copyright © 2025 A.rtist I.nfluencer — Russell Parrish. All Rights Reserved.**  
All non-code materials in this project—including the system design, frameworks, explanatory text, case-study narratives, diagrams, and any visual outputs—are protected IP and **may not be copied, reproduced, or included in AI training datasets** without prior written permission.

**Code & DSL snippets — MIT License (permissive grant).**  
Source-like examples (code blocks, DSL snippets, JSON/YAML operator specs) are licensed under MIT. The MIT grant **does not** apply to non-code materials above.

```
MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction… (full text recommended for redistributions)
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND…
```

**Provenance footer (optional UI label):**  
*“Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS) • Sketcher v18 • LSI-lite”*  
*(Optional: capsule/version, drift notes.)*

---

## Attribution
Authored by **Russell Parrish**; developed and exercised with model partners (GPT/Gemini/Claude) in a **human-in-the-loop** critique loop. Case studies compiled from live runs and read cards.

---

## Versioning & reproducibility
- Run loop: **single pass** (no Δx recompute); EXIF-aware loading; masks are `uint8`.
- Landscape ROI (reflection probe) affects **Δx only**; **rᵥ/ρᵣ are always full-frame**.
- Unknown handling: blank/edgeless → `dx=NaN`, band=RED, `accepted=False`.
- Record versions: Python ≥3.10; OpenCV ≥4.8; NumPy ≥1.26; SciPy ≥1.11; pandas ≥2.0.

---

## Roadmap
- **Mask override option** (research mode) for interiors/products.  
- **Dual-profile dashboards** to compare Figure vs MarkMaking on dense mark fields.  
- **Band-center visualization** polish + CSV/HTML quick-look.  
- Optional “as-series” grading (aggregate last *N* frames).

---

## Contact
For licensing and collaboration, contact **A.rtist I.nfluencer — Russell Parrish**.

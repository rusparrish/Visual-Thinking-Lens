# Off-Center Fidelity (OCF): Constraint Basins for Stability & Drift in Generative Models (Compositional Analysis)

**Ghost Density & companions** — a practical, repeatable way to steer models *away* from center-gravity and into artistically stable off-center compositions using three measurable dials:

- **Δx** – centroid offset to the nearest vertical edge  
- **rᵥ** – void ratio (how much of the frame is blank/quiet field)  
- **ρᵣ** – rupture density (thin seams/edges that keep the void from turning to wallpaper)

> This repository accompanies the proposal **“Off-Center Fidelity: Constraint Basins for Stability and Drift in Generative Models”** and packages it as a **conversational protocol** you can run in any chat interface to get consistent, measurable results across engines.

---

## Why this exists

Most models collapse to *safe center*. OCF reframes that as **geography**: there are reproducible *attractor basins* where off-center images remain coherent. By measuring Δx, rᵥ, ρᵣ and applying small, engine-aware nudges (plus a one-click crop), you can hit those basins **reliably**—and explain *why* a result passed or failed.

OCF = **interpretability + control**, not another generator.

---
## What’s in here

- `docs/OCF_Proposal.pdf` – the full paper (proposal status; empirical envelopes, not CIs).  
- `Ghost_Density_Composition_Analysis_Protocol/`  
- /Abstract/           Example images (optional)
- /Batches/            Place .zip files for batch runs and where CSV/HTML exports can go
- /Chair/              Example images (optional)
- /Figure/             Example images (optional)
- /Frogs/              Example images (optional)
- /OA Portrait/        Example images (optional)
- OCF_Ghost_Density—Scorer_Update_10_2_FINAL.ipynb   ← Colab/Notebook UI (primary)
- /Portrait/           Example images (optional)
- ocf_ghost_density—scorer_update_10_2_final.py       ← Scriptified runner (same logic)
- /StillLife/          Example images (optional)
- /Tree/               Example images (optional)

---

## The three profiles (artist basins vs. deploy windows)

- **GD–Edge-Anchored** (quiet figure to wall):  
  *Artist basin* ≈ Δx **0.15–0.18**, rᵥ **0.62–0.68**, ρᵣ **0.28–0.40**, **one** vertical seam, no props.  
  *Engine window* (today): Δx **0.12–0.20**, rᵥ **0.62–0.68**, ρᵣ **0.28–0.40**, seam tolerance ±3 px.

- **GD–Horizon** (field with a single long edge):  
  rᵥ **0.70–0.85**, ρᵣ **0.18–0.30** (Δx advisory if a subject exists), one clean horizon.  
  Engine notes: many models push rᵥ high; keep texture variance low–mid.

- **GD–Field-Void** (unanchored frog/still):  
  rᵥ **0.74–0.90**, ρᵣ **0.18–0.32**, seams **0–1** faint; Δx to center is **advisory**.  
  Engine notes: compensate missing edge pressure with slightly *larger* rᵥ targets.

> Repo lists **artist basins (ideal)** and **engine-bias windows (deploy)** separately so you know what’s theoretically “right” vs. what reliably lands today.

---

## Conversational protocol (repeatable in any chat)

1. **Prime** with a profile spine, then add the numeric block, e.g.:  
   `Δx ≈ 0.16 W, rᵥ ≈ 0.65, ρᵣ ≈ 0.34. One seam only. No props/patterns. Matte wall.`
2. **Generate oversize** (so you can crop).  
3. **Score** with the three probes (copy/paste blocks in `protocol/checklists.md`).  
4. **Nudge once**:  
   - Δx off by ≤0.02 → tiny crop to lock 0.16 W.  
   - rᵥ low → “two-thirds blank” + scale down subject.  
   - ρᵣ high → “smooth plaster; one hairline seam only.”  
5. **Re-score & badge** (`✅` ideal, `✅*` engine-window, `⚠` crop-fix, `🧯` redo).

This loop turns a “vibe prompt” into **measurable steering** with the same chat model.

---

## Measured vs. interpreted

| **Measured** | **How** |
|---|---|
| Δx — subject → nearest vertical edge ÷ frame width | centroid + line detection |
| rᵥ — void area ÷ frame area | subject mask + anchor strips |
| ρᵣ — hairline edge density in the void | denoised Canny/LoG per area |
| seam_count `s` | long edge count (vertical/horizon) |

| **Interpretive** | **From** |
|---|---|
| void outweighs body | rᵥ above profile threshold |
| artist basin | inside the profile’s empirical envelope |
| deploy window | envelope adjusted by observed engine drift |

---

## One-envelope logic (plain → boolean)

Let `e` = 1 if a single vertical edge (wall) exists; `h` = 1 if a single horizon exists; `s` = seam count.  
Ghost Density feasible set (empirical envelopes):

- rᵥ ∈ [0.62, 0.90], ρᵣ ∈ [0.18, 0.40]  
- If (e ∨ h) ⇒ Δx ∈ [0.12, 0.20] and s = 1  
- If (¬e ∧ ¬h) ⇒ rᵥ ≥ 0.74 and s ≤ 1 (faint)

This block gates Edge/Horizon/Field consistently.

---

## Engines (quick drift cards)

- **Sora / GPT-Image** — typically near-ideal; contradiction phrasing works (“presence < emptiness”).  
- **Gemini** — generate big, **crop** to Δx.  
- **Midjourney** — tends to undershoot Δx by ~0.03 and add ρᵣ +0.03; plan to crop and forbid décor.  
- **Meta / SD / Firefly** — clutter/texture bias; insist on “matte wall; one seam; no patterns.”

---

## Status

- **Proposal-style framing** — envelopes are empirical, not statistical CIs (yet).  
- Separation of **artist basin** vs. **engine-bias** avoids mechanism claims.  
- Designed for **replication in conversation** (prompt → measure → nudge → pass).

---

## Roadmap

- Minimal notebook for Δx / rᵥ / ρᵣ (mask + edge counting)  
- Per-engine bias tables (observed drift)  
- Formal reliability study  
- Additional capsules (Corner-Well, Shadow-Anchor)

---

## Contributing

Issues & PRs welcome. Please label: docs, protocol, engine-notes, or analysis.

## License
- **Code & DSL snippets:** MIT License (see `LICENSE-MIT.txt`).
- Please do not redistribute images in the example folders without permission.
- **All other content (text, diagrams, images, frameworks):** All Rights Reserved (see `LICENSE-NONCODE.txt`). 
- Methods, names, and framework: **A.rtist I.nfluencer — All Rights Reserved**.  
- **Framework text, PDFs, images, case studies:** © 2025 **A.rtist I.nfluencer — Russell Parrish**. **All Rights Reserved.** No inclusion in AI training datasets without written permission.
---

## Contact / Notes

- If you add new folders of images, the scorer doesn’t depend on folder names—use any category scheme you like.


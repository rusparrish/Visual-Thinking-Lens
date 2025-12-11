
# VCLI‑G & SCI — Geometry‑Coupled Image Analysis

Modern image evaluation metrics measure semantic alignment, distributional fidelity, and aesthetic preference, but none quantify temporal demand or how long an image resists perceptual resolution. VCLI-G (Visual Cognitive Load Index - Geometry Coupled) addresses this gap by measuring cognitive effort through four geometric channels: centroid wander, void topology, curvature torque, and occlusion entropy. Paired with the Structural Coherence Index (SCI), the system maps images into a 2D perceptual space that distinguishes earned complexity from chaotic noise, and intentional simplicity from default outputs. This framework enables researchers to detect when generative models converge on safe patterns, allows artists to quantify attention gravity as geometry, and provides a measurement basis for perceptual engagement independent of aesthetic judgment. VCLI-G treats high cognitive load as a controllable state rather than a failure mode, making it applicable across contexts from UI optimization to gallery curation.

**VCLI‑G (Visual Cognitive Load Index)** estimates how much perceptual *work* an image asks a viewer to do.  
**SCI (Structural Coherence Index)** estimates how *organized* that work is.  
Together they map pictures into a 2‑axis space:

- **VCLI‑G (0–5):** delay/tension/strain the image induces (centroid wander `z1`, void topology `z2`, curvature torque `z3`, occlusion entropy `z4`).  
- **SCI (0–5):** organization/regularity (regional consistency, edge alignment, scale consistency, rhythm).

> This reads the **geometry of the image** — what it *does* compositionally — not what it depicts or how “pretty” it is.  
> It’s not a similarity score, an aesthetic rater, or eye‑tracking; it’s a transparent proxy for **attention gravity**.

---

## What’s in this repo

- `UPDATED_GITHUB_VCLI_G_04_VCLI_G_APE_and_RCE_12_25.ipynb` - **UPDATED** iterative and batch scoring, includes latest updates
- `UPDATED_github_vcli_g_04_vcli_g_ape_and_rce_12_25.py` - **UPDATED** iterative and batch scoring, includes latest updates
- `GITHUB_BATCH_of_Initial_v2_VCLI_G.ipynb` — Colab‑friendly notebook: upload images, score, and export CSV.
- `github_batch_of_initial_v2_vcli_g.py` — script version for local/batch runs.
- `The_Visual_Cognitive_Load_Index_(VCLI-G).pdf` — method overview and notes.
- `README_batch.md` — quick guide for the notebook/script.
- `CITATION.cff` — how to cite.
- `LICENSE` — MIT.

---

## Install

Python 3.9+ recommended.

```bash
pip install --upgrade opencv-python-headless scikit-image numpy scipy matplotlib networkx pandas
```

> **Colab:** you can run the notebook directly; the install cell is included there.

---

## Quick start (Notebook)

1. Open `GITHUB_BATCH_of_Initial_v2_VCLI_G.ipynb` in Google Colab.
2. Run the **upload** cell and select a few images (JPG/PNG/WebP).
3. Choose a **profile**: `ai_conservative`, `physical_neutral`, or `physical_balanced_plus`.
4. Run the **results table** cell to see VCLI‑G, SCI, and features for each file.
5. A CSV (default `VCLI_G_results.csv`) will be written with all columns.

## Quick start (Script)

```bash
python github_batch_of_initial_v2_vcli_g.py   --input /path/to/images   --output results.csv   --profile physical_neutral
```

Optional flags:
```
--recursive          # walk subfolders
--limit 500          # max images
--profile {ai_conservative|physical_neutral|physical_balanced_plus}
```

---

## Profiles (scoring post‑weights)

- **ai_conservative** — skeptical of “cheap” complexity (texture/void spam). Tighter z‑clips; rewards earned torque/wander.  
- **physical_neutral** — baseline; balanced weights and squash.  
- **physical_balanced_plus** — museum‑leaning; modestly more credit for clean figure/ground and curvature tension.

Profiles don’t change feature extraction, only how normalized channels are combined and squashed onto the 0–5 band.

---

## Output columns (CSV)

- `path`, `profile`, **`VCLI_G`**
- **Geometric features:** `G1_L`, `G1_K`, `G2_V`, `G2_chi`, `G2_AR`, `G2_cut`, `G3_kvar`, `G3_infl`, `G4_H`
- **SCI + submetrics:** `SCI`, `SCI_regional`, `SCI_angle`, `SCI_scale`, `SCI_rhythm`
- **z‑channels:** `z_z1`, `z_z2`, `z_z3`, `z_z4`, `z_raw` (pre‑squash linear combo)

Interpretation cheatsheet:

- **High VCLI‑G + High SCI** → *Earned tension* (organized friction).  
- **High VCLI‑G + Low SCI** → *Chaotic complexity* (productive accidents or noise).  
- **Low VCLI‑G + High SCI** → *Resolved clarity*.  
- **Low VCLI‑G + Low SCI** → *Default simplicity*.

> Scores describe *behavior*, not value. A low score can be intentional simplicity.

---

## Reproducible case‑study cuts

- **Stratified A/B (topic‑matched)** — compare cohorts within the same subject/folder.
- **Tail rate** — share of images landing in the *Earned Tension* quadrant (VCLI‑G ≥ 3.10 and SCI ≥ 3.00 by default).
- **Signal fingerprints** — cohort means of `z1..z4` to see how load is composed.

Example cells for these appear in the notebook.

---

## Limitations

- Edge/structure centric: subtle color‑only effects, tonality without edges, or ultra‑fine texture may be under‑weighted.
- Linear combiner: the composite uses a weighted sum of normalized channels; interaction terms are monitored but not yet primary.
- Not a replacement for eye‑tracking; it’s an auditable proxy for perceptual strain and organization.

> Practitioner’s note: this is a **computational criticism** tool — a transparent, extensible proxy for an artist/designer’s
> internal evaluation loop. The opinion is calculable and adjustable.

---

## Cite

If you use this, please cite (fill in DOI when assigned):

```bibtex
@software{vclig,
  title        = {VCLI-G & SCI: Geometry-Coupled Visual Cognitive Load Index},
  author       = {Russell Parrish},
  year         = {2025},
  url          = {https://github.com/rusparrish/Visual-Thinking-Lens},
  version      = {v0.2}
}
```

Also see `CITATION.cff` in the repo.

## Limits (scope & philosophy)

- **Diagnostic, not aesthetic.** “Accepted” ≠ “good art.”  
- **Profiled, not universal.** Many great images will fail on purpose.  

---

## License & attribution

- Code is released under **MIT** (see `LICENSE`).
- Maintainer ORCID: **0009-0008-9781-7995**.

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

*Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS)
Learn more --> www.artistinfluencer.com

---

## Questions / contributions

Issues and PRs welcome — especially: occlusion DAG improvements, entropy/density metrics, and validation studies.

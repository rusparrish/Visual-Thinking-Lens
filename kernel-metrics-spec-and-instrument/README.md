# Kernel Metrics → Gradient-Field Operations
### A Deterministic Framework for Measuring Spatial Priors in Images

This repository contains a compositional analysis instrument designed to measure **spatial priors** in images using only **gradient‑field operations**. The system defines seven kernel metrics—Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds—each mapped directly to first‑order or second‑order image gradients.  
It is model‑agnostic, training‑data‑agnostic, and fully deterministic.

---

## 📌 What This Instrument Does

This toolkit converts any image into a structured **force‑field representation** using gradient magnitude, orientation, curvature, and skeletal topology.  
From these fields, it extracts the core compositional measurements:

- **Δx — Placement Offset**  
- **rᵥ — Void Ratio**  
- **ρᵣ — Packing Density**  
- **μ — Cohesion**  
- **xₚ — Peripheral Pull**  
- **θ — Orientation Stability**  
- **ds — Structural Thickness**

The output is a set of interpretable diagnostics, visual overlays, and quantitative measurements describing how an image *organizes mass and void*.


**Precise Mapping: Kernel Metrics → Gradient-Field Operations**
This document defines a deterministic way to measure spatial priors in images by mapping seven compositional kernel metrics—Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds—directly onto operations over the gradient field ∣∇𝐼∣. Instead of looking at semantics or model internals, the document treats every image as a force field of mass, void, and pull, extracted via Sobel gradients, adaptive masks, skeletons, and ridge structures. Each metric is given both a compositional intuition (what it “means” in a picture) and a precise gradient-based definition (how it’s computed), making the system reproducible and model-agnostic. Together, these metrics expose inductive biases and forbidden zones in composition space—regions models prefer, avoid, or snap back to—providing an instrument for fingerprinting, comparing, and stress-testing generative image systems.

---

## 📁 Folder Structure

```
Kernel_Metrics/
│
├── notebooks/
│   ├── full_compositional_overlay.ipynb
│   ├── gradient_field_6panel.ipynb
│   ├── advanced_field_diagnostics.ipynb
│   ├── compositional_fingerprint.ipynb
│   └── VCLI_G_masks.ipynb
│
├── src/
│   ├── gradients.py
│   ├── masks.py
│   ├── topology.py
│   ├── metrics.py
│   └── utils.py
│
├── examples/
│   ├── sample_inputs/
│   └── sample_outputs/
│
└── README.md   ← you are here
```

---

## 🧠 Core Claims

### **1. Composition is measurable.**  
Structure is not subjective. Mass, void, pull, and cohesion can be extracted from gradients.

### **2. Priors are geometric, not semantic.**  
Models reveal biases through *arrangement*, long before *meaning*.

### **3. Gradient fields are sufficient.**  
No saliency maps, no CLIP embeddings—just deterministic image physics.

### **4. Forbidden zones reveal inductive bias.**  
Regions of Δx–rᵥ–ρᵣ space that models rarely occupy indicate strong priors.

---

## 📐 What You Can Do With This

- **Fingerprint a generative model**  
  Compare distributions of Δx, rᵥ, ρᵣ, μ across engines or checkpoints.

- **Diagnose compositional failure**  
  Detect center bias, void collapse, edge avoidance, symmetry addiction, etc.

- **Analyze human imagery vs. model imagery**  
  See how artists break priors and where models cannot follow.

- **Evaluate training changes**  
  Run before/after spatial-prior maps to track improvements or regressions.

- **Study forbidden zones**  
  Understand which compositions are statistically unreachable for a model.

---

## ▶️ Quickstart

1. Upload any **JPEG or PNG** to the notebook.  
2. Run **full_compositional_overlay.ipynb**.  
3. Receive:
   - gradient field  
   - skeleton  
   - void map  
   - mass map  
   - 6‑panel diagnostic  
   - compositional fingerprint  
   - kernel metrics table

---

## 🧪 Requirements

Python ≥ 3.9  
NumPy  
OpenCV  
SciPy  
Matplotlib  
scikit-image  

---

## 📄 Citation

```
Russell Parrish. (2025). Precise Mapping: Kernel Metrics → Gradient-Field Operations.
A Deterministic Framework for Measuring Spatial Priors in Images.
russellgparrish@gmail.com www.artistinfluencer.com
```

---

## 🧭 Status

This instrument is *active, evolving research tooling*.  
It is already suitable for:
- generative‑model evaluation  
- perceptual analysis  
- composition studies  
- inductive bias experiments

More modules (ridge attractor fields, symbolic gravity maps, priors atlases) will be added.

---

## 📬 Contact

For questions, extensions, or integration inquiries, contact:  
**Rus — A.rtist I.nfluencer / Visual Thinking Lens** russellgparrish@gmail.com www.artistinfluencer.com

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


*Provenance: A.rtist I.nfluencer • Visual Thinking Lens (OS)
Learn more --> www.artistinfluencer.com and www.paralaxmetrology.com

---

## Questions / contributions

Issues and PRs welcome — especially: occlusion DAG improvements, entropy/density metrics, and validation studies.


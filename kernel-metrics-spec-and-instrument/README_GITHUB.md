# Kernel Metrics → Gradient-Field Operations
### A Deterministic Framework for Measuring Spatial Priors in Images

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-success.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-research--tooling-active.svg)](#status)

This repository implements a **compositional analysis instrument** for measuring spatial priors in images using only **gradient-field operations**.  
It defines seven kernel metrics—**Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds**—each mapped directly to first- or second-order image gradients.

The system is:

- **Deterministic** — no training, no randomness in measurement  
- **Model-agnostic** — works on any generated or human-made image  
- **Data-agnostic** — no access to training data or internal embeddings required  

---

## ✨ What This Repository Provides

This toolkit converts an input image into a structured **force-field representation**, exposing:

- void structure  
- mass concentration  
- gradient islands  
- ridge attractors  
- skeleton / compositional spine  
- orientation flow  
- peripheral pull

From these fields, it computes the seven kernel metrics:

- **Δx — Placement Offset**  
- **rᵥ — Void Ratio**  
- **ρᵣ — Packing Density**  
- **μ — Cohesion**  
- **xₚ — Peripheral Pull**  
- **θ — Orientation Stability**  
- **ds — Structural Thickness**

The output is a set of **visual diagnostics** (overlays, panels, heatmaps) and **quantitative measures** describing how an image organizes mass and void.

---

## 🗂 Repository Structure

_A suggested layout for the `Kernel_Metrics` folder:_

```text
Kernel_Metrics/
│
├── notebooks/
│   ├── 00_full_compositional_overlay.ipynb
│   ├── 01_gradient_field_6panel.ipynb
│   ├── 02_advanced_field_diagnostics.ipynb
│   ├── 03_compositional_fingerprint.ipynb
│   ├── 04_quadrant_weight_and_heatmaps.ipynb
│   └── VCLI_G_masks.ipynb
│
├── src/
│   ├── gradients.py        # Sobel fields, orientation, magnitude
│   ├── masks.py            # void / mass / island / ridge masks
│   ├── topology.py         # skeletons, basins, ridge attractors
│   ├── metrics.py          # Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds calculations
│   └── utils.py            # I/O, plotting, helpers
│
├── examples/
│   ├── sample_inputs/
│   └── sample_outputs/
│
├── LICENSE
└── README.md   ← you are here
```

> **Note:** Filenames may differ in your local copy. The structure above is a recommended organization.

---

## 🔧 Installation

This project uses standard scientific Python libraries.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Kernel_Metrics.git
cd Kernel_Metrics
```

### 2. Create and activate a virtual environment (optional but recommended)

Using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate  # on macOS / Linux
# .venv\Scripts\activate  # on Windows
```

### 3. Install dependencies

Create a `requirements.txt` including at least:

```text
numpy
opencv-python-headless
matplotlib
scipy
scikit-image
```

Then:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install numpy opencv-python-headless matplotlib scipy scikit-image
```

---

## ▶️ Quickstart (Notebook)

1. Launch Jupyter or open the notebook in **Google Colab**.
2. Open `notebooks/00_full_compositional_overlay.ipynb`.
3. Upload a **JPEG or PNG** image when prompted.
4. Run all cells.

You will get:

- LAB luminance vs Sobel gradient comparison  
- 4-panel + 6-panel gradient-field breakdowns  
- void, mass, skeleton, and ridge masks  
- full compositional overlay (Δx, xₚ, μ, void basins, spine)  
- compositional fingerprint (radar / spider chart)  
- quadrant and 3×3 weight distributions  
- a kernel metrics table summarizing Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds

---

## 📐 Use Cases

### 1. **Model Fingerprinting**

Use the kernel metrics to characterize the **spatial priors** of a generative model:

- Sample hundreds of images from a model  
- Compute Δx, rᵥ, ρᵣ, μ distributions  
- Visualize basins and **forbidden zones** in composition space  

### 2. **Comparing Engines / Checkpoints**

Evaluate changes in compositional behavior:

- GPT-Image vs Midjourney vs SDXL vs Sora (etc.)  
- Before/after a training run or architecture tweak  

### 3. **Human vs Machine Composition**

Compare curated human artworks vs model outputs:

- Where do artists routinely break priors?  
- Where do models collapse back to safe basins?  

### 4. **Failure Analysis & Debugging**

Identify:

- center bias  
- void collapse  
- edge avoidance  
- symmetry addiction  
- fragmentation vs cohesion  

and use overlays to see *why*.

---

## 🧠 Design Principles

- **No semantics.**  
  Metrics are derived purely from gradients and topology, not labels or captions.

- **No training data access.**  
  Priors are inferred from model behavior, not dataset inspection.

- **Contrast-invariant.**  
  Percentile-based thresholds ensure robustness to exposure and style.

- **Reproducible and interpretable.**  
  Every metric has a compositional intuition and a precise gradient-field definition.

---

## 📄 Citation

If you use this work in research, please cite:

```text
Rus, A. (2025).
Precise Mapping: Kernel Metrics → Gradient-Field Operations:
A Deterministic Framework for Measuring Spatial Priors in Images.
```

(Replace with canonical BibTeX once formal publication details are available.)

---

## 📜 License

This repository is released under the **MIT License**.

See the `LICENSE` file in this repository for the full text.

---

## 🧭 Status

This is **active research tooling**, not a finished product.

- ✅ Stable: core kernel mappings (Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds)  
- ✅ Stable: primary gradient-field masks and overlays  
- 🚧 In progress: ridge attractor maps, symbolic gravity, priors atlases  
- 🧪 Intended for: generative-model analysis, perceptual studies, composition research

---

## 🤝 Contributing

Issues, pull requests, and extensions are welcome, especially if you are:

- evaluating compositional priors in generative models  
- building new overlays / diagnostics on top of the kernel  
- integrating this into a larger evaluation suite

Please open an issue to discuss significant changes before submitting a PR.

---

## 📬 Contact

For questions, extensions, or integration inquiries, contact:  
**Rus — A.rtist I.nfluencer / Visual Thinking Lens** russellgparrish@gmail.com www.artistinfluencer.com

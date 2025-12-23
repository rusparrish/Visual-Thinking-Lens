# VTL Kernel Metrics: Compositional Analysis for AI-Generated Images

This repository provides a measurement tool for analyzing **spatial priors** in AI‑generated images.  
Unlike FID, CLIPScore, or T2I-CompBench, which evaluate *semantic correctness* or *distribution similarity*,  
the **VTL Kernel Metrics** framework measures *geometric composition* — the invisible structural biases that govern how models place subjects in a frame.

---

## What This Tool Measures

AI image models exhibit consistent, measurable spatial behaviors:

- Center bias  
- Void collapse  
- Packing compression  
- Cohesion loss  
- Radial collapse prior (RCP)

Traditional benchmarks cannot detect these.  
The **kernel metric system** captures them using five geometric primitives:

| Metric | Symbol | Measures | Interpretation |
|--------|--------|----------|----------------|
| Placement Offset | Δx | Horizontal centroid offset | Detects center bias / asymmetry |
| Void Ratio | rᵥ | Amount of negative space | Identifies void collapse / expansion |
| Packing Density | ρᵣ | Compression inside bounding box | Shows clustering vs dispersion |
| Cohesion | μ | Structural unity of material cluster | Fragmentation vs stability |
| Peripheral Pull | xₚ | Composite field invariant | Detects RCP vs anti-RCP behavior |

These metrics provide interpretable signals for **model comparison**, **version drift**, and **prompt testing**.

## How to Use This Notebook

### **Step 1: Setup (Run Once)**
Run these cells in order:
- Install dependencies
- Import libraries
- Define all metric functions

### **Step 2: Analyze a Single Image**

**Option A: Quick Single Analysis**
1. Upload one image
2. Calculate metrics using saliency detection (recommended)
3. Visualize results with centroid and bounding box overlay

**Option B: Compare All Detection Methods**
1. Upload one image
2. Run all three detection methods (saliency, edges, Otsu) side-by-side
   - See which method works best for your image
   - Check agreement analysis (low variance = methods agree)

### **Step 3: Batch Processing (Optional)**

Process multiple images at once
- Upload several images
- Get comparison table showing metrics across all images
- Identify patterns (e.g., "80% of Model A's outputs are centered")

---

## Notebook Features

- Single‑image analysis  
- Mask generation via **saliency**, **edges**, or **Otsu thresholding**  
- Automatic metric calculation  
- Centroid + bounding box visualization  
- Quick diagnostic (“RADIAL COLLAPSE DETECTED”, etc.)  
- Batch processing  
- Agreement analysis across detection methods  

## Detection Methods Explained

The notebook offers three subject-detection methods:

| Method | Best For | Limitations |
|--------|----------|-------------|
| **Saliency** (recommended) | Complex backgrounds, gradients, most images | Slower processing |
| **Edges** | Clean images with strong subject boundaries | Can miss subtle subjects |
| **Otsu** | High-contrast images with simple backgrounds | Fooled by gradient backgrounds |

**Default recommendation:** Use **saliency detection** unless you have specific reasons to use another method.

## Example Use Cases

### **1. Model Comparison**
Compare two AI image generators:
- Upload outputs from both models
- Check mean Δx values
- Model with lower Δx has stronger central bias

### **2. Prompt Engineering Validation**
Test if anti-collapse prompts work:
- Generate images with standard vs. structural prompts
- Compare xₚ scores
- Higher xₚ = better compositional control

### **3. Dataset Analysis**
Evaluate training data composition:
- Batch process dataset
- Check distribution of Δx, rᵥ, ρᵣ
- Identify compositional biases in training set

### **4. Version Control**
Track model updates:
- Measure kernel metrics across model versions
- Detect spatial prior drift
- Flag unexpected compositional changes

---

## What This Notebook Demonstrates

This measurement infrastructure exists and works **right now**—unlike FID/CLIP/T2I-CompBench which require:
- Reference datasets
- Batch processing
- No single-image analysis capability

**Key advantages:**
- ✅ Works on individual images immediately
- ✅ No reference dataset required
- ✅ Interpretable geometric measurements
- ✅ Detects spatial priors invisible to existing metrics
- ✅ Model-agnostic (works on any image source)


---

## Limits of Kernel Metrics

This tool measures *geometry only*, not semantics.  
It does not evaluate subject identity, prompt correctness, or realism.  
Its accuracy depends on mask quality and is less stable in:

- multi-object scenes  
- high-texture backgrounds  
- images with soft or ambiguous boundaries  

See the full “Limits of Kernel Metrics” section in the notebook for details.

---

## 📦 Installation

Install required dependencies:

```bash
pip install pillow numpy matplotlib opencv-python scipy
```

---

## ▶️ Quick Start

```python
from vtl_kernel_metrics import calculate_kernel_metrics, interpret_metrics
metrics = calculate_kernel_metrics("your_image.png", method="saliency")
print(interpret_metrics(metrics))
```

---

## 📁 File Overview

- **VTL_Kernel_Metrics_Compositional_Analysis.ipynb** — main notebook  
- **vtl_kernel_metrics.py** — standalone functions  
- **example_images/** — sample images for testing (optional)  

---

## 📄 Citation

If used in research or development:

```
Russell Parrish. Visual Thinking Lens: Kernel-Based Compositional Metrics, 2025.
www.artistinfluencer.com
russellgparrish@gmail.com
ORCID: 0009-0008-9781-7995
```

---

## 🧭 Purpose

The VTL Kernel Metrics framework is part of the broader  
**Visual Thinking Lens (VTL)** system — a modular architecture for analyzing generative behavior, inductive bias, and spatial reasoning in AI models.

This toolkit is intended for:

- ML researchers  
- model evaluators  
- prompt engineers  
- visual computing practitioners  

---

## 🛡️ License

MIT License — permitting open use, modification, and integration.

---

## Acknowledgments

Developed as part of ongoing research into **geometric inductive bias**, **spatial priors**,and **model‑agnostic evaluation techniques**.


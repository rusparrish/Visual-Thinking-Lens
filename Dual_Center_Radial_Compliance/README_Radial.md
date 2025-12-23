# Dual-Center Radial Compliance Analyzer (RCA-2) - README

## Overview

This Jupyter notebook implements **Radial Compliance Analysis (RCA-2)**, a computational framework for measuring geometric structure in images. It quantifies how visual mass is organized radially around center points, providing objective metrics for compositional analysis.

**Primary Use Case:** Measuring compositional uniformity in AI-generated images to detect optimization-induced geometric constraints.

## What RCA-2 Measures

The analyzer evaluates **radial compliance** - the degree to which an image's visual mass follows concentric ring patterns emanating from a center point. This reveals underlying compositional structure independent of semantic content.

### Core Metrics

**Mass Radial Compliance (RCS)**
- Range: 0.0 (chaotic/non-radial) to 1.0 (perfect radial organization)
- Typical values: 0.55-0.75 for most images
- Values > 0.60 indicate strong radial structure

**Centroid Offset (Δx, Δy, Δr)**
- Δx: Horizontal distance from frame center (-0.5 to +0.5, normalized)
- Δy: Vertical distance from frame center (-0.5 to +0.5, normalized)
- Δr: Euclidean radial distance from frame center (0.0 to ~0.7)
- Lower Δr indicates more centered compositions

**Void Ratio (rᵥ)**
- Range: 0.0 (completely dense) to 1.0 (completely empty)
- Typical values: 0.75-0.95
- Measures percentage of frame that is empty/background space

**Radial Eligibility Score (E_s)**
- Range: 0.0 to 1.0
- Combines compactness, isotropy (roundness), and angular variance
- Threshold: E_s ≥ 0.38 for valid radial interpretation
- Gates whether RCS should be trusted

### Dual-Center Analysis

The notebook measures radiality from **two reference points**:

1. **Frame-Centered (RC_f)** - Radiality anchored at geometric center of the image
2. **Mass-Centered (RC_s)** - Radiality anchored at the detected mass centroid

This dual measurement reveals whether compositions organize around the frame itself or around the subject.

## Workflow

### 1. Setup & Dependencies
```python
# Automatically installs required packages
!pip -q install opencv-python pillow numpy matplotlib pandas scipy
```

**Required libraries:**
- OpenCV (image processing)
- PIL/Pillow (image loading)
- NumPy (numerical operations)
- Pandas (data handling)
- Matplotlib (visualization)
- SciPy (statistical functions)

### 2. Image Processing Pipeline

The notebook processes images through 21 sequential steps:

**Steps 1-7: Mask Creation**
- Load image → Convert to grayscale → Apply Otsu/edge thresholding
- Keep largest connected component → Remove border noise
- Creates binary mask identifying "visual mass"

**Steps 8-11: Centroid & Reference Points**
- Calculate mass centroid (center of visual weight)
- Establish frame center (geometric center)
- Compute maximum corner radius for normalization

**Steps 12-15: Frame-Centered Analysis**
- Measure how mass distributes from frame center
- Generate radial profile (mass distribution vs. distance)
- Calculate Frame Radial Compliance (RC_f)

**Steps 16-18: Mass-Centered Analysis**
- Measure how mass distributes from subject center
- Generate radial profile from mass centroid
- Calculate Mass Radial Compliance (RC_s)

**Steps 19-20: Geometric Validation**
- Compute compactness, isotropy, angular variance
- Calculate Radial Eligibility Score (E_s)

**Step 21: Classification**
- Classify radial behavior based on RC_f, RC_s, E_s relationships

## Output & Interpretation

### Primary Output Columns

When analyzing a batch of images, the notebook produces a CSV with these key columns:

| Column | Description | Typical Range | What It Means |
|--------|-------------|---------------|---------------|
| `filename` | Image filename | - | Identifier |
| `mass_radial_compliance` (RCS) | Subject radial compliance | 0.4 - 0.8 | How radially organized the mass is |
| `frame_radial_compliance` | Frame radial compliance | 0.4 - 0.8 | How composition relates to frame |
| `delta_x` (Δx) | Horizontal offset | -0.3 to +0.3 | Left/right centering |
| `delta_y` (Δy) | Vertical offset | -0.3 to +0.3 | Up/down centering |
| `delta_r` (Δr) | Radial offset | 0.0 - 0.4 | Overall centering |
| `void_ratio` (rᵥ) | Empty space ratio | 0.6 - 0.98 | Sparseness of composition |
| `radial_eligibility` (E_s) | Geometric validity | 0.0 - 1.0 | Can we trust RCS? |
| `compactness` | Mass concentration | 0.0 - 1.0 | How clustered the subject is |
| `isotropy` | Roundness measure | 0.0 - 1.0 | How circular the mass is |
| `radial_label` | Classification | - | Interpretive category |

### Radial Classification Labels

The notebook assigns one of five classifications:

**"Radial present (dual-center / near-tie)"**
- RC_f ≈ RC_s, both high (> 0.60)
- Δr < 0.06
- Perfect alignment: frame center and mass centroid are nearly identical
- **Most common in AI-generated images**

**"Subject-dominant radial (rings follow mass)"**
- RC_s >> RC_f (difference > 0.05)
- E_s ≥ 0.38
- Subject is off-center but strongly radially organized internally
- Rings follow the subject, not the frame

**"Field-dominant radial collapse"**
- RC_f >> RC_s (difference > 0.05)
- Frame center dominates even when subject is off-center
- Environmental/atmospheric radiality stronger than subject

**"Weak/unclear radial (eligible mask, low coherence)"**
- E_s ≥ 0.38 (geometry supports radial interpretation)
- RC_s < 0.62 (but radial signal is weak)
- Radial structure present but not dominant

**"Mass present but radially ineligible"**
- E_s < 0.38
- Mask geometry doesn't support radial interpretation
- Subject is elongated, fragmented, or scattered

## Reading the Results

### Single Image Analysis

When analyzing one image, the notebook displays:

**Visual Output:**
1. Original image
2. Detected mask (white = subject, black = background)
3. Frame-centered overlay (rings from frame center)
4. Mass-centered overlay (rings from mass centroid)
5. Radial profiles (graphs showing mass vs. distance)

**Numerical Output:**
```
RCS: 0.6386
Δr: 0.0534
Void Ratio: 0.8155
Classification: Radial present (dual-center / near-tie)
```

### Batch Analysis

When processing multiple images:

**Low CV (Coefficient of Variation) = High Uniformity**
- RCS CV < 5% → Extremely uniform (geometric monoculture)
- RCS CV 5-10% → Moderate uniformity
- RCS CV > 15% → Expected natural diversity

**Low IQR (Interquartile Range) = Tight Constraint**
- IQR < 0.05 (5% of scale) → Very constrained
- IQR 0.05-0.15 → Moderate spread
- IQR > 0.20 → Natural diversity

**Low Δr = Aggressive Centering**
- Mean Δr < 0.05 → Extreme centering
- Mean Δr 0.05-0.15 → Moderate centering
- Mean Δr > 0.20 → Off-center compositions common

## Typical Use Cases

### 1. Testing a Single Image
```python
# Load and analyze one image
img_path = "your_image.png"
img = read_image_rgb(img_path)
result = analyze_image_dual(img)
print(result)
```

### 2. Batch Processing (Directory)
```python
# Analyze all images in a folder
results = []
for img_file in os.listdir("image_folder/"):
    img = read_image_rgb(f"image_folder/{img_file}")
    result = analyze_image_dual(img)
    results.append(result)

df = pd.DataFrame(results)
df.to_csv("rca2_results.csv", index=False)
```

### 3. Statistical Analysis
```python
# Calculate key statistics
rcs_mean = df['mass_radial_compliance'].mean()
rcs_std = df['mass_radial_compliance'].std()
rcs_cv = (rcs_std / rcs_mean) * 100

print(f"Mean RCS: {rcs_mean:.4f}")
print(f"CV: {rcs_cv:.2f}%")
```

## What Good Results Look Like

### Expected Values for Natural Photography
- RCS CV: 12-20%
- IQR: 15-25% of scale (0.15-0.25)
- Mean Δr: 0.15-0.25
- Void Ratio CV: 15-30%

### Observed Values for AI-Generated Images
- RCS CV: 4-6% (**3-5× tighter**)
- IQR: 2-5% of scale (**5-10× narrower**)
- Mean Δr: 0.05-0.10 (**2-3× more centered**)
- Void Ratio CV: 8-10% (**2-3× more uniform**)

### Red Flags for Compositional Collapse
- CV < 5% across semantically diverse prompts
- IQR < 5% of measurement scale
- Mean Δr < 0.06 (within 6% of frame center)
- Within-category variance > between-category variance

## Limitations & Considerations

**What RCA-2 Does NOT Measure:**
- Semantic content (what the image depicts)
- Perceptual quality (how "good" it looks)
- Aesthetic value (artistic merit)
- Rule-of-thirds alignment (Cartesian composition)
- Depth layering or perspective

**What RCA-2 DOES Measure:**
- Radial mass distribution patterns
- Centering bias
- Spatial sparseness
- Geometric uniformity across datasets

**Best Used For:**
- Comparing multiple images from same source
- Detecting optimization-induced constraints
- Quantifying compositional diversity (or lack thereof)
- Validating hypothesis about geometric priors

**Not Ideal For:**
- Scoring individual image quality
- Predicting human preference
- Images with extreme aspect ratios (e.g., panoramas)
- Highly abstract/scattered compositions (low E_s)

## Technical Notes

### Coordinate System
- Origin (0, 0) is top-left corner
- Normalized coordinates: frame center is (0.5, 0.5)
- Δx, Δy measured relative to center: range [-0.5, +0.5]

### Mask Detection
- Uses hybrid approach: Otsu thresholding + edge detection
- Keeps largest connected component (assumes single primary subject)
- Border penalty applied to discourage edge artifacts

### Radial Profile Fitting
- Exponential decay: p(r) = A × exp(-α × r)
- Jensen-Shannon Divergence (JSD) measures fit quality
- Lower JSD = better radial compliance

### Performance
- Typical processing time: 0.5-2 seconds per image
- Memory: ~100MB for single image analysis
- Batch processing: Linear scaling with image count

## Troubleshooting

**"Radially ineligible" classifications:**
- Check E_s score (< 0.38 means geometry doesn't support radial analysis)
- Image may have elongated, scattered, or fragmented subjects
- Not a failure—just means radial measurement isn't appropriate

**Unexpected low RCS values:**
- Verify mask detection is working (check visual output)
- Some images genuinely aren't radially organized
- Low RCS is a valid result, not an error

**High variance in batch results:**
- Expected for diverse natural photography (CV 12-20%)
- Low variance (CV < 5%) is the interesting finding
- Compare to dataset category expectations

**Processing errors:**
- Ensure images are RGB (not RGBA or grayscale)
- Check file paths are correct
- Verify sufficient memory for large batches

## Citation & Attribution

This notebook implements the RCA-2 methodology developed by Russell Parrish (A.rtist I.nfluencer) for measuring compositional collapse in AI image generation.

**Related Publications:**
- "Measuring Compositional Collapse in AI Image Generation: Evidence from MidJourney" (2025)
- "Sora Compositional Analysis: Cross-Model Validation" (2025)

**ORCID:** 0009-0008-9781-7995

## License & Usage

© 2025 Russell Parrish / A.rtist I.nfluencer. All rights reserved.

This tool is provided for research and analysis purposes. If you use RCA-2 in your work, please cite appropriately and acknowledge the source.

---

**Version:** RCA-2 (December 2025)  
**Last Updated:** 12/25/2025  
**Maintained By:** Russell Parrish

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

## 📄 Citation

If used in research or development:

```
Russell Parrish. Visual Thinking Lens: Kernel-Based Compositional Metrics, 2025.
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

## 🤝 Contributing

Issues, pull requests, and extensions are welcome, especially if you are:

- evaluating compositional priors in generative models  
- building new overlays / diagnostics on top of the kernel  
- integrating this into a larger evaluation suite

Please open an issue to discuss significant changes before submitting a PR.

## 🛡️ License

MIT License — permitting open use, modification, and integration.

---

## Acknowledgments

Developed as part of ongoing research into **geometric inductive bias**, **spatial priors**,and **model‑agnostic evaluation techniques**.

---

## 📬 Contact

For questions, extensions, or integration inquiries, contact:  
**Rus — A.rtist I.nfluencer / Visual Thinking Lens** russellgparrish@gmail.com www.artistinfluencer.com

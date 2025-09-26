# Measurement (fast & reproducible)

1. Detect anchors  
   • Vertical edge: Hough lines within ±10° of vertical and within 0.25 W of subject centroid.  
   • Horizon: Hough lines within ±10° of horizontal spanning ≥0.6 W.

2. Subject mask  
   • Coarse SAM/segmentation or manual brush; compute centroid and area %.

3. Compute  
   • Δx: (|centroidₓ − nearest frame edgeₓ|) / W (GD–Edge / GD–Horizon)  
       or (|centroidₓ − frame centerₓ|) / W (GD–Field-Void)  
   • rᵥ: 1 − (subject area + anchor strips + mandatory ground band).  
   • ρᵣ: edge pixel density after suppressing noise (σ≈1.2) normalized to frame area.  
   • seam_count s: long edges count.

4. Pass/Fail  
   • Compare to **Artist Basin** first; if fail, compare to **Engine Bias** window.  
   • Record which window passed and which **profile** (Edge/Horizon/Field).

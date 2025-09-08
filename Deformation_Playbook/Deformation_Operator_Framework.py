
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deformation Operator Playbook — Python Framework (consolidated)
- Resolves feedback: deep copies, missing operators (#2, #3, #8), unified anchors,
  stronger constraints/negatives, semantic prompt generator, engine adapters,
  light validation, seed/version stamping.
- Mirrors the OS model: Anchors → Select → Transforms → Constraints → Viewfinder.
- Code/DSL snippets are MIT-licensed; non-code content remains All Rights Reserved.
"""
from __future__ import annotations

import copy
import json
import math
from dataclasses import dataclass, asdict, field
from enum import Enum
from typing import Dict, List, Optional, Tuple, Union

# -----------------------------
# Enums & core data structures
# -----------------------------

class ContinuityLevel(Enum):
    C0 = "C0"  # position
    C1 = "C1"  # tangent
    C2 = "C2"  # curvature


class EngineType(Enum):
    GPT_DALLE = "gpt_dalle"
    SORA = "sora"
    GEMINI = "gemini"
    MIDJOURNEY = "midjourney"
    OPENART = "openart"


@dataclass
class Anchor:
    x: float  # normalized [0..1]
    y: float
    name: str = ""

    def __post_init__(self):
        if not (0.0 <= self.x <= 1.0 and 0.0 <= self.y <= 1.0):
            raise ValueError("Anchor coordinates must be normalized [0..1]")


@dataclass
class Selection:
    type: str  # "semantic", "polygon", "rect"
    tag: str
    region: Optional[Dict] = None


@dataclass
class Falloff:
    type: str = "gaussian"  # "gaussian" | "linear" | "inverse_square"
    radius: float = 0.12


@dataclass
class Vector:
    dx: float
    dy: float
    def magnitude(self) -> float:
        return math.hypot(self.dx, self.dy)
    def normalize(self) -> "Vector":
        m = self.magnitude()
        return Vector(self.dx/m, self.dy/m) if m > 0 else Vector(0.0, 0.0)


# -----------------------------
# Operators
# -----------------------------

class DeformationOperator:
    def __init__(
        self,
        target: str,
        locks: Optional[List[str]] = None,
        continuity: ContinuityLevel = ContinuityLevel.C1,
        falloff: Optional[Falloff] = None,
    ):
        self.target = target
        self.locks = locks or ["thickness", "topology"]
        self.continuity = continuity
        self.falloff = falloff or Falloff()
        self.anatomical_continuity = True  # default rail

    def to_dict(self) -> Dict:
        return {
            "op": self.__class__.__name__.lower().replace("operator", ""),
            "target": self.target,
            "locks": list(self.locks),
            "continuity": self.continuity.value,
            "falloff": asdict(self.falloff),
            "anatomical_continuity": self.anatomical_continuity,
        }


class PinOperator(DeformationOperator):
    def __init__(self, targets: Union[str, List[str]], stiffness: float = 0.95, **kw):
        if isinstance(targets, str):
            targets = [targets]
        super().__init__(targets[0], **kw)
        self.targets = targets
        self.stiffness = stiffness
    def to_dict(self) -> Dict:
        return {"op": "pin", "target": list(self.targets), "stiffness": self.stiffness}


class ExtendVectorOperator(DeformationOperator):
    """#1 Vector Extension — elbow anchored lengthening"""
    def __init__(self, target: str, anchor: str, vec: Vector, factor: float = 1.6, **kw):
        super().__init__(target, **kw)
        self.anchor, self.vec, self.factor = anchor, vec, factor
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "anchor": self.anchor,
            "vec": {"dx": self.vec.dx, "dy": self.vec.dy},
            "factor": self.factor,
        })
        return d


class SpiralFibonacciOperator(DeformationOperator):
    """#4 Fibonacci Coil — tight proximal, open distal"""
    def __init__(self, target: str, center: str, turns: float = 1.1, scale: float = 0.16,
                 handedness: str = "CW", blend: float = 0.90, **kw):
        super().__init__(target, **kw)
        self.center, self.turns, self.scale = center, turns, scale
        self.handedness, self.blend = handedness, blend
        self.avoid = ["rope", "cord", "external wrapping"]
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "center": self.center,
            "turns": self.turns,
            "scale": self.scale,
            "handedness": self.handedness,
            "blend": self.blend,
            "segment_weight": {"proximal": 0.7, "distal": 1.0},
            "require_overlap_crossing": True,
            "avoid": list(self.avoid),
        })
        return d


class ModulateSineOperator(DeformationOperator):
    """#7 Sine Modulation — single serpentine wave"""
    def __init__(self, target: str, amplitude: float = 0.012, wavelength: float = 0.18,
                 phase: float = 1.57, axis: str = "path", **kw):
        super().__init__(target, **kw)
        self.amplitude, self.wavelength, self.phase, self.axis = amplitude, wavelength, phase, axis
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "axis": self.axis,
            "amplitude": self.amplitude,
            "wavelength": self.wavelength,
            "phase": self.phase,
            "interpret": "single continuous limb; no branching",
        })
        return d


class ExtendParabolicOperator(DeformationOperator):
    """#5 Parabolic Extension — graceful arc with elbow as crest"""
    def __init__(self, target: str, vertex_lock: str, factor: float = 0.42, **kw):
        super().__init__(target, **kw)
        self.vertex_lock, self.factor = vertex_lock, factor
        self.curvature_tension = 0.72
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "vertex_lock": self.vertex_lock,
            "factor": self.factor,
            "curvature_tension": self.curvature_tension,
            "distal_taper": 0.80,
            "proximal_weight": 0.70,
            "asymmetry_bias": 0.20,
            "self_occlusion_enhance": {"strength": 0.70, "width": 0.012, "side": "inner_curve"},
            "require_elbow_continuity": True,
            "avoid": ["ballooning", "crease seam"],
        })
        return d


class PerspectiveInverseSquareOperator(DeformationOperator):
    """#6 Depth Tug — localized pull toward a point (camera fixed)"""
    def __init__(self, target: str, vanishing: Dict[str, float], magnitude: float = 0.44, **kw):
        super().__init__(target, **kw)
        self.vanishing, self.magnitude = vanishing, magnitude
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "vanishing": self.vanishing,
            "magnitude": self.magnitude,
            "thickness_lock": 0.90,
            "silhouette_preserve": 0.86,
            "z_bias": 0.18,
            "torsion_compensation": 0.20,
            "distal_scale_comp": 0.92,
            "depth_occlusion_enhance": {"strength": 0.68, "width": 0.010, "region": "under-forearm_to_wrist"},
            "require_vanishing_convergence": True,
            "convergence_tolerance": 0.05,
            "avoid": ["accordion_fold", "thin_wrist_collapse", "edge chatter"],
        })
        return d


class ScaleLogOperator(DeformationOperator):
    """#2 Logarithmic Scaling — gradual stretch along an axis"""
    def __init__(self, target: str, axis: str = "y", center: str = "", amount: float = 0.8, **kw):
        super().__init__(target, **kw)
        self.axis, self.center, self.amount = axis, center, amount
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "axis": self.axis,
            "center": self.center,
            "amount": self.amount,
            "interpret": "more stretch near base, less toward tip; width stays believable",
        })
        return d


class RotateJointOperator(DeformationOperator):
    """#3 Rotational Transform — rotate around a hinge (elbow/wrist/shoulder)"""
    def __init__(self, target: str, hinge: str, degrees: float = 12.0,
                 axial_twist: bool = False, **kw):
        super().__init__(target, **kw)
        self.hinge, self.degrees, self.axial_twist = hinge, degrees, axial_twist
    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({
            "hinge": self.hinge,
            "degrees": self.degrees,
            "axial_twist": self.axial_twist,
            "guard": {"preserve_thickness": True, "freeze_parent": True, "keep_elbow_angle": True},
        })
        return d


# Non-deforming composition operator (optional explicit form for #8)
class ViewfinderOperator(DeformationOperator):
    """#8 Ghost Density via Viewfinder — reframing without geometry change"""
    def __init__(self, shift: Dict[str, float], zoom: float = 1.0,
                 edge_proximity: Optional[Dict] = None, void_bias: Optional[Dict] = None):
        super().__init__(target="viewfinder", locks=[])
        self.shift, self.zoom = shift, zoom
        self.edge_proximity, self.void_bias = edge_proximity, void_bias
    def to_dict(self) -> Dict:
        return {
            "op": "viewfinder",
            "shift": dict(self.shift),
            "zoom": float(self.zoom),
            "edge_proximity": dict(self.edge_proximity) if self.edge_proximity else None,
            "void_bias": dict(self.void_bias) if self.void_bias else None,
        }


# -----------------------------
# Style & Capsule
# -----------------------------

@dataclass
class StyleBinder:
    medium: str = "charcoal drawing"
    lighting: str = "soft diffused light"
    clothing: str = "short-sleeved figure"
    background: str = "textured paper"
    pose: str = "neutral pose"
    def to_prompt_fragment(self) -> str:
        return f"{self.medium}, {self.lighting}, {self.clothing} on {self.background}, {self.pose}"


@dataclass
class Viewfinder:
    shift: Dict[str, float] = field(default_factory=lambda: {"dx": 0.0, "dy": 0.0})
    zoom: float = 1.0
    edge_proximity: Optional[Dict] = None
    void_bias: Optional[Dict] = None


class VCFCapsule:
    def __init__(self, version: str = "1.1"):
        self.version = version
        self.style = StyleBinder()
        self.anchors: Dict[str, Anchor] = {}
        self.selections: Dict[str, Selection] = {}
        self.transforms: List[DeformationOperator] = []
        self.constraints: Dict = {
            "seamless_integration": True,
            "material_consistency": "charcoal",
            "avoid": [
                "rope", "cord", "wrapping", "bracelet", "armor", "prosthetic",
                "segmented", "tubes", "rings", "thin_wrist_collapse", "duplicate limbs"
            ],
        }
        self.viewfinder = Viewfinder()
        self.notes = ""
        self.meta: Dict[str, str] = {"engine": "", "model": "", "seed": ""}

    # --- build API ---
    def add_anchor(self, name: str, x: float, y: float) -> "VCFCapsule":
        self.anchors[name] = Anchor(x, y, name); return self
    def add_selection(self, name: str, tag: str, selection_type: str = "semantic") -> "VCFCapsule":
        self.selections[name] = Selection(selection_type, tag); return self
    def add_transform(self, operator: DeformationOperator) -> "VCFCapsule":
        self.transforms.append(operator); return self
    def set_meta(self, engine: str = "", model: str = "", seed: str = "") -> "VCFCapsule":
        self.meta.update({"engine": engine, "model": model, "seed": seed}); return self

    # --- export ---
    def to_yaml(self) -> str:
        data = {
            "vcf_capsule": self.version,
            "style": self.style.to_prompt_fragment(),
            "anchors": {k: {"x": v.x, "y": v.y} for k, v in self.anchors.items()},
            "select": {k: {"type": s.type, "tag": s.tag} for k, s in self.selections.items()},
            "transforms": [op.to_dict() for op in self.transforms],
            "constraints": self.constraints,
            "viewfinder": asdict(self.viewfinder),
            "notes": self.notes,
            "meta": self.meta,
        }
        try:
            import yaml  # optional
            return yaml.dump(data, default_flow_style=False, sort_keys=False)
        except Exception:
            return json.dumps(data, indent=2)

    def to_json(self) -> str:
        data = {
            "vcf_capsule": self.version,
            "style": self.style.to_prompt_fragment(),
            "anchors": {k: {"x": v.x, "y": v.y} for k, v in self.anchors.items()},
            "select": {k: {"type": s.type, "tag": s.tag} for k, s in self.selections.items()},
            "transforms": [op.to_dict() for op in self.transforms],
            "constraints": self.constraints,
            "viewfinder": asdict(self.viewfinder),
            "notes": self.notes,
            "meta": self.meta,
        }
        return json.dumps(data, indent=2)


# -----------------------------
# Lint / validation
# -----------------------------

class CapsuleValidator:
    REQUIRED_ANCHORS_MAP = {
        ExtendVectorOperator: ["elbow_L"],  # anchor is elbow_L by convention
        SpiralFibonacciOperator: ["shoulder_L"],
        ExtendParabolicOperator: ["elbow_L"],
        PerspectiveInverseSquareOperator: [],
        ScaleLogOperator: [],
        RotateJointOperator: [],
    }
    CONSISTENT_ANCHOR_NAMES = {"shoulder_L", "elbow_L", "wrist_L", "skull_base", "sternal_notch", "pelvis"}

    @classmethod
    def validate(cls, cap: VCFCapsule) -> List[str]:
        errors: List[str] = []

        # naming consistency
        for name in cap.anchors.keys():
            if name not in cls.CONSISTENT_ANCHOR_NAMES:
                errors.append(f"Unknown anchor '{name}'. Use standard names: {sorted(cls.CONSISTENT_ANCHOR_NAMES)}")

        # operator requirements
        for op in cap.transforms:
            req = cls.REQUIRED_ANCHORS_MAP.get(type(op), [])
            for r in req:
                if r not in cap.anchors:
                    errors.append(f"{type(op).__name__} requires anchor '{r}'")

            # hinge validation for RotateJoint
            if isinstance(op, RotateJointOperator) and op.hinge not in cap.anchors:
                errors.append(f"RotateJointOperator hinge '{op.hinge}' missing in anchors")

            # center for ScaleLog if provided
            if isinstance(op, ScaleLogOperator) and op.center and op.center not in cap.anchors:
                errors.append(f"ScaleLogOperator center '{op.center}' missing in anchors")

        # selections sanity
        if not cap.selections:
            errors.append("No selections defined. Add at least one selection region.")

        return errors


# -----------------------------
# Prompt generation (semanticized)
# -----------------------------

class PromptGenerator:
    def __init__(self, engine: EngineType, semanticize: bool = True):
        self.engine = engine
        self.semanticize = semanticize

    @staticmethod
    def _approx_factor(val: float) -> str:
        if val >= 1.8: return "nearly double"
        if val >= 1.5: return "about one and a half times"
        if val >= 1.2: return "slightly longer"
        return "a gentle increase"

    @staticmethod
    def _angle_words(deg: float) -> str:
        if deg >= 25: return "a clear turn"
        if deg >= 10: return "a small turn"
        return "a subtle turn"

    def generate_instructional_prompt(self, cap: VCFCapsule) -> str:
        """Sora/Gemini/GPT—binder first, plain English, acceptance cues, minimal negatives."""
        parts: List[str] = [cap.style.to_prompt_fragment() + "."]
        parts.append("The body itself deforms; keep continuous skin and believable volume.")

        for t in cap.transforms:
            if isinstance(t, ExtendVectorOperator):
                words = self._approx_factor(t.factor) if self.semanticize else f"{t.factor}×"
                parts.append(
                    f"Lengthen the {t.target} outward from the {t.anchor} along a gentle diagonal—{words} the normal reach; "
                    "keep thickness and connection."
                )
            elif isinstance(t, SpiralFibonacciOperator):
                parts.append(
                    f"Form a graceful spiral in the {t.target}, tighter near the {t.center} and opening toward the hand; "
                    "show one visible overlap; the spiral is the arm itself, not wrapping."
                )
            elif isinstance(t, ModulateSineOperator):
                parts.append(
                    f"Add one gentle serpentine wave from elbow to hand; the limb’s mass follows the wave; hand stays intact."
                )
            elif isinstance(t, ExtendParabolicOperator):
                parts.append(
                    f"Shape the {t.target} into a smooth, elegant arc with the {t.vertex_lock} as the crest; "
                    "avoid a sharp crease; add a faint inner-curve shadow."
                )
            elif isinstance(t, PerspectiveInverseSquareOperator):
                parts.append(
                    "Do not change the camera. Modify only the forearm: make both top and bottom edges subtly converge toward a small point to the right, "
                    "strongest near the wrist; keep the upper arm unchanged; tighten wrist-crease spacing and add a narrow soft shadow under the forearm."
                )
            elif isinstance(t, ScaleLogOperator):
                parts.append(
                    f"Stretch the {t.target} upward gradually—more near the {t.center or 'base'}, less toward the tip—keeping width proportional; "
                    "leave the rest of the body unchanged."
                )
            elif isinstance(t, RotateJointOperator):
                words = self._angle_words(t.degrees) if self.semanticize else f"{t.degrees}°"
                parts.append(
                    f"Freeze the parent segment. Rotate the {t.target} around the {t.hinge} with {words}; "
                    "keep the elbow angle the same and preserve wrist fullness; add a subtle spiral crease."
                )
            elif isinstance(t, ViewfinderOperator):
                parts.append(
                    "Reframe only: push the subject toward the left edge, leave a wide right-side void, add a slight zoom. Do not change anatomy."
                )

        # constraints/negatives
        parts.append("No ropes, bands, prosthetics, or extra limbs. No text or watermarks.")
        # legibility cue reminder
        parts.append("Seamless integration; material consistency: " + cap.constraints.get("material_consistency", "charcoal") + ".")
        return " ".join(parts)

    def generate_midjourney_prompt(self, cap: VCFCapsule) -> str:
        base = self.generate_instructional_prompt(cap)
        params = ["--style raw", "--stylize 40", "--chaos 0"]
        avoid = set(cap.constraints.get("avoid", []))
        avoid.update({"rope", "cord", "wrapping", "bracelet", "armor", "prosthetic", "segmented", "tubes", "rings"})
        return f"{base} --no {', '.join(sorted(avoid))} {' '.join(params)}"

    def generate_openart_prompts(self, cap: VCFCapsule) -> Dict[str, str]:
        """Two-step: BASE (txt2img) and EDIT (inpaint) with strong negatives."""
        binder = cap.style.to_prompt_fragment()
        negatives = ", ".join(sorted({
            "rope","cord","wrapping","bracelet","armor","prosthetic","segmented","tubes","rings",
            "gaps","extra limbs","broken anatomy","accordion folds","thin wrist collapse","logo","watermark"
        }))
        # operator-only line
        op_line = self.generate_instructional_prompt(cap).split(". ", 1)[1] if ". " in self.generate_instructional_prompt(cap) else self.generate_instructional_prompt(cap)
        return {
            "BASE_positive": f"{binder}. Neutral pose. Realistic charcoal modeling.",
            "BASE_negative": negatives,
            "EDIT_positive": "The body itself deforms; continuous skin and believable volume. " + op_line,
            "EDIT_negative": negatives,
            "settings_hint": "CFG 5.5–6.5, steps 28–36; inpaint denoise 0.35–0.45; include elbow + wrist in mask; feather 8–16 px."
        }


# -----------------------------
# Framework & templates
# -----------------------------

class DeformationFramework:
    def __init__(self):
        self.templates = self._create_templates()

    def _create_templates(self) -> Dict[str, VCFCapsule]:
        T: Dict[str, VCFCapsule] = {}

        # 1) Arm extension (vector) — elbow anchored
        cap = VCFCapsule()
        cap.add_anchor("shoulder_L", 0.30, 0.40).add_anchor("elbow_L", 0.33, 0.58).add_anchor("wrist_L", 0.37, 0.78)
        cap.add_selection("arm_L", "left_arm_forearm_hand")
        cap.add_transform(PinOperator(["elbow_L"], stiffness=0.95))
        cap.add_transform(ExtendVectorOperator("arm_L", "elbow_L", Vector(0.65, 0.18), factor=1.6))
        cap.viewfinder = Viewfinder(shift={"dx": -0.06, "dy": 0.02}, zoom=1.03)
        cap.notes = "Gentle arm extension anchored at elbow"
        T["arm_extension"] = cap

        # 2) Sine modulation — serpentine wave
        cap = VCFCapsule()
        cap.add_anchor("elbow_L", 0.33, 0.56).add_anchor("wrist_L", 0.38, 0.78)
        cap.add_selection("arm_L", "left_arm_forearm_hand")
        cap.add_transform(PinOperator(["elbow_L", "wrist_L"], stiffness=0.96))
        cap.add_transform(ModulateSineOperator("arm_L", amplitude=0.020, wavelength=0.22))
        cap.viewfinder = Viewfinder(shift={"dx": -0.04, "dy": 0.02}, zoom=1.02)
        cap.notes = "Serpentine wave with safe defaults"
        T["sine_modulation"] = cap

        # 3) Fibonacci coil — organic torsion
        cap = VCFCapsule()
        cap.add_anchor("shoulder_L", 0.30, 0.40).add_anchor("elbow_L", 0.33, 0.58)
        cap.add_selection("arm_L", "left_arm_forearm_hand")
        cap.add_transform(SpiralFibonacciOperator("arm_L", "shoulder_L", turns=1.1, scale=0.16))
        cap.notes = "Organic spiral with tight-proximal, open-distal growth"
        T["fibonacci_coil"] = cap

        # 4) Parabolic extension — graceful arc
        cap = VCFCapsule()
        cap.add_anchor("elbow_L", 0.33, 0.58).add_anchor("wrist_L", 0.37, 0.78).add_anchor("shoulder_L", 0.30, 0.40)
        cap.add_selection("arm_L", "left_arm_forearm_hand")
        cap.add_transform(ExtendParabolicOperator("arm_L", vertex_lock="elbow_L", factor=0.42))
        cap.notes = "Parabolic arc with inner-curve occlusion"
        T["parabolic_extension"] = cap

        # 5) Depth tug — inverse-square pull (forearm only)
        cap = VCFCapsule()
        cap.add_anchor("elbow_L", 0.33, 0.58).add_anchor("wrist_L", 0.37, 0.78)
        cap.add_selection("arm_L", "left_arm_forearm_hand")
        cap.add_transform(PerspectiveInverseSquareOperator("arm_L", vanishing={"x": 0.85, "y": 0.42}, magnitude=0.44))
        cap.notes = "Localized pull toward off-frame right; camera fixed"
        T["depth_tug"] = cap

        # 6) Log scaling (neck)
        cap = VCFCapsule()
        cap.add_anchor("skull_base", 0.50, 0.20).add_anchor("sternal_notch", 0.50, 0.24)
        cap.add_selection("neck", "neck")
        cap.add_transform(ScaleLogOperator("neck", axis="y", center="sternal_notch", amount=0.78, continuity=ContinuityLevel.C2))
        cap.notes = "Gradual neck stretch; width preserved"
        T["log_scaling_neck"] = cap

        # 7) Rotational transform (forearm around elbow, palm inward)
        cap = VCFCapsule()
        cap.add_anchor("elbow_L", 0.33, 0.58).add_anchor("wrist_L", 0.37, 0.78)
        cap.add_selection("forearm_L", "left_forearm")
        cap.add_transform(RotateJointOperator("forearm_L", hinge="elbow_L", degrees=18.0))
        cap.notes = "Forearm twist with parent frozen; wrist fullness preserved"
        T["rotation_forearm"] = cap

        # 8) Ghost density via viewfinder — framing only
        cap = VCFCapsule()
        cap.add_selection("arm_L", "left_arm_forearm_hand")
        cap.add_transform(ViewfinderOperator(shift={"dx": -0.20, "dy": 0.06}, zoom=1.10,
                                             edge_proximity={"left": 0.85}, void_bias={"right": 1.25}))
        cap.notes = "Framing tension; no geometry change"
        T["ghost_density_viewfinder"] = cap

        return T

    def list_templates(self) -> List[str]:
        return list(self.templates.keys())

    def get_template(self, name: str) -> Optional[VCFCapsule]:
        return self.templates.get(name)

    def create_capsule(self, template_name: Optional[str] = None) -> VCFCapsule:
        if template_name and template_name in self.templates:
            # deep copy to prevent bleed between instances
            t = self.templates[template_name]
            c = VCFCapsule(t.version)
            c.style = copy.deepcopy(t.style)
            c.anchors = copy.deepcopy(t.anchors)
            c.selections = copy.deepcopy(t.selections)
            c.transforms = copy.deepcopy(t.transforms)
            c.constraints = copy.deepcopy(t.constraints)
            c.viewfinder = copy.deepcopy(t.viewfinder)
            c.notes = t.notes
            c.meta = copy.deepcopy(t.meta)
            return c
        return VCFCapsule()

    # convenience
    def validate(self, capsule: VCFCapsule) -> List[str]:
        return CapsuleValidator.validate(capsule)

    def make_prompt(self, capsule: VCFCapsule, engine: EngineType) -> Union[str, Dict[str, str]]:
        gen = PromptGenerator(engine, semanticize=True)
        if engine == EngineType.MIDJOURNEY:
            return gen.generate_midjourney_prompt(capsule)
        if engine == EngineType.OPENART:
            return gen.generate_openart_prompts(capsule)
        # Sora / Gemini / GPT-family
        return gen.generate_instructional_prompt(capsule)


# -----------------------------
# Demo
# -----------------------------

def _demo():
    fw = DeformationFramework()
    cap = fw.create_capsule("depth_tug").set_meta(engine="sora", model="unknown", seed="")
    errs = fw.validate(cap)
    if errs:
        print("Validation issues:", *errs, sep="\n- ")
    print("\nYAML spec:\n", cap.to_yaml())
    print("\nSora prompt:\n", fw.make_prompt(cap, EngineType.SORA))
    print("\nMidJourney prompt:\n", fw.make_prompt(cap, EngineType.MIDJOURNEY))
    print("\nOpenArt prompts:\n", json.dumps(fw.make_prompt(cap, EngineType.OPENART), indent=2))

if __name__ == "__main__":
    _demo()

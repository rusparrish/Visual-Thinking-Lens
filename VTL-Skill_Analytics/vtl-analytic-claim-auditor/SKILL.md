---
name: analytic-claim-auditor
description: Audit reports, captions, interpretations, papers, slide text, methods notes, public explanations, or agent outputs that use Playground Analytic metrics or vocabulary. Use when checking whether claims from VCLI-G, SCI, VTL Kernel, LSI v2, RCA-2, RDC, RCP, perturbation, sequence, telemetry, model-comparison, or safe-middle analyses overstate the evidence, turn metrics into quality judgments, confuse related terms, ignore QA/comparability, treat single images as cohort evidence, or need safer claim language.
---

# Analytic Claim Auditor

Use this skill to review analytic language before it is trusted, published, shared, or used as a decision basis. The goal is to keep claims aligned with the evidence available from the Playground Analytic stack.

This skill audits claims. It does not rerun extraction, recalculate scores, or replace the domain interpreter. If the evidence is missing, say what evidence would be needed.

## Inputs

Use whatever the user provides:

- Draft text: report sections, captions, slide copy, methods notes, public explanations, papers, comments, or agent outputs.
- Evidence: metric rows, CSV/JSON excerpts, screenshots, visual panels, QA fields, audit findings, prompt/model metadata, perturbation summaries, sequence rows, or cohort summaries.
- System context: VCLI-G/SCI, VTL Kernel, LSI v2, RCA-2/RDC, RCP, perturbation, sequence, telemetry, model comparison, or safe-middle frame.
- Intended audience: public, artist, research, engineering, product, curator, client, internal model team, or executive.

If the user gives only text and no evidence, audit the claim form and identify evidence gaps without asserting whether the underlying analysis is true.

## Audit Workflow

1. Identify the claim units.
   - Split the text into concrete claims.
   - Separate structural, perceptual, model-prior, prompt-fidelity, sequence, telemetry, and quality/preference claims.

2. Match each claim to evidence.
   - Name the metric, visual evidence, cohort summary, audit result, or extraction output that supports it.
   - If no evidence is present, mark it as unsupported.
   - If the evidence belongs to another layer, mark a layer mismatch.

3. Check scope.
   - Single image claims must remain local.
   - Cohort/model-prior claims require repeated comparable evidence.
   - Sequence claims require ordered comparable frames.
   - Perturbation claims require the deterministic perturbation set or a clearly documented equivalent.
   - Prompt-fidelity claims require prompt intent plus measured structural response.

4. Check vocabulary boundaries.
   - VCLI-G/SCI describe perceptual load and coherence, not quality by themselves.
   - VTL Kernel vectors describe structural coordinates and mask-mediated field behavior.
   - LSI v2 describes structural position, gates, prior distance, sequence coherence, telemetry, and perturbation robustness.
   - RCA-2/RDC/RCP describe radial compliance, default-candidate eligibility, and radial-collapse evidence.
   - Telemetry is advisory and must not change gates or acceptance.

5. Check QA and comparability.
   - Look for missing `mask_status`, hashes, preprocessing, extractor version, duplicate drift, valid perturbation count, sequence ordering, or cohort comparability.
   - If QA blocks interpretation, mark the claim as invalid until fixed.

6. Assign a finding severity.
   - `Blocker`: claim should not be used as written.
   - `Major`: claim overreaches or needs material caveating.
   - `Minor`: wording is mostly sound but imprecise.
   - `Clean`: claim is supported and scoped.

7. Rewrite risky claims.
   - Keep the intended meaning where possible.
   - Downgrade from verdicts to structural findings.
   - Add scope, evidence, and caveats.
   - Prefer "supports", "is consistent with", "candidate", "local", "in this batch", "under these settings", and "requires replication" when needed.

## Output Format

```markdown
**Analytic Claim Audit**
Classification:
Audit Status: <clean | usable with revisions | blocked>
Severity Ceiling: <blocker | major | minor>
Scope Type: <single | sequence | cohort | model comparison | unknown>

**Evidence Absence = Block:**
If claim has no supporting evidence:
→ Severity = Blocker
→ claim must be rewritten or removed

**Single Image Hard Gate:**
Single image:
→ cannot support:
  - model prior
  - collapse pattern
  - safe-middle claim
  
**If QA issues exist:**
→ must downgrade claim
→ if ignored → Blocker

**Comparability Gate:**
If comparison lacks:
- matched preprocessing
- extractor version
- QA parity

→ Severity = Major or Blocker

**Channel Isolation Rule:**
If claim uses single metric:
→ Severity = Major
→ require composite evidence

**Causal Language Detector:**
If claim uses:
- causes
- proves
- leads to

→ rewrite to:
- supports
- consistent with

**Priority:**
1. Blocker fixes
2. Scope corrections
3. Evidence linking
4. Language precision

**Batch vs Sequence Guard:**
If sequence language used without ordered data:
→ Severity = Blocker

**No Silent Upgrade:**
Do not:
- upgrade claim strength in rewrite

**Rewrite must:**
- keep intent
- remove overclaim
- add scope + evidence

**Findings**
| Severity | Claim | Issue | Safer Revision |
|---|---|---|---|
| <Blocker/Major/Minor/Clean> | <quoted or summarized claim> | <why it is unsupported, overbroad, or clean> | <replacement wording or "No change"> |

**Evidence Gaps**
- <missing metrics, QA fields, visual evidence, cohort metadata, perturbation rows, sequence order, or comparability details>

**Boundary Notes**
- <key claim boundaries that matter for this text>

**Revised Version**
<optional revised paragraph/report section if the user asked for rewriting or if compact rewrite is clearly useful>

**Confidence:**
<high | medium | low>

Drivers:
- evidence completeness
- scope clarity
- QA presence
```

## Hard Stops

- Do not validate a quality, preference, semantic, intent, or aesthetic claim from structural metrics alone.
- Do not let single-image evidence imply model behavior, distributional prior, collapse pattern, or safe-middle convergence.
- Do not treat telemetry as changing CTG, RDC, SFS, BCI, LSI100, acceptance, or core structural gates.
- Do not treat `mask_status=FAIL`, invalid masks, failed perturbation rows, missing hashes, or non-comparable preprocessing as administrative details.
- Do not interpret a single metric channel or primitive in isolation without naming the composite.
- Do not merge VTL `r_v` and LSI `rv` unless the text explicitly distinguishes their definitions.
- Do not treat Perturbation Mode `P` as sequence stability `S`.
- Do not call RDC/RCP evidence proof of all centered composition being bad or collapsed.
- Do not call CTG, SFS, VCLI-G, SCI, LSI100, or any composite a direct quality score unless separate validation evidence is supplied.

## Common Overclaims

Read `references/overclaim-patterns.md` when the draft makes strong causal, quality, model-prior, cohort, or collapse claims.

Read `references/revision-language.md` when you need safer replacement language.

## Related Skills

- Use domain auditors first when the math or pipeline itself is in question: `vcli-g-scoring-auditor`, `vtl-kernel-scoring-auditor`, `lsi-v2-scoring-auditor`, `lsi-perturbation-auditor`, or `rca-2-scoring-auditor`.
- Use report writers after this skill when the claims are clean enough to turn into audience-specific prose.
- Use `image-metric-positioning` when the claim compares this stack to CLIP, FID, aesthetic scoring, reward models, or human preference metrics.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.

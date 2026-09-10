# AI Dependency Test

A complete decision record may still depend on unsupported AI output. This working procedure separates structural record completeness from substantive independence from AI output. It supersedes the historical [AI Removability Proof](ai-removability-proof.md).

Question: Can the non-AI decision basis still be reconstructed when model-generated artifacts are excluded from the evidentiary basis?

## Preserve the record

Freeze the record identifier, revision or commit, assessment date, and referenced source versions. Retain the original record and AI artifacts for provenance. Record what the model contributed, including AI-assisted wording carried into the rationale.

In RGDS v2.0.1, `ai_assistance` is required, with `used`, `use_cases`, `artifacts`, and `controls`. Keep `used: true` when AI was used. Deleting the object is schema-invalid. Setting it to false is not a valid dependency test and misstates the history.

Create a separate assessment manifest listing model-generated artifacts and passages excluded from evidentiary support. The original references remain available to audit AI use; they cannot be used as independent support in this assessment. No automatic record transformation is specified. Do not add this manifest as an undeclared field in the RGDS JSON record.

## Part A: Structural record completeness

Run the pinned RGDS schema and semantic validator on the original record. Record commands, versions, errors, and warnings. Then inventory the following fields and identify where their supporting references are AI artifacts:

| Record area | RGDS v2.0.1 location |
|---|---|
| Question and options | `decision_question`, `options_considered` |
| Outcome and rationale | `decision_outcome` including `rationale_summary` |
| Evidence and completeness | `evidence`, `evidence_completeness` |
| Risk | `risk_posture`, `risk_assessment` |
| Assigned authority | `governance` |
| AI-use provenance | `ai_assistance` |
| Audit and follow-up | `audit`; applicable `actions` and outcome conditions |

Report `pass` only when required structure and semantic checks pass and the inventory is complete; report warnings separately. Report `fail` for missing required fields or failed checks, and `not assessed` when validation was not run. Successful validation does not establish source truth, human authorship, approval authenticity, or substantive independence. Merely retaining non-AI field names is insufficient: their content may derive from AI.

## Part B: Substantive independence

A named, qualified reviewer inspects the non-AI source packet. Record expertise, role, prior exposure to AI outputs, and any independence limitations. Where feasible, use a reviewer who did not see the model output before reviewing the source packet.

For each material rationale claim, option comparison, uncertainty, risk acceptance, and condition:

1. Identify the exact non-AI source and passage or data supporting it, with version and access information.
2. State the reasoning connecting the source to the claim. Inspect AI-assisted rationale wording against those sources instead of treating the wording as evidence.
3. Identify contradictions, missing sources, assumptions, and model-derived steps that cannot be reconstructed independently.
4. Record the reviewer's assessment and reasons, including dissent. Identify required evidence or re-review and a responsible human for each unresolved dependency.

Report one of these substantive results:

| Result | Meaning |
|---|---|
| Supported | All material steps in the declared scope have inspectable non-AI support and documented reconstruction |
| Partially supported | Some material steps have support; identified dependencies remain unresolved |
| Unsupported | Inspected evidence fails to support a material step or reconstruction relies on excluded model output |
| Indeterminate | Missing access, expertise, or other limitations prevent a defensible assessment |
| Not assessed | No substantive review was performed |

A structural pass must never be promoted to a substantive result. Missing source access warrants indeterminate, not supported. An unsupported or unresolved basis requires human re-review under the adopting process; this assessment does not retroactively approve, invalidate, or alter a decision.

## Assessment record

Store the following beside the versioned record, subject to appropriate source-access controls:

```text
Decision identifier and frozen revision:
RGDS schema/validator revision:
Assessor, role, expertise, date, prior AI exposure:
Scope and material rationale claims:
Excluded AI artifact/passage identifiers:
Non-AI source identifiers, versions, access limits:
Structural result, command output, warnings:
Claim -> source passage -> reasoning -> assessment:
Substantive result and reasons:
Dissent, unresolved dependencies, owner, follow-up date:
Review/approval status and limitations:
```

This procedure assesses a bounded reconstruction of the documented basis. It cannot establish that the same outcome would have occurred without AI, that the original author reasoned independently, that humans exercised practical authority, or that a decision is correct, legally compliant, or regulator-accepted. Anchoring and undocumented AI influence may survive an apparently independent reconstruction. Practical human influence requires separate assessment.

See the [hypothetical example](../examples/rgds-dec-0003-ai-assisted-conditional-go.md) for an indeterminate substantive result and [validation instructions](validation.md) for the reproducible structural boundary check. No empirical validation of this assessment method is claimed.

# Non-Agentic AI Contract

This reference method/profile defines adoption requirements for bounded AI assistance in regulated phase-gate decisions. It is not a legal agreement or an implemented control system. Organizations adopting the profile must establish their own operational controls and assess whether the requirements are followed.

The conceptual hierarchy is GDI general decision architecture -> AI Assistance Governance method/profile -> RGDS regulated reference implementation. The independent study is separate historical/exploratory research. The implementation contract inspected here is [RGDS v2.0.1](https://github.com/mj3b/rgds/tree/v2.0.1).

## Definitions

| Term | Meaning in this profile |
|---|---|
| AI assistance | Model-generated output used in analysis or drafting for a decision |
| Agentic behavior | AI initiating, deciding, approving, or executing without explicit human invocation of that specific action |
| Non-agentic assistance | An explicitly invoked bounded analytical task whose output receives human review before use |
| Human owner | Named individual assigned accountability within the adopting organization's authority structure |
| Decision outcome | RGDS value: `go`, `no_go`, `conditional_go`, `defer`, or `defer_with_required_evidence` |
| Escalation | Governance routing/action when authority or evidence is insufficient; not an RGDS outcome value |
| AI dependency | A material rationale step whose support cannot be reconstructed without model-generated output |

## Covenant 1: No autonomous or agentic behavior

AI must not initiate decisions, approve or reject outcomes, accept risk, trigger downstream actions, or act without explicit invocation. Permitted assistance includes summarization, comparison, extraction, candidate gap identification, and structured drafting for review. Delegating escalation or approval to AI violates this profile. These prohibitions require operational controls outside the record schema.

## Covenant 2: Assigned human authority and assessed independence

Identify the human owner and approvers and their authority scope. Require review of the decision basis and assess independence using the [AI Dependency Test](../docs/ai-dependency-test.md). Record unsupported steps and unresolved dependencies for human disposition.

RGDS records assigned human ownership, approval, and review. It cannot establish that a named person authored the rationale, understood the evidence, or exercised substantive judgment. Practical human influence requires separate assessment. A complete record and a substantive dependency assessment must have separate results.

## Covenant 3: Explicit invocation

AI assistance must be intentional, contextual, visible, and optional. Record the task, tool, and contribution. Background recommendations, ambient influence, and implicit AI defaults are prohibited. Skipping AI must be an available workflow choice; this requirement does not establish that prior decisions are independent of AI.

## Covenant 4: Reviewability and rejection

A named reviewer with relevant expertise must inspect each material AI contribution and record acceptance, rejection, or modification with reasons. Preserve corrections and dissent. Absence of rejection is not acceptance. An entry in `human_review` documents a review claim; validation cannot authenticate the review or measure its quality.

## Covenant 5: No silent risk acceptance

Humans must declare uncertainty, assumptions, disagreement, and accepted residual risk. AI must not conceal conflicts, infer risk acceptance from proceeding, or convert unresolved uncertainty into an accepted position. RGDS `risk_posture` and `risk_assessment` record the declared basis; validation cannot establish its adequacy.

## Covenant 6: Evidence subordination

Trace material decision claims to inspectable non-AI sources. AI summaries and draft rationale must not replace those sources or serve as primary justification. Retain AI artifacts for provenance while excluding them from evidentiary support in a dependency assessment. A model-derived step without non-AI support must be reported, not presumed independent.

## Compatibility with the RGDS v2.0.1 contract

Sources: the [JSON Schema](https://github.com/mj3b/rgds/blob/v2.0.1/decision-log/decision-log.schema.json) and [semantic validator](https://github.com/mj3b/rgds/blob/v2.0.1/scripts/validate_decision_log.py), pinned to commit `f6fa066c7e53d1d89d68ac8ef424b559ef58be34` for this review.

| Mechanism | Actual requirement or behavior | Limit |
|---|---|---|
| JSON Schema | Requires top-level `ai_assistance`, containing `used`, `use_cases`, `artifacts`, and `controls` | Does not verify truth of disclosure |
| Conditional JSON Schema when `used: true` | Requires `tool_name`, `tool_purpose`, `human_review`, and `ai_risk_assessment` | Presence does not establish adequate disclosure |
| Semantic validator when `used: true` | Requires nonempty use cases and artifacts, tool name, tool purpose, and at least one human review | Presence is not authentic human review |
| `human_review` item schema | Requires tier, reviewer reference, and finding summary | Does not assess expertise or independence |
| `human_override_log` | Optional; each supplied item has required shape | Does not require corrections when none are recorded |
| `ai_risk_assessment.confidence_band` | Recommended by a warning when absent with AI use | Not a mandatory schema field or calibrated confidence measure |
| Empty control references | Semantic warnings for selected control fields | Default validation permits warnings; strict mode promotes warnings to failures |

These checks cover a subset of record constraints. They do not enforce all six covenants or prevent unauthorized runtime behavior. Passing CI does not itself prevent merge unless repository controls require the checks. This profile does not assert such branch protection.

See the [hypothetical example](../examples/rgds-dec-0003-ai-assisted-conditional-go.md) and [validation instructions](../docs/validation.md). Framework mappings are [interpretive only](../docs/framework-crosswalk.md): no compliance, conformity, certification, control effectiveness, or regulator acceptance is established.

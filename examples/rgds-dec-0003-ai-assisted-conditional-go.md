# Hypothetical AI-Assisted Decision Walkthrough

Example ID: `rgds-dec-0003-ai-assisted-conditional-go` (historical local identifier retained).

Status: hypothetical narrative only. No pilot, real decision, source packet, named reviewer, or schema-valid JSON record is supplied. This identifier is not the canonical `rgds-dec-0003` in RGDS v2.0.1, which is a different decision. For executable examples, see [RGDS v2.0.1 examples](https://github.com/mj3b/rgds/tree/v2.0.1/examples).

## Scenario

A fictional team is reviewing an IND-readiness evidence package with a late toxicology report and inconsistent draft summaries. The intended demonstration is how AI contributions, human review, and missing support would be recorded. It makes no claim about whether a real submission could proceed with incomplete toxicology evidence.

An explicitly invoked AI comparison might flag differing report dates, inconsistent wording, and unsupported references to final conclusions. The human reviewer would inspect the actual source versions, record corrections or rejection, and identify unresolved questions for the authorized decision-makers. Tool outputs would remain disclosed with `ai_assistance.used: true` in a complete implementation record.

The earlier version described seven prior programs and five conditional precedents. Those counts had no supplied source packet and are withdrawn as evidence. It also displayed compliance checkmarks, placeholder owners, and a pilot label; none established an observed deployment or completed assessment.

## Intended record requirements

A real record would need a specific decision question, options, source identifiers and versions, rationale, explicit risk posture, named people with authority, approval state, and applicable conditions with owners and dates. The hypothetical `conditional_go` label in the filename does not establish an authorized or appropriate outcome. The schema cannot authenticate the people or their judgment.

## AI Dependency Test result for this narrative

| Part | Result | Reason |
|---|---|---|
| Structural record completeness | Not assessed | This Markdown narrative is not a complete RGDS JSON record |
| Substantive independence | Indeterminate | No non-AI source packet or qualified substantive assessment is available |
| Practical human influence | Not assessed | No actual review or intervention evidence exists |

A future application should use the [assessment record](../docs/ai-dependency-test.md) to map each material rationale claim to its non-AI source, identify exclusions, and document review limitations. Preserve truthful AI disclosure and version-controlled corrections. This example does not establish covenant adherence, regulatory acceptability, or immutable audit history.

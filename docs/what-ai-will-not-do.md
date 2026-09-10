# What AI Will Not Do

This working profile assigns decision authority to humans and limits AI to explicitly invoked analytical assistance. These are requirements for an adopting organization; the documentation and RGDS schema do not enforce behavior by themselves.

| Area | Boundary under this profile |
|---|---|
| Decisions | AI must not decide, approve, reject, or defer gate outcomes |
| Action | AI must not initiate workflows or trigger downstream execution |
| Risk | AI must not accept residual risk or silently resolve uncertainty |
| Review | AI must not bypass reviewers, suppress dissent, or treat silence as approval |
| Evidence | AI output must not substitute for inspectable source evidence |
| Disclosure | AI use must be recorded truthfully, including retained drafting contributions |

Humans must review outputs and record acceptance, rejection, or modification. The human owner and approvers must act within their actual authority. RGDS records assigned human ownership, approval, and review; it does not prove that these actions occurred or that the individuals exercised substantive judgment. Practical human influence requires separate assessment.

The [AI Dependency Test](ai-dependency-test.md) assesses structural record completeness and substantive independence separately. Keep the original record and its required `ai_assistance` disclosure. A qualified reviewer must inspect non-AI sources before claiming that the rationale can be reconstructed independently of AI output. Missing evidence can leave the result indeterminate.

AI-assisted drafting and comparison are permitted with review. Neither model output nor a schema-valid record establishes regulatory acceptability, compliance, conformity, certification, or decision correctness. See the [contract](../contracts/non-agentic-ai-contract.md), [architecture](ai-governance-conceptual-decision-architecture.md), and [crosswalk](framework-crosswalk.md).

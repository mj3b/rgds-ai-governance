# AI Governance: Conceptual Decision Architecture

A named approver in a record does not establish that the person understood, challenged, or changed an AI-assisted decision. This architecture defines assigned authority and evidence requirements; deployments must separately demonstrate that those requirements operate in practice.

## Research architecture

```text
GDI general decision architecture
    -> AI Assistance Governance method/profile (this repository)
        -> RGDS regulated reference implementation

Independent study: separate historical/exploratory research
HIT: adjacent assessment of practical human influence
```

The profile specializes the participation boundary conceptually. Compatibility with RGDS is inspected against v2.0.1; no universal cross-version conformance is asserted. The independent study is historical research lineage, not implementation or field-validation evidence.

## Intended decision process

```text
Human defines question and prepares non-AI evidence
    -> optional explicit invocation of a bounded AI task
    -> AI returns draft analysis with disclosed provenance
    -> named human reviews, accepts/rejects/modifies, records reasons
    -> authorized humans record outcome, risk acceptance, conditions
    -> RGDS stores assigned ownership/approval and AI disclosure
    -> structural validation and separate substantive assessment
```

Human review may require several iterations. The diagram describes required practice, not a runtime enforcement mechanism or evidence that authority is preserved.

| Participant or artifact | Assigned function | Assessment boundary |
|---|---|---|
| Evidence preparer | Select and reference sources | Source quality and selection bias require review |
| AI assistance | Draft, summarize, compare, surface candidate gaps | No delegated approval, risk acceptance, or downstream execution under this profile |
| Human owner and approvers | Exercise authority within organizational scope | Recorded names and approvals do not authenticate conduct |
| RGDS decision record | Record rationale, sources, risk, assigned ownership and review | Schema and semantic checks inspect structure and selected consistency rules |
| Dependency assessor | Assess non-AI reconstruction | Assessment is bounded by sources, expertise, and prior AI exposure |

RGDS v2.0.1 outcome values are `go`, `no_go`, `conditional_go`, `defer`, and `defer_with_required_evidence`. Escalation is a governance action, not a sixth outcome. A recorded outcome does not itself execute an action or confer institutional authorization.

## Boundary and enforcement

The [six covenants](../contracts/non-agentic-ai-contract.md) prohibit autonomous action, undisclosed influence, default acceptance, and AI output substituting for source evidence. Human approval fields record claims about accountability. Runtime permissions, review procedures, identity verification, and organizational controls belong to the adopting system.

`ai_assistance` is required disclosure, including when AI was not used. Preserve truthful historical disclosure when conducting the [AI Dependency Test](ai-dependency-test.md). Structural completeness and substantive independence are separate results. The schema cannot establish human authorship, substantive judgment, or practical influence. Git provides version-controlled history; stronger integrity claims require declared controls and evidence.

See [status and limitations](../README.md), [framework boundaries](framework-crosswalk.md), and the [executive summary](what-ai-will-not-do.md).

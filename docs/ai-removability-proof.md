> **Superseded historical text, 2026-09-09. Do not use as current guidance.**
> The original text below is retained verbatim from commit `8ae4cc2e26cc3607f1e9711f72c90300789cc918`.
> It incorrectly claims that deleting required AI disclosure preserves schema validity and that record structure proves authorship, independence, or defensibility.
> The current procedure is the [AI Dependency Test](ai-dependency-test.md). Keep truthful AI-use disclosure and the original record intact. Git history is version-controlled, not inherently immutable.

<!-- HISTORICAL BODY START -->

# AI Removability Proof

**The claim:** Every RGDS decision is valid and fully defensible with all AI outputs removed.

This document makes that claim precise, states the conditions under which it holds, and identifies the architectural mechanism that enforces it.

---

## The Claim, Precisely Stated

Let D be an RGDS decision record with `ai_assistance.used = true`.

Let D' be D with the `ai_assistance` block removed entirely.

**Claim:** D' satisfies all governance requirements that D satisfies, with no reduction in audit quality, regulatory defensibility, or accountability chain integrity.

---

## What D' Retains

| Decision Element | Present in D' | Notes |
|-----------------|:-------------:|-------|
| Decision owner (named individual) | ✓ | Defined in `accountability.decision_owner` |
| Reviewers and approvers (named) | ✓ | Defined in `accountability.reviewers[]` and `accountability.approvers[]` |
| Authority scope and escalation path | ✓ | Defined in `accountability` object |
| Decision question | ✓ | Required field, cannot be AI-generated |
| Options considered (≥2) | ✓ | Required field with rejection rationale per option |
| Evidence references | ✓ | Source links and completeness states (`complete`/`partial`/`placeholder`) |
| Risk posture | ✓ | Explicitly declared by human owner |
| Residual risk items | ✓ | Human-declared, structured |
| Decision outcome | ✓ | One of five governed types, human-authorized |
| Conditions and follow-up owners | ✓ | Named humans with deadlines |
| Decision rationale | ✓ | Human-authored in `decision_rationale` field |
| Audit trail (Git timestamps) | ✓ | Immutable, independent of AI disclosure fields |
| Schema validation status | ✓ | D' satisfies schema with `ai_assistance.used = false` |

---

## The Architectural Mechanism

Removability holds because of a structural design choice: `ai_assistance` is a disclosure object, not a dependency object.

```
RGDS Decision Record (schema structure)

Required core fields:              Optional disclosure fields:
─────────────────────              ──────────────────────────
decision_question       ←──────    ai_assistance.used
decision_deadline                  ai_assistance.tool_name
options_considered (≥2)            ai_assistance.tool_purpose
evidence_base                      ai_assistance.human_review[]
risk_posture                       ai_assistance.human_override_log[]
outcome                            ai_assistance.ai_risk_assessment
accountability.owner
accountability.approvers

Required core fields are          Disclosure fields record what
sufficient for a valid,           AI contributed. They do not
defensible decision record.       create the decision's validity.
```

If `ai_assistance` fields are absent (or removed), the decision record still satisfies all required fields. The governance requirement for human authorship of those required fields is not relaxed by the presence of AI assistance — it is only supplemented by disclosure.

---

## The Conditions Under Which the Claim Holds

The removability property holds when:

1. The `decision_rationale` field contains human-authored reasoning, not an AI-generated summary reproduced verbatim.
2. Evidence references point to primary sources, not AI-generated summaries treated as sources.
3. Risk posture is human-declared, not inferred from AI confidence output.
4. The decision owner and approvers are named individuals who reviewed the decision independently of the AI output.

If any of these conditions are violated, the decision is not truly removability-compliant — it is an AI-dependent decision with disclosure fields attached. The covenants (particularly Covenants 2, 5, and 6) exist to prevent this.

---

## Why This Property Is Required

In regulated contexts, three audit scenarios require removability:

**Scenario 1 — Model deprecation.** The AI system used in the decision is deprecated, retracted, or found to have a known failure mode. If the decision's defensibility depends on the model's output, the decision becomes retroactively compromised. If the decision is removability-compliant, it stands on its human-authored reasoning.

**Scenario 2 — Regulatory inspection.** An FDA inspector asks: "What would this decision have been without AI assistance?" A removability-compliant decision can answer directly from the human-authored fields. A non-compliant decision cannot.

**Scenario 3 — Governance evolution.** AI governance policies change. An organization that tightens its non-agentic requirements needs past decisions to remain valid under the new policy. Removability-compliant decisions are retrospectively valid under any policy that requires human accountability.

---

## Verification

To verify that a specific decision satisfies the removability property:

1. Remove the `ai_assistance` block from the record
2. Check that all required schema fields remain present and human-authored
3. Check that evidence references point to primary sources (not AI summaries)
4. Check that risk posture language does not reproduce AI confidence output
5. Confirm that the named decision owner and approvers could reconstruct the decision rationale independently

If all five checks pass, the decision satisfies the removability property.

---

*Part of the RGDS AI Governance framework. Apache 2.0.*
*See also: [Non-Agentic AI Contract](../contracts/non-agentic-ai-contract.md) · [GDI v3.0](https://github.com/mj3b/governed-decision-intelligence) · [RGDS](https://github.com/mj3b/rgds)*

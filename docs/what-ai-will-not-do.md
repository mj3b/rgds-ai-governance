# What AI Will Not Do
**Explicit Boundaries for AI Assistance in RGDS-Governed Decisions**

*Written for executives, program leaders, quality reviewers, and regulated stakeholders who require unambiguous clarity on where AI stops in regulated, phase-gated decision environments.*

---

## One-Minute Summary

AI may assist analysis. AI does not make decisions.

Under RGDS governance, all decisions are human-owned, all approvals are human-authorized, and all accountability remains with named individuals. AI is an analytical tool operating under explicit constraints. It has no decision authority under any circumstance.

---

## What AI Will Not Do — At a Glance

| Domain | AI Will Not |
|--------|------------|
| Decision authority | Decide, approve, defer, or reject gate outcomes |
| Autonomous action | Initiate workflows or operate without explicit human invocation |
| Risk | Determine, accept, or silently normalize risk posture |
| Governance | Replace escalation, review, or oversight processes |
| Evidence | Become evidence of record without reference to underlying sources |
| Transparency | Operate without disclosure in the decision record |
| Accountability | Become a prerequisite for defensible decisions |

---

## AI Will Not Make Decisions

At every phase gate, humans decide, humans approve, and humans accept or reject risk. AI generates analytical output for human review. The human reviewer makes a deliberate, documented choice to accept, reject, or modify that output. The outcome is recorded in the decision log under a named human owner.

AI does not decide gate outcomes (`go`, `conditional_go`, `defer`, `no_go`, `escalate`). AI does not approve or reject deliverables. AI does not defer decisions on behalf of humans. Decision authority always rests with named individual owners.

---

## AI Will Not Act Autonomously

There is no permitted path for autonomous or self-directed AI behavior in this governance framework.

AI will not initiate workflows or downstream actions. AI will not operate without explicit human invocation for a specific, bounded task. AI will not execute tasks without prior human review and documented disposition. AI will not trigger notifications, submissions, or approvals.

---

## AI Will Not Override or Silence Humans

AI will not override human reviewers or approvers. AI will not resolve disagreements between stakeholders. AI will not suppress dissenting views or alternative interpretations. AI will not bypass governance or escalation processes.

Human outcomes — disagreement, abstention, conditional approval, escalation — are valid, protected, and not subject to AI override.

---

## AI Will Not Determine Risk Posture

Risk posture must be explicitly declared by humans in RGDS decision records. AI will not accept or mitigate risk. AI will not infer residual risk acceptance from proceeding. AI will not normalize uncertainty into a single recommended position. AI will not collapse unresolved assumptions into conclusions.

The `risk_posture` and `residual_risk_items` fields in the RGDS decision log schema exist to make this declaration structural and required — not optional or implied.

---

## AI Will Not Become Evidence of Record

AI outputs summarize, compare, and surface patterns from authoritative evidence. They do not replace it.

AI outputs are not evidence of record by default. AI outputs do not independently satisfy regulatory or quality requirements. AI outputs cannot substitute for source documents, validated data, or authoritative reports. If an AI output influences a decision, the human owner must reference the underlying source material in the decision record — the AI output is a drafting aid, not the evidence.

---

## AI Will Not Operate Without Disclosure

All AI assistance must be visible, attributable, and reviewable. AI will not influence decisions invisibly. AI will not introduce assumptions or rationale that cannot be inspected. AI will not operate in a manner that cannot be explained to a regulator or auditor.

When AI is used, the RGDS decision log requires disclosure of: which AI system was used, what task it was invoked for, who reviewed the output, what corrections were made, and what confidence limitations apply.

---

## AI Will Not Create Dependency

Every RGDS decision must remain defensible if all AI outputs are removed. AI may accelerate analysis, but it must never become a prerequisite for approval, a justification for reduced human oversight, or a substitute for human accountability.

If removing AI outputs from a decision record would make the decision indefensible, the decision was not governed correctly. The removability property is enforced by architecture, not by policy intent.

---

## Why These Limits Exist

In regulated environments, the primary governance risk is unclear accountability — not incorrect analysis. An AI system can produce an excellent recommendation. If no named human with domain knowledge reviewed that recommendation independently, the accountability chain does not hold under audit.

These boundaries ensure that ownership remains explicit, governance remains auditable, and decisions remain defensible at the moment they are made — regardless of how capable or useful the AI system is.

---

*Part of the RGDS AI Governance framework. Apache 2.0.*
*See also: [Non-Agentic AI Contract](../contracts/non-agentic-ai-contract.md) · [Removability Proof](ai-removability-proof.md) · [GDI v3.0](https://github.com/mj3b/governed-decision-intelligence) · [RGDS](https://github.com/mj3b/rgds)*

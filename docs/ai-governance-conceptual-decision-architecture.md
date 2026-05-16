# AI Governance — Conceptual Decision Architecture

*How AI assistance operates within regulated decision environments while preserving human authority, auditability, and reversibility.*

This document defines the authority flow and boundary map for AI assistance in RGDS-governed decisions. It is written for executive review, regulatory discussion, and governance design critique. It is not a system diagram and does not describe implementation, tooling, or integration mechanics — those concerns belong only after governance and authority boundaries are established.

---

## The Core Design Constraint

AI governance in regulated environments fails in a predictable pattern: organizations adopt AI tools that produce useful outputs, human reviewers gradually accept those outputs with decreasing independent verification, and authority silently transfers from named humans to models without any documented transfer.

The architecture below prevents this by making one constraint structurally non-negotiable: **AI never sits on the authority path.** Authority flows through humans at every stage. AI produces drafts. Humans decide.

---

## Canonical Authority Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                      Phase Gate Event                            │
│         A consequential decision is required at a program gate   │
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                   Service-Line Delivery                          │
│         Analysis · Evidence Preparation · Facilitation           │
│                                                                  │
│  Authority: Advisory                                             │
│  Can: prepare, analyze, recommend                                │
│  Cannot: decide or approve                                       │
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               │ (optional)
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                   AI Assistance Layer                            │
│         Non-agentic · Human-invoked · Reviewable outputs only    │
│                                                                  │
│  Authority: None                                                 │
│  Can: summarize · compare · surface gaps · draft                 │
│  Cannot: decide · approve · accept risk · execute                │
│                                                                  │
│  Governed by: Non-Agentic AI Contract (six covenants)            │
│  Disclosure: ai_assistance object in RGDS decision record        │
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                  RGDS Decision Record                            │
│         Schema-validated artifact · System of record             │
│                                                                  │
│  Authority: Referential                                          │
│  Records: decision context · evidence · risk · ownership         │
│  Enforces: ai_assistance disclosure when AI was used             │
│  Validates: required fields in CI/CD before merge                │
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                   Human Review and Accountability                │
│         Named individuals · Explicit sign-off · Domain knowledge │
│                                                                  │
│  Authority: Absolute                                             │
│  Can: approve · reject · defer · escalate                        │
│  Cannot: delegate authority to AI or to role abstractions        │
│  Must: review AI output independently before accepting           │
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                   Phase-Gate Decision Outcome                    │
│         GO · CONDITIONAL GO · DEFER · NO-GO · ESCALATE           │
│                                                                  │
│  Authority: Final                                                │
│  Human-owned · Auditable · Defensible without AI present         │
└──────────────────────────────────────────────────────────────────┘
```

---

## Authority Boundary Map

| Layer | Can Act | Cannot Act | Authority Status |
|-------|---------|------------|-----------------|
| Service-Line Delivery | Prepare, analyze, recommend | Decide or approve | Advisory |
| AI Assistance | Generate analytical output for review | Decide, approve, accept risk, execute | None |
| RGDS Decision Record | Record, structure, validate, preserve | Decide | Referential |
| Human Review | Approve, reject, defer, escalate | Delegate authority to AI or role | Absolute |
| Phase-Gate Outcome | Enact the decision | — | Final |

**Key principle: authority flows downward through humans only.** At no point does AI sit between the decision record and the human reviewer. AI output arrives before the decision record is written; human review occurs after the decision record is drafted; the outcome is authorized by named humans, not by the quality of the AI output.

---

## AI Containment Boundary

```
┌─────────────────────────────────────────────────────────────────┐
│                  AI ASSISTANCE BOUNDARY                         │
├──────────────────────────┬──────────────────────────────────────┤
│  PERMITTED               │  PROHIBITED                          │
├──────────────────────────┼──────────────────────────────────────┤
│  Summarization           │  Decision-making of any kind         │
│  Cross-doc comparison    │  Risk acceptance or normalization    │
│  Gap and dependency      │  Workflow initiation                 │
│    surfacing             │  Auto-approval                       │
│  Structured drafting     │  Silent or ambient influence         │
│  Schema completeness     │  Evidence of record (primary)        │
│    checks                │  Escalation decisions                │
└──────────────────────────┴──────────────────────────────────────┘
         │
         ▼
  AI is structurally subordinate to governance, decision
  structure, and human review at every stage.
  Removal of AI outputs does not invalidate any decision.
```

---

## Separation of Concerns

Three concerns are deliberately kept separate. Conflating them creates governance fragility — a change in one layer breaks the others.

| Concern | Governed By | Why Separated |
|---------|------------|---------------|
| Decision structure | RGDS | Defensibility, ownership, audit — must work without AI |
| AI boundaries | Non-Agentic AI Contract | Prevent autonomy and authority leakage — must survive tooling changes |
| Service execution | Delivery governance | Enable progress — must not embed governance logic |
| Enforcement | Human governance processes | Maintain trust — must remain human-led |

This separation is intentional and non-negotiable. Governance covenants (this repository) define what AI may and may not do. Decision structure (RGDS) defines how decisions are recorded. Specification (GDI v3.0) defines the universal architecture. Each layer evolves independently without invalidating the others.

---

## Non-Technical Summary

- AI never decides
- AI never approves
- AI never accepts risk
- AI can be removed without invalidating any decision
- Humans are accountable by architecture, not by policy statement

---

## Technical Summary

- No agentic loops or background inference paths
- No implicit state transitions triggered by AI output
- No authority coupling between AI layer and decision record
- Decision record is the system of record; AI disclosure is an optional addendum
- Schema validation enforces required human-authored fields in CI/CD

---

*Part of the RGDS AI Governance framework. Apache 2.0.*
*See also: [Non-Agentic AI Contract](../contracts/non-agentic-ai-contract.md) · [Removability Proof](ai-removability-proof.md) · [GDI v3.0](https://github.com/mj3b/governed-decision-intelligence) · [RGDS](https://github.com/mj3b/rgds)*

# RGDS AI Governance — Non-Agentic AI Covenants

[![Status: Reference Governance](https://img.shields.io/badge/status-reference%20governance-5b6cff)](#status)
[![Human Governed](https://img.shields.io/badge/governance-human--governed-3bb273)](#governance-covenants)
[![Non-Agentic](https://img.shields.io/badge/AI-explicitly%20non--agentic-2d7ff9)](#the-non-agentic-boundary)
[![AI Optional](https://img.shields.io/badge/AI-optional%20and%20removable-8b949e)](#removability-guarantee)
[![Audit Compatible](https://img.shields.io/badge/property-audit--compatible%20by%20design-0aa2c0)](#framework-alignment)
[![License](https://img.shields.io/github/license/mj3b/rgds-ai-governance)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

> *AI governance frameworks tell organizations what to govern. This repository defines what AI is explicitly prohibited from doing — and makes that prohibition inspectable, versioned, and enforceable by design.*

---

## The Governance Gap This Repository Fills

Three governance problems recur in regulated AI deployment.

**The authority leakage problem.** Organizations adopt AI tools that produce recommendations. Over time, human reviewers accept those recommendations without independent verification — a pattern Parasuraman and Manzey (2010) term automation bias. The decision record shows human approval; the reasoning was AI-generated and unreviewed. Authority leaked from the named human to the model without any documented transfer.

**The reconstructability problem.** Six months after an AI-assisted decision, a regulator asks: who reviewed the AI output, what was the quality control process, what would the decision have been without AI? Organizations with no structured AI disclosure cannot answer. The decision stands but the accountability chain does not.

**The removability problem.** If AI assistance is structurally required for a decision to be defensible, then AI has become a governance dependency — a path to authority that was never authorized. Every AI-assisted decision must remain valid if the AI output is removed entirely.

This repository addresses all three by defining explicit governance covenants: what AI may do, what it is prohibited from doing, and what properties every AI-assisted decision must satisfy regardless of tooling, model, or deployment context.

---

## Architecture: Where This Repository Sits

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DECISION GOVERNANCE STACK                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  GDI v3.0 — Open Specification                                      │
│  The Decision Architecture for Governed AI                          │
│  github.com/mj3b/governed-decision-intelligence                     │
│  DOI: 10.5281/zenodo.20244601                                       │
│       │                                                             │
│       │  defines the universal decision-layer architecture          │
│       ▼                                                             │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  RGDS AI Governance (this repository)                        │   │
│  │                                                              │   │
│  │  Non-agentic AI covenants                                    │   │
│  │  Explicit prohibition contracts                              │   │
│  │  Removability guarantees                                     │   │
│  │  Authority boundary maps                                     │   │
│  │  Framework alignment (NIST, ISO 42001, EU AI Act, ARAF)     │   │
│  └──────────────────────────────────────────────────────────────┘   │
│       │                                                             │
│       │  governs AI use within                                      │
│       ▼                                                             │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  RGDS — Regulated Gate Decision Support                      │   │
│  │  github.com/mj3b/rgds                                        │   │
│  │                                                              │   │
│  │  Biopharma reference implementation                          │   │
│  │  Schema-validated decision logs                              │   │
│  │  Six canonical examples · CI/CD enforcement                  │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Independent Research — DOI: 10.5281/zenodo.20242004         │   │
│  │  github.com/mj3b/rgds-independent-study                      │   │
│  │  Ten-question study on FDA reconstructability and            │   │
│  │  AI accountability in biopharma/biotech development          │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Separation of concerns is intentional.** Governance covenants (this repository) define what AI may and may not do. Decision structure (RGDS) defines how decisions are recorded and owned. Specification (GDI) defines the universal architecture. Each layer evolves independently without invalidating the others.

---

## The Non-Agentic Boundary

The central design constraint is non-agentic AI. The term requires precision.

**Agentic behavior** is any AI action that initiates, decides, approves, or executes without explicit human invocation at the moment of that specific action. This includes background recommendations, confidence-weighted auto-approval, implicit risk acceptance, and self-triggering workflows.

**Non-agentic behavior** is AI action that generates output for human review, where the human makes a deliberate, documented choice to accept, reject, or modify that output before it influences any decision.

```
AGENTIC (prohibited)                NON-AGENTIC (governed)
─────────────────────               ──────────────────────
AI → recommendation                 Human invokes AI
AI → decision                            │
AI → approval                           ▼
AI → execution                     AI → draft output
                                         │
Result: authority leakage           Human reviews
                                         │
                                    Human accepts / rejects / modifies
                                         │
                                    Decision record captures:
                                    - what AI contributed
                                    - what human changed
                                    - who is accountable
                                         │
                                    Result: authority preserved
```

The distinction is not about AI capability. A capable model can generate an excellent recommendation. The governance question is whether a named human with domain knowledge and accountability reviewed that recommendation before it entered the decision record. If not, authority leaked regardless of recommendation quality.

---

## Governance Covenants

Six covenants define the non-agentic AI contract. Each addresses a specific failure mode.

```
┌─────────────────────────────────────────────────────────────────────┐
│  COVENANT 1 — NO AUTONOMOUS OR AGENTIC BEHAVIOR                     │
├─────────────────────────────────────────────────────────────────────┤
│  AI must not: initiate decisions · approve outcomes · accept risk   │
│               trigger downstream actions · act without invocation   │
│                                                                     │
│  Failure mode prevented: authority leakage to model                 │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  COVENANT 2 — HUMAN AUTHORITY IS ABSOLUTE                           │
├─────────────────────────────────────────────────────────────────────┤
│  Every decision: owned by a named human · reviewable without AI    │
│                  valid if all AI outputs are removed                │
│                                                                     │
│  Failure mode prevented: reconstructability failure under audit     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  COVENANT 3 — EXPLICIT INVOCATION ONLY                              │
├─────────────────────────────────────────────────────────────────────┤
│  AI assistance must be: intentional · contextual · visible          │
│                          optional · tied to a specific task         │
│                                                                     │
│  Failure mode prevented: silent or ambient AI influence             │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  COVENANT 4 — REVIEWABILITY AND REJECTION ARE MANDATORY             │
├─────────────────────────────────────────────────────────────────────┤
│  All AI outputs: readable · editable · explicitly reviewed          │
│                  accepted or rejected by a named human              │
│                                                                     │
│  Failure mode prevented: automation bias / unreviewed influence     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  COVENANT 5 — NO SILENT RISK ACCEPTANCE                             │
├─────────────────────────────────────────────────────────────────────┤
│  AI must not: normalize assumptions · collapse uncertainty          │
│               mask disagreement · infer unresolved risk acceptance  │
│                                                                     │
│  Failure mode prevented: implicit risk posture from AI output       │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  COVENANT 6 — EVIDENCE SUBORDINATION                                │
├─────────────────────────────────────────────────────────────────────┤
│  AI may: summarize · compare · highlight · surface candidates       │
│  AI may not: replace source evidence · serve as primary justif.     │
│                                                                     │
│  Failure mode prevented: AI output displacing authoritative evidence│
└─────────────────────────────────────────────────────────────────────┘
```

Full covenant text: [`contracts/non-agentic-ai-contract.md`](contracts/non-agentic-ai-contract.md)

---

## Authority Flow

Authority in this architecture flows through humans only. AI never sits on the authority path.

```
Phase Gate Event
      │
      ▼
┌─────────────────────────────┐
│   Service-Line Delivery     │  Advisory authority
│   Analysis · Preparation    │  Can recommend, cannot decide
└──────────────┬──────────────┘
               │
               ▼ (optional)
┌─────────────────────────────┐
│   AI Assistance Layer       │  No authority
│   Non-agentic · Invoked     │  Output is draft only
│   Reviewable · Removable    │  Cannot initiate, approve, execute
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   RGDS Decision Record      │  Referential authority
│   Schema-validated artifact │  Records what was decided and why
│   ai_assistance fields      │  Discloses what AI contributed
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Human Review              │  Absolute authority
│   Named individuals         │  Accept · Reject · Defer · Escalate
│   Explicit sign-off         │  Cannot delegate to AI
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Phase-Gate Outcome        │  Final
│   GO · CONDITIONAL GO       │  Human-owned
│   DEFER · NO-GO · ESCALATE  │  Auditable · Defensible
└─────────────────────────────┘
```

---

## Removability Guarantee

If the `ai_assistance` block is removed from any RGDS decision record:

| Decision Element | Status After AI Removal |
|-----------------|------------------------|
| Decision owner and approvers | Intact |
| Evidence references and completeness | Intact and reviewable |
| Risk posture and residual risk | Intact and enforceable |
| Decision rationale | Human-authored, intact |
| Conditions and follow-up owners | Intact |
| Audit trail and accountability chain | Intact |
| Regulatory defensibility | Preserved |

AI removal does not invalidate past decisions, alter outcomes, or compromise regulatory defensibility. This property is enforced by architecture — the decision record schema treats `ai_assistance` as a disclosure object, not a structural dependency.

---

## Prohibited Patterns

The following patterns violate the non-agentic contract regardless of how they are implemented or labeled.

| Pattern | Why It Is Prohibited | Failure Mode |
|---------|---------------------|--------------|
| Autonomous agents | AI acts without explicit human invocation | Authority leakage |
| Auto-approval flows | AI recommendation becomes decision without review | Reconstructability failure |
| Confidence-weighted decisioning | AI confidence score determines outcome | Authority leakage |
| Background recommendations | AI influences decisions without disclosure | Silent authority |
| Self-triggering workflows | AI initiates downstream actions | Agentic behavior |
| Implicit AI defaults | AI output assumed approved unless overridden | Removes rejection as the default |
| AI as evidence of record | AI output treated as authoritative source | Evidence subordination violation |

---

## Framework Alignment

These covenants satisfy specific requirements in each major AI governance framework.

| Framework | Requirement | Covenant Satisfaction |
|-----------|------------|----------------------|
| NIST AI RMF GOVERN | Accountability structures and human oversight policies | Covenants 1, 2, 4 define authority boundaries and human ownership requirements |
| ISO/IEC 42001 | Human oversight requirements; documented evidence of governance | Covenants 3, 4 enforce documented human review; contract is the governance evidence |
| EU AI Act Art. 14 | Human oversight measures for high-risk AI | Covenant 2 (absolute human authority); Covenant 4 (mandatory review and rejection) |
| EU AI Act Art. 13 | Transparency and provision of information | Covenant 3 (explicit invocation); Covenant 6 (evidence subordination) |
| ARAF v3.0 | Reconstructability principle | Covenant 2 (decisions valid without AI); Removability guarantee |
| FDA Jan. 2025 Draft | Human oversight of AI-assisted regulatory submissions | Covenants 1–4 map directly to the 7-step AI credibility framework |

Alignment does not imply certification. Organizations are responsible for their own compliance assessments.

---

## What AI May Do

When explicitly invoked under these covenants, AI assistance is permitted for bounded analytical tasks.

| Permitted Task | Constraint |
|---------------|-----------|
| Evidence summarization | Human edits and signs off; output is draft |
| Cross-document comparison | Inconsistencies surfaced; human resolves |
| Gap identification | Candidate gaps flagged; human confirms |
| Structured drafting | Decision-log sections drafted; owner finalizes all content |
| Schema completeness checks | Missing fields flagged; AI does not "approve" compliance |

Every permitted task produces a draft. The human produces the decision.

---

## Repository Contents

```
rgds-ai-governance/
│
├── contracts/
│   └── non-agentic-ai-contract.md     ← Six binding covenants with
│                                         definitions and prohibited patterns
├── docs/
│   ├── ai-governance-conceptual-      ← Authority flow and boundary map
│   │   decision-architecture.md         for executive and regulatory review
│   ├── ai-removability-proof.md       ← Formal statement of removability
│   ├── client-one-pager-what-ai-      ← Executive-facing boundary
│   │   will-not-do.md                   clarification (one-minute read)
│   └── service-line-overview.md       ← How governance operates in
│                                         consulting and delivery contexts
└── examples/
    └── rgds-dec-0003-ai-assisted-     ← Worked AI-assisted decision
        conditional-go.md                demonstrating disclosure fields
                                         and covenant compliance
```

---

## Reading Guide

| You are | Start here |
|---------|-----------|
| Executive / Approver | [`docs/client-one-pager-what-ai-will-not-do.md`](docs/client-one-pager-what-ai-will-not-do.md) — one-minute read |
| Governance / Risk reviewer | [`contracts/non-agentic-ai-contract.md`](contracts/non-agentic-ai-contract.md) → this README |
| Regulatory / FDA auditor | Removability Guarantee section → [`docs/ai-removability-proof.md`](docs/ai-removability-proof.md) |
| AI governance researcher | Framework Alignment section → [`docs/ai-governance-conceptual-decision-architecture.md`](docs/ai-governance-conceptual-decision-architecture.md) |
| Technical implementer | [`contracts/non-agentic-ai-contract.md`](contracts/non-agentic-ai-contract.md) → RGDS `ai_assistance` schema fields |

---

## Relationship to the Full Governance Stack

| Repository | Role | DOI |
|------------|------|-----|
| **[mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence)** | GDI v3.0 — universal decision-layer specification | [10.5281/zenodo.20244601](https://doi.org/10.5281/zenodo.20244601) |
| **[mj3b/rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)** | Non-agentic AI covenants (this repository) | — |
| **[mj3b/rgds](https://github.com/mj3b/rgds)** | Biopharma reference implementation | — |
| **[mj3b/rgds-independent-study](https://github.com/mj3b/rgds-independent-study)** | Ten-question independent research study | [10.5281/zenodo.20242004](https://doi.org/10.5281/zenodo.20242004) |

---

## Status

Reference governance artifact — not a production system, not regulatory advice, not a legal agreement.

Published to support transparency, auditability, and defensible AI-assisted decision design in regulated environments. Versioning and change history tracked in [`CHANGELOG.md`](CHANGELOG.md).

---

## Author

**Mark Julius Banasihan**
Decision governance systems for regulated, high-stakes environments.

[GitHub](https://github.com/mj3b) · [LinkedIn](https://linkedin.com/in/markjuliusbanasihan) · [ORCID](https://orcid.org/0009-0001-8121-2878) · Atlanta, Georgia, United States

# Non-Agentic AI Contract
**Explicit Prohibitions and Human Accountability Covenants**

This document defines **binding governance covenants** for the use of AI in
regulated, phase-gated decision environments governed by
**RGDS (Regulated Gate Decision Support)**.

Its purpose is to make **non-agentic intent explicit, inspectable, and enforceable**
in contexts where AI-assisted analysis may influence regulated decisions.

> **Relationship to RGDS**  
> This contract governs *whether and how AI assistance may be used*.  
> **RGDS governs how decisions are recorded, evaluated, and owned.**  
> RGDS repository: https://github.com/mj3b/rgds

---

## Contract Scope

This contract applies to:

- all AI-assisted analysis referenced in RGDS decision logs
- all workflows claiming alignment with RGDS governance principles
- all contexts where AI output may influence a phase-gated decision

This contract applies **regardless of tooling, model type, deployment pattern, or vendor**.

---

## Definitions

| Term | Definition |
|------|------------|
| **AI Assistance** | Any model-generated output used to support human analysis |
| **Agentic Behavior** | Autonomous initiation, decision-making, or action without explicit human invocation and approval |
| **Decision** | A recorded gate outcome (e.g., `go`, `conditional_go`, `no_go`) |
| **Human Owner** | The named individual accountable for a decision and its consequences |
| **Evidence** | Source material used to justify or inform a decision |

---

## Core Covenants (Non-Negotiable)

### Covenant 1 — No Autonomous or Agentic Behavior

AI **must not**:

- initiate decisions
- approve, reject, or defer outcomes
- accept, mitigate, or reframe risk
- trigger downstream actions
- act independently of explicit human invocation

AI **cannot** function as an agent, delegate, or authority surrogate under any circumstance.

---

### Covenant 2 — Human Authority Is Absolute

All decisions must:

- be owned by a named human
- be reviewable without AI assistance
- remain valid if all AI outputs are removed

AI outputs have **no authority** outside explicit human review and acceptance.

---

### Covenant 3 — Explicit Invocation Only

AI assistance must be:

| Requirement | Description |
|------------|-------------|
| Intentional | Explicitly requested by a human |
| Contextual | Tied to a specific decision or analysis task |
| Visible | Clearly labeled as AI-assisted |
| Optional | Fully skippable without blocking progress |

There is **no background, default, passive, or ambient AI influence**.

---

### Covenant 4 — Reviewability and Rejection Are Mandatory

All AI outputs must be:

- readable and editable
- explicitly reviewed by a human
- explicitly accepted or rejected
- attributable to a specific human reviewer

Unreviewed AI output **must not** influence decisions.

---

### Covenant 5 — No Silent Risk Acceptance

AI **must not**:

- normalize assumptions
- collapse uncertainty
- mask disagreement
- infer acceptance of unresolved risk

Risk posture must be **explicitly declared by humans** in RGDS decision records.

---

### Covenant 6 — Evidence Subordination

AI outputs may:

- summarize evidence
- compare alternatives
- highlight inconsistencies
- surface candidate risks

AI outputs may **not**:

- replace source evidence
- override documented facts
- serve as primary justification for a decision

AI is **supporting evidence**, never authoritative evidence.

---

## Explicitly Prohibited Patterns

The following patterns are **out of bounds** under this contract:

| Prohibited Pattern | Rationale |
|------------------|-----------|
| Autonomous agents | Violates human accountability |
| Auto-approval flows | Removes explicit ownership |
| Confidence-weighted decisioning | Creates false authority |
| Background recommendations | Enables silent influence |
| Self-triggering workflows | Breaks phase-gate control |
| Implicit AI defaults | Obscures human intent |

---

## Compatibility with RGDS

This contract is designed to operate alongside RGDS by ensuring that:

- AI use is optional at every gate
- decisions remain reconstructable over time
- accountability remains human-centric
- governance survives tooling or model changes

RGDS decision logs remain the **system of record** for:

- decision outcome
- evidence linkage
- risk declaration
- ownership and accountability

---

## Enforcement Boundary

This contract:

- **defines governance boundaries**
- **does not prescribe tooling**
- **does not implement enforcement**

Operational enforcement is the responsibility of delivery systems,
governance processes, and human reviewers.

---

## Contract Status

This document is a **governance reference artifact**, not a legal agreement.

It is published to support:

- transparency
- auditability
- defensible AI-assisted decision design

Versioning and change history are tracked at the repository level.

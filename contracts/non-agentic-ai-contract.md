# Non-Agentic AI Contract
**Explicit Prohibitions and Human Accountability Covenants**

*Governing AI assistance in regulated, phase-gated decision environments under RGDS and GDI v3.0*

---

## Purpose and Scope

This contract defines binding governance covenants for AI assistance in regulated decision environments. It applies to all AI-assisted analysis referenced in RGDS decision logs, all workflows claiming alignment with RGDS governance principles, and all contexts where AI output may influence a phase-gated decision outcome.

The covenants apply regardless of tooling, model type, deployment pattern, or vendor. They are technology-agnostic by design: governance boundaries must survive tooling changes, model upgrades, and organizational transitions.

**Relationship to RGDS and GDI:**

```
GDI v3.0 Specification
(universal decision architecture)
         │
         ├── defines: what a governed decision record contains
         │            how accountability is structured
         │            what human oversight requires
         ▼
RGDS AI Governance (this contract)
(AI boundary definition)
         │
         ├── defines: what AI may do
         │            what AI is prohibited from doing
         │            what every AI-assisted decision must satisfy
         ▼
RGDS Decision Log
(enforcement artifact)
         │
         └── enforces: ai_assistance disclosure schema
                       schema validation in CI/CD
                       named human accountability at every gate
```

---

## Definitions

| Term | Definition |
|------|-----------|
| **AI Assistance** | Any model-generated output used to support human analysis in a decision context |
| **Agentic Behavior** | Any AI action that initiates, decides, approves, or executes without explicit human invocation at the moment of that specific action |
| **Non-Agentic Behavior** | AI action that generates output for human review, where the human makes a deliberate, documented choice before that output influences any decision |
| **Decision** | A recorded gate outcome (`go`, `conditional_go`, `defer`, `no_go`, `escalate`) |
| **Human Owner** | The named individual accountable for a decision and its consequences — not a role, team, or system |
| **Evidence** | Human-reviewed source material used to justify or inform a decision |
| **Authority Leakage** | Transfer of decision-making influence from a named human to an AI system without explicit authorization |
| **Removability** | The property that a decision remains fully valid and defensible if all AI outputs associated with it are removed |

---

## Core Covenants

### Covenant 1 — No Autonomous or Agentic Behavior

**Failure mode addressed:** Authority leakage to model. A capable model produces an excellent recommendation; a fatigued reviewer accepts without independent verification; the decision record shows human approval but the reasoning was AI-generated and unreviewed.

AI must not:
- initiate decisions
- approve, reject, or defer outcomes
- accept, mitigate, or reframe risk on behalf of humans
- trigger downstream actions
- act independently of explicit human invocation at the moment of that specific action

AI cannot function as an agent, delegate, or authority surrogate under any circumstance.

```
Prohibited flow:           Governed flow:
AI → recommendation        Human invokes AI for specific task
AI → decision                  │
AI → approval              AI → draft output
                               │
                           Human reviews independently
                               │
                           Human decides: accept / reject / modify
                               │
                           Decision record: outcome + disclosure
```

---

### Covenant 2 — Human Authority Is Absolute

**Failure mode addressed:** Reconstructability failure. Six months after a decision, a regulator asks who reviewed the AI output. If no human review is documented, the accountability chain does not hold regardless of outcome quality.

All decisions must:
- be owned by a named individual (not a role, not a system)
- be reviewable without AI assistance
- remain valid and defensible if all AI outputs are removed

AI outputs have no authority outside explicit human review and documented acceptance.

---

### Covenant 3 — Explicit Invocation Only

**Failure mode addressed:** Silent or ambient AI influence. Background recommendations, default AI integration, and implicit AI behavior all create undisclosed influence paths that cannot be audited.

AI assistance must be:

| Requirement | Meaning | Why It Matters |
|-------------|---------|----------------|
| Intentional | Explicitly requested by a named human for a specific task | Prevents default or ambient influence |
| Contextual | Tied to a specific decision or analysis task | Enables traceability |
| Visible | Clearly labeled as AI-assisted in the decision record | Enables audit |
| Optional | Fully skippable without blocking progress | Preserves non-dependency |

There is no permitted path for background, passive, default, or ambient AI influence.

---

### Covenant 4 — Reviewability and Rejection Are Mandatory

**Failure mode addressed:** Automation bias. Parasuraman and Manzey (2010) document that humans over-rely on algorithmic recommendations, particularly under cognitive load or time pressure. The governance response is to make rejection the structurally equal alternative to acceptance — not an exception requiring justification.

All AI outputs must be:
- readable and editable by the reviewing human
- explicitly reviewed by a named individual with relevant domain knowledge
- explicitly accepted, rejected, or modified — not implicitly accepted by default
- attributable to a specific human reviewer in the decision record

Unreviewed AI output must not influence decisions. The absence of a rejection is not acceptance.

---

### Covenant 5 — No Silent Risk Acceptance

**Failure mode addressed:** Implicit risk posture from AI output. AI systems trained to produce coherent recommendations will tend to resolve ambiguity into a single position. In regulated contexts, that resolution constitutes risk acceptance — which must be human-declared.

AI must not:
- normalize assumptions across a decision record
- collapse uncertainty into a single recommended position
- mask disagreement between evidence sources
- infer acceptance of unresolved risk from proceeding

Risk posture must be explicitly declared by named humans in RGDS decision records. The `risk_posture` and `residual_risk_items` fields exist specifically to make this declaration structural, not optional.

---

### Covenant 6 — Evidence Subordination

**Failure mode addressed:** AI output displacing authoritative evidence. If an AI-generated summary replaces the primary source in a decision record, the decision is grounded in a model output rather than in verified data.

AI output may:
- summarize evidence for analytical efficiency
- compare evidence sources to surface inconsistencies
- highlight candidate gaps or dependencies
- surface precedent patterns from similar contexts

AI output may not:
- replace primary source evidence
- override documented facts from authoritative sources
- serve as the primary justification for a decision outcome
- be cited as evidence of record without reference to the underlying source

Every decision must remain defensible on its source evidence alone, without the AI summary present.

---

## Prohibited Patterns Reference

| Pattern | Covenant Violated | Why It Is Out of Bounds |
|---------|------------------|------------------------|
| Autonomous agents | C1 | AI acts without explicit human invocation |
| Auto-approval flows | C1, C4 | AI recommendation becomes decision without documented human review |
| Confidence-weighted decisioning | C1, C2 | AI confidence score determines outcome; authority leaks to model |
| Background recommendations | C3 | Undisclosed influence path; cannot be audited |
| Self-triggering workflows | C1 | AI initiates downstream actions |
| Implicit AI defaults | C3, C4 | AI output assumed approved unless overridden; inverts the governance requirement |
| AI as evidence of record | C6 | AI output cited as authoritative source without reference to underlying data |
| Delegating escalation to AI | C1, C2 | Escalation decisions require human authority scope assessment |

---

## Compatibility with RGDS Decision Log Schema

The RGDS decision log schema enforces these covenants at the artifact level through the `ai_assistance` disclosure object. When `ai_assistance.used = true`, the following fields are required:

| Schema Field | Covenant | What It Enforces |
|-------------|----------|-----------------|
| `ai_assistance.tool_name` | C3 | Explicit identification of the AI system used |
| `ai_assistance.tool_purpose` | C3 | Specific task AI was invoked for |
| `ai_assistance.human_review[]` | C4 | Named reviewer, review tier, and findings |
| `ai_assistance.human_override_log[]` | C4 | Documented corrections and rationale |
| `ai_assistance.ai_risk_assessment` | C5 | Confidence band and documented cautions |

Schema enforcement runs in CI/CD on every commit. A decision record with `ai_assistance.used = true` that omits required disclosure fields fails validation and cannot be merged.

Worked example demonstrating full disclosure: [`examples/rgds-dec-0003-ai-assisted-conditional-go.md`](../examples/rgds-dec-0003-ai-assisted-conditional-go.md)

---

## Contract Status

Reference governance artifact. This contract defines governance boundaries. It does not prescribe tooling, implement enforcement, or constitute a legal agreement.

Operational enforcement is the responsibility of delivery systems, governance processes, and human reviewers. Versioning and change history are tracked at the repository level.

*Part of the RGDS decision governance framework. Apache 2.0. See also: [GDI v3.0](https://github.com/mj3b/governed-decision-intelligence) · [RGDS](https://github.com/mj3b/rgds)*

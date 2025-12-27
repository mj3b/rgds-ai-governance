# AI Service Line Integration with RGDS (Pilot Overview)

This document explains how Syner-G’s AI service line integrates with Regulated Gate Decision Support (RGDS)
to provide bounded, defensible support in regulated, phase-gated environments — without altering decision
authority, governance, or accountability.

This is written for:
- AI Analysts and Principal AI Business Analysts
- Strategy & Transformation delivery leaders
- Regulated client stakeholders (Regulatory, Quality, Program Leadership)

---

## Context: Why This Exists

Syner-G’s AI service line is a newly launched, pilot-stage offering embedded within the Strategy & Transformation vertical.
It is designed to help clients across all stages of AI adoption — from apprehensive beginners to advanced users — through
human-governed, bounded solutions that emphasize trust, change management, and practical delivery outcomes.

Because the offering is new, early projects are used to refine and scale:
- playbooks and best practices
- resourcing models and delivery patterns
- internal training and cross-functional enablement
- business development insights grounded in real client work

RGDS fits this pilot model because it provides a concrete, non-agentic governance pattern that can be applied consistently
across regulated engagements.

---

## What RGDS Provides to the AI Service Line

RGDS is a decision-support operating model that makes phase-gate decisions defensible by forcing:

- explicit decision ownership
- evidence linkage (what was used, where it came from)
- risk visibility (what is known, unknown, accepted)
- conditions and contingencies (what must be true, what happens if it is not)
- auditability (what changed, who approved it, when)

RGDS is explicitly non-agentic. It does not decide. It records and governs decisions.

In the AI service line context, RGDS becomes:
- a repeatable governance pattern for clients who need trust
- an internal playbook anchor for consistent delivery
- a “decision memory” structure that makes AI assistance safe to adopt incrementally

---

## What the AI Service Line Adds to RGDS (Without Changing Authority)

The AI service line can add bounded support to RGDS in ways that reduce late-stage surprises and decision compression.
Under this model, AI outputs are treated as:
- informational inputs
- explicitly reviewable
- explicitly rejectable
- never authoritative

Examples of permitted support:
- inconsistency detection across documents and evidence
- dependency mapping (what decisions rely on which inputs)
- contradiction spotting (new findings vs prior assumptions)
- risk surfacing (what changed, what was assumed, what is missing)
- structured summarization into RGDS fields for faster review

All assistance is governed by the Non-Agentic AI Contract in this repository.

---

## Hard Boundary: Decision Authority Never Moves

Under this integration model:
- AI may prepare information for a decision
- only humans may make, approve, or own decisions
- RGDS remains the authoritative decision record

Any solution that blurs this boundary is out of scope.

---

## Delivery Pattern: How Work Actually Runs

In practice, AI-assisted RGDS delivery follows a repeatable pattern:

1. **Intake and scoping (human-led)**
   - clarify the gate decision and who owns it
   - define allowed AI assistance boundaries
   - define required evidence sources

2. **Evidence preparation (human-curated)**
   - evidence is gathered and approved for use
   - sensitive sources are handled per client governance

3. **Bounded AI assistance (non-authoritative)**
   - AI produces review artifacts (summaries, diffs, flags, dependency maps)
   - outputs are labeled as AI-assisted and include traceability to sources

4. **Human review and decision**
   - accountable owners accept/reject/modify AI-assisted outputs
   - final decisions are recorded in RGDS with explicit rationale and conditions

5. **Pilot learning loop (service-line shaping)**
   - what worked / failed is captured
   - playbooks and resourcing models are updated through explicit change control

This pattern supports clients wherever they are in their AI journey, including those who are cautious or unfamiliar with AI.

---

## Role of the Principal AI Business Analyst

The Principal AI Business Analyst operates as the integration layer between:
- regulated delivery reality (timelines, interdependencies, review cycles)
- governance and quality expectations
- cross-functional decision-makers
- bounded AI assistance patterns that reduce friction without creating risk

Key responsibilities in this model:
- define and enforce decision boundaries (what AI can and cannot do)
- translate messy evidence and review cycles into governed decision records
- design repeatable playbooks and templates for the service line
- mentor and cross-train analysts and BAs who lack deep AI experience
- support change management so adoption increases without undermining trust

---

## Where to Start (Pilot Guidance)

For early pilot engagements, prioritize use cases that:
- reduce late discovery of misalignment
- improve review efficiency without changing outcomes
- produce high-value, low-risk decision artifacts

Start with:
- dependency mapping and timeline risk surfacing
- cross-document consistency checks
- structured decision summaries that reduce meeting load

Avoid early pilots that:
- attempt automation of regulatory judgment
- imply “AI approval”
- remove human accountability from the loop

---

## References

- Non-Agentic AI Contract: `contracts/non-agentic-ai-contract.md`
- AI-Assisted Decision Example: `examples/rgds-dec-0003-ai-assisted-conditional-go.md`

# AI Assistance Governance

A working method/profile for bounded AI participation in consequential decisions.

Research question: Can a documented AI participation boundary and a two-part dependency assessment make the non-AI basis of an AI-assisted decision inspectable?

RGDS records assigned human ownership, approval, and review. Schema and semantic validation check recorded structure and selected internal constraints. They do not prove human authorship, substantive human judgment, or that assigned authority had practical force. Practical human influence requires separate assessment.

## Architecture and scope

```text
GDI: general decision architecture
  -> AI Assistance Governance: method/profile for bounded AI participation
    -> RGDS: regulated biopharma reference implementation

RGDS Independent Study: separate historical/exploratory research
```

[GDI](https://github.com/mj3b/governed-decision-intelligence) supplies the general architecture. This profile defines participation rules and an assessment procedure. [RGDS v2.0.1](https://github.com/mj3b/rgds/tree/v2.0.1) supplies the implementation contract inspected for this revision. This hierarchy describes conceptual roles, without asserting a formal cross-version conformance test. Changes to any layer require a compatibility review.

The [independent study](https://github.com/mj3b/rgds-independent-study) is separate historical/exploratory source review and modeling work. It is not validation evidence for this profile. Its DOI belongs to that research object and is not this repository's identifier. Proposed Node & Norm placement is `NN-DE`, method/profile; admission remains pending.

## Six governance covenants

These are adoption requirements. This documentation does not implement runtime controls or establish that a deployment follows them.

| Covenant | Required practice | Failure mode addressed |
|---|---|---|
| 1. No autonomous or agentic behavior | AI must not decide, approve, accept risk, or trigger downstream actions | Unauthorized action |
| 2. Assigned human authority and assessed independence | Identify the human owner and approvers; assess the non-AI decision basis | Ceremonial ownership or unsupported rationale |
| 3. Explicit invocation | Record the specific task and AI use | Undisclosed influence |
| 4. Review and rejection | A named reviewer records acceptance, rejection, or modification | Unreviewed reliance |
| 5. Explicit risk acceptance | Humans document uncertainty, dissent, and accepted residual risk | Silent risk acceptance |
| 6. Evidence subordination | Trace material rationale claims to inspectable non-AI sources | Model output substituting for evidence |

The [contract](contracts/non-agentic-ai-contract.md) defines these requirements and the actual RGDS field checks. Under this profile, non-agentic assistance means a human invokes a bounded analytical task and reviews the output before its use. It is a local governance definition, not a claim about all AI systems.

## AI Dependency Test

The [AI Dependency Test](docs/ai-dependency-test.md) asks whether the non-AI decision basis can be reconstructed when model-generated artifacts are excluded from the evidentiary basis.

1. Structural record completeness: retain and validate the complete original record, including truthful `ai_assistance` disclosure. Inventory the required decision, evidence, risk, and authority fields.
2. Substantive independence: a qualified reviewer traces the material rationale to non-AI sources, records unsupported dependencies, and assesses whether those sources support reconstruction without model output.

`ai_assistance` is a required top-level object in RGDS v2.0.1. Deleting it fails schema validation. Changing `used: true` to `used: false` would misstate historical AI use. Exclusion is an assessment view, not deletion from the source record. Structural success does not imply substantive success, regulatory defensibility, or a counterfactual claim that the same decision would have occurred without AI.

The earlier [removability document](docs/ai-removability-proof.md) is retained with a supersession notice for provenance.

## Interpretive framework crosswalk

The [crosswalk](docs/framework-crosswalk.md) maps selected external concepts to possible records and review practices. It does not establish compliance, conformity, certification, control effectiveness, model credibility, or regulator acceptance. Applicability and adequacy require separate assessment in the adopting context.

## Reading guide

| Reader | Document |
|---|---|
| Executive or approver | [What AI will not do](docs/what-ai-will-not-do.md) |
| Governance reviewer | [Non-agentic AI contract](contracts/non-agentic-ai-contract.md) |
| Assessment reviewer | [AI Dependency Test](docs/ai-dependency-test.md) |
| Architecture reviewer | [Conceptual decision architecture](docs/ai-governance-conceptual-decision-architecture.md) |
| Framework reviewer | [Interpretive crosswalk](docs/framework-crosswalk.md) |
| Example reader | [Hypothetical worked example](examples/rgds-dec-0003-ai-assisted-conditional-go.md) |
| Maintainer | [Validation instructions](docs/validation.md) and [remediation report](docs/remediation-report.md) |

## Repository contents

```text
rgds-ai-governance/
├── README.md
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── NOTICE
├── contracts/
│   └── non-agentic-ai-contract.md
├── docs/
│   ├── ai-dependency-test.md
│   ├── ai-governance-conceptual-decision-architecture.md
│   ├── ai-removability-proof.md       (superseded historical text)
│   ├── framework-crosswalk.md
│   ├── remediation-report.md
│   ├── validation.md
│   └── what-ai-will-not-do.md
├── examples/
│   └── rgds-dec-0003-ai-assisted-conditional-go.md
├── scripts/
│   ├── check_docs.py
│   └── check_rgds_contract.py
└── .github/workflows/
    └── validate.yml
```

## Status, limitations, and citation

| Dimension | Current state |
|---|---|
| Object | AI Assistance Governance method/profile |
| Development | Working, unreleased remediation of the historical documentation |
| Evidence | Documentation and contract inspection; hypothetical example only |
| Review | AI-assisted remediation; owner review pending; independent review open |
| Technical | Documentation profile with lightweight regression checks; no runtime enforcement |
| Validation scope | Local links and selected RGDS v2.0.1 contract assumptions |
| Open evidence gates | Qualified substantive application, independent assessment, field effectiveness |
| Admission | Pending owner review and RGDS-family reassessment; no Registry admission asserted |

No deployment study, regulatory outcome improvement, or demonstrated human independence is established here. A schema-valid record can contain fabricated or unexamined claims. Reviewer competence, evidence access, time, organizational authority, and actual interventions require separate evidence. [HIT](https://github.com/mj3b/human-influence-telemetry) is an adjacent assessment method for practical human influence; no HIT evaluation is claimed for this profile.

[CHANGELOG.md](CHANGELOG.md) preserves historical entries and records corrections separately. Cite this method using [CITATION.cff](CITATION.cff), including the exact commit used; no new release or DOI is asserted.

Author: **Mark Julius Banasihan**, [ORCID](https://orcid.org/0009-0001-8121-2878), [GitHub](https://github.com/mj3b). Existing authorship is retained. Codex assisted this remediation with repository inspection, drafting, and validation scripts under the owner's instructions; this does not establish owner approval of the resulting text. See [NOTICE](NOTICE) and [LICENSE](LICENSE).

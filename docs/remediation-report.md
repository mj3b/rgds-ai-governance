# Node & Norm Remediation Report

Date: 2026-09-09. Scope: `mj3b/rgds-ai-governance` only.

Controlling specification: Node & Norm Repository Remediation Audit v0.1 from the owner's “Design Node Norm Repo” conversation, with the nine requirements in the authorized handoff. Baseline commit: `8ae4cc2e26cc3607f1e9711f72c90300789cc918`. The related Blueprint v0.1 supplies the admission gates below. This is a repository assessment, not a Registry admission decision.

## Changes and evidence boundaries

| Requirement | Change | Inspectable evidence |
|---|---|---|
| 1. Dependency assessment | Replaced active guarantee with separate structural and substantive procedures; preserve truthful disclosure | [AI Dependency Test](ai-dependency-test.md); pinned contract regression check |
| 2. Human authority | Removed active absolute-authority and authorship-enforcement claims; separate assigned authority from practical influence | [Contract](../contracts/non-agentic-ai-contract.md), [architecture](ai-governance-conceptual-decision-architecture.md), [executive summary](what-ai-will-not-do.md) |
| 3. Framework claims | Sourced interpretive crosswalk, explicit no-compliance/no-conformity/no-certification boundaries; withdrew unsupported ARAF row | [Crosswalk](framework-crosswalk.md) |
| 4. Navigation | Corrected renamed document link, removed deleted service-line entry, updated reading guide and inventory | [README](../README.md); local documentation checker |
| 5. Architecture | GDI -> AI Assistance Governance method/profile -> RGDS; separate historical/exploratory study | README and architecture |
| 6. Provenance | Preserved original proof body below notice, prior changelog text, LICENSE, and all existing commits | [Historical proof](ai-removability-proof.md), [CHANGELOG](../CHANGELOG.md) |
| 7. Metadata | Added CFF, research/status boundaries, corrected NOTICE identity and disclosed AI assistance | [CITATION.cff](../CITATION.cff), [NOTICE](../NOTICE), README |
| 8. Validation | Added local-link/inventory and narrow pinned RGDS contract checks with CI | [Validation instructions](validation.md) |
| 9. Admission assessment | Gate-by-gate assessment and outstanding decisions | This report |

Additional defects corrected within scope: `escalate` was incorrectly listed as an RGDS outcome; required disclosure fields were conflated with optional fields and warnings; the illustrative example claimed pilot/compliance status without supporting records. The example is now explicitly hypothetical, its unsupported seven/five precedent counts are withdrawn as evidence, and its structural result is not assessed while its substantive result is indeterminate. No clinical or regulatory recommendation is supplied.

## Validation results

- Local documentation checker: 50 relative Markdown links and 17 declared inventory files passed; targeted superseded-wording checks passed.
- Pinned RGDS contract regression: passed baseline validation, disclosure-deletion rejection, conditional schema and semantic requirements, optional override log, and confidence/disclosure warning checks.
- Upstream RGDS v2.0.1 inspection: all six examples passed strict validation; all nine upstream regression tests passed using `jsonschema[format]==4.25.1`. The first run with the system environment lacked format dependencies; rerunning with the declared extras resolved the date-format failure without upstream changes.
- CFF: passed the CFF 1.2.0 JSON Schema using parsed YAML. Workflow YAML was parsed and inspected; remote CI status is reported in the pull request.
- Preservation: LICENSE unchanged; original proof body and preexisting changelog text verified against the baseline commit. No existing file was deleted.
- External links: 11 of 13 current Markdown URLs returned HTTP 200. EUR-Lex and ISO returned HTTP 403 to the automated client; their official source pages were inspected through web retrieval/search. Automated reachability for those two remains unverified, with no broken target established.
- Diff whitespace check: passed.

These results establish bounded repository consistency. They do not establish substantive independence, practical human influence, regulatory compliance, or institutional admission.

## Provenance and versioning

No GitHub releases or Git tags were present at inspection. The historical `v1.0.0` and `v0.1.0` changelog headings remain verbatim, including their dates and old filenames. They are historical descriptions, not newly asserted releases. This correction is recorded as Unreleased. No release/tag was created, renamed, or overwritten. Existing document paths remain present; the proof body is explicitly superseded rather than silently rewritten.

The original author's identity and Apache-2.0 license remain. CFF's `software` value is a packaging constraint explained in the validation document; the scholarly object is a method/profile. No independent-study DOI is assigned to this repository. Codex performed AI-assisted inspection, drafting, and validation scripting under owner authorization. Owner approval of the resulting text and independent review are not inferred.

## Admission-gate assessment

These judgments apply to the remediated candidate, before owner review and merge.

| Blueprint gate | Assessment | Evidence or remaining action |
|---|---|---|
| Research question | Satisfied for candidate | Bounded reconstruction question in README |
| Object identity | Satisfied for candidate | Working method/profile, implementation separate |
| Claim boundary | Satisfied for candidate | Structure, substantive independence, practical influence separated |
| Evidence | Satisfied for bounded documentation claims | Versioned contract and sources inspectable; no empirical effects claimed |
| Limitations | Satisfied for candidate | Source access, anchoring, review quality, field effectiveness limits published |
| Status | Satisfied for candidate | Working/unreleased; hypothetical example; independent review open |
| Attribution | Satisfied for candidate | Existing author/ORCID retained; external sources identified |
| Collaboration | Satisfied for candidate | No third-party ownership or Node & Norm stewardship asserted |
| Citation | Satisfied for candidate | Repository-specific CFF; no borrowed DOI or invented release |
| Reproducibility | Satisfied for bounded inspection | Local docs and pinned contract inspection path added |
| AI assistance | Disclosed; owner review open | Material remediation assistance disclosed without claiming human approval |
| Relationship | Satisfied for candidate | GDI -> profile -> RGDS; study separately classified |
| Corrections | Satisfied for candidate | Known active errors corrected and historical claims marked superseded |
| Provenance | Satisfied for this pass | History retained; no transfer performed; future migration still requires review |

Recommendation: candidate for admission as a working method/profile after owner acceptance of the correction and a renewed RGDS-family review. The original audit's “hold and reframe” defects are addressed in the candidate text. This pass does not establish institutional admission. Formal Registry placement and recognized version remain decisions for Node & Norm; the independent-study remediation remains outside this pass and a dependency for the planned family reassessment.

Substantive application to an inspectable source packet, independent assessment, and field effectiveness remain open research gates. These gaps prohibit claims of validated independence or effectiveness; they need not be misrepresented as proof that a transparently working method has no research value.

No repository transfer, Node & Norm organization modification, or independent-study edit was performed.

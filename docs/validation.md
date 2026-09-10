# Validation and Inspection

This repository originally contained Markdown documentation only, with no executable validator, test suite, or CI workflow. The remediation adds checks for the specific path and schema-claim drift found. These checks do not validate governance effectiveness or replace substantive review.

## Local documentation check

Requires Python 3.9 or later, standard library only:

```sh
python3 scripts/check_docs.py
```

Checks local inline Markdown file targets and simple heading anchors, the declared inventory, the historical supersession notice, and selected superseded phrases in current guidance. Historical changelog entries and the preserved proof body are excluded from active-claim checks. External availability, arbitrary Markdown syntax, and semantic claim correctness are outside this script's scope.

## RGDS contract boundary check

Use a separate clean reference checkout. This procedure reads it and tests in-memory copies; it does not modify RGDS records or publish changes to that repository.

```sh
git clone --branch v2.0.1 --depth 1 https://github.com/mj3b/rgds.git /tmp/rgds-reference
python3 -m pip install 'jsonschema[format]==4.25.1'
python3 scripts/check_rgds_contract.py /tmp/rgds-reference
```

The check requires commit `f6fa066c7e53d1d89d68ac8ef424b559ef58be34`. It validates the AI-assisted canonical baseline, demonstrates that deleting `ai_assistance` fails, distinguishes semantic requirements from optional fields and warnings, and demonstrates that schema validity cannot authenticate historical AI use. It produces no substantive independence result.

The [workflow](../.github/workflows/validate.yml) runs the documentation and contract checks on pull requests, main pushes, and manual dispatch. It does not itself configure protected branches or enforce the six covenants at runtime.

## Human review and preservation

Review all current prose for claims that exceed evidence. Confirm the [AI Dependency Test](ai-dependency-test.md) records two separate results and retains truthful disclosure. Inspect the [crosswalk](framework-crosswalk.md) against its named sources. Verify that the historical proof body, prior changelog text, LICENSE, existing commits, and release/tag identifiers remain preserved.

Citation metadata uses CFF 1.2.0's `software` type as a repository packaging category because CFF only permits `software` or `dataset`. The title, abstract, and README identify the artifact as a working method/profile; the metadata does not imply executable governance enforcement. Version 1.1.0 and its release date identify the owner-authorized publication. No DOI is assigned. Cite the release and, when needed, the exact commit.

For recorded results and open admission gates, see the [remediation report](remediation-report.md).

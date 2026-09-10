#!/usr/bin/env python3
"""Check local Markdown targets and specific current-guidance drift; not a semantic audit."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
links = 0
for path in sorted(ROOT.rglob('*.md')):
    if '.git' in path.parts or '.reference-rgds' in path.parts:
        continue
    text = path.read_text()
    # Preserve historical text without treating it as active guidance.
    if path.name == 'ai-removability-proof.md':
        if 'Superseded historical text' not in text or 'ai-dependency-test.md' not in text:
            errors.append(f'{path.relative_to(ROOT)}: missing supersession notice')
        text = text.split('<!-- HISTORICAL BODY START -->')[0]
    if path.name == 'CHANGELOG.md':
        text = text.split('## [v1.0.0]')[0]
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        parsed = urlsplit(target.strip('<>'))
        if parsed.scheme or parsed.netloc:
            continue
        dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        links += 1
        if not dest.exists():
            errors.append(f'{path.relative_to(ROOT)}: missing target {target}')
        elif parsed.fragment:
            headings = re.findall(r'^#{1,6}\s+(.+)$', dest.read_text(), re.M)
            anchors = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
            if unquote(parsed.fragment) not in anchors:
                errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')
    if path.name in {'README.md', 'non-agentic-ai-contract.md',
                     'ai-governance-conceptual-decision-architecture.md', 'what-ai-will-not-do.md'}:
        for phrase in ['human authority is absolute', 'satisfy specific requirements',
                       'schema validation enforces required human-authored',
                       'disclosure is an optional addendum',
                       'client-one-pager-what-ai-will-not-do.md', 'service-line-overview.md']:
            if phrase in text.lower():
                errors.append(f'{path.relative_to(ROOT)}: superseded phrase {phrase}')
# Inline inventory paths in README are also checked through its explicit manifest.
expected = ['README.md','CHANGELOG.md','CITATION.cff','LICENSE','NOTICE',
            'contracts/non-agentic-ai-contract.md','docs/ai-dependency-test.md',
            'docs/ai-governance-conceptual-decision-architecture.md',
            'docs/ai-removability-proof.md','docs/framework-crosswalk.md',
            'docs/remediation-report.md','docs/validation.md','docs/what-ai-will-not-do.md',
            'examples/rgds-dec-0003-ai-assisted-conditional-go.md',
            'scripts/check_docs.py','scripts/check_rgds_contract.py','.github/workflows/validate.yml']
for name in expected:
    if not (ROOT / name).is_file():
        errors.append(f'missing inventory file: {name}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {links} local Markdown links and {len(expected)} inventory files; targeted wording checks')

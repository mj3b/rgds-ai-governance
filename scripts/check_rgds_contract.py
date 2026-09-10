#!/usr/bin/env python3
"""Regression checks against an explicit external RGDS checkout; never alter source records."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from jsonschema import Draft202012Validator, FormatChecker

PIN = 'f6fa066c7e53d1d89d68ac8ef424b559ef58be34'
if len(sys.argv) != 2:
    raise SystemExit('Usage: python scripts/check_rgds_contract.py /path/to/rgds-v2.0.1')
root = Path(sys.argv[1]).resolve()
head = subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'], text=True).strip()
if head != PIN:
    raise SystemExit(f'Expected RGDS v2.0.1 {PIN}; found {head}')
if subprocess.check_output(['git','-C',str(root),'status','--porcelain'], text=True).strip():
    raise SystemExit('Reference checkout must be clean')
schema = json.loads((root/'decision-log/decision-log.schema.json').read_text())
validator = Draft202012Validator(schema, format_checker=FormatChecker())
spec = importlib.util.spec_from_file_location('rgds_validator',root/'scripts/validate_decision_log.py')
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
def require(condition, message):
    if not condition:
        raise SystemExit('FAIL: '+message)
record = json.loads((root/'examples/rgds-dec-0006-ai-assisted-conditional-go.json').read_text())
require(not list(validator.iter_errors(record)), 'baseline schema validation')
require(not module.semantic_checks(record)[0], 'baseline semantic validation')
original = copy.deepcopy(record)
removed = copy.deepcopy(record); del removed['ai_assistance']
require(any(e.validator == 'required' and 'ai_assistance' in e.message
            for e in validator.iter_errors(removed)), 'deleted disclosure must fail schema')
for field, code in [('tool_name','E_AI_004'),('tool_purpose','E_AI_005'),('human_review','E_AI_006')]:
    changed = copy.deepcopy(record); changed['ai_assistance'].pop(field,None)
    require(any(e.validator == 'required' and field in e.message for e in validator.iter_errors(changed)), field+' conditional schema requirement')
    require(any(code in e for e in module.semantic_checks(changed)[0]), field+' semantic requirement')
changed = copy.deepcopy(record); changed['ai_assistance'].pop('human_override_log',None)
require(not list(validator.iter_errors(changed)) and not module.semantic_checks(changed)[0],
        'override log is optional')
changed['ai_assistance']['ai_risk_assessment'] = {}
require(not list(validator.iter_errors(changed)), 'empty risk assessment has valid schema shape')
errs, warns = module.semantic_checks(changed)
require(not errs and any('W_AI_002' in w for w in warns), 'missing confidence is a warning')
# Deliberately false disclosure can retain valid shape: validation cannot authenticate history.
changed = copy.deepcopy(record); changed['ai_assistance']['used'] = False
require(not list(validator.iter_errors(changed)), 'false disclosure can be schema-valid')
require(any('W-AI-003' in w for w in module.semantic_checks(changed)[1]), 'inconsistent disclosure warning')
require(record == original, 'original must remain unchanged')
print('PASS: pinned baseline, disclosure deletion, semantic requirements, optional fields, warning boundaries')
print('These checks do not assess human authorship, substantive independence, or practical influence.')

---
name: automotive-pytest-unit-test
description: Add pytest unit tests for Python automotive software, targeting 100% branch coverage without modifying product code. Use for Python test generation, ISO 26262 Part 6-aware unit test evidence, branch coverage closure, Doxygen-style test comments, and XML/HTML traceability.
---

# Automotive Pytest Unit Test Skill

## Purpose

Use this skill when the task is to add or improve `pytest` unit tests for an existing Python codebase used in automotive software, especially when the goal is high or complete branch coverage and auditable unit-test evidence.

The target outcome is:

- meaningful `pytest` unit tests for existing Python product code;
- branch coverage target of **100%** using `coverage.py` / `pytest-cov` branch measurement;
- tests derived from available test basis artifacts such as requirements, software unit design, interface specifications, safety requirements, or change requests;
- Python-valid Doxygen-style comments above every generated test function;
- XML and HTML bidirectional traceability when a test basis is available;
- package/module-scoped Git commits that follow the repository's existing branch and commit policy.

## Activation boundaries

Use this skill for:

- adding tests for Python product modules;
- improving branch coverage for Python unit tests;
- creating pytest fixtures, parametrized tests, and focused mocks;
- producing unit-test evidence and traceability for automotive software projects.

Do **not** use this skill for:

- system, vehicle, hardware-in-the-loop, or integration test development unless the user explicitly asks;
- modifying product logic to make coverage easier;
- generating superficial tests that execute code without meaningful assertions;
- claiming formal ISO 26262 compliance beyond the evidence created by the implemented tests.

## Non-negotiable constraints

1. **Do not modify product code.**
   - Product code includes implementation modules under locations such as `src/`, package directories, production services, control logic, algorithms, generated-code wrappers, and runtime configuration used by the application.
   - Allowed changes are limited to tests, fixtures, test data, test-only utilities, traceability artifacts, coverage configuration, and documentation required to run the tests.
   - If product code appears defective, untestable, unreachable, or requires dependency injection/refactoring, report the issue and propose a product-code improvement. Do not implement the product-code change unless the user explicitly authorizes it.

2. **Do not hide coverage gaps.**
   - Do not add `# pragma: no cover`, `# pragma: no branch`, exclusions, or coverage configuration changes merely to satisfy the metric.
   - Coverage exclusions are allowed only when already established by project policy or when the code is genuinely non-executable in the target context, and the exclusion must be reported.

3. **Branch coverage target is 100%.**
   - Measure branch coverage with `--cov-branch` or an equivalent `coverage.py` configuration.
   - If 100% branch coverage cannot be achieved without modifying product code, produce a coverage gap report that identifies the exact files, lines, branches, reason, and recommended product-code change.

4. **Automotive unit-test evidence is required.**
   - Tests must be requirement/design driven when a test basis exists.
   - Tests must include positive, negative, and edge cases where applicable.
   - Tests must exercise normal behavior, abnormal/error behavior, boundary behavior, and relevant decision outcomes.
   - Avoid overstating compliance. State that tests are written to support ISO 26262 Part 6 unit-test evidence, not that the project is fully compliant.

5. **Mock only when necessary.**
   - Prefer real values, real pure functions, deterministic fixtures, and narrow test doubles.
   - Use mocks for external hardware, network, file system, OS services, time, randomness, third-party side effects, slow operations, or unavailable interfaces.
   - Keep mocks close to the boundary being isolated. Do not mock the product function under test.

## Required workflow

### 1. Preflight repository inspection

Before writing tests:

1. Inspect `AGENTS.md`, repository docs, existing test conventions, and CI configuration.
2. Inspect Git state with `git status --short` and avoid overwriting unrelated user changes.
3. Identify:
   - Python package/module layout;
   - current pytest configuration;
   - existing fixtures and test utilities;
   - coverage configuration;
   - product modules lacking tests;
   - available test basis artifacts and identifiers.
4. Establish a coverage baseline using the repository's preferred command. If no command exists, use a command like:

```bash
python -m pytest --cov=<PACKAGE_OR_SRC_PATH> --cov-branch --cov-report=term-missing:skip-covered --cov-report=xml:coverage.xml --cov-report=html:htmlcov
```

5. Record uncovered lines and branch arcs before changes.

### 2. Select test scope

Work package by package or module by module.

Prioritize in this order:

1. safety-relevant modules or modules tied to explicit requirements;
2. modules with uncovered branches;
3. modules with complex decisions or exception paths;
4. public APIs and stable interfaces before private helpers;
5. pure functions before side-effect-heavy code.

### 3. Derive test cases

For each unit under test, derive cases using applicable software test techniques:

| Technique | Use when |
|---|---|
| Requirements-based testing | Test basis contains requirement or design IDs. |
| Equivalence partitioning | Inputs naturally form valid/invalid classes. |
| Boundary value analysis | Numeric ranges, thresholds, lengths, timeouts, counters, or state limits exist. |
| Decision table testing | Multiple boolean conditions affect behavior. |
| State transition testing | Behavior depends on state, mode, lifecycle, or previous calls. |
| Pairwise / combinatorial testing | Several independent parameters interact. |
| Error guessing | Known failure modes, invalid inputs, automotive robustness concerns, defensive code. |
| Interface testing | Unit interacts with adapters, ports, protocol messages, or configuration objects. |
| Branch / condition coverage analysis | Uncovered decisions remain after functional test design. |

Every meaningful behavior should have assertions. Do not rely only on execution for coverage.

### 4. Implement pytest tests

Use idiomatic pytest:

- use `pytest.mark.parametrize` for input partitions and boundary values;
- use fixtures for shared setup only when they improve clarity;
- use `tmp_path`, `monkeypatch`, `capsys`, `caplog`, and `pytest.raises` where appropriate;
- assert externally observable behavior, return values, state changes, exceptions, emitted logs, or boundary interactions;
- keep tests deterministic and independent;
- avoid sleeps, network calls, nondeterministic time, real hardware, or environment-dependent behavior;
- prefer simple direct construction over excessive mocking;
- use `autospec=True` or strict fake objects where mocks are unavoidable;
- name tests so the behavior and condition are obvious.

### 5. Add Doxygen-style comments above every generated test function

Python does not support C/C++ `/** ... */` block comments. Use Python-valid Doxygen-style line comments immediately above each test function.

Use this format:

```python
## @test TC_<PACKAGE>_<MODULE>_<FUNCTION>_<NNN>
#  @brief Verifies <behavior> under <condition>.
#  @details AI model/version: <actual Codex/model identifier if available; otherwise "model identifier unavailable">.
#  @generated_at <ISO-8601 datetime with timezone>.
#  @testtechnique <Equivalence Partitioning | Boundary Value Analysis | Decision Table | State Transition | Error Guessing | Branch Coverage Analysis | ...>.
#  @testbasis <REQ/SUD/interface/design ID, or "No formal test basis provided">.
#  @trace <basis ID(s)> -> TC_<...>; TC_<...> -> <basis ID(s)>.
#  @pre <preconditions and fixture setup>.
#  @expected <expected result or oracle>.
def test_<unit>_<condition>_<expected_behavior>():
    ...
```

Rules:

- Do not invent model identifiers. Use the actual visible Codex/model identifier when available; otherwise write `model identifier unavailable`.
- Use the current system date/time with timezone. If timezone is unknown, use UTC.
- Include the specific test technique used for the test.
- Include a test basis ID when available.
- Keep comments concise but auditable.

### 6. Measure and close branch coverage

After each coherent test batch:

1. Run the tests for the changed package/module.
2. Run branch coverage for the target scope.
3. Inspect missing branches with terminal, XML, JSON, or HTML reports.
4. Add or adjust tests for missing meaningful branches.
5. Repeat until branch coverage is 100% or remaining gaps are proven unreachable without product-code changes.

Recommended commands:

```bash
python -m pytest tests/<PACKAGE_OR_MODULE> --cov=<PACKAGE_OR_SRC_PATH> --cov-branch --cov-report=term-missing:skip-covered
python -m coverage json -o coverage.json
python -m coverage html
```

If branch coverage remains below target, include a coverage gap report with:

- file path;
- line number or branch arc;
- uncovered condition;
- why no test can cover it without product-code changes;
- recommended product-code change;
- safety/testability impact.

### 7. Create traceability when a test basis exists

When requirements, software unit design, interface specifications, safety requirements, tickets, or other test basis artifacts are available:

1. Extract stable basis IDs.
2. Assign stable test case IDs.
3. Map basis-to-test and test-to-basis.
4. Write XML traceability to `test_evidence/traceability.xml` unless the repository has another evidence directory.
5. Render an HTML view to `test_evidence/traceability.html`.
6. Keep the mapping synchronized with Doxygen-style comments in test files.

Minimum XML structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<traceabilityReport project="<project-name>" generatedAt="<ISO-8601 datetime>" generator="Codex Skill automotive-pytest-unit-test">
  <testBasis id="REQ-001" type="requirement" source="requirements.md">
    <title>Requirement title</title>
    <linkedTestCase id="TC_PACKAGE_MODULE_001" />
  </testBasis>
  <testCase id="TC_PACKAGE_MODULE_001" file="tests/test_module.py" function="test_behavior_condition_expected">
    <technique>Boundary Value Analysis</technique>
    <linkedBasis id="REQ-001" />
  </testCase>
</traceabilityReport>
```

### 8. Git branch and commit policy

Follow the repository's branch and commit policy exactly when it exists.

If no policy is present:

1. Do not rewrite history.
2. Do not commit unrelated files.
3. Do not run `git add .`.
4. Stage explicit files only.
5. Prefer package/module-level commits:

```bash
git add tests/<package>/ test_evidence/traceability.xml test_evidence/traceability.html
git commit -m "test(<package>): add pytest branch coverage"
```

6. Use commit message scopes matching package names.
7. Commit only after relevant tests pass, unless the user explicitly asks for a work-in-progress commit.

Suggested branch name when a new branch is needed and no repository policy exists:

```text
test/pytest-branch-coverage-<package-or-scope>
```

### 9. Subagent usage guidance

When the user asks Codex to use subagents:

- Use one explorer subagent to map packages/modules and test basis artifacts.
- Use one worker subagent per package or bounded module group to write tests.
- Use a read-only reviewer/auditor subagent to check coverage gaps, traceability, comments, and product-code immutability.
- Avoid concurrent writes to the same test file.
- The parent agent should run final coverage, resolve conflicts, verify no product code changed, and create commits.

### 10. Final response requirements

At completion, summarize:

- packages/modules tested;
- branch coverage before and after;
- test techniques used;
- positive, negative, and edge-case coverage added;
- mocks used and why each mock was necessary;
- traceability artifacts created or reason they were not created;
- coverage gaps, if any, and recommended product-code improvements;
- Git branch and commits created;
- exact validation commands run.

## Quality gate checklist

Before finishing, verify all of the following:

- [ ] Product code was not modified.
- [ ] Tests pass with `python -m pytest` or the repository's canonical test command.
- [ ] Branch coverage was measured with branch coverage enabled.
- [ ] Target branch coverage is 100%, or every remaining gap has a documented reason and recommendation.
- [ ] Each generated test function has Python-valid Doxygen-style comments.
- [ ] Positive, negative, and edge cases were included where applicable.
- [ ] Mocks are minimal and justified.
- [ ] Traceability XML and HTML were created when a test basis exists.
- [ ] Commits are package/module scoped and contain no unrelated files.

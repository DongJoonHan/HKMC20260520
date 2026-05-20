# Codex Automotive Pytest Skill Package

This package contains a repo-scoped Codex Skill and an optional Codex custom subagent configuration for Python automotive unit-test generation.

## Contents

```text
.agents/skills/automotive-pytest-unit-test/SKILL.md
.agents/skills/automotive-pytest-unit-test/scripts/run_branch_coverage.sh
.agents/skills/automotive-pytest-unit-test/scripts/generate_traceability_report.py
.agents/skills/automotive-pytest-unit-test/references/test-authoring-checklist.md
.agents/skills/automotive-pytest-unit-test/assets/traceability-template.xml
.agents/skills/automotive-pytest-unit-test/assets/traceability-report-template.html
.codex/agents/automotive-pytest-tester.toml
```

## Install into a repository

Unzip this package at the repository root:

```bash
unzip codex-automotive-pytest-skill.zip -d <repo-root>
```

Codex should discover the repo-scoped skill from:

```text
<repo-root>/.agents/skills/automotive-pytest-unit-test/SKILL.md
```

The optional subagent configuration is located at:

```text
<repo-root>/.codex/agents/automotive-pytest-tester.toml
```

If your Codex version does not resolve repo-relative `skills.config.path`, edit the TOML file and replace:

```toml
path = ".agents/skills/automotive-pytest-unit-test/SKILL.md"
```

with the absolute path to `SKILL.md`.

## Example prompts

```text
Use the automotive_pytest_tester subagent to add pytest unit tests for src/brake_control, targeting 100% branch coverage. Do not modify product code.
```

```text
Use the automotive-pytest-unit-test skill. Generate tests for the steering module, create XML/HTML traceability from requirements.md, and commit by package.
```

## Notes

- The skill intentionally forbids product-code edits.
- The branch coverage target is 100%, but unreachable branches must be reported instead of hidden.
- Traceability artifacts should be generated when a test basis exists.

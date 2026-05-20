# Codex 자동차 Pytest 스킬 패키지

이 패키지는 Python 자동차 소프트웨어 단위 테스트 생성을 위한 저장소 범위 Codex 스킬과 선택형 Codex 사용자 지정 서브에이전트 설정을 포함합니다.

## 구성

```text
.agents/skills/automotive-pytest-unit-test/SKILL.md
.agents/skills/automotive-pytest-unit-test/scripts/run_branch_coverage.sh
.agents/skills/automotive-pytest-unit-test/scripts/generate_traceability_report.py
.agents/skills/automotive-pytest-unit-test/references/test-authoring-checklist.md
.agents/skills/automotive-pytest-unit-test/assets/traceability-template.xml
.agents/skills/automotive-pytest-unit-test/assets/traceability-report-template.html
.codex/agents/automotive-pytest-tester.toml
```

## 저장소에 설치

이 패키지를 저장소 루트에 압축 해제합니다:

```bash
unzip codex-automotive-pytest-skill.zip -d <repo-root>
```

Codex는 다음 위치에서 저장소 범위 스킬을 인식해야 합니다:

```text
<repo-root>/.agents/skills/automotive-pytest-unit-test/SKILL.md
```

선택형 서브에이전트 설정은 다음 위치에 있습니다:

```text
<repo-root>/.codex/agents/automotive-pytest-tester.toml
```

사용 중인 Codex 버전이 저장소 상대 경로인 `skills.config.path`를 해석하지 못한다면, TOML 파일을 열어 다음 값을:

```toml
path = ".agents/skills/automotive-pytest-unit-test/SKILL.md"
```

`SKILL.md`의 절대 경로로 바꾸십시오.

## 예시 프롬프트

```text
Use the automotive_pytest_tester subagent to add pytest unit tests for src/brake_control, targeting 100% branch coverage. Do not modify product code.
```

```text
Use the automotive-pytest-unit-test skill. Generate tests for the steering module, create XML/HTML traceability from requirements.md, and commit by package.
```

## 참고 사항

- 이 스킬은 제품 코드 수정을 의도적으로 금지합니다.
- Branch coverage 목표는 100%이지만, 도달할 수 없는 분기는 숨기지 말고 보고해야 합니다.
- 테스트 기준이 존재하는 경우 추적성 산출물은 XML 및 HTML로 생성해야 합니다.

---

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

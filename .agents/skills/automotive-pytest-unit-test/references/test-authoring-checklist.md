# Automotive Pytest Unit Test Authoring Checklist

Use this checklist while applying the `automotive-pytest-unit-test` skill.

## Repository inspection

- [ ] Read `AGENTS.md`, README, CI, pytest, and coverage configuration.
- [ ] Inspect `git status --short`.
- [ ] Identify product source roots and test roots.
- [ ] Identify current test naming, fixture, and parametrization conventions.
- [ ] Identify available test basis artifacts and stable basis IDs.

## Product-code immutability

- [ ] No product implementation files changed.
- [ ] No coverage exclusions added to product code.
- [ ] Any recommended product-code improvements are documented separately.

## Test design

- [ ] Positive cases included.
- [ ] Negative/error cases included.
- [ ] Boundary and edge cases included.
- [ ] Branch/condition outcomes exercised.
- [ ] Requirements/design/interface IDs linked when available.
- [ ] Tests include meaningful assertions.
- [ ] Mocks are minimized and justified.

## Doxygen-style comments

- [ ] Every generated test has a `## @test` comment block.
- [ ] AI model/version is recorded or explicitly marked unavailable.
- [ ] Generation timestamp is ISO-8601 with timezone.
- [ ] Test techniques are listed.
- [ ] Test basis and trace links are listed.
- [ ] Expected result/oracle is listed.

## Coverage and evidence

- [ ] Branch coverage command run with `--cov-branch`.
- [ ] Coverage report saved or command output recorded.
- [ ] Remaining gaps documented with file, line, branch, reason, and recommendation.
- [ ] Traceability XML created when basis exists.
- [ ] Traceability HTML rendered when basis exists.

## Git

- [ ] Existing branch policy followed.
- [ ] No `git add .` used.
- [ ] Only related files staged.
- [ ] Commits grouped by package/module.
- [ ] Tests pass before commit.

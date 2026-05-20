#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  run_branch_coverage.sh <coverage-target> [pytest-args...]

Examples:
  run_branch_coverage.sh src/my_package tests/my_package
  run_branch_coverage.sh my_package tests --maxfail=1

This script runs pytest with branch coverage enabled and writes:
  - coverage.xml
  - htmlcov/
  - terminal missing-branch summary
USAGE
}

if [[ $# -lt 1 ]]; then
  usage
  exit 2
fi

COVERAGE_TARGET="$1"
shift

python -m pytest "$@" \
  --cov="$COVERAGE_TARGET" \
  --cov-branch \
  --cov-report=term-missing:skip-covered \
  --cov-report=xml:coverage.xml \
  --cov-report=html:htmlcov

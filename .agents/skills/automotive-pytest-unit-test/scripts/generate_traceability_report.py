#!/usr/bin/env python3
"""Render a simple HTML traceability report from traceability XML.

Expected XML root:
  <traceabilityReport project="..." generatedAt="..." generator="...">
    <testBasis id="..." type="..." source="...">
      <title>...</title>
      <linkedTestCase id="..." />
    </testBasis>
    <testCase id="..." file="..." function="...">
      <technique>...</technique>
      <linkedBasis id="..." />
    </testCase>
  </traceabilityReport>
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def text_of(parent: ET.Element, tag: str, default: str = "") -> str:
    child = parent.find(tag)
    if child is None or child.text is None:
        return default
    return child.text.strip()


def attr(element: ET.Element, key: str, default: str = "") -> str:
    return element.attrib.get(key, default).strip()


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def render(xml_path: Path) -> str:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    if root.tag != "traceabilityReport":
        raise ValueError(f"Expected root tag 'traceabilityReport', got {root.tag!r}")

    project = attr(root, "project", "Unknown project")
    generated_at = attr(root, "generatedAt", "Unknown generation time")
    generator = attr(root, "generator", "Unknown generator")

    basis_items = root.findall("testBasis")
    test_cases = root.findall("testCase")

    basis_rows: list[str] = []
    for item in basis_items:
        linked = ", ".join(
            esc(attr(link, "id")) for link in item.findall("linkedTestCase") if attr(link, "id")
        )
        basis_rows.append(
            "<tr>"
            f"<td>{esc(attr(item, 'id'))}</td>"
            f"<td>{esc(attr(item, 'type'))}</td>"
            f"<td>{esc(attr(item, 'source'))}</td>"
            f"<td>{esc(text_of(item, 'title'))}</td>"
            f"<td>{linked}</td>"
            "</tr>"
        )

    test_rows: list[str] = []
    for case in test_cases:
        techniques = ", ".join(esc(t.text.strip()) for t in case.findall("technique") if t.text and t.text.strip())
        linked = ", ".join(
            esc(attr(link, "id")) for link in case.findall("linkedBasis") if attr(link, "id")
        )
        test_rows.append(
            "<tr>"
            f"<td>{esc(attr(case, 'id'))}</td>"
            f"<td>{esc(attr(case, 'file'))}</td>"
            f"<td>{esc(attr(case, 'function'))}</td>"
            f"<td>{esc(text_of(case, 'title'))}</td>"
            f"<td>{techniques}</td>"
            f"<td>{linked}</td>"
            "</tr>"
        )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Unit Test Traceability Report - {esc(project)}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 2rem; line-height: 1.45; }}
    table {{ border-collapse: collapse; width: 100%; margin: 1rem 0 2rem; }}
    th, td {{ border: 1px solid #ccc; padding: 0.5rem; vertical-align: top; }}
    th {{ background: #f3f3f3; text-align: left; }}
    code {{ background: #f6f6f6; padding: 0.1rem 0.25rem; }}
  </style>
</head>
<body>
  <h1>Unit Test Traceability Report</h1>
  <p><strong>Project:</strong> {esc(project)}</p>
  <p><strong>Generated at:</strong> {esc(generated_at)}</p>
  <p><strong>Generator:</strong> {esc(generator)}</p>

  <h2>Basis to Test Cases</h2>
  <table>
    <thead>
      <tr><th>Basis ID</th><th>Type</th><th>Source</th><th>Title</th><th>Linked Test Cases</th></tr>
    </thead>
    <tbody>
      {''.join(basis_rows) if basis_rows else '<tr><td colspan="5">No test basis entries found.</td></tr>'}
    </tbody>
  </table>

  <h2>Test Cases to Basis</h2>
  <table>
    <thead>
      <tr><th>Test Case ID</th><th>File</th><th>Function</th><th>Title</th><th>Techniques</th><th>Linked Basis</th></tr>
    </thead>
    <tbody>
      {''.join(test_rows) if test_rows else '<tr><td colspan="6">No test case entries found.</td></tr>'}
    </tbody>
  </table>
</body>
</html>"""


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Render traceability XML to HTML.")
    parser.add_argument("xml", type=Path, help="Path to traceability.xml")
    parser.add_argument("html", type=Path, help="Output path for traceability.html")
    args = parser.parse_args(argv)

    try:
        output = render(args.xml)
    except Exception as exc:  # noqa: BLE001 - CLI should print a concise diagnostic
        print(f"error: {exc}", file=sys.stderr)
        return 1

    args.html.parent.mkdir(parents=True, exist_ok=True)
    args.html.write_text(output, encoding="utf-8")
    print(f"wrote {args.html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

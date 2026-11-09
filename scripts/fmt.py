#!/usr/bin/env python3
"""Rewrite data/*.yaml in the canonical layout (stable key order, one entry per block).

Usage:
    python scripts/fmt.py
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

DATA = Path(__file__).resolve().parent.parent / "data"
KEYS = ["title", "url", "org", "year", "type", "topic", "methods", "stage", "summary"]


def q(s: str) -> str:
    return json.dumps(str(s).strip(), ensure_ascii=False)


def dump_entries(entries: list[dict]) -> str:
    blocks = []
    for e in entries:
        lines = [
            f"- title: {q(e['title'])}",
            f"  url: {e['url'].strip()}",
            f"  org: [{', '.join(q(o) for o in e['org'])}]",
            f"  year: {int(e['year'])}",
            f"  type: {e['type']}",
            f"  topic: {q(e['topic'])}",
            f"  methods: [{', '.join(q(m) for m in e['methods'])}]",
            f"  stage: {e['stage']}",
            f"  summary: {q(e['summary'])}",
        ]
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


def main() -> None:
    config = yaml.safe_load((DATA / "_domains.yaml").read_text(encoding="utf-8"))
    for dom in config["domains"]:
        path = DATA / dom["file"]
        if not path.exists():
            continue
        entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        order = {t["name"]: i for i, t in enumerate(dom["topics"])}
        entries.sort(key=lambda e: (order.get(e["topic"], 999), -int(e["year"]), e["title"].lower()))
        header = f"# {dom['title']}. Schema and rules: see CONTRIBUTING.md.\n\n"
        path.write_text(header + dump_entries(entries), encoding="utf-8")
    print("formatted")


if __name__ == "__main__":
    main()

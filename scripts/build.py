#!/usr/bin/env python3
"""Validate the applied-control data files and generate the README, indexes, and explorer.

Usage:
    python scripts/build.py            # validate and regenerate all outputs
    python scripts/build.py --check    # validate and fail if generated files are stale (used in CI)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
TEMPLATE = ROOT / "scripts" / "explorer_template.html"

REQUIRED_KEYS = ["title", "url", "org", "year", "type", "topic", "methods", "stage", "summary"]
MAX_SUMMARY_WORDS = 35
CURRENT_YEAR = date.today().year


# --------------------------------------------------------------------------- loading


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_all():
    vocab = load_yaml(DATA / "_vocab.yaml")
    config = load_yaml(DATA / "_domains.yaml")
    domains = []
    for dom in config["domains"]:
        entries = load_yaml(DATA / dom["file"]) or []
        for e in entries:
            e["domain"] = dom["id"]
        domains.append({**dom, "entries": entries})
    return vocab, config, domains


# --------------------------------------------------------------------------- validation


def validate(vocab, domains) -> list[str]:
    errors: list[str] = []
    seen_urls: dict[str, str] = {}
    seen_titles: dict[str, str] = {}
    methods = set(vocab["methods"])
    all_topics = Counter(t["name"] for dom in domains for t in dom["topics"])
    for name, c in all_topics.items():
        if c > 1:
            errors.append(f"_domains.yaml: topic {name!r} is declared in {c} domains (names must be unique)")
    for dom in domains:
        topics = [t["name"] for t in dom["topics"]]
        for i, e in enumerate(dom["entries"]):
            where = f"{dom['file']}[{i}] {e.get('title', '<no title>')!r}"
            missing = [k for k in REQUIRED_KEYS if k not in e]
            if missing:
                errors.append(f"{where}: missing keys {missing}")
                continue
            extra = set(e) - set(REQUIRED_KEYS) - {"domain"}
            if extra:
                errors.append(f"{where}: unknown keys {sorted(extra)}")
            if not isinstance(e["url"], str) or not e["url"].startswith("https://"):
                errors.append(f"{where}: url must start with https://")
            if not isinstance(e["org"], list) or not e["org"]:
                errors.append(f"{where}: org must be a non-empty list")
            if not isinstance(e["year"], int) or not 1940 <= e["year"] <= CURRENT_YEAR:
                errors.append(f"{where}: year {e['year']!r} out of range")
            if e["type"] not in vocab["types"]:
                errors.append(f"{where}: type {e['type']!r} not in vocabulary")
            if e["stage"] not in vocab["stages"]:
                errors.append(f"{where}: stage {e['stage']!r} not in vocabulary")
            if e["topic"] not in topics:
                errors.append(f"{where}: topic {e['topic']!r} not declared for domain {dom['id']}")
            if not isinstance(e["methods"], list) or not 1 <= len(e["methods"]) <= 4:
                errors.append(f"{where}: methods must be a list of 1-4 tags")
            else:
                for m in e["methods"]:
                    if m not in methods:
                        errors.append(f"{where}: method {m!r} not in vocabulary")
            words = len(str(e["summary"]).split())
            if words > MAX_SUMMARY_WORDS:
                errors.append(f"{where}: summary has {words} words (max {MAX_SUMMARY_WORDS})")
            if "—" in e["summary"]:
                errors.append(f"{where}: avoid em dashes in summaries")
            url_key = normalize_url(e["url"])
            if url_key in seen_urls:
                errors.append(f"{where}: duplicate url (also in {seen_urls[url_key]})")
            seen_urls[url_key] = where
            title_key = re.sub(r"\W+", "", e["title"].lower())
            if title_key in seen_titles:
                errors.append(f"{where}: duplicate title (also in {seen_titles[title_key]})")
            seen_titles[title_key] = where
    return errors


def normalize_url(url: str) -> str:
    url = url.strip().lower().rstrip("/")
    url = re.sub(r"^https?://(www\.)?", "", url)
    return url


# --------------------------------------------------------------------------- rendering helpers


def slug(text: str) -> str:
    """GitHub-compatible heading anchor."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def md_escape(text: str) -> str:
    return text.replace("[", "\\[").replace("]", "\\]")


def sort_key(e):
    return (-e["year"], e["title"].lower())


def org_str(e) -> str:
    return ", ".join(e["org"])


def entry_md(n: int, e) -> str:
    tags = " · ".join(e["methods"])
    return (
        f"{n}. **[{md_escape(e['title'])}]({e['url']})** · {org_str(e)} · {e['year']} · *{e['type']}*  \n"
        f"   {e['summary'].strip()} <sub>`{e['stage']}` · {tags}</sub>"
    )


def compact_md(e, domain_titles) -> str:
    return (
        f"- [{md_escape(e['title'])}]({e['url']}) · {org_str(e)} · {e['year']} "
        f"<sub>{domain_titles[e['domain']]}</sub>"
    )


# --------------------------------------------------------------------------- outputs


def render_readme(config, vocab, domains) -> str:
    all_entries = [e for d in domains for e in d["entries"]]
    cases = [e for e in all_entries if e["domain"] != "resources"]
    orgs = {o for e in cases for o in e["org"]}
    method_counts = Counter(m for e in all_entries for m in e["methods"])
    stage_counts = Counter(e["stage"] for e in cases)
    years = [e["year"] for e in all_entries]

    out: list[str] = []
    out.append(f"# {config['title']}\n")
    out.append(f"{config['tagline'].strip()}\n")
    n_case_domains = sum(1 for d in domains if d["id"] != "resources" and d["entries"])
    n_resources = len(all_entries) - len(cases)
    out.append(
        f"**{len(cases)} deployment case studies** from **{len(orgs)} organizations** across "
        f"**{n_case_domains} domains** ({min(years)}–{max(years)}), plus **{n_resources}** surveys, "
        f"tools, talks, and books. "
        f"Browse the [interactive explorer]({config['explorer_url']}), or the indexes "
        f"[by method](docs/by-method.md) and [by organization](docs/by-organization.md).\n"
    )
    out.append(config["intro"].strip() + "\n")

    # Legend
    out.append("**How to read an entry**\n")
    out.append(
        "Each entry gives the title, the organizations behind the deployment, the year, and the "
        "format, followed by a one-line summary. The small print shows the deployment stage and "
        "the control methods involved.\n"
    )
    out.append("| Stage | Meaning | Entries |\n|---|---|---|")
    for s, desc in vocab["stages"].items():
        out.append(f"| `{s}` | {desc} | {stage_counts.get(s, 0)} |")
    out.append("")

    # Table of contents
    out.append("## Contents\n")
    for d in domains:
        if not d["entries"]:
            continue
        used = [t["name"] for t in d["topics"] if any(e["topic"] == t["name"] for e in d["entries"])]
        sub = " · ".join(f"[{t}](#{slug(t)})" for t in used)
        out.append(f"- **[{d['title']}](#{slug(d['title'])})** ({len(d['entries'])})  \n  {sub}")
    out.append("- [Browse by method](#browse-by-method)")
    out.append("- [Related lists](#related-lists)")
    out.append("- [Contributing](#contributing)\n")

    # Sections
    for d in domains:
        if not d["entries"]:
            continue
        out.append(f"## {d['title']}\n")
        out.append(f"{d['blurb'].strip()}\n")
        for t in d["topics"]:
            items = sorted((e for e in d["entries"] if e["topic"] == t["name"]), key=sort_key)
            if not items:
                continue
            out.append(f"### {t['name']}\n")
            for n, e in enumerate(items, 1):
                out.append(entry_md(n, e))
            out.append("\n**[back to top](#contents)**\n")

    # Method index summary
    out.append("## Browse by method\n")
    out.append(
        "The same deployments, regrouped by the control method they rely on. "
        "Full lists are in [docs/by-method.md](docs/by-method.md).\n"
    )
    out.append("| Method | Entries | Description |\n|---|---:|---|")
    for m, c in sorted(method_counts.items(), key=lambda kv: (-kv[1], kv[0].lower())):
        out.append(f"| [{m}](docs/by-method.md#{slug(m)}) | {c} | {vocab['methods'][m]} |")
    out.append("")

    out.append("## Related lists\n")
    out.append(config["related"].strip() + "\n")
    out.append("## Contributing\n")
    out.append(config["contributing"].strip() + "\n")
    out.append("## License\n")
    out.append(config["license"].strip() + "\n")
    out.append(
        "<sub>This README is generated from the files in [`data/`](data/) by "
        "[`scripts/build.py`](scripts/build.py). Edit the data, not this file.</sub>\n"
    )
    return "\n".join(out)


def render_by_method(vocab, domains) -> str:
    titles = {d["id"]: d["title"] for d in domains}
    groups = defaultdict(list)
    for d in domains:
        for e in d["entries"]:
            for m in e["methods"]:
                groups[m].append(e)
    out = ["# Applied control, by method\n", "[back to README](../README.md)\n"]
    order = sorted(groups, key=lambda m: m.lower())
    out.append(" · ".join(f"[{m}](#{slug(m)})" for m in order) + "\n")
    for m in order:
        out.append(f"## {m}\n")
        out.append(f"{vocab['methods'][m]}. {len(groups[m])} entries.\n")
        for e in sorted(groups[m], key=sort_key):
            out.append(compact_md(e, titles))
        out.append("")
    return "\n".join(out)


def render_by_org(domains) -> str:
    titles = {d["id"]: d["title"] for d in domains}
    groups = defaultdict(list)
    for d in domains:
        for e in d["entries"]:
            for o in e["org"]:
                groups[o].append(e)
    out = ["# Applied control, by organization\n", "[back to README](../README.md)\n"]
    order = sorted(groups, key=lambda o: o.lower())
    letters = sorted({o[0].upper() for o in order})
    out.append(" · ".join(f"[{l}](#{l.lower()})" for l in letters) + "\n")
    current = None
    for o in order:
        letter = o[0].upper()
        if letter != current:
            out.append(f"## {letter}\n")
            current = letter
        out.append(f"**{o}** ({len(groups[o])})\n")
        for e in sorted(groups[o], key=sort_key):
            out.append(compact_md(e, titles))
        out.append("")
    return "\n".join(out)


def render_explorer(config, vocab, domains) -> str:
    payload = {
        "title": config["title"],
        "domains": [{"id": d["id"], "title": d["title"]} for d in domains if d["entries"]],
        "stages": vocab["stages"],
        "methods": vocab["methods"],
        "entries": [
            {k: e[k] for k in REQUIRED_KEYS + ["domain"]}
            for d in domains
            for e in sorted(d["entries"], key=sort_key)
        ],
    }
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", blob)


def wrap_document(fragment: str) -> str:
    """Turn the explorer fragment (head part, <!--BODY-->, body part) into a standalone page."""
    head, body = fragment.split("<!--BODY-->", 1)
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"{head.strip()}\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated files are out of date")
    ap.add_argument("--fragment", type=Path, help="also write the explorer as an HTML fragment to this path")
    args = ap.parse_args()

    vocab, config, domains = load_all()
    errors = validate(vocab, domains)
    if errors:
        print(f"{len(errors)} validation error(s):", file=sys.stderr)
        for err in errors:
            print("  - " + err, file=sys.stderr)
        return 1

    explorer = render_explorer(config, vocab, domains)
    if args.fragment:
        args.fragment.write_text(explorer.replace("<!--BODY-->", ""), encoding="utf-8")
    outputs = {
        ROOT / "README.md": render_readme(config, vocab, domains),
        DOCS / "by-method.md": render_by_method(vocab, domains),
        DOCS / "by-organization.md": render_by_org(domains),
        DOCS / "index.html": wrap_document(explorer),
    }
    stale = []
    for path, text in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(path.relative_to(ROOT))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    if stale:
        print("Generated files are out of date. Run `python scripts/build.py` and commit:", file=sys.stderr)
        for p in stale:
            print(f"  - {p}", file=sys.stderr)
        return 1

    n = sum(len(d["entries"]) for d in domains)
    print(f"OK: {n} entries validated" + ("" if args.check else ", outputs written"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

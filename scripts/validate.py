#!/usr/bin/env python3
"""Validate the language manifest and its source files."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "languages.json"
GREETING = "Hello, GitHub!"


def main() -> None:
    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise SystemExit("languages.json must contain a non-empty list")

    names = [entry["name"] for entry in entries]
    paths = [entry["path"] for entry in entries]
    if names != sorted(names, key=str.casefold):
        raise SystemExit("languages.json entries must be sorted by name")
    if len(names) != len(set(names)):
        raise SystemExit("language names must be unique")
    if len(paths) != len(set(paths)):
        raise SystemExit("source paths must be unique")

    errors = []
    for entry in entries:
        source = ROOT / entry["path"]
        if not source.is_file():
            errors.append(f"missing: {entry['path']}")
            continue
        content = source.read_text(encoding="utf-8")
        if not content.strip():
            errors.append(f"empty: {entry['path']}")
        elif GREETING not in content:
            errors.append(f"greeting missing: {entry['path']}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(entries)} languages. Every source says: {GREETING}")


if __name__ == "__main__":
    main()

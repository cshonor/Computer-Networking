#!/usr/bin/env python3
"""Insert top_down/ into relative links targeting NN_* chapter folders."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOP_DOWN = ROOT / "top_down"
CHAPTER_RE = re.compile(
    r"((?:\.\./)+)((?:0[1-9]|99)_[A-Za-z0-9_]+)"
)
# Root-relative markdown links: ](01_network_basics/ or ](02_application...
ROOT_LINK_RE = re.compile(
    r"(\]\()((?:0[1-9]|99)_[A-Za-z0-9_]+/)"
)

SKIP_DIRS = {".git", "top_down", "node_modules", ".cursor"}


def fix_content(text: str, *, in_root_readme: bool = False) -> tuple[str, int]:
    n = 0

    def rel_sub(m: re.Match[str]) -> str:
        nonlocal n
        prefix, name = m.group(1), m.group(2)
        if f"top_down/{name}" in text[m.start() : m.start() + 80]:
            return m.group(0)
        n += 1
        return f"{prefix}top_down/{name}"

    out = CHAPTER_RE.sub(rel_sub, text)
    if in_root_readme:
        out2, c2 = out, 0

        def root_sub(m: re.Match[str]) -> str:
            nonlocal c2
            c2 += 1
            return f"{m.group(1)}top_down/{m.group(2)}"

        out2 = ROOT_LINK_RE.sub(root_sub, out)
        return out2, n + c2
    return out, n


def main() -> None:
    total = 0
    files = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in (".md", ".py", ".txt"):
            continue
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        if TOP_DOWN in path.parents and path.is_relative_to(TOP_DOWN):
            # still fix ../NN_ -> ../top_down/NN_ is wrong; ../../NN_ from subsection is ok with CHAPTER_RE
            pass
        text = path.read_text(encoding="utf-8")
        new_text, n = fix_content(
            text, in_root_readme=(path.name == "README.md" and path.parent == ROOT)
        )
        if n and new_text != text:
            path.write_text(new_text, encoding="utf-8")
            total += n
            files += 1
    print(f"updated {files} files, {total} substitutions")


if __name__ == "__main__":
    main()

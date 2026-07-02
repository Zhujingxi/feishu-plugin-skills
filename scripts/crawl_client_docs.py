#!/usr/bin/env python3
"""Refresh the Feishu/Lark client documentation locator for this skill.

This script crawls the official Open Platform documentation directory endpoint,
filters the Developer Guides and Client API roots, and writes an English-only
locator file at references/client-docs-source-catalog.md. It does not mirror the
full documentation text into the skill; it creates a compact source catalog that
future agents can use to open the current official page before implementation.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

DOC_DIRECTORY_API = "https://open.feishu.cn/api/tools/docment/directory_list"
DOC_BASE = "https://open.feishu.cn/document"
ROOT_NAMES = {"\u5f00\u53d1\u6307\u5357": "Developer Guides", "\u5ba2\u6237\u7aef API": "Client API"}
USER_AGENT = "Hermes Feishu skill documentation crawler"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def section_key(full_path: str) -> str:
    parts = [p for p in full_path.split("/") if p]
    known = [
        "platform-overveiw",
        "develop-robots",
        "uMTMuMTMuMTM",
        "docs-add-on",
        "base-extensions",
        "block",
        "development-link-preview",
        "feishu-cards",
        "native-integration",
        "web-app-open-ability",
        "mcp_open_tools",
    ]
    for key in known:
        if key in parts:
            return key
    return parts[-2] if len(parts) > 1 else (parts[0] if parts else "root")


def walk(node: dict, trail: list[str], docs: list[dict]) -> None:
    name = node.get("name", "")
    full_path = node.get("fullPath", "")
    new_trail = trail + [name]
    if node.get("type") == "DocumentType":
        docs.append({"name": name, "fullPath": full_path, "trail": new_trail})
    for child in node.get("items") or []:
        walk(child, new_trail, docs)


def percent_encode_path(path: str) -> str:
    return urllib.parse.quote(path, safe="/-._~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    references = skill_root / "references"
    references.mkdir(parents=True, exist_ok=True)

    payload = fetch_json(DOC_DIRECTORY_API)
    docs: list[dict] = []
    for item in payload.get("data", {}).get("items", []):
        if item.get("name") in ROOT_NAMES:
            walk(item, [], docs)

    lines = [
        "# Feishu/Lark Client Documentation Source Catalog",
        "",
        "Generated from the official Open Platform directory endpoint and markdown page URLs. This file is an English-only locator for agents; it intentionally avoids copying localized page titles. Open the linked official page before implementing exact details.",
        "",
        f"- Directory source: `{DOC_DIRECTORY_API}`",
        "- Starting page checked: `https://open.feishu.cn/document/client-docs/intro`",
        f"- Document pages discovered: {len(docs)}",
        "- Roots indexed: Developer Guides and Client API",
        "",
    ]

    for root_cn, root_en in ROOT_NAMES.items():
        root_docs = [d for d in docs if d["trail"] and d["trail"][0] == root_cn]
        groups: dict[str, list[dict]] = defaultdict(list)
        for doc in root_docs:
            groups[section_key(doc["fullPath"])].append(doc)
        lines.extend([f"## {root_en}", ""])
        for section in sorted(groups):
            lines.extend([f"### `{section}`", ""])
            for doc in sorted(groups[section], key=lambda item: item["fullPath"]):
                encoded = percent_encode_path(doc["fullPath"])
                lines.append(f"- `{encoded}` — {DOC_BASE}{encoded}")
            lines.append("")

    catalog = references / "client-docs-source-catalog.md"
    catalog.write_text("\n".join(lines) + "\n", encoding="utf-8")

    text = catalog.read_text(encoding="utf-8")
    if re.search(r"[\u4e00-\u9fff]", text):
        raise SystemExit("generated catalog contains CJK characters; keep persisted skill artifacts English-only")
    print(f"wrote {catalog} with {len(docs)} document pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

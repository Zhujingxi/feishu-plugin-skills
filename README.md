# Feishu/Lark Plugin Development Skill

Portable SKILL.md-compatible guidance for Feishu/Lark Open Platform and plugin development.

This skill helps an AI coding agent decide whether a task should be implemented as a Feishu/Lark in-client plugin surface or as a server/API automation, then points the agent at the right reference module.

The main `SKILL.md` is intentionally self-contained for OpenCode, Codex, and other coding agents that may not reliably browse Feishu/Lark documentation during a run. Reference files preserve deeper module details, source provenance, and a mirrored copy of official markdown documentation so an agent can classify, scaffold, secure, verify, search, and inspect source docs offline.

## Install with Vercel Skills CLI

This repository is meant to be installed with the open agent skills CLI from `vercel-labs/skills`.

```bash
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development
```

Install globally for a specific agent:

```bash
npx skills add -g Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent codex -y
```

Install for one or more specific supported agents:

```bash
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent claude-code
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent codex
npx skills add -g Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent codex claude-code opencode gemini-cli -y
```

Avoid running a non-interactive global install without `--agent`, such as `npx skills add -g ... -y`. In `skills@1.5.14`, that fallback can target every known agent, including project-only agents such as PromptScript. PromptScript has no global install path, so the CLI may finish with `Failed to install 1` even after installing the skill successfully for the other agents. For PromptScript, use a project-local install instead:

```bash
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent promptscript -y
```

List the skills exposed by this repository without installing:

```bash
npx skills add Zhujingxi/feishu-plugin-skills --list
```

Use the skill without installing it:

```bash
npx skills use Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development
```

The same source can be referenced as a full GitHub URL:

```bash
npx skills add https://github.com/Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development
```

## What is included

- `SKILL.md` — self-contained coding-agent guide with classification workflow, implementation cheat sheets, debugging playbook, and quick guidance.
- `skills.sh.json` — Vercel Skills CLI metadata/grouping for this repository.
- `references/open-platform-docs-overview.md` — organized Feishu/Lark Open Platform full-documentation mirror overview and source anchors.
- `references/open-platform-docs-source-catalog.md` — generated full source locator for the official Open Platform documentation tree, with local mirror paths.
- `references/open-platform-docs-mirror-index.json` — machine-readable source URL to local mirrored markdown lookup.
- `references/open-platform-docs-mirror/` — mirrored official markdown page content for local search and offline access.
- `references/open-platform-fundamentals.md` — app model, credentials, permissions, tokens, events, and Web App basics.
- `references/base-bitable-extensions.md` — Base/Bitable table view, record view, automation action, and `opdev` workflows.
- `references/cloud-docs-and-apis.md` — Docx, Sheets, Drive, Wiki, Bitable REST, import/export, SDK/CLI/MCP workflows.
- `references/client-components.md` — Workplace Blocks, Docs add-ons, document widgets, and client UI surfaces.
- `references/feishu-project-plugins.md` — Feishu Project plugin workflows using `@lark-project/cli` / `lpm`.
- `references/source-provenance.md` — source inventory and known documentation limits.
- `references/verification-checklist.md` — review checklist before shipping Feishu/Lark work.
- `scripts/crawl_client_docs.py` — regenerates the official Open Platform documentation source catalog and local markdown mirror.

## Supported source formats

The Skills CLI accepts all standard source formats for this repository:

```bash
# GitHub shorthand
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development

# Full GitHub URL
npx skills add https://github.com/Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development

# Local checkout
npx skills add . --skill feishu-plugin-development
```

## Local documentation search

The official Feishu/Lark pages are mirrored under `references/open-platform-docs-mirror/` for agents that cannot reliably open external documentation links. Search the mirror instead of loading it wholesale:

```bash
rg -ni "base extension|bitable|opdev|automation action" references/open-platform-docs-mirror references/open-platform-docs-source-catalog.md
rg -ni "h5sdk.config|jsapi_ticket|signature|login" references/open-platform-docs-mirror
rg -ni "docs add-on|document widget|workplace block|block runtime" references/open-platform-docs-mirror references/open-platform-docs-source-catalog.md
python scripts/crawl_client_docs.py --validate
```

Authored skill files stay in English. The generated upstream documentation mirror preserves official source-language content and uses ASCII-safe local paths.

## Updating

Use the Skills CLI update flow, or reinstall from the repository:

```bash
npx skills update feishu-plugin-development
# or
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development -y
```

## Safety notes

- No secrets are included in this repository.
- Do not commit App Secret, tenant tokens, user tokens, refresh tokens, private tenant IDs, or raw PII into this skill.
- Always re-check current Feishu/Lark official docs and Developer Console labels before production implementation.

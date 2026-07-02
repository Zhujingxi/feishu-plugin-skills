# Feishu/Lark Plugin Development Skill

Portable SKILL.md-compatible guidance for Feishu/Lark Open Platform and plugin development.

This skill helps an AI coding agent decide whether a task should be implemented as a Feishu/Lark in-client plugin surface or as a server/API automation, then points the agent at the right reference module.

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

- `SKILL.md` — main routing skill with classification workflow and quick guidance.
- `skills.sh.json` — Vercel Skills CLI metadata/grouping for this repository.
- `references/client-docs-overview.md` — organized Feishu/Lark Developer Guides + Client API crawl overview and source anchors.
- `references/client-docs-source-catalog.md` — generated full source locator for the official client documentation tree.
- `references/open-platform-fundamentals.md` — app model, credentials, permissions, tokens, events, and Web App basics.
- `references/base-bitable-extensions.md` — Base/Bitable table view, record view, automation action, and `opdev` workflows.
- `references/cloud-docs-and-apis.md` — Docx, Sheets, Drive, Wiki, Bitable REST, import/export, SDK/CLI/MCP workflows.
- `references/client-components.md` — Workplace Blocks, Docs add-ons, document widgets, and client UI surfaces.
- `references/feishu-project-plugins.md` — Feishu Project plugin workflows using `@lark-project/cli` / `lpm`.
- `references/source-provenance.md` — source inventory and known documentation limits.
- `references/verification-checklist.md` — review checklist before shipping Feishu/Lark work.
- `scripts/crawl_client_docs.py` — regenerates the official client-docs source catalog.

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

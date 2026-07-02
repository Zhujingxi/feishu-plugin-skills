# Feishu/Lark Plugin Development Skill

Portable SKILL.md-compatible guidance for Feishu/Lark Open Platform and plugin development.

This skill helps an AI coding agent decide whether a task should be implemented as a Feishu/Lark in-client plugin surface or as a server/API automation, then points the agent at the right reference module.

## What is included

- `SKILL.md` — main routing skill with classification workflow and quick guidance.
- `references/open-platform-fundamentals.md` — app model, credentials, scopes, tokens, events, Web App/H5 basics.
- `references/base-bitable-extensions.md` — Base/Bitable table view, record view, automation action, and `opdev` workflows.
- `references/cloud-docs-and-apis.md` — Docx, Sheets, Drive, Wiki, Bitable REST, import/export, SDK/CLI/MCP workflows.
- `references/client-components.md` — Workplace Blocks, Docs add-ons, document widgets, and client UI surfaces.
- `references/feishu-project-plugins.md` — Feishu Project plugin workflows using `@lark-project/cli` / `lpm`.
- `references/source-provenance.md` — source inventory and known documentation limits.
- `references/verification-checklist.md` — review checklist before shipping Feishu/Lark work.

## Quick install for Hermes Agent

Install the whole skill directory, including all reference files:

```bash
curl -fsSL https://raw.githubusercontent.com/Zhujingxi/feishu-plugin-skills/main/install.sh | bash
```

Then start a fresh Hermes session or run:

```text
/reload-skills
/skill feishu-plugin-development
```

You can also start Hermes with the skill preloaded:

```bash
hermes -s feishu-plugin-development
```

## Install into a specific Hermes profile

Set `HERMES_PROFILE` before running the installer:

```bash
HERMES_PROFILE=coder curl -fsSL https://raw.githubusercontent.com/Zhujingxi/feishu-plugin-skills/main/install.sh | bash
```

This installs to:

```text
~/.hermes/profiles/coder/skills/productivity/feishu-plugin-development
```

## Manual install

Clone the repository and copy it into your Hermes skills directory:

```bash
git clone https://github.com/Zhujingxi/feishu-plugin-skills.git
mkdir -p ~/.hermes/skills/productivity
cp -R feishu-plugin-skills ~/.hermes/skills/productivity/feishu-plugin-development
```

If the destination already exists, remove or back it up first.

## Install from a Vercel deployment

This repository includes a tiny Vercel installer endpoint. After deploying the repo to Vercel, users can install with:

```bash
curl -fsSL https://YOUR-VERCEL-DOMAIN.vercel.app/api/install | bash
```

The Vercel endpoint emits a shell installer that downloads the latest `main` branch tarball from GitHub and copies the full skill directory into Hermes.

## Use in another SKILL.md-compatible coding agent

If your agent supports `SKILL.md` directories, copy or clone this repository into that agent's skill directory. Keep the directory structure intact because `SKILL.md` links to files under `references/`.

## Updating

Run the installer again:

```bash
curl -fsSL https://raw.githubusercontent.com/Zhujingxi/feishu-plugin-skills/main/install.sh | bash
```

The installer replaces the existing skill directory atomically enough for normal local use by staging into a temporary directory first.

## Safety notes

- No secrets are included in this repository.
- Do not commit App Secret, tenant tokens, user tokens, refresh tokens, private tenant IDs, or raw PII into this skill.
- Always re-check current Feishu/Lark official docs and Developer Console labels before production implementation.

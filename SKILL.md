---
name: feishu-plugin-development
description: Use when designing, building, debugging, or reviewing Feishu/Lark Open Platform apps, Base/Bitable extensions, cloud document integrations, widgets/blocks, Docs add-ons, or Feishu Project plugins. Separates plugin surfaces from server APIs and provides workflows, commands, permissions, pitfalls, and verification steps.
version: 0.1.0
author: Open Agent Skill
license: MIT
platforms: [macos, linux, windows]
environments: [node, browser, server]
tags: [feishu, lark, open-platform, bitable, base, cloud-docs, plugins, widgets, productivity]
---

# Feishu/Lark Plugin Development

## Overview

Use this portable agent skill to choose and implement the right Feishu/Lark extension path in coding agents such as OpenCode, Codex, Claude Code, Cursor, and other `SKILL.md`-compatible coding agents. It is plain `SKILL.md` content plus local reference files; it does not require any agent-specific runtime APIs. Feishu/Lark uses overlapping terms such as app, plugin, extension, block, widget, add-on, H5 app, Base/Bitable extension, and server API integration. The first job is to classify the requested capability before coding.

Core rule:

- If the user wants an embedded UI inside Feishu/Lark, use the relevant in-client plugin surface: Base/Bitable extension, Workplace Block, Docs add-on/document widget, Web App/H5, message card, or Feishu Project plugin.
- If the user wants automation, import/export, document creation, spreadsheet updates, Bitable CRUD, synchronization, or AI-agent operations without an embedded Feishu UI, use server APIs, the official SDKs, `lark-cli`, or MCP. Do not call that a plugin unless packaging creates an in-client app surface.

How agents should use this skill:

1. Start with the classification checklist and surface decision tree before editing code.
2. Use the module index below to load only the relevant detailed reference for the selected Feishu/Lark surface.
3. Use `references/client-docs-overview.md` when a task touches Feishu/Lark client-side surfaces or when the user asks for official client documentation coverage.
4. Use `references/source-provenance.md` to map important claims to source URLs and known extraction limits.
5. Use `references/verification-checklist.md` before handing off a Feishu/Lark implementation or skill update.

Primary provenance is summarized in `references/source-provenance.md`, with a review checklist in `references/verification-checklist.md`. Detailed implementation notes are split by module under `references/` so OpenCode, Codex, and other coding agents can load the smallest useful context. The original workspace research files are not required at runtime; the actionable workflows below are self-contained for triage, implementation planning, and review.

Browser follow-up extraction recovered the core official Open Platform, Base/Bitable, Cloud Docs, and Bitable API pages listed in `references/source-provenance.md`. Feishu Project, Docs add-on, Workplace Block, and some sample repository details still require live re-checking before production implementation. Always verify exact current API shapes, CLI templates, permissions, and console labels in the official docs or Developer Console before shipping.

## When to Use

Use this skill when the task involves:

- Feishu Open Platform / Lark Open Platform app development.
- Deciding between a self-built app and marketplace/store app.
- Base/Bitable extensions: table view, record view, automation action.
- Cloud Docs, Docx, Sheets, Drive, Wiki, Bitable server APIs.
- Importing/exporting Markdown, DOCX, PDF, XLSX, CSV, or media.
- Workplace Blocks, Docs add-ons, document widgets, or H5 Web Apps.
- Feishu Project plugin development with `@lark-project/cli` / `lpm`.
- Debugging permissions, tokens, BlockTypeID/appId mismatch, upload failures, or release review issues.
- Reviewing whether a proposed implementation is actually a plugin, a widget, a server integration, or a CLI/MCP automation.

## Setup / Prerequisites

Before implementation, confirm the environment and access path. Do this early in OpenCode/Codex sessions so the agent does not scaffold the wrong surface or leak credentials.

Environment requirements:

- Use a project workspace with Node.js and npm available; most Feishu/Lark plugin CLIs scaffold Node/TypeScript projects.
- Have a browser and the Feishu or Lark desktop/web client available for Developer Console setup, login redirects, upload/release checks, and real in-client verification.
- Confirm whether the tenant is Feishu China (`open.feishu.cn`) or Lark international (`open.larksuite.com`); use matching docs, console, CLI login, domains, and package examples.
- Confirm Developer Console access, tenant/admin approval path, target app ownership, and the exact product surface: Base/Bitable, Docs, Workplace, Web App/H5, message cards, Project, or backend-only APIs.
- Record App ID, capability IDs such as BlockTypeID, and required scopes in local docs. Treat App Secret, tenant tokens, user tokens, and refresh tokens as secrets; keep them out of frontend code, logs, commits, and skill files.
- For protected OpenAPI calls, plan a backend over HTTPS. Plugin frontends may call only safe public endpoints directly; token exchange, App Secret usage, and privileged API calls belong server-side.

Toolchain setup:

- Base/Bitable extensions: install `opdev` with `npm install @lark-opdev/cli@latest -g -f`, then run `opdev login` and `opdev whoami` before scaffolding or upload.
- Feishu Project plugins: install `@lark-project/cli` with `npm i -g @lark-project/cli`, use `lpm start` for development and `lpm release` for release.
- Backend/API automations: choose an official SDK, direct HTTP client, optional `lark-cli` (`@larksuite/cli`), or optional OpenAPI MCP server. Do not use these tools as a substitute for an in-client plugin bundle.
- Account selection matters: verify the active CLI account, tenant, app, and environment before `opdev upload`, `lpm release`, or API testing.

Best-practice defaults:

- Start from the generated template for the selected surface; do not copy stale community examples without re-checking current templates and docs.
- Request the smallest scopes that satisfy the task, then also grant resource-level access by sharing the target Docs/Sheets/Base/folders with the app or user.
- Build against disposable test resources first, test as the intended tenant/user, and capture request IDs or screenshots for handoff.
- Prefer progressive disclosure: keep main implementation notes concise, then load only the module reference needed for the selected surface.

## Feishu/Lark Module Index

Use this section as the routing table for coding agents. Keep `SKILL.md` as the general principle, classification checklist, and quick workflow. Load the linked reference only after the target surface is known.

| Module | Use when the task is about | General principle | Detailed reference |
|---|---|---|---|
| Client Documentation Overview | Official client-docs crawl map, Developer Guides and Client API coverage, source anchors | Start here when the task asks for Feishu/Lark client docs completeness or when choosing between H5, Docs add-on, Base, Workplace, cards, and link preview. | `references/client-docs-overview.md`, `references/client-docs-source-catalog.md` |
| Open Platform Fundamentals | App model, self-built vs store apps, credentials, token identity, permissions, events, Web App/H5 basics | An Open Platform app is the capability and permission container; choose distribution, identity, scopes, resource grants, and event transport before coding. | `references/open-platform-fundamentals.md` |
| Base/Bitable Extensions | Table view, record view, automation action, Base UI extensions, `opdev` upload/debug | If the user needs UI or workflow logic inside Base, use a Base extension; if they only need data CRUD, use server APIs instead. | `references/base-bitable-extensions.md` |
| Cloud Docs and Server APIs | Docx, Sheets, Drive, Wiki, Bitable REST, import/export, backend automation, SDK/CLI/MCP operations | Server APIs manipulate resources without creating an embedded Feishu/Lark UI; select token identity and resource grants first. | `references/cloud-docs-and-apis.md` |
| Client Components | Workplace Blocks, Docs add-ons, document widgets, Web App/H5, message-card-adjacent UI | Use client components only when the user needs an in-client product surface; keep secrets and protected OpenAPI calls backend-side. | `references/client-components.md` |
| Feishu Project Plugins | Feishu Project extension points, `lpm`, Project plugin release/debug | Feishu Project plugins are a separate ecosystem; use `@lark-project/cli`/`lpm`, not `opdev`. | `references/feishu-project-plugins.md` |
| Tooling and Verification | CLI choice, examples, MCP, source review, final checks | Prefer official generated templates and current docs; verify in the real tenant/product surface before handoff. | `references/verification-checklist.md`, `references/source-provenance.md` |

## Classification Workflow

Before coding, classify the requested capability. Do not scaffold until these answers are explicit:

1. Is an embedded Feishu/Lark UI required, or is this backend/API automation?
2. Which host product owns the user experience: Base, Docs, Workplace, Web App/H5, message cards, Project, or no client surface?
3. Is the target tenant Feishu China or Lark international?
4. Is this a self-built/internal app or marketplace/store distribution?
5. Which identity should access resources: tenant app, specific user, or store-app flow?
6. Which scopes and resource-level grants are required?
7. Which CLI/template matches the selected surface?
8. What real tenant, app, document/Base/project, and user will verify the result?

## Surface Decision Tree

- Need Base UI?
  - Table-level visualization, dashboards, maps, or print layouts: use a Base table/data table view extension and load `references/base-bitable-extensions.md`.
  - One-record preview or enrichment panel: use a Base record view extension and load `references/base-bitable-extensions.md`.
  - Workflow step without persistent UI: use a Base automation action extension and load `references/base-bitable-extensions.md`.
- Need document-side UI?
  - Use Docs add-on/document widget patterns and load `references/client-components.md`.
- Need workplace tile/dashboard UI?
  - Use Workplace Block/widget patterns and load `references/client-components.md`.
- Need full custom in-client page?
  - Use Web App/H5 inside an Open Platform app and load `references/open-platform-fundamentals.md` plus `references/client-components.md` when frontend container details matter.
- Need Feishu Project extension points?
  - Use Feishu Project plugins with `@lark-project/cli` / `lpm` and load `references/feishu-project-plugins.md`.
- Need no embedded UI?
  - Use Cloud Docs, Sheets, Drive, Bitable REST, SDKs, `lark-cli`, or MCP and load `references/cloud-docs-and-apis.md`.

## Core Principles for All Modules

- Treat Open Platform apps as the permission, capability, release, and credential container.
- Separate in-client plugin surfaces from server APIs. Server APIs do not become plugins unless the package also creates an in-client app surface.
- Keep App Secret, tenant tokens, user tokens, refresh tokens, and privileged OpenAPI calls out of frontend bundles and skill files.
- Use least scopes plus resource-level sharing; a scope alone often does not grant access to user-owned Docs, Sheets, Base, Drive, or Wiki resources.
- Start from current official generated templates and current Developer Console labels. Community examples are useful only after checking freshness.
- Verify CLI login/account/tenant before upload or release.
- Test against disposable real resources in the target tenant before handoff.
- Record request IDs, log IDs, screenshots, exact scopes, and resource grants in project-local notes when debugging or releasing.

## Quick Tooling Map

| Tool | Package | Use for | Reference |
|---|---|---|---|
| `opdev` | `@lark-opdev/cli` | Base/Bitable table view, record view, and automation action extensions | `references/base-bitable-extensions.md` |
| `lpm` | `@lark-project/cli` | Feishu Project plugins | `references/feishu-project-plugins.md` |
| `lark-cli` | `@larksuite/cli` | General Feishu/Lark operations and API automation from terminal/agents | `references/cloud-docs-and-apis.md` |
| Official SDKs | Java, Python, Go, Node | Server-side API integrations and token flows | `references/cloud-docs-and-apis.md` |
| OpenAPI MCP | `larksuite/lark-openapi-mcp` | Exposing Feishu/Lark APIs to MCP-capable AI tools | `references/cloud-docs-and-apis.md` |

## Verification Checklist

A Feishu/Lark implementation or skill update is not ready until the relevant checks pass:

- Re-open official docs or Developer Console for the selected surface and confirm current CLI/template/API names.
- Confirm Feishu China vs Lark international environment and domains.
- Confirm frontmatter stays valid and support files remain under allowed directories such as `references/`, `templates/`, `scripts/`, or `assets/`.
- Confirm no secrets, tokens, private keys, tenant/user identifiers, or raw PII were added to persisted skill artifacts.
- Confirm persisted skill/repo artifacts remain English-only.
- Confirm the main `SKILL.md` remains a routing document: principles, prerequisites, module index, classification, and quick checks only. Put deep module details in `references/`.
- For generic open-agent distribution, verify from the repo root:

```bash
npx --yes skills add . --list
npx --yes skills use . --skill feishu-plugin-development --full-depth
```

Use `references/verification-checklist.md` for the complete review checklist and `references/source-provenance.md` for claim-to-source mapping.

## Installation and Portability

This repository is packaged for the open agent skills ecosystem. The supported install method is the Vercel Skills CLI:

```bash
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development
```

For global installs, specify the target agent explicitly:

```bash
npx skills add -g Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent codex -y
```

Avoid non-interactive global installs without `--agent`, such as `npx skills add -g ... -y`. In `skills@1.5.14`, that fallback can target every known agent, including project-only agents such as PromptScript. PromptScript has no global install path, so the CLI may report `Failed to install 1` even after installing successfully for the other agents. Install PromptScript project-locally instead:

```bash
npx skills add Zhujingxi/feishu-plugin-skills --skill feishu-plugin-development --agent promptscript -y
```

Use `npx skills add Zhujingxi/feishu-plugin-skills --list` to inspect the package without installing. Do not depend on a Hermes-only shell installer; `npx skills` is the supported install path.

## Source Provenance Quick Links

- Use `references/source-provenance.md` for the detailed source inventory and known extraction limitations.
- Use `references/client-docs-overview.md` for the latest organized crawl of official Developer Guides and Client API pages.
- Use `references/client-docs-source-catalog.md` as a generated locator for the full official client documentation tree.
- To refresh the generated catalog, run `python scripts/crawl_client_docs.py` from the skill root and then re-run the verification checklist.
- For generated documentation catalogs, keep the skill as a locator and routing guide, not a full upstream mirror. Preserve complete official URL coverage in `references/client-docs-source-catalog.md`, summarize practical workflows in module references, and send agents back to official pages for exact API parameters.
- Persisted skill artifacts must remain English-only. If upstream paths or titles contain CJK or other non-ASCII text, percent-encode URL/path segments or use escaped string literals in scripts.
- When the touched code has no canonical test suite, create a focused temporary verifier with an OS-safe `tempfile` path under the platform temp directory and a `hermes-verify-` prefix. Verify syntax, generated output invariants, determinism when applicable, English-only persisted output, and `git diff --check`; remove the verifier after the run and report it as ad-hoc verification.
- Use the module-specific reference from the `Feishu/Lark Module Index` instead of loading unrelated material.
- `references/implementation-details.md` remains as a compatibility index for older instructions that expected one implementation-details file.

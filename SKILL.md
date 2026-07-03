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
3. Use `references/open-platform-docs-overview.md` when a task touches Feishu/Lark client-side surfaces or when the user asks for official Open Platform documentation coverage.
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
| Open Platform Documentation Mirror | Official Open Platform documentation crawl map, Developer Guides and full official directory coverage, source anchors | Start here when the task asks for Feishu/Lark Open Platform docs completeness or when choosing between H5, Docs add-on, Base, Workplace, cards, and link preview. | `references/open-platform-docs-overview.md`, `references/open-platform-docs-source-catalog.md` |
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


## OpenCode/Codex Agent Operating Rules

This skill is optimized for coding agents that may not reliably open external links. Treat the local skill files as the working knowledge base, and use the official URLs as source anchors to re-check only when network/browser access is available.

1. Do not start from a blank custom implementation. First classify the surface, then scaffold from the current official CLI/template for that surface.
2. Do not assume every Feishu/Lark task is a plugin. Backend CRUD, import/export, synchronization, and AI-agent document operations are server API integrations unless an in-client UI surface is explicitly built.
3. Prefer local references over live browsing when the agent is blocked by documentation pages. Use this `SKILL.md` for the common path and the module references for deeper details.
4. If exact API parameters, current console labels, or generated template layouts matter, re-check the official docs or Developer Console before final release; the local skill captures best-practice workflow, not every versioned field.
5. Keep secrets out of the repository and out of generated frontend bundles. App Secret, tenant tokens, user tokens, refresh tokens, and private tenant/user IDs belong in environment variables or a backend secret store.
6. Verify with real execution whenever possible: CLI account check, scaffold/build/test command, upload/release command, API request against a disposable resource, or in-client screenshot/recorded result.
7. Record practical handoff facts in project-local docs: chosen surface, tenant domain, app/capability IDs, scopes, resource grants, request IDs/log IDs, test resource, and remaining manual console steps. Do not record secrets.

If the user's request is ambiguous, make the smallest safe assumption only for exploration. For implementation, stop and ask for the missing tenant/app/resource decision rather than building the wrong surface.

## Self-Contained Implementation Cheat Sheets

Use these condensed workflows when a coding agent cannot or should not fetch external pages. Load the module reference for the selected surface when more detail is needed.

### Open Platform app and permissions

- The Open Platform app is the top-level container for credentials, capabilities, permissions, releases, bots, events, Web App/H5, blocks/widgets, link preview, and plugin surfaces.
- Choose distribution early: self-built/internal app for one tenant; marketplace/store app for public multi-tenant distribution. Store apps have stricter review and capability caveats.
- Token identity controls resource visibility:
  - `tenant_access_token`: app identity in a tenant; good for backend automation, app-owned cloud space, bot-added documents, and resources shared with the app.
  - `user_access_token`: a specific user identity; good for user-owned resources and collaborator permissions.
  - `app_access_token`: store-app management flows.
- Permissions have two layers: Developer Console scopes and resource-level grants. A scope alone often cannot access a user-owned Docs/Sheets/Base resource.
- For tenant-token access to user documents, enable Bot capability and have the owner add/share the app on the target document/Base/folder with the needed permission.
- Permission error `99991672` often includes `permission_violations`; inspect it to find missing scopes.
- Capture Feishu error payloads and the `X-Tt-Logid` response header when debugging API calls.

### Base/Bitable extensions

Use Base/Bitable extensions only when the user needs UI or workflow logic inside Base. Use server APIs for backend data CRUD without embedded UI.

- Table/Data Table View: table-level visualization, dashboards, maps, print layouts.
- Record View: one-record previews, enrichment panels, order/contract summaries.
- Automation Action: workflow execution without persistent UI, such as OCR, AI extraction, enrichment, external API calls, and notifications.

Toolchain and scaffold:

```bash
npm install @lark-opdev/cli@latest -g -f
opdev login
opdev whoami
opdev create ${app_dir}/${view_dir} -a bitable-extensions -s table-view
opdev create ${app_dir}/${view_dir} -a bitable-extensions -s record-view
opdev create ${app_dir}/${action_dir} -a bitable-extensions -s automated-action
cd ${app_dir}/${view_or_action_dir}
npm install
npm run start      # UI debugging when provided
npm run test       # automation action execute() simulation when provided
npm run upload     # or opdev upload ./dist
```

Critical files and pitfalls:

- `app.json` must contain the correct app ID.
- `block.json` must contain the exact capability-specific `blockTypeID`. Table view, record view, and automation action IDs are not interchangeable.
- Confirm CLI account, tenant, and environment with `opdev whoami` before upload.
- Configure server/domain allowlists before network calls.
- Typical SDK package for UI extensions: `@lark-opdev/block-bitable-api`.
- Automation actions use `@lark-opdev/block-basekit-server-api`, register via `basekit.addAction()`, implement `execute(args, context)`, and must return a value matching `resultType`.
- Automation actions should use `context.fetch` for external HTTP calls; avoid axios/got in the sandbox. Known sandbox-sensitive packages include axios, got, bcrypt, moment, jsdom, and sharp.
- Extracted sandbox limits include under 1 GB memory and request concurrency at most 400; verify current limits before production.
- Upload is not enough: select the uploaded block version in Developer Console, fill icon/name/description/localization, create an app version, submit release/review, then verify in a real Base.

### Cloud Docs, Sheets, Drive, Wiki, and Bitable server APIs

Use server APIs when the deliverable manipulates resources but does not require embedded Feishu/Lark UI.

Common identifiers:

- Drive folder/file: `folder_token`, `file_token`, `root_token`.
- Docx: `document_id`; legacy docs may use `doc_token`.
- Sheets: `spreadsheet_token`, `sheet_id`, ranges such as `Sheet1!A1:D10`.
- Bitable/Base: `app_token`, `table_id`, `view_id`, `record_id`, `field_id`.
- Wiki: `space_id`, `node_token`, `obj_token`; wiki pages may require resolving the underlying resource token.

Common endpoint families:

- Docx: create document, list blocks, create child blocks, update blocks, batch-delete child blocks.
- Sheets: create spreadsheet, get metadata, query sheets, read/write ranges, batch update ranges.
- Bitable: create app, list/create tables, list/create fields, query/search/list records, create/update/delete records, batch operations.
- Drive: create folder/document, upload/download, file metadata, list folder children, copy/move/delete, import/export tasks.

Implementation rules:

1. Parse the resource token from the URL and classify the product.
2. Decide `tenant_access_token` vs `user_access_token`.
3. Apply minimal scopes and configure resource-level access.
4. Use official SDKs or direct HTTP with token caching, retry/backoff, pagination, and async polling.
5. Prefer Query Records over historical List Records for Bitable filtering/search when it satisfies the task.
6. Serialize writes to the same Bitable table; same-table concurrent writes can trigger conflict/readiness errors.
7. Use uuidv4 `client_token` idempotency keys for retried create-record calls.
8. Upload media/material before referencing attachment fields.
9. Import/export cloud documents through async import/export tasks; do not treat online documents as ordinary downloadable Drive files.
10. Log request IDs/error payloads and verify on a disposable real resource.

Known extracted constraints to re-check against current docs: Create Bitable app around 20 requests/minute; create record around 50 requests/second; list/query records page size up to 500; same table writes should not be concurrent; batch add up to 500 records; Bitable table plus dashboard count around 100, views around 200, records around 20,000.

### Web App/H5 and client components

Use client components only when the user needs an in-client product surface.

- Web App/H5: full custom page inside Feishu/Lark; serve over HTTPS; configure homepage/redirect URLs; implement JSAPI signature and login-free identity exchange through backend when needed.
- Docs add-on/cloud document widget: document-side UI, slash/menu/floating/modal/embedded flows; configure `app.json`, security/domain allowlists, document-bound or backend storage, and Docs add-on client APIs.
- Workplace Block: workbench tile/dashboard/quick action; use official block tools and framework structure; verify lifecycle, refresh, storage, network, navigation, and open abilities in the real client.
- Link Preview: rich preview for pasted/opened URLs; implement server-side callback verification and avoid leaking private data.
- Feishu Cards/CardKit: interactive messages in chat/bot notifications; choose CardKit/template builder or direct card JSON; configure callbacks for buttons/forms/selectors; test rendering across theme/language/screen size.
- Legacy Gadget/Mini Program material should be avoided for new development unless explicitly maintaining existing code.

Client-surface security rules:

- Client bundles can use safe client/container APIs, but protected OpenAPI calls and token exchange must go through a backend over HTTPS.
- JSAPI availability differs by H5, Docs add-on, Base extension, Workplace Block, client version, and tenant. If an API is undefined, first verify the host surface and capability.
- Local browser success is not enough; verify inside the Feishu/Lark client.

### Feishu Project plugins

Feishu Project plugins are separate from Open Platform/Base extensions. Use `@lark-project/cli` / `lpm`, not `opdev`.

Common extension points include detail pages, navigation pages, list/table views, table column widgets, form or node widgets, field types, node scheduling, plugin config pages, action buttons, event listeners/interceptors, automation triggers/actions, and MCP server integration for AI Agent services.

Workflow:

```bash
npm i -g @lark-project/cli
lpm start
# build and debug in the real Project client
lpm release
```

Before `lpm start`, enable local debugging in the Feishu Project plugin detail page. Route protected Project OpenAPI calls through a backend, use HTTPS for external APIs, and verify the released version in the real Feishu Project client.


## Local Documentation Search Workflow

The mirrored official docs are stored locally so coding agents do not need to rely on opening Feishu/Lark links during implementation. Do not load the whole mirror into context. Search first, then read only the relevant pages.

Recommended searches from the skill root:

```bash
rg -ni "h5sdk.config|jsapi_ticket|signature|login" references/open-platform-docs-mirror
rg -ni "base extension|bitable|table view|record view|automation action|opdev" references/open-platform-docs-mirror references/open-platform-docs-source-catalog.md
rg -ni "docs add-on|document widget|selection|viewport|bridge" references/open-platform-docs-mirror references/open-platform-docs-source-catalog.md
rg -ni "workplace block|block runtime|open capability|storage|navigation" references/open-platform-docs-mirror references/open-platform-docs-source-catalog.md
```

Use `references/open-platform-docs-mirror-index.json` when you need source URL to local-file lookup. Use `references/open-platform-docs-overview.md` for search aliases and the surface map.

## Debugging Playbook

- Wrong surface: if the work is just CRUD/import/export/sync, switch to server APIs. If a persistent in-client UI is required, pick Base, Docs, Workplace, H5, Cards, Link Preview, or Project explicitly.
- Permission denied: check scopes, approval state, token identity, resource sharing, advanced permissions, and whether the app/bot has been added to the target document/Base/folder.
- CLI upload/release fails: check active account/tenant/environment, app ID, capability ID, semantic version, icon/name/localization metadata, and console release requirements.
- Base automation fails at runtime: check sandbox packages, use `context.fetch`, validate `resultType`, return shape, i18n keys, and declared permissions.
- JSAPI/client API undefined: check host surface, capability enablement, domain/security allowlist, client version, and whether the API is H5-only, Docs-add-on-only, Base-only, or Block-only.
- API data mismatch: log Feishu error body and `X-Tt-Logid`; inspect token identity and resource token type; for Wiki resources, resolve object tokens as needed.
- Local works but client fails: check HTTPS, CSP/domain allowlist, mixed content, client version, target tenant, and real resource permissions.

## Verification Checklist

A Feishu/Lark implementation or skill update is not ready until the relevant checks pass:

- Re-open official docs or Developer Console for the selected surface and confirm current CLI/template/API names.
- Confirm Feishu China vs Lark international environment and domains.
- Confirm frontmatter stays valid and support files remain under allowed directories such as `references/`, `templates/`, `scripts/`, or `assets/`.
- Confirm no secrets, tokens, private keys, tenant/user identifiers, or raw PII were added to persisted skill artifacts.
- Confirm authored skill/repo guidance remains English-only; generated upstream documentation mirrors may preserve the source language and must stay under `references/open-platform-docs-mirror/`.
- Confirm the main `SKILL.md` remains a self-contained coding-agent guide: principles, prerequisites, classification, common workflows, and quick checks. Put exhaustive catalogs, mirrored upstream docs, and long source inventories in `references/`.
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
- Use `references/open-platform-docs-overview.md` for the latest organized crawl of official all official directory roots.
- Use `references/open-platform-docs-source-catalog.md` to map official pages to mirrored local markdown files.
- Use `references/open-platform-docs-mirror-index.json` for machine-readable source URL -> local file lookup.
- Use `references/open-platform-docs-mirror/` for mirrored official markdown page content when live documentation access is unreliable. Search it narrowly with `rg` first, then read only the matching files needed for the task.
- To refresh the generated catalog and mirror, run `python scripts/crawl_client_docs.py` from the skill root and then re-run the verification checklist.
- The mirror stores official page content for local search/access. Still re-check live docs before production release when exact current API parameters, CLI templates, or console labels are high-risk.
- Authored skill artifacts must remain English-only. Generated upstream documentation mirrors may preserve source-language content under `references/open-platform-docs-mirror/`; generated catalogs and scripts should keep ASCII-safe paths and English headings.
- When the touched code has no canonical test suite, create a focused temporary verifier with an OS-safe `tempfile` path under the platform temp directory and a `hermes-verify-` prefix. Run it against the changed behavior, not just the happy-path CLI. For `scripts/crawl_client_docs.py`, verify `normalize_markdown()` whitespace behavior, `validate_mirror()` on a minimal fixture, `python -m py_compile scripts/crawl_client_docs.py`, `python scripts/crawl_client_docs.py --validate`, and `git diff --check`. Remove the verifier after the run and report it explicitly as ad-hoc verification, not suite green.
- Use the module-specific reference from the `Feishu/Lark Module Index` instead of loading unrelated material.
- `references/implementation-details.md` remains as a compatibility index for older instructions that expected one implementation-details file.

# Feishu/Lark Module 4: Widgets, Blocks, Docs Add-ons, and Client Components

This reference contains the detailed documentation for `Module 4: Widgets, Blocks, Docs Add-ons, and Client Components`. The main `SKILL.md` is the general principle and routing index; load this file only when the selected task needs these deeper implementation details.

## Module 4: Widgets, Blocks, Docs Add-ons, and Client Components

Feishu/Lark client components are frontend extensions hosted inside product surfaces. They are distinct from server APIs and from full standalone H5 apps.

### Surface selection

| Need | Recommended surface |
|---|---|
| Full page custom app in Feishu client | Web App / H5 |
| Small workplace dashboard or information tile | Workplace Block / Workplace Widget |
| Component launched from or embedded in document context | Docs Add-on / Document Widget |
| Custom UI for one Base record | Base Record View |
| Custom visualization over a Base table | Base Table View Extension |
| Background automation in Base | Base Automation Action Extension |
| Backend-only document/Base/Drive automation | Server APIs / SDK / CLI / MCP |
| Project management product extension | Feishu Project plugin |

Provenance: `sources/widgets-blocks.md`; docs including Workplace Block `https://open.feishu.cn/document/client-docs/block/hosting-scenario-introduction/workplace?lang=zh-CN`, Docs add-on intro `https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/docs-add-on/docs-add-on-introduction?from=home`, and Feishu document-widget help center pages.

### Workplace Blocks

A Workplace Block is a lightweight information unit integrated into the workplace/workbench. Use it for dashboards, KPIs, status widgets, quick actions, and embedded enterprise entrypoints.

Treat it as an app capability: configure metadata, add capability in Developer Console, build a frontend component, connect backend services as needed, submit release/review, and test in the real Feishu/Lark client.

Implementation details for workplace block manifest/runtime should be checked in current official docs before coding because public extracted detail was limited.

### Docs Add-ons / Document Widgets

Docs add-ons and document widgets are document-side UI capabilities. User-facing help docs mention entry points through document menus, plus commands, and slash commands. Example use cases include formatting helpers, Mermaid/text drawing, timelines, navigation, terminology, translation, or project-management panels.

Use Docx/Drive server APIs when no embedded document UI is needed. Use Docs add-on/widget only when the user needs an in-document UI component or interactive workflow.

Implementation-specific SDK/runtime details should be verified against official Lark Docs add-on docs before coding.

### Security for client components

- Never place App Secret or long-lived tokens in frontend bundles.
- Protected OpenAPI calls should go through backend services or official token flows.
- Use HTTPS for external API calls to avoid mixed-content blocking.
- Keep scopes minimal but sufficient.
- Test as a real user with the target tenant/resource permissions.

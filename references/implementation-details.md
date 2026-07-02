# Feishu/Lark Implementation Details Index

This file is a compatibility index. The main `SKILL.md` now serves as the general principle and module router; detailed material is split by Feishu/Lark surface so coding agents can load only the reference they need.

## Module References

| Need | Load |
|---|---|
| Open Platform app model, credentials, tokens, permissions, events, Web App/H5 basics | `references/open-platform-fundamentals.md` |
| Base/Bitable table view, record view, automation action extensions and `opdev` workflows | `references/base-bitable-extensions.md` |
| Cloud Docs, Docx, Sheets, Drive, Wiki, Bitable REST APIs, import/export, server integrations | `references/cloud-docs-and-apis.md` |
| Workplace Blocks, Docs add-ons, document widgets, Web App/H5 client-component security | `references/client-components.md` |
| Feishu Project plugins, `lpm`, extension points, release workflow, Project-specific pitfalls | `references/feishu-project-plugins.md` |

Use `references/source-provenance.md` for source URLs and known extraction gaps. Use `references/verification-checklist.md` before handoff.

# Source Provenance for `feishu-plugin-development`

This file records the sources used to synthesize the skill. Local workspace notes are the immediate provenance; official URLs are listed so future maintainers can re-check details.

## Workspace research files

- `WORKPLAN.md`
- `SOURCE_INDEX.md`
- `sources/platform-fundamentals.md`
- `sources/platform-fundamentals-sources.txt`
- `sources/bitable-extensions.md`
- `sources/bitable-extensions-sources.txt`
- `sources/cloud-docs-apis.md`
- `sources/cloud-docs-apis-sources.txt`
- `sources/widgets-blocks.md`
- `sources/widgets-blocks-sources.txt`
- `sources/tutorials-project.md`
- `sources/tutorials-project-sources.txt`
- `sources/supplemental-record-view-blocks.md`
- `sources/supplemental-record-view-blocks-sources.txt`
- `sources/supplemental-project-plugin.md`
- `sources/supplemental-project-plugin-sources.txt`
- `sources/browser-extracted-official-docs.md`
- Browser follow-up extracts under `browser-extracts/*.md`
- Seed extraction files under `sources/seed-*.md`

## 2026-07 client documentation crawl

A refreshed crawl started from `https://open.feishu.cn/document/client-docs/intro` and used the official documentation directory endpoint `https://open.feishu.cn/api/tools/docment/directory_list`. The crawler now stores mirrored official markdown content inside the skill for local query/access by coding agents.

Generated skill references:

- `references/client-docs-overview.md` — organized English overview of the Feishu/Lark Developer Guides and Client API roots, including official source anchors and routing guidance.
- `references/client-docs-source-catalog.md` — generated full locator for the official client documentation tree. It indexes 1,805 discovered document pages under Developer Guides and Client API roots and maps them to local mirror files.
- `references/client-docs-mirror-index.json` — generated machine-readable index mapping official source URLs and markdown source URLs to local mirror paths.
- `references/client-docs-mirror/` — generated mirror of official markdown page content. The latest run mirrored 1,793 pages; 12 directory entries returned markdown 404 responses.

The crawl showed that client-side/plugin work spans Web App/H5, Docs add-ons, Base/Bitable extensions, Workplace Blocks, link preview, Feishu Cards/CardKit, Client APIs, developer tools, and deprecated Gadget/Mini Program material. Deprecated/historical pages remain in the catalog for discoverability but should not be used for new development unless the user explicitly requests legacy maintenance.

## Browser-extracted official docs

The follow-up browser extraction recovered official page content that normal extraction previously missed. Local files:

- `browser-extracts/platform-overview.md` — Open Platform application types and capabilities.
- `browser-extracts/base-extension-introduction.md` — Base/Bitable OpenAPI vs plugin overview, concepts, and plugin types.
- `browser-extracts/base-table-view-extension.md` and `browser-extracts/lark-base-table-view-extension.md` — table/data-table view extension flow.
- `browser-extracts/base-record-view-extension.md` and `browser-extracts/lark-base-record-view-extension.md` — record view extension flow.
- `browser-extracts/base-automation-extension.md` and `browser-extracts/lark-base-automation-extension.md` — automation action flow, sandbox restrictions, permissions, and i18n.
- `browser-extracts/docs-overview.md` — Cloud Docs resource model and access flow.
- `browser-extracts/api-create-bitable.md` — Bitable app creation endpoint details.
- `browser-extracts/api-list-records.md` — historical list-records endpoint, parameters, limits, and Query Records recommendation.
- `browser-extracts/api-create-record.md` — create-record endpoint fields, idempotency, errors, and constraints.

The four `browser-extracts/github_*README*.md` files only contain `404: Not Found` and were not used as factual sources.

## Official Feishu/Lark Open Platform sources

Open Platform fundamentals:

- https://open.feishu.cn/document/platform-overveiw/overview
- https://open.feishu.cn/document/home/app-types-introduction/self-built-apps-and-store-apps
- https://open.feishu.cn/document/client-docs/intro?lang=zh-CN
- https://open.feishu.cn/document/server-docs/api-call-guide/calling-process/get-access-token
- https://open.feishu.cn/document/server-docs/event-subscription-guide/overview
- https://open.feishu.cn/document/server-docs/api-call-guide/generic-error-code
- https://open.feishu.cn/document/faq/trouble-shooting/how-to-fix-the-99991672-error

Base/Bitable extensions:

- https://open.feishu.cn/document/base-extensions/base-extension-introduction?lang=zh-CN
- https://open.feishu.cn/document/base-extensions/base-table-view-extension-development-guide?lang=zh-CN
- https://open.feishu.cn/document/base-extensions/base-automation-extension-development-guide?lang=zh-CN
- https://open.feishu.cn/document/base-extensions/base-record-view-extension-development-guide?lang=zh-CN
- https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/base-extensions/base-view-extensions/base-table-view-extension-development-guide
- https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/base-extensions/base-automation-extensions/base-automation-extension-development-guide
- https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/base-extensions/base-automation-extensions/base-record-view-extension-development-guide
- https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/base-extensions/base-extension-introduction?from=home
- https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/base-extensions/faq

Cloud Docs, Sheets, Drive, and Bitable APIs:

- https://open.feishu.cn/document/server-docs/docs/docs-overview
- https://open.larksuite.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/docs-overview
- https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/docx-overview
- https://open.larksuite.com/document/server-docs/docs/sheets-v3/guide/overview
- https://open.feishu.cn/document/server-docs/docs/bitable-v1/bitable-overview
- https://open.larksuite.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/bitable-overview
- https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/upload_all
- https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/import_task/import-user-guide
- https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/export_task/create
- https://open.feishu.cn/document/server-docs/docs/permission/overview

Widgets, Blocks, and Docs add-ons:

- https://open.feishu.cn/document/client-docs/block/hosting-scenario-introduction/workplace?lang=zh-CN
- https://open.feishu.cn/document/client-docs/block/hosting-scenario-introduction/workplace
- https://open.larksuite.com/document/uAjLw4CM/uYjL24iN/docs-add-on/docs-add-on-introduction?from=home
- https://www.feishu.cn/hc/zh-CN/articles/799229201268-%E6%96%87%E6%A1%A3%E5%B0%8F%E7%BB%84%E4%BB%B6%E7%AE%80%E4%BB%8B
- https://open.larksuite.com/document/home/introduction-to-custom-app-development/self-built-application-development-process
- https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/platform-overveiw/develop-process/multi-lingual-app-details

Feishu Project plugins:

- https://project.feishu.cn/b/helpcenter/1p8d7djs/hscnld90
- https://project.feishu.cn/b/helpcenter/1p8d7djs/nh4exbsn
- https://project.feishu.cn/b/helpcenter/1p8d7djs/49k1ojm9
- https://project.feishu.cn/b/helpcenter/1p8d7djs/41jvuw3r
- https://project.feishu.cn/b/helpcenter/1p8d7djs/zeyhwyhg
- https://project.feishu.cn/b/helpcenter/1p8d7djs/aa6btca8
- https://project.feishu.cn/b/helpcenter/1p8d7djs/4bsmoql6

Tooling, examples, and tutorials:

- https://open.feishu.cn/document/no_class/feishu-developer-tool---command-line
- https://open.larksuite.com/document/uYjL24iN/uEzMzUjLxMzM14SMzMTN/ide-with-commands
- https://www.feishu.cn/feishu-cli
- https://open.feishu.cn/document/mcp_open_tools/feishu-cli-let-ai-actually-do-your-work-in-feishu
- https://github.com/larksuite/cli
- https://github.com/larksuite/lark-openapi-mcp
- https://github.com/larksuite/openclaw-lark
- https://github.com/go-lark/lark
- https://github.com/Ocyss/FeishuPlugin
- https://juejin.cn/post/7599964577901019136
- https://juejin.cn/post/7368320489889726500

## Known provenance limitations

- Follow-up browser extraction recovered the core Open Platform overview, Base/Bitable extension guides, Cloud Docs overview, and selected Bitable API references.
- GitHub sample README browser fetches returned `404: Not Found`; use official templates generated by `opdev` before relying on sample code.
- Project plugin, Docs add-on, and Workplace Block implementation details still rely partly on earlier source notes and should be re-opened live before coding.
- The skill intentionally marks Docs add-on and Workplace Block runtime details as verify-before-coding areas.
- CLI template structures and SDK method names may change across `@lark-opdev/cli`, `@lark-project/cli`, and generated scaffold versions.

# Feishu/Lark Client Documentation Overview

This reference organizes the official Feishu/Lark client-side documentation that starts from `https://open.feishu.cn/document/client-docs/intro`. It is an agent routing guide plus pointers into the local mirrored markdown documentation. For exact parameter names, SDK versions, UI labels, and release rules, search `references/client-docs-mirror/`, use `references/client-docs-source-catalog.md`, and re-open the live official source when production freshness matters.

## Crawl coverage

The current refresh used the official Open Platform documentation directory endpoint:

- Directory API: `https://open.feishu.cn/api/tools/docment/directory_list`
- Seed page: `https://open.feishu.cn/document/client-docs/intro`
- Indexed roots: Developer Guides and Client API
- Pages discovered in those roots: 1,805
- Markdown pages mirrored locally: 1,793
- Pages that failed during the latest crawl: 12
- Full generated index: `references/client-docs-source-catalog.md`
- Machine-readable mirror index: `references/client-docs-mirror-index.json`
- Mirrored markdown root: `references/client-docs-mirror/`

The official directory uses opaque historical paths such as `/uAjLw4CM/...`; the visible English/Chinese site route may show `client-docs/...`. Prefer the official URL from the catalog, then use the `.md` variant when extracting clean markdown.

## Top-level areas discovered

Developer Guides are not limited to one plugin type. They include these important areas:

- Platform introduction and app types.
- Development process, release, versioning, permissions, app review, and multilingual app metadata.
- Bot development and custom bot behavior.
- Web App/H5 development and open capabilities.
- Mini Program/Gadget development, marked not recommended in the current docs.
- Docs add-ons / cloud document widgets.
- Base/Bitable extensions.
- Workplace Blocks / workplace widgets.
- Link preview development.
- Feishu Cards and CardKit/card JSON.
- Native integration and web components.
- Developer tools, FAQs, platform notices, and management norms.

Client API roots include:

- Web App / Mini Program API: H5 JSAPI overview, auth, login, user info, chat, contact picker, settings, share, authorization, launch options, password/device verification, watermark, mail, web-view message bridge, app badge, UI, navigation, network, geolocation, local storage, files, media, canvas, update, performance, and device APIs.
- Docs add-on API: bridge/container behavior, lifecycle, base data structures, block and document APIs, selection/range, user info, collaboration, storage, and event APIs.
- Base/Bitable extension API: table/view/record/field APIs, events, UI bridge, selection/context, permission helpers, and automation-extension server APIs.
- Workplace Block API: block lifecycle, runtime, storage/network, UI, navigation, and open capability APIs.
- Mini Program base components and historical API versions, both marked not recommended where the official tree says so.

## Surface map for plugin work

| Surface | Official guide area | Client API area | Use when | Avoid when |
|---|---|---|---|---|
| Bot | Developer Guides > Develop Bots | Server events/OpenAPI, card callbacks | Conversation UX, notifications, group operations, event replies | You need embedded document/Base UI |
| Web App / H5 | Developer Guides > Develop Web Apps | Client API > Web App / Mini Program API | Full-page app in Feishu/Lark client, JSAPI, login-free identity, navigation/container APIs | You only need backend data automation |
| Docs add-on / cloud document widget | Developer Guides > Develop Docs Add-ons | Client API > Docs Add-on | UI inside Docs, Sheets, or document context, document block interaction | You only need to create/edit docs via API |
| Base/Bitable extension | Developer Guides > Develop Base Extensions | Client API > Base/Bitable Extension | Table view, record view, or automation action inside Base | You only need Bitable CRUD/import/export |
| Workplace Block | Developer Guides > Develop Workplace Blocks | Client API > Workplace Block | Workplace dashboard tile/widget or quick action block | A full H5 app is needed |
| Link Preview | Developer Guides > Development link preview | Callback/API pages under that guide | Rich previews for pasted links and URL unfurl workflows | You only send ordinary messages/cards |
| Feishu Card / CardKit | Developer Guides > Feishu Cards | Server callbacks plus card JSON/CardKit docs | Interactive message/card surfaces in chats, bots, notifications | You need persistent app UI |
| Gadget/Mini Program | Developer Guides > Develop Gadgets (Not Recommended) | Historical Mini Program APIs | Legacy maintenance only | New development; use H5 or supported surfaces instead |

## Recommended investigation workflow

1. Classify the requested user experience by host product: chat, H5 app, Docs, Base, Workplace, link preview, card, or backend-only.
2. Search the matching guide area in `references/client-docs-source-catalog.md` or `references/client-docs-mirror/`.
3. Load only the matching module reference:
   - Base extension: `references/base-bitable-extensions.md`
   - Client surfaces: `references/client-components.md`
   - Open Platform app/auth/release: `references/open-platform-fundamentals.md`
   - Server Docs/API automation: `references/cloud-docs-and-apis.md`
4. Use the mirrored markdown for local lookup, then verify exact CLI package, generated template structure, app capability name, permission scope, and source domain in live official docs before production release.
5. For every frontend/plugin surface, draw a hard line between client bundle and backend: app secrets, token exchange, privileged OpenAPI calls, and long-lived tokens stay backend-side.
6. Verify in a real tenant and product surface before handing off.


## Local search recipes for coding agents

Use the mirrored markdown as a local documentation store, not as a blob to load all at once. Start with a narrow text search, then read only the best one to three matching files. Examples from the repository root:

```bash
# H5 JSAPI authentication and signatures
rg -ni "h5sdk.config|jsapi_ticket|signature|tenant_access_token|user_access_token" references/client-docs-mirror

# Base/Bitable extensions and automation actions
rg -ni "base extension|bitable|table view|record view|automation action|opdev|basekit" references/client-docs-mirror references/client-docs-source-catalog.md

# Docs add-on and document widget APIs
rg -ni "docs add-on|document widget|block.insertBlock|selection|viewport|bridge" references/client-docs-mirror references/client-docs-source-catalog.md

# Workplace Block and block runtime APIs
rg -ni "workplace block|hosting scenario|block runtime|block api|storage|navigation" references/client-docs-mirror references/client-docs-source-catalog.md

# Locate a local mirror file from an official URL or source fragment
python - <<'PY'
import json
from pathlib import Path
needle = "base-table-view-extension-development-guide"
idx = json.loads(Path("references/client-docs-mirror-index.json").read_text())
for page in idx["pages"]:
    if needle.lower() in (page["source"] + " " + page["path"]).lower():
        print(page["source"], "->", "references/" + page["path"])
PY
```

Search alias hints:

- Base/Bitable extension: `Base`, `Bitable`, `base extension`, `bitable extension`, `table view`, `record view`, `automation action`, `opdev`, `basekit`.
- Docs add-on/document widget: `Docs add-on`, `document widget`, `cloud document block`, `block`, `selection`, `viewport`, `bridge`.
- Workplace Block/widget: `Workplace Block`, `workplace widget`, `hosting scenario`, `block runtime`, `open capability`, `storage`, `navigation`.
- Web App/H5: `H5`, `Web App`, `JSAPI`, `h5sdk.config`, `login`, `signature`, `jsapi_ticket`, `config`.
- Cards and link preview: `CardKit`, `card JSON`, `message card`, `link preview`, `callback`, `template`.

If the user uses Feishu or Lark product terms in another language, search both the English surface name above and the exact product/API identifier from the user's code or error message. The local mirror preserves official source language, while authored skill guidance stays in English.

## Official source anchors

Use these anchors to start a focused re-check:

- Open Platform overview: `https://open.feishu.cn/document/home/intro`
- App types and capabilities: `https://open.feishu.cn/document/home/app-types-introduction/overview`
- Self-built app development process: `https://open.feishu.cn/document/home/introduction-to-custom-app-development/self-built-application-development-process`
- Web App overview: `https://open.feishu.cn/document/uYjL24iN/uMTMuMTMuMTM/introduction`
- H5 JSAPI overview: `https://open.feishu.cn/document/uYjL24iN/uMTMuMTMuMTM/`
- Docs add-on overview: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/docs-add-on-introduction`
- Docs add-on app.json configuration: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/03-cloud-doc-block-rapid-development-guide/appjson-configuration-instructions`
- Docs add-on security configuration: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/08-cloud-doc-block-security-configuration/cloud-doc-block-security-configuration`
- Docs add-on data storage: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/04-cloud-doc-block-data-storage/04-cloud-doc-block-data-storage`
- Base/Bitable extension overview: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/base-extensions/base-extension-introduction`
- Base table view extension guide: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/base-extensions/base-view-extensions/base-table-view-extension-development-guide`
- Base record view extension guide: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/base-extensions/base-automation-extensions/base-record-view-extension-development-guide`
- Base automation extension guide: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/base-extensions/base-automation-extensions/base-automation-extension-development-guide`
- Workplace Block overview: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/guide/hosting-scenario-introduction/workplace`
- Workplace Block quick start: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/quick-start`
- Workplace Block development tools: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/devtools`
- Link preview guide: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/development-link-preview/link-preview-development-guide`
- Feishu Card overview: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/feishu-card-overview`

## Notes for agents

- Treat the catalog as a locator and the mirror as the searchable local documentation store. Do not load the whole catalog or mirror unless you are searching for a specific page.
- The official docs expose `.md` pages for many URLs; the mirror stores those markdown pages under ASCII-safe paths.
- The directory contains not-recommended and historical sections. Do not scaffold new Mini Program/Gadget or historical card work unless the user explicitly asks for legacy maintenance.
- If a page has both Feishu and Lark variants, use the variant matching the tenant and console domain.
- Names drift: Base/Bitable, Block/widget, Docs add-on/document widget, and Card/CardKit may vary by locale and product generation. Confirm labels in the target Developer Console.

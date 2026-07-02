# Feishu/Lark Module 4: Client Components and In-Client Plugin Surfaces

This reference covers the Feishu/Lark surfaces that run inside the client or inside a host product: Web App/H5, Docs add-ons/cloud document widgets, Workplace Blocks, link preview, and Feishu Cards. For Base/Bitable extension details, use `references/base-bitable-extensions.md`. For the full official documentation index generated from the latest crawl, use `references/client-docs-source-catalog.md`.

## What changed in the 2026-07 refresh

The skill was refreshed from `https://open.feishu.cn/document/client-docs/intro` plus the official documentation directory API. The crawl discovered 1,805 pages across Developer Guides and Client API roots and cached 1,684 markdown pages before the network crawl was stopped. The important result for agents is coverage: client work is not just Docs add-ons and Workplace Blocks. It also includes Web App/H5 JSAPI, link preview, Feishu Cards/CardKit, Base extension APIs, workplace APIs, and deprecated Mini Program/Gadget material.

Load `references/client-docs-overview.md` first when you need to choose a client-side surface. Load this file when you have already selected an in-client surface and need implementation guidance.

## Surface selection

| Need | Recommended surface | Primary docs |
|---|---|---|
| Full custom page in Feishu/Lark client | Web App / H5 | Develop Web Apps + Client API > Web App / Mini Program API |
| Document-side UI or workflow | Docs add-on / cloud document widget | Develop Docs Add-ons + Client API > Docs Add-on |
| Workplace dashboard tile or quick action | Workplace Block | Develop Workplace Blocks + Client API > Workplace Block |
| Rich preview when users paste/open links | Link Preview | Develop link preview |
| Interactive message surface in chat/bot notifications | Feishu Card / CardKit / card JSON | Feishu Cards |
| Base table/record/automation extension | Base/Bitable extension | `references/base-bitable-extensions.md` |
| Backend automation with no UI | Server APIs, SDK, CLI, MCP | `references/cloud-docs-and-apis.md` |
| Legacy Mini Program/Gadget | Avoid for new development unless maintaining existing code | Official docs mark Gadget/Mini Program as not recommended |

## Shared rules for every client surface

- The Open Platform app remains the capability, credential, permission, release, and event container.
- Client bundles must not contain App Secret, tenant tokens, user refresh tokens, long-lived credentials, or privileged OpenAPI calls.
- Use frontend client APIs only for client capabilities: container navigation, selection, picker UI, local storage, document/context bridge, and safe runtime calls.
- Put token exchange, `app_secret`, privileged OpenAPI, and cross-resource operations in a backend service over HTTPS.
- Configure both application scopes and resource-level grants. Many resource APIs require the target document/Base/folder to be shared with the app or accessed through a valid user token.
- Verify in the real Feishu/Lark client, not just a local browser, because JSAPI availability, container behavior, and permissions differ by client version and tenant.
- Check current official docs before coding: CLI package names, generated template layout, and console labels change.

## Web App / H5

Use Web App/H5 for a full-page custom app inside Feishu/Lark. It is a normal web frontend hosted by your service, with Feishu/Lark client APIs layered on top.

Official source anchors:

- Web App overview: `https://open.feishu.cn/document/uYjL24iN/uMTMuMTMuMTM/introduction`
- H5 JSAPI overview: `https://open.feishu.cn/document/uYjL24iN/uMTMuMTMuMTM/`
- JSAPI auth step: `https://open.feishu.cn/document/uYjL24iN/uEzM4YjLxMDO24SMzgjN`
- Open abilities include web-meta, orientation, menu configuration, navigation-bar controls, and browser-opening behavior under Develop Web Apps.

Typical flow:

1. Create a self-built or store app in Developer Console.
2. Enable Web App/H5 capability and configure the homepage/redirect URLs.
3. Serve the frontend through HTTPS.
4. Implement JSAPI signature/config on the backend when protected JSAPIs are needed.
5. Use login-free identity flows from the client and exchange codes on the backend for user access tokens.
6. Use Client API pages for chat, contact, file, media, navigation, storage, geolocation, and container UI calls.
7. Test in desktop and mobile clients if the app is used on both.

Common H5 client API groups discovered in the crawl:

- Authentication/config: `h5sdk.config`, request access/session checks, authorization scope helpers.
- User and contact: get user info, enter profile, choose contact.
- Chat: enter/choose/toggle chat, send message card, bot entry, chat badge changes.
- UI: modal, prompt, loading/toast, navigation bar, tab bar, window sizing, page scroll, pull refresh, leave confirmation.
- Navigation: `navigateTo`, `redirectTo`, `switchTab`, `reLaunch`, `navigateBack`, `openSchema`, `closeWindow`.
- Network: request, upload/download, WebSocket, tracing.
- Files/media/device: file picker, docs picker, image/video/audio/recording/camera, accelerometer, compass, screenshot, phone call, vibration.
- Storage and performance: local storage, update manager, performance recorder.

## Docs add-on / cloud document widget

Use Docs add-ons when the UI belongs inside a document context. Examples include document helpers, block insertion or transformation tools, in-document data panels, content generation helpers, workflow panels, and document-specific shortcuts.

Official source anchors:

- Overview: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/docs-add-on-introduction`
- Quick start: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/03-cloud-document-widget-quick-development-guide/03-cloud-document-widget-quick-developme`
- Terms: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/02-cloud-doc-block-noun-explanation`
- App.json configuration: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/03-cloud-doc-block-rapid-development-guide/appjson-configuration-instructions`
- Security configuration: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/08-cloud-doc-block-security-configuration/cloud-doc-block-security-configuration`
- Data storage: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/04-cloud-doc-block-data-storage/04-cloud-doc-block-data-storage`
- FAQ: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/docs-add-on/faq`

Implementation checklist:

1. Confirm the target document host and add-on entry point: document menu, plus menu, slash command, floating panel, modal, or embedded block behavior.
2. Create/configure the Open Platform app and Docs add-on capability.
3. Configure `app.json` for contributed views. The docs list view entries such as normal rendering page, fullscreen, float card, popup, and modal views; confirm current schema in the official page.
4. Configure domain/security allowlists before calling external services.
5. Decide storage model: document-bound storage, add-on-local state, backend storage, or server APIs. Avoid putting secrets in client-side storage.
6. Use Docs add-on Client API pages for bridge operations, lifecycle, selection/range, block/document structures, collaboration and user info, storage, and event handling.
7. If server APIs are also needed, route through backend with appropriate user or tenant token.
8. Verify in a real document with the target user role and tenant permissions.

Client API areas discovered for Docs add-ons include lifecycle (`LifeCycle.notifyAppReady`), bridge/container resize and modal behavior, block and range data structures, selection APIs, user/context APIs, storage, and event subscriptions.

## Workplace Blocks

Use Workplace Blocks for lightweight workplace/workbench tiles, dashboards, quick actions, and status components. They are smaller than full H5 apps and are hosted by the workplace product surface.

Official source anchors:

- Workplace Block overview: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/guide/hosting-scenario-introduction/workplace`
- Quick start: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/quick-start`
- Development tools: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/devtools`
- Framework introduction: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/block-frame/block-framework-introduction`
- Lifecycle: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/block-frame/logic-layer/lifecycle/lifecycle`
- Directory structure: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/guide/directory-structure`
- Config reference: `https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/block/block-frame/config`

Implementation checklist:

1. Confirm the user needs a workplace tile/widget, not a full H5 page.
2. Create an app and enable the Workplace Block capability.
3. Install and use the current official development tools for Block scaffolding/debugging.
4. Follow the generated framework structure: view layer, logic layer, configuration, lifecycle, and packaging.
5. Use Workplace Block Client API pages for runtime, lifecycle, UI, storage, network, navigation, and open abilities.
6. Keep external OpenAPI calls backend-side if they require app secrets or privileged tokens.
7. Validate display, refresh/update behavior, and permissions in the real workplace client.

The official tree includes many view-layer details: TTML, TTSS, CSS-like attributes, event system, logic-layer registration, framework interfaces, update mechanism, local cache, network, OpenSchema/login, VChart extension, and experience blocks. Use the catalog to locate exact pages instead of guessing framework syntax.

## Link Preview

Use Link Preview when users paste or share URLs and Feishu/Lark should show a rich preview card pulled from your service.

Official source anchors:

- Development guide: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/development-link-preview/link-preview-development-guide`
- Quick start: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/development-link-preview/quick-start`
- Typical case: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/development-link-preview/typical-case`
- Pull preview data callback: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/development-link-preview/pull-link-preview-data-callback-structure`

Implementation checklist:

1. Confirm URL ownership, matching rules, and preview security model.
2. Configure link preview capability and callback endpoint.
3. Implement callback verification and preview-data response server-side.
4. Avoid leaking private data in previews; preview callbacks may be triggered by pasted links in contexts you did not anticipate.
5. Test with internal and external chats if both are in scope.

## Feishu Cards / CardKit

Use Feishu Cards for interactive messages in chat, bot notifications, and approval/workflow interactions. Cards are not the same as embedded app surfaces, but they are a major client UX surface.

Official source anchors:

- Feishu Card overview: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/feishu-card-overview`
- CardKit overview: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/feishu-card-cardkit/feishu-cardkit-overview`
- Build card content: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/feishu-card-cardkit/build-card-content`
- Card JSON 2.0 structure: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-json-v2-structure`
- Interactive bot quick start: `https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/quick-start/develop-a-card-interactive-bot`

Implementation checklist:

1. Choose CardKit/template builder or direct card JSON.
2. Choose send path: app bot, custom bot, or server API.
3. Configure interactive callbacks and event subscriptions if the card has buttons, forms, or selectors.
4. Use current JSON schema for card components; the tree includes JSON 2.0 and historical JSON 1.0 pages.
5. Validate card rendering in the target chat client, theme, language, and screen size.

## Deprecated or historical surfaces

The crawl found large sections for Gadgets/Mini Programs and historical versions. The official tree labels Gadget/Mini Program development as not recommended. Do not start new development there unless the user explicitly requests legacy maintenance. Prefer H5/Web App, Base extensions, Docs add-ons, Workplace Blocks, or cards depending on the host surface.

## Troubleshooting checklist

- If JSAPI calls fail, re-check JSAPI signature generation, domain allowlist, client version, app capability enablement, and whether the API belongs to H5, Mini Program, Docs add-on, Base extension, or Workplace Block.
- If a client API is undefined, verify host surface; APIs are not universally available across H5, Docs add-ons, Base extensions, and Workplace Blocks.
- If OpenAPI calls fail from a plugin, move protected calls to backend and verify scopes/resource grants.
- If upload/release fails, verify CLI login tenant, app ID, capability ID, semantic version, icon/name/localization metadata, and release review requirements.
- If UI works locally but not in Feishu/Lark, check HTTPS, CSP/domain allowlist, mixed content, client version, and real resource permissions.

# Feishu/Lark Module 1: Open Platform Fundamentals

This reference contains the detailed documentation for `Module 1: Open Platform Fundamentals`. The main `SKILL.md` is the general principle and routing index; load this file only when the selected task needs these deeper implementation details.

## Module 1: Open Platform Fundamentals

### App and distribution model

Feishu/Lark Open Platform apps are the top-level container for credentials, capabilities, permissions, release versions, and event subscriptions. The official platform overview describes an app as both the service delivered to users and the carrier used to call Feishu/Lark open capabilities.

Choose the app distribution model early:

| Dimension | Self-built/custom app | Marketplace/store app |
|---|---|---|
| Audience | One enterprise tenant | Many Feishu/Lark tenants or personal users |
| Developer | Internal IT or an authorized developer | ISV / third-party provider |
| Default use | Internal tools, prototypes, tenant-specific workflows | Commercial or public distribution |
| Review path | Tenant admin approval and app release | Platform/store review, store requirements, broader localization/support |
| Capability caveat | Existing app capabilities are generally available | Official overview notes that workplace widgets/blocks are not supported for store apps |

Open Platform apps can expose multiple shapes in one app:

- Bot: conversation interaction, notifications, chat/group management, event-driven replies, and message cards.
- Web App/H5: full-page web UI inside the Feishu/Lark client, usually with JS-SDK login-free identity and backend token exchange.
- Block/widget: lightweight client component surfaces such as cloud document widgets and Base/Bitable extensions.
- Link preview and mobile login: specialized capabilities for cards/preview rendering or third-party mobile account login.

A capability selection can combine shapes. For example, an H5 app can also enable Bot and events so frontend actions trigger chat notifications. Treat each shape as a capability with its own release, permission, runtime, and verification path.

Provenance: browser extract `browser-extracts/platform-overview.md`; Feishu overview `https://open.feishu.cn/document/platform-overveiw/overview?lang=zh-CN`; app-type docs including self-built/store app guides.

### Credentials and tokens

Do not hardcode app secrets in frontend code. Token choice determines identity and visible resources.

| Token | Identity | Common use | Notes |
|---|---|---|---|
| `tenant_access_token` | App in a tenant | backend automation, bot/app-owned data, resources shared with the app | Valid about 2 hours; custom apps use app ID + app secret. |
| `user_access_token` | A specific user | acting on user-owned documents or inheriting user permissions | Requires OAuth/consent; refresh token rotation matters. |
| `app_access_token` | Store app identity | store app management flows | Store apps also involve app ticket handling. |

Official SDKs for Java, Python, Go, and Node.js handle much of the token lifecycle. For small scripts, direct HTTP is possible, but cache tokens and refresh proactively.

Provenance: `sources/platform-fundamentals.md`, `sources/cloud-docs-apis.md`; Feishu authentication docs such as `https://open.feishu.cn/document/server-docs/api-call-guide/calling-process/get-access-token` and SDK guides.

### Permissions and resource grants

Feishu/Lark access control has at least two layers:

1. Application scopes configured in Developer Console, such as `docx:document`, `docx:document:readonly`, `sheets:spreadsheet`, `bitable:app`, `bitable:app:readonly`, or `drive:drive`.
2. Resource-level access to the specific document, folder, Base, table, or record. An app with the right scope still cannot access a user document unless it is shared with the app or the call uses a valid `user_access_token` for an authorized user.

If the API returns permission error `99991672`, inspect the response for `permission_violations`; it often names the missing scope.

For a backend app using `tenant_access_token` to access user-visible Docs/Sheets/Base resources, enable the Bot capability and ask the document owner to add the app as a collaborator with the needed permission.

Provenance: `sources/platform-fundamentals.md`, `sources/cloud-docs-apis.md`; Feishu scope list and permission docs including `https://open.feishu.cn/document/faq/trouble-shooting/how-to-fix-the-99991672-error`.

### Events and callbacks

Feishu supports event subscriptions through:

- WebSocket persistent connection: recommended for many self-built apps because it avoids exposing a public callback URL during development.
- HTTP webhook callback: required or common for store apps, legacy integrations, and external server flows. Requires public URL verification.

Avoid subscribing to both v1 and v2 versions of the same event unless duplicate handling is intentional.

Provenance: `sources/platform-fundamentals.md`; event docs under `https://open.feishu.cn/document/server-docs/event-subscription-guide/overview`.

### Web App / H5 basics

Use Web App/H5 when you need a full-page app UI in the Feishu client. Typical flow:

1. Create a self-built or store app.
2. Enable Web App capability and configure homepage URL.
3. Integrate the H5 JS-SDK if native JSAPIs are needed.
4. Backend provides JSAPI signature parameters derived from `jsapi_ticket`.
5. Inside the client, use login-free identity flows such as `requestAuthCode`, then exchange code for `user_access_token` on the backend.
6. Use Applink when deep-linking or controlling container/window behavior.

Provenance: `sources/platform-fundamentals.md`; H5 and Applink docs listed in `platform-fundamentals-sources.txt`.

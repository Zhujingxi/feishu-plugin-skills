# Feishu/Lark Module 2: Base/Bitable Extensions

This reference contains the detailed documentation for `Module 2: Base/Bitable Extensions`. The main `SKILL.md` is the general principle and routing index; load this file only when the selected task needs these deeper implementation details.

## Module 2: Base/Bitable Extensions

Base/Bitable extensions are in-client plugin surfaces hosted by Base/Bitable. They are not the same as Bitable server APIs.

### Extension types

Official Base/Bitable extension docs distinguish OpenAPI from in-client plugins. Use OpenAPI when integrating your own system with Base data or doing backend CRUD. Use Base/Bitable plugins when you must embed custom behavior directly inside Base.

| Type | Host context and entry point | Use when | Typical tooling |
|---|---|---|---|
| Table View Extension / Data Table View | Added from a Base table header via the new-view/add-more-extensions flow | custom visualization, maps, Gantt-like views, dashboards, printable layouts | `opdev`, React/TypeScript + Webpack or Vue template, `@lark-opdev/block-bitable-api` |
| Record View Extension | Added after expanding a single record, from the side panel plus/add-plugin entry | custom record previews, print views, enrichment panels, contract/order summaries | `opdev`, `record-view` template, Base extension SDK/context APIs |
| Automation Action Extension | Added while creating a Base automation workflow | OCR, AI extraction, enrichment, external API calls, notifications | `opdev`, `basekit.addAction()`, `execute(args, context)` |

Decision rule:

- Use table view for table-level or aggregate UX.
- Use record view for one-record UX.
- Use automation action for workflow execution without a persistent table UI.
- Use Bitable REST APIs for backend CRUD/import/export with no embedded UI.

Terminology differs by locale. Feishu Chinese docs call the product "multidimensional table"; Lark English docs call it "Base" and note the older Bitable naming. Lark console labels may say Base extensions, Data Table View, Record View, and Automation Action. Feishu console labels may say Bitable plugin, data table view, record view, and automation operation. Match the target tenant/documentation domain (`open.feishu.cn` vs `open.larksuite.com`) when writing user instructions.

Provenance: browser extracts `base-extension-introduction.md`, `base-table-view-extension.md`, `base-record-view-extension.md`, `base-automation-extension.md`, and the corresponding Lark English extracts; official docs including `https://open.feishu.cn/document/base-extensions/base-extension-introduction?lang=zh-CN`.

### Toolchain

Install and authenticate the Open Platform/Base extension CLI:

```bash
npm install @lark-opdev/cli@latest -g -f
opdev login
opdev whoami
```

During `opdev login`, choose the matching Feishu or Lark environment. Confirm `opdev whoami` before upload because upload authorization is tied to the logged-in developer account and tenant.

Scaffold the correct capability template:

```bash
# Table view extension
opdev create ${app_dir}/${view_dir} -a bitable-extensions -s table-view

# Record view extension
opdev create ${app_dir}/${view_dir} -a bitable-extensions -s record-view

# Automation action extension
opdev create ${app_dir}/${action_dir} -a bitable-extensions -s automated-action
```

Current official guides describe React + TypeScript + Webpack templates, with Vue available for UI extensions. Initialize and run from the generated directory:

```bash
cd ${app_dir}/${view_or_action_dir}
npm install
npm run start      # UI extension local debugging where the template provides it
npm run test       # automation action execute() simulation where provided
npm run upload     # builds/uploads a semantic version, or use opdev upload ./dist
```

Important generated files:

- `app.json`: binds local code to the Feishu/Lark app via `appId`.
- `block.json`: binds local code to the exact extension capability via `blockTypeID`; its `url` can be changed to point local debugging at a different Base document.
- `debug.json`: UI templates can use fields such as `v` / `vb` to specify the Base version for debugging.

The `BlockTypeID` is capability-specific. A table-view ID, record-view ID, and automation-action ID are not interchangeable. The official upload flow reads `appId` from `app.json`, then locates the matching `blockTypeID` in `block.json`; a mismatch uploads to the wrong target or fails.

Provenance: browser extracts `base-table-view-extension.md`, `base-record-view-extension.md`, `base-automation-extension.md`, plus Lark English equivalents.

### Base extension workflow

1. Define the extension type: table view, record view, or automation action.
2. Choose Feishu China vs Lark international docs and self-built vs store distribution.
3. Create a self-built app or store app in Developer Console.
4. Add the exact Base/Bitable extension capability: Data Table View, Record View, or Automation Action.
5. Record App ID and BlockTypeID immediately.
6. Configure a server/domain allowlist if the extension will make network requests.
7. Install and log in to `opdev`; confirm the target environment and account with `opdev whoami`.
8. Scaffold the correct template.
9. Confirm `app.json` and `block.json` match the Developer Console app/capability.
10. Apply for scopes. The browser-extracted guides specifically call out `bitable:app` and `bitable:app:readonly` for SDK access, enabled under user identity (`user_access_token`) when the extension reads/writes user-visible Base data.
11. Build frontend/action code.
12. For table/record views, run `npm run start`; the official table-view guide says the dev server opens a Base document with a `debugPort` parameter, then you add the local component through the new-view/add-plugin flow.
13. For automation actions, implement `src/register.ts` with `basekit.addAction()` and run `npm run test` to simulate `execute()` where the generated template provides it.
14. Upload with `npm run upload` or `opdev upload ./dist` and enter a semantic version such as `0.0.1`.
15. In Developer Console, select the uploaded block version, add icon/name/description/localization, create an app version, and submit release/review.
16. Verify in a real Base under the intended tenant/user permissions.

### Base extension SDK pattern

The key frontend SDK surfaced in research is `@lark-opdev/block-bitable-api`:

```ts
import { bitable } from '@lark-opdev/block-bitable-api';

const tableMetaList = await bitable.base.getTableMetaList();
const table = await bitable.base.getActiveTable();
```

For automation actions, the official browser-extracted guide uses `@lark-opdev/block-basekit-server-api`:

```ts
import { basekit, ParamType } from '@lark-opdev/block-basekit-server-api';

basekit.addAction({
  execute: async function(args, context) {
    return {};
  },
  resultType: { type: ParamType.Object },
});
```

Automation action details from the official guide:

- `formItems` defines the automation form UI and maps user inputs to `args` by item ID.
- `execute(args, context)` contains runtime logic and must return a value, even if the value is `{}`.
- `resultType` must match the `execute` return value so later automation nodes can reference results.
- Use `context.fetch` for external HTTP calls; the official guide says not to use axios or got in the automation sandbox.
- To obtain document/Base permissions inside the action, declare `permission: { type: 2 }` where the current template/docs require it.
- Use `basekit.setI18n` for localization; extracted locales include `zh-CN`, `zh-HK`, `zh-TW`, `en-US`, and `ja-JP`.
- Automation sandbox limits in the extracted guide: memory under 1 GB and request concurrency at most 400.
- Third-party packages may be used, but the extracted guide lists axios, got, bcrypt, moment, jsdom, and sharp as not runnable in the sandbox.

Confirm current SDK names and generated template structure against the official docs and the created scaffold before final implementation.

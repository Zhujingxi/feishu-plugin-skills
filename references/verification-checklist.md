# Verification Checklist

Use this file when reviewing an implementation based on the `feishu-plugin-development` skill.

## 1. Classification

- [ ] The deliverable is classified as one of: server API integration, Base extension, Workplace Block, Docs add-on/document widget, Web App/H5, Feishu Project plugin, message card, CLI/MCP automation.
- [ ] The selected surface matches the user-visible requirement.
- [ ] The implementation does not call a backend-only API integration a plugin unless an in-client app surface is actually built.

## 2. App and credentials

- [ ] Self-built vs marketplace/store app decision is documented, including the official caveat that store apps do not support workplace widgets/blocks where relevant.
- [ ] App ID is recorded in project-local config/docs, not hardcoded in many files.
- [ ] App Secret is stored only in a secret manager or environment variable.
- [ ] Frontend bundle does not contain App Secret or long-lived tokens.
- [ ] Token type is documented: `tenant_access_token`, `user_access_token`, or store app token flow.

## 3. Permissions

- [ ] Required scopes are listed with official names.
- [ ] Scopes are approved in Developer Console.
- [ ] Resource-level sharing/grants are configured for the test document/Base/folder: app-owned space, bot-added document app for tenant-token access to user resources, or user-token collaborator sharing as appropriate.
- [ ] Missing-scope behavior has been tested or at least documented.

## 4. Surface-specific checks

### Base/Bitable extension

- [ ] Uses `opdev`, not `lpm`.
- [ ] Correct extension type selected: table view, record view, or automation action.
- [ ] `app.json` `appId` matches Developer Console.
- [ ] `block.json` `blockTypeID` matches the exact capability type.
- [ ] `opdev whoami` confirms the expected account and Feishu/Lark environment.
- [ ] Build/test command from scaffold passes (`npm run start` for UI debugging where applicable; `npm run test` for automation action execute simulation where provided).
- [ ] `opdev upload` has been run and uploaded version selected in console.
- [ ] Verified in a real Base as target user.
- [ ] Any network-calling extension has the required server/domain allowlist configured.
- [ ] Automation actions use `context.fetch`, not axios/got, and document sandbox limits and unsupported packages if relevant.
- [ ] Automation actions declare permission/i18n/resultType consistently with the generated template and official docs.

### Feishu Project plugin

- [ ] Uses `lpm`, not `opdev`.
- [ ] Local debug is enabled before `lpm start`.
- [ ] Protected OpenAPI calls go through backend.
- [ ] External calls use HTTPS.
- [ ] `lpm release` has produced a version.
- [ ] Verified in Feishu Project client.

### Server API integration

- [ ] Uses official SDK, direct HTTP with token caching, `lark-cli`, or MCP appropriately.
- [ ] Pagination implemented for list/query endpoints, with Bitable page-size caps checked against current docs.
- [ ] Query Records is preferred over the historical List Records endpoint when filtering/search requirements allow.
- [ ] Async import/export polling implemented.
- [ ] Rate limits and retries are handled with endpoint-specific limits, serialized Bitable writes, and uuidv4 `client_token` idempotency where needed.
- [ ] Request IDs, Feishu error payloads, and `X-Tt-Logid` headers are logged.

### Widgets/Blocks/Docs add-ons

- [ ] Current official runtime/manifest docs were re-checked.
- [ ] Component host surface is documented.
- [ ] Backend proxy/token flow exists for protected data access.
- [ ] Real Feishu/Lark client verification completed.

## 5. Release and handoff

- [ ] App/plugin version and release/review state are documented.
- [ ] Minimal reproduction or test resource URL is recorded outside the skill if needed.
- [ ] Known limitations and manual console steps are documented.
- [ ] User-facing handoff avoids exposing secrets or raw PII.

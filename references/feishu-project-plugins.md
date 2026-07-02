# Feishu/Lark Module 5: Feishu Project Plugins

This reference contains the detailed documentation for `Module 5: Feishu Project Plugins`. The main `SKILL.md` is the general principle and routing index; load this file only when the selected task needs these deeper implementation details.

## Module 5: Feishu Project Plugins

Feishu Project plugins are a separate ecosystem from Open Platform/Base extensions. Use `@lark-project/cli` / `lpm`, not `opdev`.

### Extension points

Feishu Project plugin 2.0 extension points documented in research include:

- Detail page.
- Navigation page.
- List/table view.
- Table column widget.
- Form page widget.
- Node form widget.
- Field type extension.
- Node scheduling extension.
- Plugin configuration page.
- More-actions buttons for instances, WBS nodes, and workflow nodes.
- Create button.
- Node transition button.
- Batch operation button.
- Event listeners and event interceptors.
- Automation triggers and actions.
- MCP server for AI Agent services.

Provenance: `sources/tutorials-project.md`, supplemental Project source files, and official Project help center URLs such as `https://project.feishu.cn/b/helpcenter/1p8d7djs/nh4exbsn`, `https://project.feishu.cn/b/helpcenter/1p8d7djs/49k1ojm9`, and `https://project.feishu.cn/b/helpcenter/1p8d7djs/41jvuw3r`.

### Project plugin workflow

1. Open Feishu Project Workbench.
2. Enter the Feishu Project Open Platform from the avatar/open-platform entry.
3. Create a new plugin with name/icon.
4. Add plugin components or automation connectors.
5. Enable local debugging on the plugin detail page.
6. Install CLI and run local dev:

```bash
npm i -g @lark-project/cli
lpm start
```

7. Build UI, commonly with Semi Design. For React 19, use `@douyinfe/semi-ui-19` if the docs/template require it.
8. Route protected Feishu Project OpenAPI calls through a backend server; do not call them directly from plugin frontend.
9. Use HTTPS for external APIs.
10. Release bundle:

```bash
lpm release
```

11. Manage version in the Project developer console and verify in the real Feishu Project client.

### Project plugin pitfalls

- `lpm start` may not work until local debug is explicitly enabled.
- The frontend cannot directly call Feishu Project OpenAPI for protected operations.
- Mixed HTTP content is blocked inside HTTPS Feishu Project pages.
- `opdev` examples for Bitable are not Project plugin examples; do not mix CLIs or templates.

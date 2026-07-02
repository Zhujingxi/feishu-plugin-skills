# Feishu/Lark Module 3: Cloud Docs, Sheets, Drive, and Bitable Server APIs

This reference contains the detailed documentation for `Module 3: Cloud Docs, Sheets, Drive, and Bitable Server APIs`. The main `SKILL.md` is the general principle and routing index; load this file only when the selected task needs these deeper implementation details.

## Module 3: Cloud Docs, Sheets, Drive, and Bitable Server APIs

Server APIs run outside the Feishu/Lark client. They manipulate resources but do not create embedded UI.

### Resource model

Official Cloud Docs docs describe Cloud Docs as the umbrella for online documents, spreadsheets, Base/Bitable, Wiki, and Drive/cloud space resources. APIs cover file upload/download, online document creation/editing, file/folder management, and Wiki/Drive management. Mind Notes are explicitly outside the currently supported Cloud Docs open-capability set in the extracted Feishu overview.

Cloud Docs is resource-centered. Common identifiers:

| Product/resource | Identifier | Notes |
|---|---|---|
| Cloud space root | `root_token` | Container for Cloud Docs resources. |
| Folder | `folder_token` | Container for files and subfolders. |
| File | `file_token` | Generic file object in Drive/cloud space. |
| Legacy document | `doc_token` | Legacy Feishu document token; newer Docx APIs use `document_id`. |
| Docx document | `document_id` | Root page block often uses the same ID; Wiki docs may require resolving `obj_token`. |
| Sheets spreadsheet | `spreadsheet_token`, `sheet_id` | Values APIs use ranges like `Sheet1!A1:D10`. |
| Bitable/Base | `app_token`, `table_id`, `view_id`, `record_id`, `field_id` | URL tokens differ for `/base` vs `/wiki`; wiki may require resolving object token. |
| Wiki | `space_id`, `node_token`, `obj_token` | `node_token` is the mount point; `obj_token` is the underlying cloud document resource. |
| Comment | `comment_id` | Comment identifier in online documents. |

Access depends on credential identity:

- `tenant_access_token` can directly access resources owned by the app's application cloud space. The extracted overview notes this application cloud space is not manageable through the normal UI and is managed through file-management APIs.
- `user_access_token` can directly access resources owned by the authorized user.
- For `tenant_access_token` to access a user's existing document/Base/folder, the app must enable Bot capability and the document owner must add the document app from the document page menu.
- For `user_access_token` to access another user's resource, the owner must grant access through the normal share/collaborator flow.

When API calls fail, capture the response payload and the `X-Tt-Logid` response header; the official Cloud Docs access flow points to log retrieval by that header.

Provenance: browser extract `browser-extracts/docs-overview.md`; `sources/cloud-docs-apis.md`; official Docs, Sheets, Bitable, Drive, and Wiki OpenAPI docs.

### Common API families

Docx:

- Create document: `POST /open-apis/docx/v1/documents`
- List blocks: `GET /open-apis/docx/v1/documents/:document_id/blocks`
- Create child blocks: `POST /open-apis/docx/v1/documents/:document_id/blocks/:block_id/children`
- Update block: `PATCH /open-apis/docx/v1/documents/:document_id/blocks/:block_id`
- Delete child blocks: `DELETE /open-apis/docx/v1/documents/:document_id/blocks/:block_id/children/batch_delete`

Sheets:

- Create spreadsheet: `POST /open-apis/sheets/v3/spreadsheets`
- Get metadata: `GET /open-apis/sheets/v3/spreadsheets/:spreadsheet_token`
- Query sheets: `GET /open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/query`
- Read range: `GET /open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values`
- Write range: `PUT /open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values`
- Batch update ranges: `POST .../values_batch_update`

Bitable:

- Create app: `POST /open-apis/bitable/v1/apps`
- List/create tables: `/open-apis/bitable/v1/apps/:app_token/tables`
- List/create fields: `/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields`
- List records: `GET /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records`
- Create/update/delete/search records: `records`, `records/:record_id`, `records/search`
- Batch operations: `records/batch_create`, `records/batch_update`, `records/batch_get`

Browser-extracted Bitable endpoint details to preserve during implementation:

- Create Bitable app (`POST /open-apis/bitable/v1/apps`): extracted rate limit is 20 requests/minute. Request body accepts optional `name` (up to 255 characters), optional `folder_token`, and optional `time_zone` such as `Asia/Macau`. With `tenant_access_token`, `folder_token` can only target a folder created by the app itself. The response includes `app_token`, `default_table_id`, `folder_token`, `name`, and `url`. To create from a template, first obtain the template `app_token`, then use the file-copy API.
- List records (`GET .../records`): the extracted page marks this as a historical endpoint and recommends using Query Records instead when possible. It supports `view_id`, `filter`, `sort`, `field_names`, `text_field_as_array`, `user_id_type`, `display_formula_ref`, `automatic_fields`, `page_token`, and `page_size` up to 500. If `filter` or `sort` is set, `view_id` is ignored. Filter length is capped at 2000 characters and does not support Person or linked-record fields; sort length is capped at 1000 characters and does not support formula or linked-record fields.
- Create record (`POST .../records`): extracted rate limit is 50 requests/second. The caller identity must have edit permission on the Base. Query parameters include `user_id_type`, `client_token` (uuidv4 idempotency key), and `ignore_consistency_check`. Field values are keyed by field name; examples include string text, numeric number, option strings/arrays, millisecond timestamps for dates, booleans, Person arrays whose IDs match `user_id_type`, hyperlinks as `{text, link}`, attachment tokens, linked record IDs, and geolocation coordinates.
- Concurrency and consistency: extracted error codes and notes warn that the same table does not support concurrent write APIs; `1254291` is write conflict, `1254607` means data is not ready and should be retried after waiting, and `1254608` indicates a duplicate identical update request.
- Limits from extracted error tables/notes include table plus dashboard count up to 100, views up to 200, records up to 20,000, and batch add up to 500 records.
- Attachment fields require uploading material/media first. Error `1254303` means the attachment token does not belong to the target Base/table context.
- Synchronized tables from other data sources do not support create/update/delete operations.
- Advanced permissions can deny operations even when base scopes exist; extracted create-record errors include `1254302 Permission denied` for missing advanced permission.

Drive:

- Create folder: `POST /open-apis/drive/v1/files/create_folder`
- Create online document: `POST /open-apis/drive/v1/files/create_document`
- Get metadata: `GET /open-apis/drive/v1/metas`
- List folder children: `GET /open-apis/drive/v1/files`
- Copy/move/delete file: `copy`, `move`, `DELETE /files/:file_token`
- Upload small file: `POST /open-apis/drive/v1/files/upload_all`
- Large upload: prepare → upload part → finish
- Media upload for embedding: `drive/v1/medias/*`

Provenance: `sources/cloud-docs-apis.md`; source inventory in `cloud-docs-apis-sources.txt`.

### Import/export workflows

Markdown/DOCX/TXT/CSV/XLSX import:

1. Upload local file via Drive upload API.
2. Create import task with `extra`, for example `{"obj_type":"docx","file_extension":"md"}`.
3. Poll import task until it returns the new document token/type.
4. Optionally use Docx/Sheets/Bitable APIs for post-processing.

The `file_extension` in `extra` must match the actual uploaded suffix.

Cloud document export:

1. Create export task with token/type and target file extension, such as docx → pdf, sheet → xlsx/csv, bitable → xlsx/csv.
2. Poll export task for `file_token`.
3. Download via export-task file download endpoint.

Cloud documents are not downloaded directly as ordinary Drive files; use export APIs.

Provenance: `sources/cloud-docs-apis.md`; import/export docs including `https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/import_task/import-user-guide` and export task references.

### Server integration workflow

1. Classify resource type and token from URL.
2. Decide `tenant_access_token` vs `user_access_token`.
3. Apply for minimal required scopes.
4. Grant resource-level permission to the app or user.
5. Use SDK or direct HTTP client with token caching and retry/backoff.
6. Implement pagination and async task polling where needed.
7. Log Feishu request IDs/error codes for debugging.
8. Verify against a real test document/Base owned by the target tenant.

### Server API constraints

- Use endpoint-specific rate limits from current docs rather than a single global limit. Browser-extracted examples show Create Bitable app at 20 requests/minute, List Records at 20 requests/second, and Create Record at 50 requests/second.
- Prefer Query Records over the historical List Records endpoint when filtering/search behavior matters.
- Bitable list/query endpoints return paginated data; extracted List Records page size defaults to 20 and caps at 500.
- Create/update writes to the same Bitable table must not run concurrently; serialize or queue writes and retry `1254291`/`1254607` carefully.
- Use `client_token` uuidv4 idempotency keys on create-record calls when retrying.
- Bitable record count and batch limits from extracted docs include 20,000 records per table and up to 500 records per batch add.
- Sheets single range reads can hit response-size limits around 10 MB.
- Single Drive folder node limit noted in research: 1500 items.
- Import/export is asynchronous.
- Attachment fields require media/material upload first; media/file tokens can be scoped to the specific Bitable/table context.
- Advanced permissions in Bitable may require Manage permission for operations that look like read/edit.

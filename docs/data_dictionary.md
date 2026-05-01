# Data Dictionary

Policy RAG With Citations uses synthetic markdown documents that simulate workplace policy content.

## Source Documents

| File | Policy | Purpose |
|---|---|---|
| `data/policies/remote_work_policy.md` | Remote Work Policy | Remote work eligibility, work location, core hours, equipment, office travel, violations |
| `data/policies/expense_policy.md` | Expense Reimbursement Policy | Eligible expenses, receipts, deadlines, meal limits, prohibited expenses, approval |
| `data/policies/security_policy.md` | Information Security Policy | Passwords, MFA, data classification, incident reporting, device security, access reviews |

## Chunk Fields

| Field | Description |
|---|---|
| `doc_id` | File stem used as the document identifier |
| `title` | Policy title extracted from the first markdown H1 heading |
| `section` | Policy section extracted from markdown H2 headings |
| `source` | Source file path for citation traceability |
| `text` | Section-level policy text used for retrieval |

## Source Metadata Fields

| Field | Description |
|---|---|
| `citation` | Bracketed citation label such as `[1]` |
| `title` | Policy title |
| `section` | Retrieved policy section |
| `source` | Source file path |
| `score` | Rounded retrieval similarity score |

## Generated Reports

| File | Purpose |
|---|---|
| `reports/corpus_profile.json` | Policy document and chunk profile |
| `reports/retrieval_eval.json` | Retrieval evaluation metrics |
| `reports/demo_outputs.md` | Demo questions, answers, sources, scores, and abstention behavior |

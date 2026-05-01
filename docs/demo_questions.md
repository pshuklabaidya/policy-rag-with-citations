# Demo Questions

These questions demonstrate citation-grounded answering over synthetic workplace policy documents.

## Supported Questions

```bash
python scripts/query_policy.py "What is the deadline for submitting an expense report?"
```

Expected source:

```text
[1] Expense Reimbursement Policy - EX-3 Submission Deadline
```

```bash
python scripts/query_policy.py "When must security incidents be reported?"
```

Expected source:

```text
[1] Information Security Policy - SEC-4 Incident Reporting
```

```bash
python scripts/query_policy.py "What are the core collaboration hours for remote employees?"
```

Expected source:

```text
[1] Remote Work Policy - RW-3 Core Collaboration Hours
```

```bash
python scripts/query_policy.py "Which systems require multi-factor authentication?"
```

Expected source:

```text
[1] Information Security Policy - SEC-2 Multi-Factor Authentication
```

```bash
python scripts/query_policy.py "Are personal devices allowed for regular remote work?"
```

Expected source:

```text
[1] Remote Work Policy - RW-4 Equipment
```

## Unsupported Question

```bash
python scripts/query_policy.py "What is the company stock price?" --min-score 0.50
```

Expected behavior:

```text
The available policy documents do not contain enough relevant evidence to answer this question with a citation-grounded response.
```

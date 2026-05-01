# Policy RAG Demo Outputs

Generated examples for supported and unsupported policy questions.

All policy data is synthetic and used for portfolio demonstration only.

## Question: What is the deadline for submitting an expense report?

### Answer

Expense reports must be submitted within 30 days of the transaction date. Late submissions require manager approval and may be denied if business justification is missing. [1] This answer is grounded in Expense Reimbursement Policy, section EX-3 Submission Deadline. Supporting retrieved sections: [2], [3].

### Sources

| Citation | Policy | Section | Score | Source |
|---|---|---|---:|---|
| [1] | Expense Reimbursement Policy | EX-3 Submission Deadline | 0.2203 | data/policies/expense_policy.md |
| [2] | Expense Reimbursement Policy | Expense Reimbursement Policy | 0.1672 | data/policies/expense_policy.md |
| [3] | Expense Reimbursement Policy | EX-6 Approval | 0.0984 | data/policies/expense_policy.md |

## Question: When must security incidents be reported?

### Answer

Suspected security incidents must be reported to the security team within one hour of discovery. Incidents include lost devices, suspicious login alerts, phishing attempts, unauthorized data access, and malware warnings. [1] This answer is grounded in Information Security Policy, section SEC-4 Incident Reporting. Supporting retrieved sections: [2], [3].

### Sources

| Citation | Policy | Section | Score | Source |
|---|---|---|---:|---|
| [1] | Information Security Policy | SEC-4 Incident Reporting | 0.4016 | data/policies/security_policy.md |
| [2] | Information Security Policy | SEC-5 Device Security | 0.109 | data/policies/security_policy.md |
| [3] | Information Security Policy | Information Security Policy | 0.0724 | data/policies/security_policy.md |

## Question: What are the core collaboration hours for remote employees?

### Answer

Remote employees must be available during core collaboration hours from 10:00 AM to 3:00 PM in their assigned team time zone, Monday through Friday, unless otherwise approved. [1] This answer is grounded in Remote Work Policy, section RW-3 Core Collaboration Hours. Supporting retrieved sections: [2].

### Sources

| Citation | Policy | Section | Score | Source |
|---|---|---|---:|---|
| [1] | Remote Work Policy | RW-3 Core Collaboration Hours | 0.637 | data/policies/remote_work_policy.md |
| [2] | Remote Work Policy | RW-5 Travel To Office | 0.0978 | data/policies/remote_work_policy.md |
| [3] | Remote Work Policy | Remote Work Policy | 0.0459 | data/policies/remote_work_policy.md |

## Question: Which systems require multi-factor authentication?

### Answer

Multi-factor authentication is required for email, source code repositories, cloud platforms, finance systems, HR systems, and any application containing confidential data. [1] This answer is grounded in Information Security Policy, section SEC-2 Multi-Factor Authentication. Supporting retrieved sections: [2].

### Sources

| Citation | Policy | Section | Score | Source |
|---|---|---|---:|---|
| [1] | Information Security Policy | SEC-2 Multi-Factor Authentication | 0.6052 | data/policies/security_policy.md |
| [2] | Expense Reimbursement Policy | EX-3 Submission Deadline | 0.0674 | data/policies/expense_policy.md |
| [3] | Information Security Policy | SEC-6 Access Reviews | 0.0387 | data/policies/security_policy.md |

## Question: What is the company stock price?

### Answer

The available policy documents do not contain enough relevant evidence to answer this question with a citation-grounded response.

### Sources

| Citation | Policy | Section | Score | Source |
|---|---|---|---:|---|
| [1] | Information Security Policy | SEC-1 Passwords | 0.2463 | data/policies/security_policy.md |
| [2] | Remote Work Policy | RW-4 Equipment | 0.2283 | data/policies/remote_work_policy.md |
| [3] | Information Security Policy | SEC-5 Device Security | 0.1134 | data/policies/security_policy.md |

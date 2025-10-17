## CIS Control 05: Account Management

### 🎯 Purpose

Establish and maintain processes to **manage user accounts**, including creation, modification, disabling, and removal, to ensure that only authorized users have access to systems and data, and that privileges are appropriate to roles.

The goal is to **reduce risk from compromised or inactive accounts** and enforce the principle of least privilege.

---

### 🧩 Key Principles

* **Authorization:** Every account must have an approved owner and defined purpose.
* **Least Privilege:** Users should have only the access necessary to perform their tasks.
* **Lifecycle Management:** Account provisioning, modification, and deprovisioning must follow defined processes.
* **Monitoring:** Detect and remediate dormant, orphaned, or excessive privilege accounts.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **5.1** | Maintain an **inventory of all user accounts**, including privileged and service accounts.                                               |
| **5.2** | Implement automated provisioning and deprovisioning to ensure timely updates for user lifecycle events (hire, role change, termination). |
| **5.3** | Apply the principle of least privilege when assigning permissions and roles.                                                             |
| **5.4** | Periodically review accounts and privileges to remove inactive or unnecessary access.                                                    |
| **5.5** | Separate **privileged accounts** (administrators, service accounts) from regular user accounts, and monitor their use.                   |
| **5.6** | Enforce strong authentication policies, including multi-factor authentication (MFA) where possible.                                      |
| **5.7** | Implement alerting for anomalous account activity, including multiple failed login attempts or privilege escalations.                    |

---

### 🧰 Example Tools

* **Identity and Access Management (IAM):** Microsoft Active Directory, Okta, JumpCloud
* **Privileged Access Management (PAM):** CyberArk, BeyondTrust, Thycotic
* **Monitoring & Auditing:** Splunk, ELK Stack, Azure Sentinel

---

### 🧠 Best Practices

* Integrate **account management** with HR and IT systems for automated updates.
* Enforce **role-based access control (RBAC)** or **attribute-based access control (ABAC)**.
* Monitor and rotate **service account credentials** regularly.
* Disable or archive **inactive accounts** immediately.
* Regularly audit **privileged accounts** separately from standard users.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                           |
| ---------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | User access management and least privilege are fundamental for network security.      |
| **ISO/IEC 27001:2022** | A.5.7, A.9.2              | Management of user accounts, roles, and access rights.                                |
| **NIST CSF**           | PR.AC-1 / PR.AC-4         | Identities and credentials are managed consistently; privileged access is restricted. |

---

### 📊 Example Policy Snippet

```text
All user accounts must be authorized, documented, and assigned to an approved owner.  
Accounts must follow the principle of least privilege, and privileged accounts must be separated and monitored.  
Inactive accounts shall be disabled within 24 hours of inactivity or termination, and accounts shall be reviewed quarterly for compliance.
```

---

### 📚 References

* [CIS Control 05 – Account Management](https://www.cisecurity.org/controls/account-management)
* [NIST SP 800-53 Rev.5 – AC-2, AC-5, AC-6](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 9.2](https://www.iso.org/standard/75652.html)

---

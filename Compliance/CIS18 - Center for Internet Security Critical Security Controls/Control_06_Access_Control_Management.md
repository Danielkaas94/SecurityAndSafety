## CIS Control 06: Access Control Management

### 🎯 Purpose

Implement and enforce **access control measures** to ensure that users, devices, and applications can access only the resources necessary for their role, preventing unauthorized access to systems and sensitive data.

The goal is to **minimize attack surfaces** by restricting access based on the principle of least privilege and continuously monitoring access rights.

---

### 🧩 Key Principles

* **Least Privilege:** Users and processes should have only the access necessary to perform their tasks.
* **Role-Based Access:** Permissions should align with organizational roles and responsibilities.
* **Segmentation:** Sensitive systems and data should be isolated with strict access controls.
* **Continuous Monitoring:** Access rights and activity should be regularly reviewed to detect anomalies.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------- |
| **6.1** | Define and document access requirements for all systems, applications, and data based on user roles.                      |
| **6.2** | Implement **role-based access control (RBAC)** or **attribute-based access control (ABAC)** to enforce least privilege.   |
| **6.3** | Apply **segmentation and network zoning** to isolate sensitive systems from general access.                               |
| **6.4** | Enforce strong authentication, including **multi-factor authentication (MFA)**, for all privileged or sensitive accounts. |
| **6.5** | Review and recertify user access rights at regular intervals, including privileged accounts.                              |
| **6.6** | Monitor and log access attempts and anomalies, and integrate alerts into the SOC or monitoring system.                    |
| **6.7** | Immediately remove access for terminated users or decommissioned devices.                                                 |

---

### 🧰 Example Tools

* **IAM & Access Management:** Microsoft Active Directory, Okta, AWS IAM
* **Privileged Access Management (PAM):** CyberArk, BeyondTrust, Thycotic
* **Monitoring & Logging:** Splunk, ELK Stack, Graylog, Azure Sentinel
* **Network Segmentation & Firewalls:** Cisco ASA/ISE, Palo Alto, pfSense

---

### 🧠 Best Practices

* Enforce **least privilege** by default for all users, devices, and applications.
* Integrate **access control policies** into HR and onboarding/offboarding workflows.
* Regularly audit **privileged accounts** and enforce MFA on all critical access.
* Use **temporary elevated privileges** for administrative tasks instead of permanent admin rights.
* Monitor **failed login attempts** and unusual access patterns in real time.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                        |
| ---------------------- | ------------------------- | ---------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Enforces access management to protect network and information systems.             |
| **ISO/IEC 27001:2022** | A.9.1–A.9.4               | Access control policies, user access management, and user responsibilities.        |
| **NIST CSF**           | PR.AC-1 / PR.AC-5         | Access permissions are managed, reviewed, and enforced; privileges are restricted. |

---

### 📊 Example Policy Snippet

```text
Access to all enterprise systems must follow the principle of least privilege.  
Roles and access rights must be clearly defined and reviewed quarterly.  
Privileged accounts require multi-factor authentication, and all access events must be logged and monitored.
```

---

### 📚 References

* [CIS Control 06 – Access Control Management](https://www.cisecurity.org/controls/access-control-management)
* [NIST SP 800-53 Rev.5 – AC-2, AC-3, AC-5, AC-6](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 9](https://www.iso.org/standard/75652.html)

---

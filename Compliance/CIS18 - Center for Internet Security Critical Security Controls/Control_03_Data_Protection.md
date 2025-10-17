## CIS Control 03: Data Protection

### 🎯 Purpose

Develop processes and technical controls to **identify, classify, securely handle, and protect data** — both in transit and at rest — to safeguard the confidentiality, integrity, and availability of sensitive information throughout its lifecycle.

The goal is to minimize the risk of data breaches, loss, or unauthorized disclosure by ensuring data is protected according to its sensitivity and business value.

---

### 🧩 Key Principles

* **Data Identification:** Understand what data exists and where it resides.
* **Classification:** Categorize data based on sensitivity and business impact.
* **Protection:** Apply appropriate encryption, access controls, and retention policies.
* **Minimization:** Collect, store, and share only the data necessary for business operations.
* **Lifecycle Management:** Securely handle creation, transmission, storage, and destruction.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| **3.1** | Establish and maintain a **data management process** that defines data handling procedures across its lifecycle. |
| **3.2** | Identify and document **sensitive data repositories**, including databases, file servers, and cloud storage.     |
| **3.3** | Classify data based on confidentiality, integrity, and availability requirements.                                |
| **3.4** | Apply **encryption** for sensitive data at rest and in transit (e.g., AES-256, TLS 1.2+).                        |
| **3.5** | Implement **data access controls** aligned with least privilege and need-to-know principles.                     |
| **3.6** | Regularly back up and securely store critical data to ensure recovery in case of corruption or loss.             |
| **3.7** | Securely **dispose** of data when it is no longer needed (e.g., shredding, wiping, cryptographic erase).         |
| **3.8** | Conduct periodic audits to ensure compliance with data protection and privacy regulations.                       |

---

### 🧰 Example Tools

* **Encryption:** VeraCrypt, BitLocker, LUKS, OpenSSL
* **Data Discovery & Classification:** Spirion, Varonis, Microsoft Purview, OpenDLP
* **Data Loss Prevention (DLP):** Symantec DLP, Forcepoint DLP, Microsoft Defender DLP
* **Backup:** Veeam, Duplicati, BorgBackup, AWS Backup

---

### 🧠 Best Practices

* Implement **role-based access** (RBAC) or **attribute-based access** (ABAC) to protect sensitive files.
* Use **tokenization** or **masking** for personally identifiable information (PII).
* Maintain an **up-to-date data inventory** integrated with your asset management system.
* Enforce **multi-factor authentication (MFA)** for systems accessing sensitive data.
* Conduct **data protection impact assessments (DPIAs)** for high-risk processing activities.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                             |
| ---------------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Ensuring security and confidentiality of data, including access control and encryption. |
| **ISO/IEC 27001:2022** | A.8.10–A.8.12             | Data deletion, masking, and protection of data in transit and at rest.                  |
| **NIST CSF**           | PR.DS-1 to PR.DS-5        | Data-at-rest and data-in-transit are protected; data integrity is maintained.           |
| **GDPR**               | Article 32                | Security of processing, encryption, and confidentiality.                                |

---

### 📊 Example Policy Snippet

```text
All sensitive data must be classified and protected in accordance with its confidentiality level.  
Encryption must be applied to all sensitive data stored on enterprise systems and transmitted across public or untrusted networks.  
Data shall be retained only for as long as necessary for its business purpose and securely destroyed thereafter.
```

---

### 📚 References

* [CIS Control 03 – Data Protection](https://www.cisecurity.org/controls/data-protection)
* [NIST SP 800-53 Rev.5 – SC-12, SC-13, MP-6, SI-12](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 8.10–8.12](https://www.iso.org/standard/75652.html)
* [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/art-32-gdpr/)

---

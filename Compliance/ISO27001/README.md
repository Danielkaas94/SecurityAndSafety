# ISO/IEC 27001: Information Security Management System (ISMS)

ISO/IEC 27001:2022 defines the requirements for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS).  
It provides a structured approach to managing sensitive company information, ensuring it remains secure through a balance of **people**, **processes**, and **technology**.

---

## 📘 Purpose

This section of the repository aims to:
- Break down each clause and Annex A control in ISO 27001.
- Provide practical implementation guidance for organizations of all sizes.
- Map ISO 27001 controls to related frameworks like **NIS2** and **ISO 27002**.
- Help security teams and SOCs align their operational processes with international best practices.

---

## 🧭 Folder Structure

| Folder | Description |
|--------|--------------|
| **/clauses** | Contains detailed explanations and implementation guidance for Clauses 4–10 of ISO 27001. |
| **/annexA_controls** | Contains the 93 controls introduced in Annex A of the 2022 revision, grouped under A.5–A.8. |
| **/mappings** | Cross-references to related frameworks (e.g. NIS2, ISO 27002). |

---

## 📄 Core Clauses

| Clause | Title | Description |
|--------|--------|-------------|
| 4 | Context of the Organization | Define the internal and external context, interested parties, and ISMS scope. |
| 5 | Leadership | Establish top management commitment, roles, and responsibilities. |
| 6 | Planning | Identify risks and opportunities, establish objectives, and plan changes. |
| 7 | Support | Ensure adequate resources, competence, awareness, and communication. |
| 8 | Operation | Implement and control the processes needed to meet ISMS requirements. |
| 9 | Performance Evaluation | Monitor, measure, analyze, and evaluate ISMS performance. |
| 10 | Improvement | Drive continual improvement through corrective actions and audits. |

---

## 🧩 Annex A Control Groups

| Group | Description | Example Focus Areas |
|--------|--------------|---------------------|
| **A.5** | Organizational Controls | Policies, roles, risk management, and supplier security. |
| **A.6** | People Controls | Awareness, training, and disciplinary processes. |
| **A.7** | Physical Controls | Secure areas, equipment protection, and access management. |
| **A.8** | Technological Controls | System hardening, malware protection, backup, and monitoring. |

---

## 🔗 Mappings

The `/mappings` folder contains cross-framework relationships such as:
- **ISO 27001 ↔ NIS2**
- **ISO 27001 ↔ ISO 27002**
- (Future) ISO 27001 ↔ SOC 2 or CIS Controls

These mappings simplify compliance integration and demonstrate how overlapping controls can serve multiple frameworks simultaneously.

---

## 🛠 Practical Use Cases

This documentation can support:
- SOC alignment with ISO 27001 control requirements.
- Security posture assessments and internal audits.
- Policy creation and compliance evidence tracking.
- Integration of ISO 27001 with other regulatory frameworks (GDPR, NIS2, etc.).

---

## 🧠 References

- [ISO/IEC 27001:2022 – Official Standard](https://www.iso.org/standard/82875.html)
- [ISO/IEC 27002:2022 – Code of Practice for Information Security Controls](https://www.iso.org/standard/75652.html)
- [ENISA: Implementation Guidance for ISO 27001 & NIS2](https://www.enisa.europa.eu/)

---
---
---

## 🚧 Initial Folder Structure of ISO27001 🚧

```markdown
SecurityAndSafety/
└── compliance/
    ├── NIS2/
    └── ISO27001/
        ├── README.md
        ├── clauses/
        │   ├── 4_Context_of_the_organization.md
        │   ├── 5_Leadership.md
        │   ├── 6_Planning.md
        │   ├── 7_Support.md
        │   ├── 8_Operation.md
        │   ├── 9_Performance_evaluation.md
        │   └── 10_Improvement.md
        ├── annexA_controls/
        │   ├── A5_Organizational_controls.md
        │   ├── A6_People_controls.md
        │   ├── A7_Physical_controls.md
        │   └── A8_Technological_controls.md
        └── mappings/
            ├── ISO27001_to_NIS2.md
            └── ISO27001_to_ISO27002.md
```
### 📘 CIS Controls v8 (CIS18)

The **Center for Internet Security (CIS) Critical Security Controls**, also known as **CIS18**, is a prioritized set of actions designed to help organizations improve their cybersecurity posture. These controls provide prescriptive, actionable guidance to prevent, detect, and respond to the most common cyber threats.

The CIS Controls are developed and maintained by the **Center for Internet Security (CIS)** — a community-driven, non-profit organization focused on best practices for securing IT systems and data.

---

### 🧩 Purpose of This Folder

This section of the repository provides a structured overview of the **CIS18 controls**, each documented in a dedicated Markdown file.
The intent is to:

* Offer clear summaries of each control
* Highlight implementation examples and mappings to related frameworks (e.g., NIS2, ISO27001)
* Support internal security documentation and compliance alignment

---

# CIS Controls v8 (CIS18)

This folder contains documentation for all **18 CIS Critical Security Controls** (v8), detailing implementation steps, best practices, example tools, policies, and mappings to other frameworks such as **ISO27001**, **NIST CSF**, and **NIS2**.

The controls are designed to help organizations **prioritize and implement cybersecurity measures** to protect systems, data, and networks.

---

## 📑 Controls Overview

| #  | Control                                                | Description                                                              | Link                                                                                 |
| -- | ------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| 01 | Inventory and Control of Enterprise Assets             | Identify and manage hardware assets to reduce attack surface             | [Control 01](./Control_01_Inventory_and_Control_of_Enterprise_Assets.md)             |
| 02 | Inventory and Control of Software Assets               | Track and manage software installations to prevent unauthorized software | [Control 02](./Control_02_Inventory_and_Control_of_Software_Assets.md)               |
| 03 | Data Protection                                        | Protect sensitive data at rest and in transit                            | [Control 03](./Control_03_Data_Protection.md)                                        |
| 04 | Secure Configuration of Enterprise Assets and Software | Establish secure configurations and maintain baselines                   | [Control 04](./Control_04_Secure_Configuration_of_Enterprise_Assets_and_Software.md) |
| 05 | Account Management                                     | Manage user accounts, privileges, and access controls                    | [Control 05](./Control_05_Account_Management.md)                                     |
| 06 | Access Control Management                              | Implement least privilege and restrict unnecessary access                | [Control 06](./Control_06_Access_Control_Management.md)                              |
| 07 | Continuous Vulnerability Management                    | Identify, assess, and remediate vulnerabilities continuously             | [Control 07](./Control_07_Continuous_Vulnerability_Management.md)                    |
| 08 | Audit Log Management                                   | Collect, manage, and analyze logs for security monitoring                | [Control 08](./Control_08_Audit_Log_Management.md)                                   |
| 09 | Email and Web Browser Protections                      | Protect users from phishing, malware, and malicious websites             | [Control 09](./Control_09_Email_and_Web_Browser_Protections.md)                      |
| 10 | Malware Defenses                                       | Prevent, detect, and remediate malware infections                        | [Control 10](./Control_10_Malware_Defenses.md)                                       |
| 11 | Data Recovery                                          | Ensure data can be recovered after loss or incident                      | [Control 11](./Control_11_Data_Recovery.md)                                          |
| 12 | Network Infrastructure Management                      | Secure and monitor network devices and configurations                    | [Control 12](./Control_12_Network_Infrastructure_Management.md)                      |
| 13 | Security Awareness and Skills Training                 | Educate personnel to reduce human-driven risks                           | [Control 13](./Control_13_Security_Awareness_and_Skills_Training.md)                 |
| 14 | Security Monitoring                                    | Continuously monitor systems and networks for threats                    | [Control 14](./Control_14_Security_Monitoring.md)                                    |
| 15 | Service Provider Management                            | Assess and monitor third-party and vendor security                       | [Control 15](./Control_15_Service_Provider_Management.md)                            |
| 16 | Application Software Security                          | Secure software throughout development and deployment                    | [Control 16](./Control_16_Application_Software_Security.md)                          |
| 17 | Incident Response Management                           | Prepare for, detect, respond to, and recover from incidents              | [Control 17](./Control_17_Incident_Response_Management.md)                           |
| 18 | Penetration Testing                                    | Identify vulnerabilities proactively through testing                     | [Control 18](./Control_18_Penetration_Testing.md)                                    |

---

## ⚙️ How to Use

1. Browse each control to understand **purpose, implementation steps, and best practices**.
2. Refer to the **example tools** for practical deployment guidance.
3. Use the **policy snippets** to draft internal security policies.
4. Check **framework mappings** to align CIS controls with ISO27001, NIST CSF, and NIS2 compliance efforts.

---

## 📚 References

* [CIS Controls v8](https://www.cisecurity.org/controls/cis-controls-list/)
* [ISO/IEC 27001:2022](https://www.iso.org/standard/75652.html)
* [NIST Cybersecurity Framework (CSF)](https://www.nist.gov/cyberframework)
* [NIS2 Directive](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)

---

I can also **add a simple badge-style table or navigation links** at the top for easier GitHub browsing if you want a more polished README.

Do you want me to do that next?


---
---


## 🚧 Initial Folder Structure of CIS18 🚧

``` 
SecurityAndSafety/
└── compliance/
    ├── NIS2/
    ├── ISO27001/
    └── CIS18/
        ├── README.md
        └── Controls/
            ├── Control_01_Inventory_and_Control_of_Enterprise_Assets.md
            ├── Control_02_Inventory_and_Control_of_Software_Assets.md
            ├── Control_03_Data_Protection.md
            ├── Control_04_Secure_Configuration_of_Enterprise_Assets_and_Software.md
            ├── Control_05_Account_Management.md
            ├── Control_06_Access_Control_Management.md
            ├── Control_07_Continuous_Vulnerability_Management.md
            ├── Control_08_Audit_Log_Management.md
            ├── Control_09_Email_and_Web_Browser_Protections.md
            ├── Control_10_Malware_Defenses.md
            ├── Control_11_Data_Recovery.md
            ├── Control_12_Network_Infrastructure_Management.md
            ├── Control_13_Network_Monitoring_and_Defense.md
            ├── Control_14_Security_Awareness_and_Skills_Training.md
            ├── Control_15_Service_Provider_Management.md
            ├── Control_16_Application_Software_Security.md
            ├── Control_17_Incident_Response_Management.md
            └── Control_18_Penetration_Testing.md
```

---


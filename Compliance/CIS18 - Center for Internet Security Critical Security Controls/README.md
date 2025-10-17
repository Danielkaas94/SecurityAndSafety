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

### 🗂️ Folder Structure

| Control No. | Title                                                  | Description                                                                                                |
| ----------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| 01          | Inventory and Control of Enterprise Assets             | Maintain a detailed inventory of all enterprise assets to ensure only authorized devices are given access. |
| 02          | Inventory and Control of Software Assets               | Manage all software within the enterprise to prevent unauthorized or vulnerable applications.              |
| 03          | Data Protection                                        | Establish processes and technical controls to safeguard sensitive data.                                    |
| 04          | Secure Configuration of Enterprise Assets and Software | Ensure systems are securely configured and maintained.                                                     |
| 05          | Account Management                                     | Manage user accounts and permissions to minimize unauthorized access.                                      |
| 06          | Access Control Management                              | Implement role-based access and least privilege principles.                                                |
| 07          | Continuous Vulnerability Management                    | Continuously identify and remediate vulnerabilities.                                                       |
| 08          | Audit Log Management                                   | Collect and review audit logs for anomalies and incidents.                                                 |
| 09          | Email and Web Browser Protections                      | Secure email and web access to reduce phishing and malware risks.                                          |
| 10          | Malware Defenses                                       | Deploy and maintain tools to prevent and detect malware.                                                   |
| 11          | Data Recovery                                          | Implement reliable backup and restoration processes.                                                       |
| 12          | Network Infrastructure Management                      | Secure and maintain network infrastructure devices and configurations.                                     |
| 13          | Network Monitoring and Defense                         | Monitor network traffic and detect suspicious activity.                                                    |
| 14          | Security Awareness and Skills Training                 | Educate users on security best practices and emerging threats.                                             |
| 15          | Service Provider Management                            | Manage security risks associated with third-party service providers.                                       |
| 16          | Application Software Security                          | Integrate security practices throughout the software development lifecycle.                                |
| 17          | Incident Response Management                           | Establish and maintain an effective incident response process.                                             |
| 18          | Penetration Testing                                    | Test the effectiveness of security controls through authorized simulated attacks.                          |

---

### 🔗 References

* [Center for Internet Security – CIS Controls v8](https://www.cisecurity.org/controls/cis-controls-list)
* [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
* [NIST Cybersecurity Framework (NIST CSF)](https://www.nist.gov/cyberframework)

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
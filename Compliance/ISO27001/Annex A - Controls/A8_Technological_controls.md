# Annex A.8 — Technological Controls

## 🧭 Overview

Annex A.8 focuses on technological and system-level controls to protect information assets from cyber threats, unauthorized access, and data loss.  
These controls complement organizational, people, and physical measures.

---

## 🔑 Control Areas

| Control ID | Title                                                       | Summary                                                                                              |
| ---------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **A.8.1**  | User endpoint devices                                       | Ensure information processed, stored, or accessed through user devices is adequately protected.      |
| **A.8.2**  | Privileged access rights                                    | Limit and monitor privileged accounts to reduce risk of misuse or compromise.                        |
| **A.8.3**  | Information access restriction                              | Restrict access to information based on business and security requirements.                          |
| **A.8.4**  | Access to source code                                       | Protect source code from unauthorized access, modification, or disclosure.                           |
| **A.8.5**  | Secure authentication                                       | Implement strong authentication methods proportional to the access risk.                             |
| **A.8.6**  | Capacity management                                         | Ensure system capacity meets business demands and avoids performance degradation.                    |
| **A.8.7**  | Protection against malware                                  | Deploy and maintain controls to prevent, detect, and recover from malware infections.                |
| **A.8.8**  | Management of technical vulnerabilities                     | Identify, assess, and remediate technical vulnerabilities in a timely manner.                        |
| **A.8.9**  | Configuration management                                    | Establish and maintain secure configurations for hardware, software, and systems.                    |
| **A.8.10** | Information deletion                                        | Ensure secure deletion of data when no longer required, including on removable media and backups.    |
| **A.8.11** | Data masking                                                | Apply masking or anonymization to protect sensitive data in non-production environments.             |
| **A.8.12** | Data leakage prevention                                     | Implement measures to detect and prevent unauthorized transfer of information.                       |
| **A.8.13** | Information backup                                          | Regularly back up information and verify backups through testing and restoration.                    |
| **A.8.14** | Redundancy of information processing facilities             | Implement redundancy to ensure availability of critical services and information.                    |
| **A.8.15** | Logging                                                     | Record relevant events and retain logs to support monitoring, investigation, and compliance.         |
| **A.8.16** | Monitoring activities                                       | Monitor networks and systems for unusual or unauthorized activities.                                 |
| **A.8.17** | Clock synchronization                                       | Synchronize system clocks to a reliable time source for accurate log correlation.                    |
| **A.8.18** | Use of privileged utility programs                          | Restrict and monitor the use of powerful utilities that could override controls.                     |
| **A.8.19** | Installation of software on operational systems             | Ensure only authorized and verified software is installed on operational systems.                    |
| **A.8.20** | Networks security                                           | Protect network infrastructure and data in transit using secure architectures and controls.          |
| **A.8.21** | Security of network services                                | Ensure that network services are securely designed, configured, and managed.                         |
| **A.8.22** | Segregation of networks                                     | Separate networks based on sensitivity and business requirements to reduce risk.                     |
| **A.8.23** | Web filtering                                               | Control access to external websites to prevent exposure to threats or inappropriate content.         |
| **A.8.24** | Use of cryptography                                         | Apply cryptographic controls to protect confidentiality, integrity, and authenticity of information. |
| **A.8.25** | Secure development life cycle                               | Integrate security activities throughout all stages of system and software development.              |
| **A.8.26** | Application security requirements                           | Define and implement security requirements for applications and systems.                             |
| **A.8.27** | Secure system architecture and engineering principles       | Apply secure design principles to system and network architectures.                                  |
| **A.8.28** | Secure coding                                               | Enforce secure coding standards and perform code reviews to reduce vulnerabilities.                  |
| **A.8.29** | Security testing in development and acceptance              | Conduct security testing before releasing systems or applications into production.                   |
| **A.8.30** | Outsourced development                                      | Ensure third-party development follows the organization’s security requirements.                     |
| **A.8.31** | Separation of development, test and production environments | Maintain isolation between development, testing, and production environments.                        |
| **A.8.32** | Change management                                           | Control and document all changes to systems to reduce unintended impacts.                            |
| **A.8.33** | Test information                                            | Protect sensitive information used during testing and development activities.                        |
| **A.8.34** | Protection of information systems during audit testing      | Safeguard systems and data during internal or external audit activities.                             |

*Reference:*
- [Advisera: ISO 27001 Annex A Controls](https://advisera.com/iso27001/technological-controls/)

---

## 🧠 Implementation Tips

- Enforce **least privilege access** across all systems.  
- Maintain an **up-to-date asset inventory** to track devices and systems.  
- Perform **regular penetration testing and vulnerability scans**.  
- Implement **centralized logging** and SIEM for monitoring.  
- Backup critical data with **offsite or cloud redundancy**.  

---

## 📋 Example Evidence

| Area | Example Evidence |
|------|-----------------|
| Access Control | Access logs, user account reviews |
| Encryption | Certificates, configuration files |
| Logging | SIEM dashboards, alert reports |
| Backup | Backup logs, restoration tests |

---

## 🔗 Mappings

| Framework | Related Section |
|------------|-----------------|
| NIS2 | Operational and Cybersecurity Controls |
| ISO 27002 | Section 8 |
| CIS Controls | 4: Secure Configuration, 7: Email and Web Protections, 8: Malware Defenses |

---

## 🏛 Annex A Controls

| Annex A Group | Link |
|---------------|------|
| A.5 Organizational Controls | [A5_Organizational_controls.md](./A5_Organizational_controls.md) |
| A.6 People Controls | [A6_People_controls.md](./A6_People_controls.md) |
| A.7 Physical Controls | [A7_Physical_controls.md](./A7_Physical_controls.md) |
| A.8 Technological Controls | [A8_Technological_controls.md](./A8_Technological_controls.md) |

---

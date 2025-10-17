## CIS Control 04: Secure Configuration of Enterprise Assets and Software

### 🎯 Purpose

Establish and maintain **secure configurations** for all enterprise assets, including workstations, servers, network devices, and software, to reduce vulnerabilities and prevent attackers from exploiting default or weak settings.

The goal is to ensure systems are **hardened** against attacks from misconfigurations and to enforce consistency across the organization.

---

### 🧩 Key Principles

* **Baseline Security:** Define and enforce standard configurations for all asset types.
* **Change Management:** Track configuration changes to detect unauthorized modifications.
* **Continuous Monitoring:** Ensure deviations from secure baselines are identified and corrected promptly.
* **Automation:** Use tools to apply and enforce configurations at scale.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **4.1** | Establish a **baseline secure configuration** for all asset types (workstations, servers, network devices, cloud resources, applications). |
| **4.2** | Implement automated configuration management tools to deploy and enforce baselines.                                                        |
| **4.3** | Harden operating systems and applications by disabling unnecessary services, ports, and accounts.                                          |
| **4.4** | Regularly review vendor security guidelines and benchmarks (e.g., CIS Benchmarks, NIST STIGs).                                             |
| **4.5** | Monitor for deviations from baseline configurations and remediate promptly.                                                                |
| **4.6** | Document and approve all configuration changes via change management processes.                                                            |
| **4.7** | Periodically audit configurations to validate compliance with internal policies and regulatory requirements.                               |

---

### 🧰 Example Tools

* **Configuration Management:** Ansible, Puppet, Chef, SaltStack
* **Hardening Guides:** CIS Benchmarks, Microsoft Security Baselines, NIST STIGs
* **Monitoring & Auditing:** OpenSCAP, Lynis, Tripwire, OSSEC

---

### 🧠 Best Practices

* Maintain separate baselines for **different asset types** and **environments** (production, test, development).
* Use **version-controlled configuration repositories** for transparency and rollback.
* Automate configuration drift detection and remediation wherever possible.
* Integrate secure configuration checks into **continuous integration/continuous deployment (CI/CD)** pipelines.
* Include cloud infrastructure (AWS, Azure, GCP) in configuration management and hardening efforts.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                                        |
| ---------------------- | ------------------------- | -------------------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Ensures secure configuration and patching of network and information systems.                      |
| **ISO/IEC 27001:2022** | A.8.1 & A.14.2            | Security requirements for systems acquisition, development, and maintenance; hardening of systems. |
| **NIST CSF**           | PR.IP-1 / PR.IP-3         | Systems are configured securely and monitored for compliance with baselines.                       |

---

### 📊 Example Policy Snippet

```text
All enterprise assets must adhere to approved secure configuration baselines.  
No asset shall run with default credentials, unnecessary services, or unapproved software.  
Configuration changes must be documented, approved, and deployed via automated configuration management tools.  
Periodic audits shall verify compliance with baseline standards.
```

---

### 📚 References

* [CIS Control 04 – Secure Configuration of Enterprise Assets and Software](https://www.cisecurity.org/controls/secure-configuration-of-enterprise-assets-and-software)
* [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks/)
* [NIST SP 800-53 Rev.5 – CM-2, CM-6, CM-7](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 14.2](https://www.iso.org/standard/75652.html)

---

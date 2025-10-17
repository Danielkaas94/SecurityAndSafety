## CIS Control 18: Penetration Testing

### 🎯 Purpose

Conduct **regular penetration testing** to identify vulnerabilities and weaknesses in systems, networks, and applications before attackers can exploit them.

The goal is to **proactively discover and remediate security gaps** to improve overall organizational security posture.

---

### 🧩 Key Principles

* **Proactive Assessment:** Identify vulnerabilities before they are exploited.
* **Comprehensive Coverage:** Test systems, applications, networks, and configurations.
* **Prioritization:** Focus on high-risk areas first.
* **Remediation:** Address findings promptly and track resolution.

---

### ⚙️ Implementation Steps

| Step     | Description                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------ |
| **18.1** | Develop a **penetration testing program** that defines scope, frequency, and methodology.                    |
| **18.2** | Conduct **internal and external tests**, including network, application, and social engineering assessments. |
| **18.3** | Use qualified personnel or third-party providers to perform penetration tests.                               |
| **18.4** | Document findings, including vulnerabilities, potential impact, and recommended mitigations.                 |
| **18.5** | Prioritize remediation based on **risk and criticality** of the findings.                                    |
| **18.6** | Track remediation and retest to ensure vulnerabilities are addressed.                                        |
| **18.7** | Integrate penetration testing results into **risk management and security improvement plans**.               |

---

### 🧰 Example Tools

* **Network & Web Application Testing:** Nmap, Nessus, OpenVAS, Burp Suite, OWASP ZAP
* **Red Teaming Platforms:** Cobalt Strike, Metasploit, Core Impact
* **Reporting & Tracking:** Jira, ServiceNow, Dradis, DefectDojo

---

### 🧠 Best Practices

* Conduct tests **regularly** and after major changes or deployments.
* Combine **automated scanning with manual testing** for depth and accuracy.
* Ensure testing does **not disrupt critical operations**.
* Validate that **remediated vulnerabilities** are fixed with follow-up testing.
* Maintain **confidentiality** and legal compliance during all tests.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                                               |
| ---------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Penetration testing helps identify weaknesses that could impact critical network and information systems. |
| **ISO/IEC 27001:2022** | A.12.6, A.14.2            | Testing and evaluation of security controls to ensure effectiveness.                                      |
| **NIST CSF**           | PR.IP-12 / DE.CM-8        | Vulnerabilities are identified through testing, and remediation is applied.                               |

---

### 📊 Example Policy Snippet

```text
Penetration tests must be conducted at least annually and after significant changes to systems or applications.  
Findings must be documented, prioritized based on risk, and remediated within defined timelines.  
Remediation effectiveness must be validated through follow-up testing.
```

---

### 📚 References

* [CIS Control 18 – Penetration Testing](https://www.cisecurity.org/controls/penetration-testing)
* [NIST SP 800-115 – Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/publications/detail/sp/800-115/final)
* [ISO/IEC 27002:2022 – Clause 12.6, 14.2](https://www.iso.org/standard/75652.html)

---

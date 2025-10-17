## CIS Control 09: Email and Web Browser Protections

### 🎯 Purpose

Implement safeguards for **email and web browsers**, the two most common vectors for malware, phishing, and other cyberattacks, to protect users and enterprise systems.

The goal is to **reduce the risk of compromise** by controlling content, enforcing safe configurations, and monitoring for threats.

---

### 🧩 Key Principles

* **Threat Mitigation:** Block malicious content before it reaches users.
* **Secure Configurations:** Harden browsers and email clients against exploitation.
* **User Awareness:** Educate users on safe email and web practices.
* **Monitoring:** Detect and respond to suspicious or malicious activity from email and web traffic.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| **9.1** | Enforce email filtering for **spam, phishing, and malware**, including URL and attachment scanning.                |
| **9.2** | Configure browsers and email clients securely, disabling unnecessary plugins, scripts, and auto-download features. |
| **9.3** | Deploy **anti-phishing solutions** and domain-based email authentication (SPF, DKIM, DMARC).                       |
| **9.4** | Monitor for **malicious or suspicious URLs and attachments** in emails and web traffic.                            |
| **9.5** | Maintain an updated **allowlist/denylist** for email attachments, domains, and websites.                           |
| **9.6** | Educate users on **safe browsing** and **email practices**, including recognizing phishing attempts.               |
| **9.7** | Integrate email and web protections with endpoint security and SIEM for detection and alerting.                    |

---

### 🧰 Example Tools

* **Email Security:** Proofpoint, Mimecast, Microsoft Defender for Office 365
* **Web Filtering:** Zscaler, Cisco Umbrella, Palo Alto URL Filtering
* **Anti-Phishing:** KnowBe4, Cofense, PhishMe
* **Browser Hardening:** Group Policy, Microsoft Edge/Chrome security templates

---

### 🧠 Best Practices

* Apply **automatic updates** to browsers, email clients, and associated plugins.
* Block or restrict **macros and scripts** in attachments unless explicitly needed.
* Use **sandboxing** for suspicious attachments or untrusted websites.
* Maintain **DNS filtering** and **secure web gateways** to prevent access to malicious domains.
* Train employees with **regular phishing simulations** and awareness programs.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                            |
| ---------------------- | ------------------------- | -------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Email and web protections reduce risk to network and information systems.              |
| **ISO/IEC 27001:2022** | A.12.2, A.13.1            | Protection against malware and secure network services, including email and web usage. |
| **NIST CSF**           | PR.AT-1 / PR.DS-5         | Users are informed and trained; protective measures against malware are applied.       |

---

### 📊 Example Policy Snippet

```text
All email and web traffic must be filtered for spam, phishing, and malware before reaching end users.  
Browsers and email clients must be configured according to approved security baselines.  
Users must complete annual training on safe email and web practices, and phishing simulations will be conducted quarterly.
```

---

### 📚 References

* [CIS Control 09 – Email and Web Browser Protections](https://www.cisecurity.org/controls/email-and-web-browser-protections)
* [NIST SP 800-53 Rev.5 – SC-7, SC-18, SI-3](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 12.2, 13.1](https://www.iso.org/standard/75652.html)

---

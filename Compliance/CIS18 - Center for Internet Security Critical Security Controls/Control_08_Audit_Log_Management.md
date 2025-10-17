## CIS Control 08: Audit Log Management

### 🎯 Purpose

Collect, manage, and analyze **audit logs** from systems, applications, and network devices to detect suspicious activity, support incident response, and maintain accountability.

The goal is to ensure **visibility into user and system behavior**, enabling timely detection of threats and aiding forensic investigations.

---

### 🧩 Key Principles

* **Comprehensive Logging:** Capture all relevant events for security monitoring.
* **Integrity:** Ensure logs are protected from tampering or unauthorized access.
* **Retention:** Maintain logs long enough to support investigations and compliance requirements.
* **Analysis:** Regularly review and correlate logs to identify anomalies and potential threats.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------- |
| **8.1** | Identify critical systems, applications, and devices for log collection.                                   |
| **8.2** | Enable **audit logging** for user authentication, system changes, application events, and security alerts. |
| **8.3** | Centralize logs using a **Security Information and Event Management (SIEM)** solution.                     |
| **8.4** | Protect logs from tampering using **write-once storage**, encryption, or digital signatures.               |
| **8.5** | Define log retention policies based on regulatory requirements and business needs.                         |
| **8.6** | Continuously monitor and analyze logs to detect anomalies, suspicious activity, or policy violations.      |
| **8.7** | Integrate log review into incident response procedures and periodic audits.                                |

---

### 🧰 Example Tools

* **SIEM:** Splunk, ELK Stack, Graylog, IBM QRadar, Microsoft Sentinel
* **Log Collection:** syslog, rsyslog, nxlog, Fluentd
* **Integrity & Storage:** WORM storage, encrypted log archives, blockchain-based logging

---

### 🧠 Best Practices

* Collect logs from **all critical sources**, including servers, endpoints, firewalls, routers, and cloud platforms.
* Ensure **time synchronization** across systems (e.g., using NTP) for accurate correlation.
* Implement **real-time alerting** for high-priority events.
* Regularly test **log collection and alerting processes** to ensure reliability.
* Maintain separation of duties so that log administrators cannot alter security logs without oversight.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                             |
| ---------------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Ensures logging, monitoring, and reporting of critical network and information systems. |
| **ISO/IEC 27001:2022** | A.12.4                    | Event logging, monitoring, and retention for auditing and forensic purposes.            |
| **NIST CSF**           | DE.CM-7 / DE.CM-8         | Logs are collected, protected, and analyzed to detect cybersecurity events.             |

---

### 📊 Example Policy Snippet

```text
All critical systems must generate audit logs for authentication events, administrative actions, and security-relevant changes.  
Logs must be transmitted to a centralized SIEM and protected from modification.  
Retention of logs shall comply with legal and regulatory requirements, and logs must be reviewed at least weekly for anomalies.
```

---

### 📚 References

* [CIS Control 08 – Audit Log Management](https://www.cisecurity.org/controls/audit-log-management)
* [NIST SP 800-53 Rev.5 – AU-2, AU-6, AU-12](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 12.4](https://www.iso.org/standard/75652.html)

---

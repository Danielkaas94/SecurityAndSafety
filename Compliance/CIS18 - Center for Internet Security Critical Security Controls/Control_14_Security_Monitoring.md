## CIS Control 14: Security Monitoring

### 🎯 Purpose

Implement continuous **security monitoring** of systems, networks, and applications to detect unauthorized activity, anomalous behavior, and potential security incidents.

The goal is to **identify threats early**, support rapid response, and reduce the impact of security breaches.

---

### 🧩 Key Principles

* **Visibility:** Ensure all critical systems and networks are monitored.
* **Real-Time Detection:** Identify suspicious activity promptly.
* **Correlation & Analysis:** Aggregate and analyze data from multiple sources to detect threats.
* **Integration:** Feed monitoring insights into incident response and remediation workflows.

---

### ⚙️ Implementation Steps

| Step     | Description                                                                                                                 |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |
| **14.1** | Define the scope of monitoring for all critical systems, applications, and network segments.                                |
| **14.2** | Deploy **security monitoring tools** such as SIEM, IDS/IPS, endpoint detection, and logging solutions.                      |
| **14.3** | Collect and centralize logs and events from all relevant sources, including endpoints, network devices, and cloud services. |
| **14.4** | Correlate events to detect suspicious patterns, anomalies, and potential threats.                                           |
| **14.5** | Establish **alerting and escalation procedures** for detected threats.                                                      |
| **14.6** | Continuously tune monitoring rules and alerts to reduce false positives and improve detection accuracy.                     |
| **14.7** | Integrate monitoring outputs with incident response, threat intelligence, and vulnerability management processes.           |

---

### 🧰 Example Tools

* **SIEM Platforms:** Splunk, ELK Stack, IBM QRadar, Microsoft Sentinel
* **IDS/IPS:** Snort, Suricata, Palo Alto, Cisco Firepower
* **Endpoint Detection & Response (EDR):** CrowdStrike Falcon, SentinelOne, Microsoft Defender for Endpoint
* **Network Monitoring:** Nagios, Zabbix, SolarWinds

---

### 🧠 Best Practices

* Ensure **comprehensive coverage** across all critical assets, including cloud and remote endpoints.
* Correlate multiple log sources for **early threat detection**.
* Establish **baseline behaviors** to detect deviations indicative of compromise.
* Regularly **review alerts and monitoring effectiveness**, updating rules and thresholds.
* Maintain **integration with SOC and incident response teams** for rapid action.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                               |
| ---------------------- | ------------------------- | ----------------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Continuous monitoring ensures security and resilience of network and information systems. |
| **ISO/IEC 27001:2022** | A.12.4, A.16.1            | Event monitoring, detection of security events, and response procedures.                  |
| **NIST CSF**           | DE.CM-1 / DE.CM-7         | Monitoring of networks and systems is continuous and anomalies are detected and reported. |

---

### 📊 Example Policy Snippet

```text
All critical systems, applications, and network devices must be continuously monitored for anomalous or suspicious activity.  
Security events must be centralized in a SIEM, correlated, and reviewed daily.  
Alerts must follow documented escalation procedures and feed directly into incident response workflows.
```

---

### 📚 References

* [CIS Control 14 – Security Monitoring](https://www.cisecurity.org/controls/security-monitoring)
* [NIST SP 800-53 Rev.5 – SI-4, SI-7, AU-6](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 12.4, 16.1](https://www.iso.org/standard/75652.html)

---

## CIS Control 12: Network Infrastructure Management

### 🎯 Purpose

Establish processes to **secure and manage network infrastructure**, including routers, switches, firewalls, and other network devices, to reduce vulnerabilities and prevent unauthorized access or disruption.

The goal is to ensure **network security, stability, and availability** while minimizing exposure to attacks.

---

### 🧩 Key Principles

* **Inventory:** Maintain an accurate list of all network devices.
* **Segmentation:** Divide networks to limit lateral movement of attackers.
* **Secure Configurations:** Harden network devices and enforce baseline configurations.
* **Monitoring:** Continuously monitor network traffic for anomalies.
* **Change Control:** Track and authorize network configuration changes.

---

### ⚙️ Implementation Steps

| Step     | Description                                                                                                          |
| -------- | -------------------------------------------------------------------------------------------------------------------- |
| **12.1** | Maintain an **up-to-date inventory** of all network devices, including IP addresses and configurations.              |
| **12.2** | Harden devices by disabling unnecessary services, changing default credentials, and applying security updates.       |
| **12.3** | Implement **network segmentation and zoning** to separate sensitive systems from general access.                     |
| **12.4** | Use **firewalls, intrusion detection/prevention systems (IDS/IPS), and VPNs** to protect network boundaries.         |
| **12.5** | Monitor network traffic and logs for anomalies, suspicious activity, or unauthorized access.                         |
| **12.6** | Apply change management for all network configuration modifications, including approval, testing, and documentation. |
| **12.7** | Periodically audit network devices to ensure compliance with security policies and baselines.                        |

---

### 🧰 Example Tools

* **Network Monitoring:** Nagios, PRTG, SolarWinds, Zabbix
* **IDS/IPS:** Snort, Suricata, Palo Alto, Cisco Firepower
* **Firewalls & VPNs:** pfSense, Cisco ASA/ISE, Fortinet, Palo Alto
* **Configuration Management:** Ansible, Puppet, Cisco DNA Center

---

### 🧠 Best Practices

* Segment critical systems (e.g., servers, sensitive data) from end-user networks.
* Regularly update firmware and software on all network devices.
* Enforce **strong authentication** for network device administration.
* Implement **network access control (NAC)** for devices connecting to the network.
* Continuously **monitor for unusual traffic patterns** indicative of attacks or misconfigurations.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                         |
| ---------------------- | ------------------------- | ----------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Secure configuration and monitoring of critical network infrastructure.             |
| **ISO/IEC 27001:2022** | A.12.1, A.13.1            | Network security management; secure configuration and monitoring of communications. |
| **NIST CSF**           | PR.IP-1 / PR.PT-1         | Network devices are securely configured and continuously monitored.                 |

---

### 📊 Example Policy Snippet

```text
All network devices must be inventoried, hardened, and maintained according to approved baselines.  
Network segmentation must be enforced to separate sensitive systems, and all configuration changes must follow change management procedures.  
Network traffic must be continuously monitored for anomalies and unauthorized access.
```

---

### 📚 References

* [CIS Control 12 – Network Infrastructure Management](https://www.cisecurity.org/controls/network-infrastructure-management)
* [NIST SP 800-53 Rev.5 – AC-4, SC-7, CM-2](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 12.1, 13.1](https://www.iso.org/standard/75652.html)

---

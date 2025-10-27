# ⚙️ ELK Stack Crash Course (SIEM Edition)

A practical introduction to using Elasticsearch, Logstash, and Kibana for SOC and security monitoring.

---

## 🔍 1. What Is the ELK Stack?

**ELK = Elasticsearch + Logstash + Kibana**

| Component | Purpose | Example Use |
|------------|----------|--------------|
| **Elasticsearch** | Storage and search engine | Stores logs, enables fast search queries |
| **Logstash** | Data pipeline | Ingests and parses logs from multiple sources |
| **Kibana** | Visualization and dashboard tool | Displays dashboards, visualizations, and alerts |

> Together, they form the backbone of an open-source SIEM, sometimes extended with **Beats** (lightweight agents) or **Elastic Agent / Fleet** for centralized management.

---

## 🧱 2. ELK Architecture Overview

```mermaid
flowchart LR
    A[Beats / Syslog / Agents] --> B[Logstash]
    B --> C[Elasticsearch]
    C --> D[Kibana Dashboard]
    D --> E[Analyst Review & Alerts]
````

**Data Flow:**

1. Logs are collected by agents (e.g., Filebeat, Winlogbeat, Auditbeat).
2. Logstash parses and enriches logs.
3. Elasticsearch indexes and stores the data.
4. Kibana visualizes and queries events for analysts.

---

## 🧩 3. Common Data Sources

| Source             | Type        | Example Log Fields                 |
| ------------------ | ----------- | ---------------------------------- |
| Windows Event Logs | Host-based  | EventID, User, Process, IP         |
| Sysmon             | Host-based  | CommandLine, ParentProcess, Hash   |
| Firewall Logs      | Network     | Source IP, Destination IP, Action  |
| Web Server Logs    | Application | URL, Response Code, Referrer       |
| EDR/NDR Alerts     | Security    | Alert Type, Severity, Indicator    |
| Authentication     | Identity    | Username, Logon Type, Success/Fail |

---

## ⚙️ 4. Logstash Basics

Logstash uses **pipelines** with *input*, *filter*, and *output* sections.

### Example: Ingest Windows Event Logs via Winlogbeat

```conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [event_id] == 4625 {
    mutate { add_tag => ["failed_login"] }
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "windows-events-%{+YYYY.MM.dd}"
  }
}
```

This example:

* Receives logs from **Beats agents**
* Tags failed login attempts
* Sends the data to Elasticsearch for indexing

---

## 🧮 5. Elasticsearch Essentials

### Common Terms

| Term         | Meaning                                                 |
| ------------ | ------------------------------------------------------- |
| **Index**    | Collection of related documents (like a database table) |
| **Document** | Single JSON object (like a database row)                |
| **Field**    | Data attribute (e.g., `source.ip`, `event.code`)        |
| **Query**    | Search instruction (e.g., all failed logins)            |

### Sample Query (KQL)

```kql
event.code:4625 AND user.name:"administrator"
```

### REST API Query (JSON)

```bash
GET /windows-events-*/_search
{
  "query": {
    "match": { "event.code": "4625" }
  }
}
```

---

## 📊 6. Kibana for Analysts

### Dashboards and Visualizations

In Kibana:

1. Go to **Discover** → Explore indexed data
2. Use **Visualize** → Create charts and metrics
3. Build **Dashboards** → Combine multiple visualizations

Common SOC Dashboards:

* Failed vs Successful Logins (by country, time, user)
* PowerShell Command Activity
* File Access or Modification Events
* Network Traffic Heatmap
* Top 10 Hosts by Alert Count

---

## 🚨 7. Alerts & Detection Rules

Kibana’s **Detection Engine** lets you create rules like in commercial SIEMs.

### Example Rule (JSON)

```json
{
  "rule_id": "failed_login_bruteforce",
  "name": "Multiple Failed Logins (Bruteforce Detection)",
  "index": ["windows-events-*"],
  "query": "event.code:4625",
  "from": "now-5m",
  "to": "now",
  "threshold": {
    "field": "user.name",
    "value": 5
  },
  "severity": "medium"
}
```

This rule triggers if a user has **5+ failed logins** in 5 minutes.

---

## 🧠 8. Enrichment and Correlation

To make ELK behave more like a full SIEM:

* **Enrich IPs** with GeoIP and ASN lookups
* **Map hashes** to VirusTotal or internal threat intel feeds
* **Correlate events** across time windows using **Logstash aggregate filter**
* Use **Elastic Common Schema (ECS)** for consistent field naming

---

## 🛠 9. Example Beats Configuration

Example `filebeat.yml` snippet to collect and ship logs:

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/auth.log
    fields:
      source_type: "auth"
output.logstash:
  hosts: ["localhost:5044"]
```

---

## 🔐 10. SOC Use Cases with ELK

| Use Case              | Description                                      | Detection Method                 |
| --------------------- | ------------------------------------------------ | -------------------------------- |
| Brute Force Login     | Identify repeated login failures                 | `event.code:4625` with threshold |
| Suspicious PowerShell | Detect encoded command lines                     | `process.command_line:* -enc*`   |
| Data Exfiltration     | Monitor large outbound transfers                 | Traffic volume > threshold       |
| Lateral Movement      | RDP or SMB connections between hosts             | `network.protocol:RDP`           |
| Privilege Escalation  | Monitor `whoami` and `net localgroup` executions | Command line analysis            |

---

## 🧩 11. Advanced: Extending ELK to SIEM+

| Feature             | Add-on                                                                  |
| ------------------- | ----------------------------------------------------------------------- |
| Threat Intelligence | [Elastic Security](https://www.elastic.co/security) or MISP integration |
| Case Management     | TheHive or Kibana Cases                                                 |
| Automation          | Cortex SOAR or ElastAlert                                               |
| Long-Term Retention | S3 / Cold storage tiers                                                 |
| Dashboards          | Sigma → Kibana converter or Sigma rules directly                        |

---

## 📚 12. References & Learning Resources

* [Elastic Security Documentation](https://www.elastic.co/guide/en/security/current/index.html)
* [Beats Overview](https://www.elastic.co/beats/)
* [Logstash Filter Reference](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html)
* [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current/index.html)
* [Sigma Rules Repository](https://github.com/SigmaHQ/sigma)

---

### ✅ Summary

The ELK Stack can serve as a powerful **low-cost SIEM solution** if properly tuned:

* **Logstash** = normalization
* **Elasticsearch** = storage and query power
* **Kibana** = analysis and visualization
* **Elastic Security** = detection and alerting layer

Combined, they provide a strong foundation for a modern SOC — flexible, open, and deeply customizable.

---

*Next step recommendation: Build your own simple ELK lab with Winlogbeat and Sysmon logs from a Windows VM. Once it runs, practice creating queries, visualizations, and detection rules.*




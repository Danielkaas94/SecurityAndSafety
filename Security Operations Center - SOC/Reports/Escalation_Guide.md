# 🧭 Escalation Guide

After completing your alert report and reaching a verdict, the next step is determining whether the alert should be escalated to Level 2 (L2) analysts or other teams.  
Proper escalation ensures that critical incidents receive prompt attention and that the SOC operates efficiently as a tiered system.

---

## 🎯 When to Escalate

You should **escalate** an alert to L2 under any of the following conditions:

| Condition | Description |
|------------|--------------|
| **Major Attack Indicators** | The alert suggests a large-scale or advanced intrusion (e.g., ransomware, APT activity, data exfiltration). |
| **Remediation Required** | Manual actions are needed, such as malware removal, host isolation, or password resets. |
| **Cross-Team Communication Needed** | The situation involves other departments, customers, management, or external entities (e.g., law enforcement). |
| **Uncertain Verdict** | You do not fully understand the alert or need assistance from a more experienced analyst. |

> 💡 **Tip:** Escalate early if in doubt. It’s better to hand off a benign alert than to miss a critical one.

---

## 🔄 Escalation Steps

Escalation procedures vary between SOC teams, but the following workflow is standard and adaptable to most setups.

### 1. Write the Alert Report  
Ensure your **Five Ws** (Who, What, When, Where, Why) are clearly documented and that your verdict (True Positive / False Positive / Needs Review) is justified.

### 2. Change the Alert Status  
Update the alert in the SOC dashboard (e.g., Splunk ES, TheHive, Cortex SOAR) to **“In Progress”** or **“Escalated”** depending on internal policy.

### 3. Assign to L2  
Reassign the alert or ticket to the **L2 analyst on shift**. This will typically trigger an automatic notification.

### 4. Notify L2  
Ping the assigned L2 in the corporate chat (Slack, Teams, etc.) or inform them directly in person if required.  
Include:
- The alert/ticket ID  
- A summary of your findings  
- Any immediate concerns (e.g., ongoing lateral movement)

### 5. Await Feedback  
L2 will:
- Review your report and findings  
- Conduct deeper analysis (e.g., reverse engineering, memory forensics, lateral movement mapping)  
- Contact you if clarification is needed  
- Begin Incident Response procedures if escalation confirms a major security incident  

---

## 🧩 SOC Dashboard Escalation Flow

```mermaid
flowchart TD
    A[🔔 Alert Triggered in SIEM] --> B[👀 L1 Analyst Reviews Alert]
    B --> C{Verdict Reached?}
    C -->|False Positive| D[🗑 Close Alert]
    C -->|True Positive / Unclear| E[📝 Write Report (Five Ws)]
    E --> F[🔄 Set Status: In Progress]
    F --> G[👆 Assign to L2 On-Shift]
    G --> H[💬 Notify via Chat or Ticket System]
    H --> I[L2 Reviews & Confirms Details]
    I --> J{Incident Severity?}
    J -->|Minor| K[✔ Mark as Resolved]
    J -->|Major| L[🚨 Start Incident Response Process]
```

---

## 🧠 L2 Responsibilities After Escalation

Once an alert has been escalated, the **Level 2 Analyst** assumes ownership of the case and proceeds as follows:

| Task                            | Description                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------- |
| **Validate L1 Findings**        | Confirm that the alert is indeed a True Positive and the data supports escalation.        |
| **Deeper Technical Analysis**   | Perform advanced triage using logs, forensics, and threat intelligence.                   |
| **Coordinate with Other Teams** | Communicate with IT, network, or DFIR teams as necessary for containment and remediation. |
| **Incident Classification**     | Determine whether the case qualifies as a formal **security incident**.                   |
| **Document Actions Taken**      | Add detailed notes and updates to the same ticket for full traceability.                  |
| **Close or Escalate Further**   | Resolve the alert if it’s contained or escalate to L3 / IR if required.                   |

---

## ✅ Key Takeaways

* Always **document before escalation** — the L2 analyst should not need to reconstruct the situation from scratch.
* **Communication is critical** — concise, factual, and structured handoffs save hours of investigation time.
* The **quality of escalation** reflects the maturity of your SOC — clear, evidence-based reports ensure consistency and build trust across tiers.

---

**Next Recommended Reading:**

* [Alert Reporting Guide](./Reporting_Guide.md)
* [Incident Response Procedures (coming soon)](#)

# 🚨 Alert Report — Data Exfiltration Attempt

**Date:** 2025-04-29  
**Analyst:** Daniel K.  
**Alert ID:** SOC-2025-00512  
**Verdict:** ✅ True Positive  
**Severity:** Critical  

---

## 🧩 Five Ws Analysis

**Who:**  
User *it-admin@company.local*

**What:**  
Large outbound data transfer (3.8 GB) to Dropbox via unauthorized client.

**When:**  
Started 22:14 CET, completed 22:17 CET.

**Where:**  
Workstation *IT-ADMIN01*, IP *10.0.10.55*  
Destination: *dropboxusercontent.com (162.125.4.4)*

**Why:**  
No business justification. SIEM correlation matched insider threat model (rule: "High volume transfer after-hours").

---

## 🧪 Evidence Collected

| Source | Evidence |
|--------|-----------|
| Proxy Logs | 3.8 GB uploaded to Dropbox |
| Sysmon | Process `DropboxUploader.exe` (unsigned) |
| Threat Intel | File hash unknown, first seen today |
| User HR Data | User under performance review (contextual flag) |

---

## 🧠 Analyst Notes

Potential insider data theft or policy breach.  
Immediate containment recommended.

---

## 🚩 Escalation Decision

**Escalated to L2 + DFIR** — full forensic acquisition, HR involvement, and legal notification required.

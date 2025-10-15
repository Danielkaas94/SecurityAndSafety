# 🧠 Alert Report — Phishing Attempt Detected

**Date:** 2025-03-18  
**Analyst:** Daniel K.  
**Alert ID:** SOC-2025-00341  
**Verdict:** ✅ True Positive  
**Severity:** Medium  

---

## 🧩 Five Ws Analysis

**Who:**  
User *anna.larsen@company.local* reported a suspicious email received from *"HR-Portal <hr-portal@outlook.com>"*.

**What:**  
The email contained a link leading to a fake login page impersonating Microsoft 365. URL was *hxxps://m365-verification[.]info*.

**When:**  
Email received at 09:13 CET. User reported the email at 09:27 CET.

**Where:**  
Mail gateway log confirmed inbound SMTP connection from IP *185.203.119.83* (AS20473, Netherlands).

**Why:**  
Indicators matched known phishing campaigns from open-source intelligence feeds (Abuse.ch and PhishTank).  
The link was live at time of investigation.

---

## 🧪 Evidence Collected

| Source | Evidence |
|--------|-----------|
| Email Header | SPF fail, DKIM fail |
| Attachment | None |
| URL Scan | Domain age < 24 hours, category: phishing |
| Threat Intel | Matched IOC from PhishTank list |

---

## 🧠 Analyst Notes

User awareness training appears effective — user reported within minutes.  
Recommend blocking domain and sender at gateway level.

---

## 🚩 Escalation Decision

**Not escalated to L2** — alert contained sufficient context, no compromise detected.  
Preventive actions documented and domain blacklisted.

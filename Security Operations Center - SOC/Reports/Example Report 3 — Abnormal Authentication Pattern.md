# 🔐 Alert Report — Abnormal Authentication Pattern

**Date:** 2025-04-11  
**Analyst:** Daniel K.  
**Alert ID:** SOC-2025-00463  
**Verdict:** ⚠️ Needs Review  
**Severity:** Medium  

---

## 🧩 Five Ws Analysis

**Who:**  
User: *morten.hansen@company.local*

**What:**  
Multiple failed logins to VPN followed by successful login from an IP in Poland.

**When:**  
Failures between 01:43–01:51 CET, successful login at 01:52 CET.

**Where:**  
Source IP: *45.134.56.192* (Warsaw, PL)

**Why:**  
Unusual location for user’s profile. No known travel notification.

---

## 🧪 Evidence Collected

| Source | Evidence |
|--------|-----------|
| VPN Logs | 8 failed attempts followed by success |
| GeoIP | High-risk country |
| SIEM Correlation | User login baseline: Denmark only |
| Threat Intel | IP listed in 1 abuse feed (low confidence) |

---

## 🧠 Analyst Notes

Could be legitimate user traveling, but needs verification.  
No MFA push spam detected.

---

## 🚩 Escalation Decision

**Escalated to L2** — verify via HR or direct user contact.  
Recommend temporary MFA reset if no confirmation.

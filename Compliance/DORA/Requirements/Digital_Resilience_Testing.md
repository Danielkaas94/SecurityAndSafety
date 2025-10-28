# Digital_Resilience_Testing.md
**DORA — Digital Operational Resilience Testing (Including TLPT)**

## Purpose
Ensure that critical functions and ICT systems are tested regularly to validate resilience, detect weaknesses, and verify recovery and response capabilities.

## Scope
Critical functions, systems supporting critical/important services, production and pre-production environments as applicable.

## Core Requirements (derived from DORA — Article 26 and RTS on TLPT)
1. **Testing Programme**
   - Maintain a documented testing programme covering: periodic vulnerability scanning, penetration testing, disaster recovery exercises, continuity testing, and advanced testing (Threat-Led Penetration Testing — TLPT) where applicable.

2. **Frequency & Types**
   - Standard tests (vulnerability scans, pen tests, DR tests): scheduled periodically (frequency based on risk profile).  
   - **TLPT Requirement:** Entities identified under DORA’s scope for TLPT must carry out TLPT **at least every 3 years**, subject to competent authority adjustments by risk profile. TLPTs must follow the RTS and applicable national TLPT frameworks (e.g., TIBER-like). :contentReference[oaicite:6]{index=6}

3. **Scope & Safety**
   - Define scope avoiding undue disruption to production. Use careful planning, legal agreements, and “kill switches”. Ensure back-out/rollback plans and notify relevant parties as required by the TLPT authority.

4. **Independent Execution**
   - TLPTs and other advanced tests should be performed by independent, experienced red teams under a formal test framework and with competent authority / TLPT authority oversight when applicable.

5. **Reporting & Remediation**
   - After testing: deliver findings, prioritized remediation plan, timelines and evidence of remediation to competent authority where required. Include purple-team replay/closure sessions per RTS.

6. **Documentation & Evidence**
   - Keep test artefacts (scopes, rules of engagement, results, remediation evidence) in a secure evidence repository.

## Practical Controls & Runbook
- Maintain a Testing Calendar integrated with Change Management and Business Calendars to avoid high-risk windows.
- Use dedicated test accounts and environment snapshots for safe testing where possible.
- For TLPT, follow national competent authority/TLPT authority guidance and provide required summaries to the authority after completion.

## References
- Regulation (EU) 2022/2554 — Article 26 (Digital operational resilience testing). :contentReference[oaicite:7]{index=7}  
- ESMA / Joint Committee final report & RTS on TLPT (guidance on TLPT mechanics and TIBER alignment). :contentReference[oaicite:8]{index=8}

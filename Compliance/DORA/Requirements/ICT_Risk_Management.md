# ICT_Risk_Management.md
**DORA — ICT Risk Management (Requirements & Implementation Notes)**

## Purpose
Define a firm-wide, board-level ICT risk management framework that identifies, assesses, mitigates and monitors ICT risks supporting business processes and critical functions.

## Scope
All information and communication technology (ICT) assets, systems, processes, data flows, cloud/native services, and third-party ICT services used by the financial entity.

## Core Requirements (derived from DORA — Articles 5–14 & RTS)
1. **Governance & Ownership**
   - Board-level accountability for ICT risk. Assign a named ICT Risk Owner and maintain an ICT Risk Committee (or equivalent).  
   - Document roles & responsibilities (CISO / Head of ICT / Business Owners / Risk) and escalation paths.  
   - *Rationale:* DORA mandates management responsibility and governance for ICT risk. :contentReference[oaicite:0]{index=0}

2. **ICT Risk Management Framework**
   - Maintain a documented ICT risk management framework covering: identification, classification, risk assessment methodology, appetite/tolerance, controls, monitoring and reporting cadence.  
   - Integrate into enterprise risk management (ERM) and ISMS where applicable.

3. **Asset & Dependency Inventory**
   - Maintain an up-to-date inventory of ICT assets, data flows, logical/physical architecture diagrams, and a register of critical functions and dependencies (including third-party ICT providers).

4. **Risk Assessment & Treatment**
   - Periodic (and event-driven) risk assessments with likelihood/impact scoring, mapped to controls and owners.  
   - Track remediation actions, timelines, residual risk and acceptance by named owners.

5. **Control Baseline**
   - Adopt technical, organisational and procedural controls aligned to ISO/IEC 27001 Annex A, NIS2 expectations and DORA’s requirements (access control, monitoring, backup, segregation of duties, patching, vulnerability management, logging/monitoring).  
   - Use control baselines for new projects and procurements (security by design).

6. **Change & Release Management**
   - Formal change-control process, testing gates, rollback procedures, pre-deployment risk assessment for changes affecting critical functions.

7. **Continuity & Backup**
   - Backup and restore policies, RTO/RPO defined per critical function, regular restore testing.

8. **Monitoring & Detection**
   - Centralised logging, SIEM/analytics, defined detection coverage for critical systems and KPIs (MTTD/MTTR).

9. **Third-Party & Supply-Chain Visibility**
   - Ensure contractual and technical visibility into third-party dependencies (see `Third_Party_Risk.md`).

## Metrics & Reporting
- Define KPIs: number of critical unmitigated vulnerabilities, patch lead time, MTTD, MTTR, % of critical functions with recovery plans tested, risk exposure trend.
- Regular reporting to the board and to the ICT Risk Committee.

## Implementation Notes & Practical Controls
- Use a risk register (spreadsheet or tool). Link findings to tickets (Jira, ServiceNow).
- Automate inventory and asset discovery where possible.
- Map existing ISO27001 controls to DORA requirements as a gap exercise.

## References
- Regulation (EU) 2022/2554 (DORA) — Articles 5–14. :contentReference[oaicite:1]{index=1}
- EBA Guidelines on ICT and security risk management (amendments in context of DORA). :contentReference[oaicite:2]{index=2}

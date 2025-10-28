# 🔗 DORA ↔ ISO/IEC 27001:2022 Mapping

## Purpose
Cross-reference mapping that shows how key DORA requirements (Regulation (EU) 2022/2554) map to ISO/IEC 27001:2022 clauses and Annex A controls.  
This is designed to help you demonstrate how an implemented ISMS (ISO 27001) supports DORA compliance — and where gaps will likely remain (e.g., TLPT, EU supervisory powers, mandatory reporting templates). :contentReference[oaicite:0]{index=0}

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Strong alignment — ISO clause/control covers the DORA requirement when properly implemented |
| ⚙️ | Partial overlap — ISO provides the intent or baseline but not the full DORA specificity |
| ⚠️ | Related but notable gap — ISO does not mandate the DORA-specific requirement (e.g., EU supervisory powers, TLPT mandates) |
| ❌ | Not applicable / no ISO equivalent |

---

## High-level Observations (load-bearing)
- **ISO/IEC 27001:2022 provides a strong foundation for ICT risk management, governance, incident handling and supplier controls** — making it a practical base for DORA readiness. :contentReference[oaicite:1]{index=1}  
- **DORA adds prescriptive, sector-specific obligations not contained in ISO**: mandatory incident reporting templates/timelines to competent authorities, TLPT obligations for certain entities, and an EU oversight regime for critical ICT third-party providers. Those items are usually gaps to address beyond ISO. :contentReference[oaicite:2]{index=2}

---

## Mapping Table (selected DORA topics → ISO27001)

| **DORA area / Articles** | **Short summary** | **ISO/IEC 27001:2022 (Clause / Annex A)** | **Alignment** | **Notes / How to show evidence** |
|--------------------------|-------------------|--------------------------------------------|---------------|----------------------------------|
| **Governance & Accountability** (Arts. 5–6) | Board-level ICT risk governance, roles, policies | Clauses 5–10 (Leadership, Planning, Operation); Annex A.5 (Organisational controls: roles & responsibilities). | ✅ | Use ISMS scope, roles matrix, board minutes, policy framework and SoA to show board accountability and documented responsibilities. :contentReference[oaicite:3]{index=3} |
| **ICT Risk Management Framework** (Arts. 7–14) | Risk identification, assessment, controls lifecycle | Clause 6 (Planning), Clause 8 (Operation), Annex A controls across Organizational/Technological sets (risk treatment, asset management, vulnerability mgmt). | ✅ | Risk register, risk assessment methodology (ISO 27005 alignment), SoA mapping of Annex A controls to risks. :contentReference[oaicite:4]{index=4} |
| **Incident Management & Reporting** (Arts. 15–20) | Detection, classification, internal & external reporting obligations | Annex A.5/Org controls + Annex A techn. controls (logging, monitoring) and Clause 9 (performance eval). ISO A.16-ish objectives (incident mgmt) — implemented as incident mgmt processes. | ⚙️ | ISO supports incident management (playbooks, testing). **Gap:** DORA requires specific regulatory reporting timelines, templates and escalation to competent authorities — include regulator-specific reporting runbooks and evidence of test reporting. :contentReference[oaicite:5]{index=5} |
| **Digital Operational Resilience Testing (incl. TLPT)** (Art. 26) | Routine testing + threat-led penetration testing (TLPT) for certain entities | Annex A (penetration testing, vulnerability mgmt, continuity tests) – generic testing controls. | ⚠️ | ISO expects security testing but **does not mandate TLPT frequency/RTS-style governance**. For DORA: add TLPT programme, Rules of Engagement, independent red teams, kill-switches, and TLPT evidence. See TLPT guidance. :contentReference[oaicite:6]{index=6} |
| **Third-Party ICT Risk & Oversight** (Arts. 25–39) | Due diligence, contracts, monitoring, concentration risk; oversight of critical ICT providers | Annex A.5 (organizational), Annex A.15 (Supplier relationships / third-party controls in 2013 mapping) and multiple organizational controls in Annex A 2022 (procurement, supplier lifecycle). | ⚙️ | ISO covers supplier controls (due diligence, contracts). **Gap:** DORA requires contractual clauses enabling regulator access and a Union-level oversight regime for CTPPs — include contract addenda, concentration risk register, and evidence of third-party monitoring. :contentReference[oaicite:7]{index=7} |
| **Operational Resilience / Business Continuity** (various Arts) | RTO/RPO, recovery plans, testing | Annex A: continuity & backup controls, operation clause, change management controls | ✅ | Use BCP/DR documents, restore test reports and evidence of RTO/RPO metrics in board reporting as proof. :contentReference[oaicite:8]{index=8} |
| **Logging, Monitoring & Detection** | Central logging, SIEM, MTTD/MTTR metrics | Annex A technological controls (access logging, monitoring, detection) | ✅ | SIEM dashboards, alerts, detection KPIs, SOC runbooks, SIEM tuning records. |
| **Information Sharing / Threat Intelligence** (Art. 40–45) | Voluntary sharing of threat info | Annex A controls for information exchange & communications; Clause 7 support (awareness/competence) | ⚙️ | ISO covers controlled info sharing practices — produce sharing agreements, TS/TP channels and evidence of membership in ISACs or voluntary sharing protocols. |
| **Documentation, Recordkeeping & Evidence** | Incident logs, test reports, contracts, SoA | Clause 7 (Support — documented info), Clause 9 (Performance evaluation), Annex A controls | ✅ | ISO already requires documented info and audit trails — include DORA-specific templates in doc repository. :contentReference[oaicite:9]{index=9} |
| **Supervisory / EU-level Oversight** (Arts. 31–41) | Designation, oversight and enforcement powers over critical ICT providers | **No direct ISO equivalent** (legal/regulatory supervisory regime) | ❌ | This is a regulatory regime (EBA/Joint Committee oversight). Demonstrate alignment by keeping evidence for authorities (audit logs, supplier contracts allowing supervisory access) — but ISO cannot replace the legal obligations. :contentReference[oaicite:10]{index=10} |

---

## Practical implementation guidance (quick wins)
1. **SoA + Addenda**: Expand your ISMS Statement of Applicability (SoA) to explicitly reference DORA requirements and where Annex A controls are used to meet them; add a DORA column (Implemented / Partial / Gap) for audits. :contentReference[oaicite:11]{index=11}  
2. **Regulatory Runbooks**: Create regulator-specific incident reporting runbooks that map ISO incident categories to DORA reporting thresholds and templates. (Keep tabletop exercise evidence.) :contentReference[oaicite:12]{index=12}  
3. **TLPT Roadmap**: Where TLPT applies, build a TLPT roadmap (scoping, engagement model, independent red team roster, assurance evidence) and cross-reference it from Annex A testing controls. :contentReference[oaicite:13]{index=13}  
4. **Third-party contract clauses**: Add DORA-compliant clauses (audit rights, data portability, continuity, supervisory access) to supplier templates and maintain a concentration-risk register. :contentReference[oaicite:14]{index=14}

---

## Suggested repo columns (if you export to spreadsheet)
- DORA Article | DORA Requirement Summary | ISO Clause/Annex A Control | SoA: Implemented? (Y/P/N) | Evidence (file path) | Owner | Notes / Gaps

---

## References (key sources)
- Regulation (EU) 2022/2554 — *Digital Operational Resilience Act (DORA).* (Official text). :contentReference[oaicite:15]{index=15}  
- ISO/IEC 27001:2022 — *Information security management systems* (standard summary / scope). :contentReference[oaicite:16]{index=16}  
- EBA — final/RTS materials and oversight work on DORA (harmonisation / TLPT oversight context). :contentReference[oaicite:17]{index=17}  
- ISO 27001:2022 Annex A explained (practical Annex A breakdown used for mapping). :contentReference[oaicite:18]{index=18}  
- BishopFox / TLPT practical guidance — preparing for DORA TLPT requirements. :contentReference[oaicite:19]{index=19}

---

**Maintainer:** Daniel Kaas  
*Part of security & safety / DORA mapping work.*


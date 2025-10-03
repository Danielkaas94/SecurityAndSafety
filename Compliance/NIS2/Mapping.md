#NIS2 #Mapping #ISO27001  #AnnexA #Risikostyring #IncidentResponse #SupplyChainSecurity #BusinessContinuity #DisasterRecovery #Governance #Ledelsesansvar #Awareness #Adgangskontrol #Identitetshåndtering #Kryptering #Kommunikationssikkerhed #Logging #Overvågning #Dokumentation #Compliance #ENISA
# NIS2 → Mappings

Formål: At kortlægge NIS2-krav mod relevante controls i ISO/IEC 27001, CIS Controls og andre rammeværk.  
Brug denne fil til hurtigt at finde overlap og hvilke eksisterende controls der kan dække et NIS2-krav.

---

## Formatforklaring
- **NIS2-krav**: Kort tekst eller reference til artikel i direktivet.  
- **ISO 27001 (Annex A)**: Relevante Annex A-kontroller (fx A.5.1, A.8.2).  
- **CIS Controls**: Nummer og kort titel på CIS-kontrollen.  
- **Kommentar / Implementeringshint**: Hurtige noter om hvordan kravet opfyldes teknisk eller organisatorisk.

---

## 1) Risikostyring
- **NIS2-krav**: Etablering og løbende opdatering af risikostyring for cybersikkerhed.  
- **ISO 27001 (Annex A)**: A.6.1.2, A.8.2, A.18.2  
- **CIS Controls**: 2 (Inventory and Control of Software Assets), 17 (Incident Response)  
- **Kommentar**: Brug ISO 27005 eller NIST SP 800-30 til metode. Dokumentér risikomatrix og plan.

---

## 2) Incident response og rapportering
- **NIS2-krav**: Pligt til hændelsesrapportering til myndigheder (24h early, 72h detailed, 1m final).  
- **ISO 27001 (Annex A)**: A.16 (Information Security Incident Management)  
- **CIS Controls**: 17 (Incident Response and Management)  
- **Kommentar**: Implementér SOC playbooks, eskalationsveje og rapporteringsskabeloner.

---

## 3) Supply chain security
- **NIS2-krav**: Leverandørstyring, due diligence og kontraktkrav for kritiske leverandører.  
- **ISO 27001 (Annex A)**: A.15 (Supplier relationships)  
- **CIS Controls**: 15 (Service Provider Management)  
- **Kommentar**: Indfør tredjeparts risikovurderinger og audits i SLA.

---

## 4) Business Continuity & Disaster Recovery
- **NIS2-krav**: Foranstaltninger for fortsat drift og gendannelse efter hændelser.  
- **ISO 27001 (Annex A)**: A.17 (Information security aspects of business continuity management)  
- **CIS Controls**: 11 (Data Recovery)  
- **Kommentar**: Test DR-planer, lav øvelser og opbevar offline backups.

---

## 5) Governance og ledelsesansvar
- **NIS2-krav**: Ledelsen er ansvarlig for sikkerhedspolitik og overholdelse.  
- **ISO 27001 (Annex A)**: A.5.1 (Policies for information security), A.6.1 (Organisation of information security)  
- **CIS Controls**: 4 (Access Control Management), 14 (Security Awareness and Skills Training)  
- **Kommentar**: Dokumentér at direktionen modtager rapporter og tager beslutninger.

---

## 6) Awareness og træning
- **NIS2-krav**: Krav om løbende træning og awareness-programmer.  
- **ISO 27001 (Annex A)**: A.7.2.2 (Information security awareness, education and training)  
- **CIS Controls**: 14 (Security Awareness and Skills Training)  
- **Kommentar**: Lav e-learning, phishingtests og awarenesskampagner.

---

## 7) Adgangskontrol og identitetshåndtering
- **NIS2-krav**: Sikre styring af brugerkonti, adgangsrettigheder og MFA.  
- **ISO 27001 (Annex A)**: A.9 (Access control)  
- **CIS Controls**: 6 (Access Control Management), 5 (Account Management)  
- **Kommentar**: Indfør princip om "least privilege", MFA og periodiske access reviews.

---

## 8) Kryptering og kommunikationssikkerhed
- **NIS2-krav**: Beskytte data i hvile og i transit med passende kryptering.  
- **ISO 27001 (Annex A)**: A.10 (Cryptography), A.13.2 (Information transfer)  
- **CIS Controls**: 3 (Data Protection)  
- **Kommentar**: Brug TLS 1.3, sikre nøglehåndtering og politik for kryptering.

---

## 9) Logging og overvågning
- **NIS2-krav**: Krav om overvågning, logning og detektion af hændelser.  
- **ISO 27001 (Annex A)**: A.12.4 (Logging and monitoring), A.16 (Incident management)  
- **CIS Controls**: 8 (Audit Log Management), 13 (Network Monitoring and Defense)  
- **Kommentar**: SIEM-løsning eller central loghåndtering, retention-policy.

---

## 10) Dokumentation og bevis for compliance
- **NIS2-krav**: Dokumentér sikkerhedstiltag, procedurer og audits.  
- **ISO 27001 (Annex A)**: A.18.1 (Compliance with legal and contractual requirements)  
- **CIS Controls**: 16 (Application Software Security), 18 (Penetration Testing)  
- **Kommentar**: Gem revisionsrapporter, self-assessments, politikker og tekniske logs.

---

## Mappeskabelon (copy/paste for hver ny mapping)
- **NIS2-krav**: 
- **NIS2-artikel / reference**: 
- **ISO 27001 (Annex A)**: 
- **CIS Controls**: 
- **Andre rammeværk**: (fx NIST CSF, GDPR-artikler hvis relevant)
- **Eksempler på beviser / artefakter**: (logfiler, politikker, rapporter, contracts)
- **Kommentar / Implementeringshint**: 

---

## Prioritering og næste skridt
1. Prioritér mappings for de krav som er mest relevante for din sektor eller dine noter.  
2. Tilføj konkrete artefakter per mapping (fx link til policy i dit repo, eksempel på playbook).  
3. Udvid med en kolonne for "Gap status" i checklists.md der refererer til denne mapping.  
4. Når du har flere mappings, overvej et simpelt script eller en CSV for at gøre søgning og filter let.

---

## Kilder og værktøjer til mapping
- ISO/IEC 27001 Annex A kontrolskema.  
- CIS Controls officielle beskrivelser.  
- ENISA vejledninger og sektorspecifikke dokumenter.  
- NIST publikationer for teknisk dybde.

## 📌 Næste skridt
- Udbyg listen med sektor-specifikke krav (fx energi, sundhed, finans).  
- Tilføj en kolonne for “Gap status” så mapping hænger sammen med checklists.md.  
- Evt. lav en CSV-version for nem filtrering i Excel/Sheets.  
#NIS2 #EssentialSector #Energy

---
# ⚡ Energy Sector (Energi)

**Kategori:** Essential Sector  
**Omfang:** El-, gas-, varme- og oliesektoren, herunder både produktion, transmission, distribution og lagerfaciliteter.  
**Lovgrundlag:** NIS2 artikel 3 og bilag I, punkt 1 (Energy)

---

## 📋 Relevante NIS2-krav

**Artikel 21 – Risikostyring og sikkerhedsforanstaltninger**  
- Krav om risikovurdering, netværkssegmentering, hændelsesdetektion, hærdning af systemer og forsyningskædekrav.  
- Integration af cybersikkerhed i både IT (informationssystemer) og OT (operationelle teknologier).  

**Artikel 23 – Hændelsesrapportering**  
- Krav om 24-timers early warning og 72-timers detaljeret rapportering til kompetent myndighed (fx Energistyrelsen eller CFCS).  

**Artikel 26 – Sanktioner og tilsyn**  
- Krav om dokumentation og tilsyn med kritiske infrastrukturer.

---

## ⚙️ Sektorens særlige karakteristika

Energisektoren er unik, fordi den kombinerer **OT (Operational Technology)** med **IT (Information Technology)**, og hændelser kan have **fysiske konsekvenser**.  
Et cyberangreb kan føre til blackouts, trykfejl, brændstoflæk eller farlige spændingsniveauer.

Typiske komponenter:
- SCADA-systemer og PLC’er  
- Produktions- og kontrolnetværk  
- Fjernovervågning og fjernstyring  
- Leverandørintegration (f.eks. data fra producenter, sensorer, og cloud dashboards)

---

## 🧠 Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **Ransomware / wiper malware** | Angreb som NotPetya og Industroyer, der lammede energisystemer i Ukraine. |
| **Supply chain exploits** | Angreb via softwareopdateringer, som kompromitterer OT-netværk (SolarWinds-lignende). |
| **Fjernadgang / RDP misbrug** | Uautoriseret adgang til SCADA/PLC-systemer. |
| **Manglende segmentering mellem IT og OT** | En infektion i kontorsystemer kan sprede sig til kontrolnetværk. |
| **Legacy systemer** | Gamle RTUs og PLC’er uden moderne sikkerhedsfeatures. |
| **Manglende overvågning i OT-miljøet** | Svært at opdage anomalier i industrielle netværk. |

---

## 🧩 Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Netværkssegmentering** | Adskil IT og OT-netværk. Brug firewalls, jump hosts og DMZ-zoner. |
| **Asset management** | Fuld inventarliste over både IT- og OT-komponenter. |
| **Patch management (OT)** | Risikobaseret patching og test i sandbox før deployment. |
| **Monitoring & SIEM** | OT-specifik overvågning (fx via passive IDS som Zeek, Nozomi, Dragos). |
| **Incident Response (OT)** | Playbooks tilpasset industrielle miljøer og fysiske konsekvenser. |
| **Physical Security** | Adgangskontrol, kameraer, og sikring mod sabotage. |
| **Supply Chain Control** | Leverandører skal levere signed firmware/software og dokumenteret sikkerhed. |

---

## 🧾 Typiske artefakter og beviser

- Netværkstopologi (med IT/OT-segmentering)  
- Asset register (med firmwareversioner og ansvarlige)  
- OT Incident Response-plan  
- Leverandørgodkendelsesliste  
- Backup- og gendannelsesprocedurer for SCADA  
- Penetrationstest- og auditrapporter  

---

## ⚡ Eksempel på Incident Response-playbook (kort OT-version)

**Scenario:** Uregelmæssig SCADA-trafik og pludselige kommandoer sendt til fjernstation.

1. **Detection:** IDS alarmerer om uautoriseret kommando.  
2. **Containment:** Afbryd affected segment; brug manuel kontrol.  
3. **Communication:** Informér kontrolrum, CISO, og CFCS inden for 1 time.  
4. **Investigation:** Analyser logs og firmware-integritet.  
5. **Recovery:** Gendan fra sikker konfiguration, test systemets stabilitet.  
6. **Report:** Send 24/72h rapport.  
7. **Lessons learned:** Opdater segmenteringsregler og overvågningsuse-cases.

---

## 🧠 Mapping til ISO 27001 Annex A (eksempler)

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Risikostyring | A.6.1.2, A.8.2, A.18.2 | Risikovurdering med fokus på OT og fysiske konsekvenser. |
| Adgangsstyring | A.9 | RBAC for SCADA og kontrolrum, adskilt fra IT-login. |
| Hændelsesstyring | A.16 | Incident playbooks for strømudfald og manipulation. |
| Leverandørstyring | A.15 | Due diligence for producenter og softwareleverandører. |
| Business continuity | A.17 | Nødprocedurer for drift ved netværkstab. |
| Teknisk sårbarhed | A.12.6 | Firmware patch management for PLC’er. |

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Energy Sector](https://nis2resources.eu/sectors/#energy)  
- [ENISA – Good Practices for the Energy Sector](https://www.enisa.europa.eu/topics/critical-information-infrastructures-and-services/energy)  
- [CFCS – Trusselsvurdering for Energisektoren](https://cfcs.dk/da/vejledninger/)  
- [ISA/IEC 62443 – Security for Industrial Automation and Control Systems](https://www.isa.org/isa62443)  

---

## ✅ Næste skridt
- Udarbejd en fuld assetliste for både IT og OT.  
- Etabler zoner og conduit-modellen fra IEC 62443.  
- Planlæg tabletop-øvelse for “loss of visibility” i kontrolnetværk.  
- Kræv signed firmware og leverandørpatches i alle kontrakter.  
- Implementér minimum 3 OT-overvågningsregler (anomalier, uautoriseret adgang, ændringer i PLC-logik).  

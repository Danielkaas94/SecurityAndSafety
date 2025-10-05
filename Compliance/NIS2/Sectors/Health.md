#NIS2 #EssentialSector #Health 

---
# 🏥 Health Sector (Sundhedssektoren)

**Kategori:** Essential Sector  
**Omfang:** Hospitaler, klinikker, laboratorier, blodbanker, medicotekniske leverandører, samt elektroniske sundhedsdataplatforme.  
**Lovgrundlag:** NIS2 artikel 3 og bilag I, punkt 5 (Health sector)  
**Tilsynsmyndighed (DK):** Sundhedsdatastyrelsen, Center for Cybersikkerhed  

---

## 📋 Relevante NIS2-krav

**Artikel 21 – Risikostyring og sikkerhedsforanstaltninger**  
- Sundhedssektoren skal beskytte både administrative IT-systemer (EPJ, økonomi) og kliniske OT/IoT-systemer (scannere, respiratorer, monitorer).  
- Krav om governance, incident response, og dokumentation af risikohåndtering.  

**Artikel 23 – Hændelsesrapportering**  
- Krav om indrapportering inden 24 timer efter alvorlig hændelse og 72 timers detaljeret rapport, særligt hvis patientdata eller drift er påvirket.  

**Artikel 26 – Sanktioner og tilsyn**  
- Hospitaler og sundhedsinstitutioner kan underlægges inspektioner og sanktioner ved manglende compliance.  

---

## 🧠 Sektorens karakteristika

Sundhedssektoren adskiller sig fra mange andre brancher, fordi den håndterer **livskritiske systemer** og **meget følsomme data** samtidig.  
Et cyberangreb kan føre til **tab af liv**, **brud på patientdata**, eller **afbrydelser i akut drift**.

Systemtyper:
- Elektroniske patientjournaler (EPJ/EHR)  
- Kliniske informationssystemer (LIS, RIS, PACS)  
- Medicoteknisk udstyr (IoMT – Internet of Medical Things)  
- Netværk til billeddiagnostik, laboratorier og medicindistribution  
- Sundhedsdataplatforme og nationale registre  

---

## 🧩 Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **Ransomware** | Angreb som WannaCry (2017) lammede britiske hospitaler (NHS). |
| **IoT/OT-sårbarheder** | Ubeskyttet medicinsk udstyr (CT-scannere, pumper, monitorer). |
| **Data breaches** | Tyveri af patientjournaler, testresultater, og persondata. |
| **Supply chain attacks** | Softwareleverandører, laboratorieplatforme eller medicoudstyr kompromitteret. |
| **Insider threats** | Utilsigtet eller bevidst adgang til patientdata. |
| **Lack of patching** | Udstyr med fast firmware og manglende opdateringsrutiner. |
| **Legacy systems** | Ældre EPJ-systemer med svag autentifikation. |

---

## ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Network segmentation** | Adskil medicoteknisk netværk (IoMT/OT) fra administrativ IT. |
| **Access control** | Role-Based Access Control (RBAC) for læger, sygeplejersker og teknikere. |
| **Incident response (healthcare)** | Playbooks for ransomware, data breach og driftstab i kritiske afdelinger. |
| **Asset management** | Registrer alle medicotekniske enheder og firmwareversioner. |
| **Patch management (IoMT)** | Test og implementer patches i samarbejde med leverandører. |
| **Data encryption** | Krypter al patientdata ved lagring og transmission. |
| **Monitoring & SIEM** | 24/7 overvågning af både IT og medicotekniske netværk. |
| **Backups & recovery** | Offline, verificerede backups af EPJ og laboratoriedata. |

---

## 🧾 Typiske artefakter og beviser

- Netværksdiagram (IT vs. medicoteknisk netværk)  
- Liste over kritiske systemer og ansvarlige ejere  
- Backup- og recoveryplaner  
- IR-playbooks for ransomware og data leak  
- Leverandørgodkendelser og kontrakter  
- Change management-protokoller for medicinsk software  

---

## 🧠 Eksempler på hændelser

| Hændelse | Eksempel | Konsekvens |
|-----------|-----------|------------|
| Ransomware mod hospital | Helse Sør-Øst (Norge, 2018) | Patientdata kompromitteret, systemer nede i dagevis. |
| WannaCry | NHS (UK, 2017) | 70.000 enheder påvirket, operationer aflyst. |
| Insider access | Tyskland (2021) | Læge lækkede patientjournaler til medier. |
| Supply chain exploit | SolarWinds (2020) | Medicoteknisk IT påvirket indirekte. |

---

## 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Risikostyring | A.6.1.2, A.8.2 | Risikoanalyse af EPJ, PACS og IoMT-systemer. |
| Adgangsstyring | A.9 | RBAC og 2FA for klinisk IT. |
| Hændelsesstyring | A.16 | Playbooks og rapporteringsprocedurer til myndigheder. |
| Databeskyttelse | A.18 | GDPR og sundhedslovgivning (personfølsomme data). |
| Kontinuitet | A.17 | Beredskabsplan for akut drift og patientbehandling. |
| Leverandørstyring | A.15 | Krav til medicotekniske leverandører og serviceaftaler. |
| Logging og overvågning | A.12.4 | Audit logs for EPJ-adgang og medicoudstyr. |

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Health Sector](https://nis2resources.eu/sectors/#health)  
- [ENISA – Cybersecurity in Health Sector](https://www.enisa.europa.eu/topics/health-sector)  
- [Danish Health Data Authority – Informationssikkerhed](https://sundhedsdatastyrelsen.dk/)  
- [ISO 81001-1:2021 – Health Software and Health IT Security](https://www.iso.org/standard/77370.html)  
- [European Commission – eHealth Network](https://health.ec.europa.eu/ehealth-digital-health-and-care/ehealth-network_en)  

---

## ✅ Næste skridt

- Kortlæg kritiske systemer og forbindelser (IT, OT, IoMT).  
- Udarbejd risiko- og konsekvensanalyse pr. klinisk afdeling.  
- Etabler 24/7 overvågning (SIEM/SOC) for både administrative og medicinske netværk.  
- Planlæg tabletop-øvelse for ransomware i klinisk drift.  
- Formalisér samarbejde mellem IT, sikkerhed, og klinisk teknik.  

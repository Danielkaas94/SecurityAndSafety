#NIS2 #EssentialSector #Transport

# 🚉 Transport Sector (Transport)

**Kategori:** Essential Sector  
**Omfang:** Luftfart, jernbane, søfart og vejtransport.  
**Lovgrundlag:** NIS2 artikel 3 og bilag I, punkt 2 (Transport)

---

## 📋 Relevante NIS2-krav

**Artikel 21 – Risikostyring og sikkerhedsforanstaltninger**  
- Krav om sikring af både operationelle systemer (OT) og digitale infrastrukturer (IT).  
- Omfatter beskyttelse af navigations-, kommunikations-, og logistiksystemer.  

**Artikel 23 – Hændelsesrapportering**  
- Krav om rapportering til relevant myndighed (fx Trafikstyrelsen eller CFCS) inden for 24/72 timer.  

**Artikel 26 – Tilsyn og sanktioner**  
- Transportoperatører skal kunne dokumentere risikostyring, sikkerhedspolitikker og beredskabsplaner.

---

## 🚦 Sektorens karakteristika

Transportsektoren er højt integreret og afhænger af **realtidsdata, automatisering og GPS-kommunikation**.  
En hændelse kan hurtigt få både **fysiske** og **økonomiske konsekvenser** — fx forsinkelser, tab af last, eller ulykker.

Typiske elementer:
- Air Traffic Management (ATM) og flyvepladsoperationer  
- Jernbanesignal- og kontrolsystemer  
- Maritime navigations- og lastkontrolsystemer  
- Smart traffic management og vej-infrastruktur  

---

## 🧠 Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **Ransomware** | Angreb på havne (fx Maersk 2017), jernbaner eller flyselskaber. |
| **GPS-spoofing og jamming** | Manipulation af navigationsdata for fly, skibe eller køretøjer. |
| **Supply chain exploits** | Softwareopdateringer eller tredjepartssystemer som angribes (eksempel: logistiksoftware). |
| **Data integrity attacks** | Ændring af fragtdata, ruteplaner eller trafiklys-systemer. |
| **IoT og SCADA-sårbarheder** | I trafiklys, broer, tunneller eller togsignalsystemer. |
| **Indvendige trusler (insider threats)** | Ansatte med adgang til operationelle systemer eller kontrolnetværk. |

---

## ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Network segregation** | Adskil trafikstyringsnetværk fra kontor-IT. |
| **GPS-sikkerhed** | Brug redundant navigation (GLONASS, Galileo), overvåg signalintegritet. |
| **Access control** | Implementér multi-factor authentication for kontrolrum og vedligeholdelsessystemer. |
| **Incident response (transport)** | Udarbejd playbooks for ransomware, signalforstyrrelser, og dataintegritetsbrud. |
| **Backup & recovery** | Offline backup af kritiske styringsdata (tunnelkontrol, flyveplaner, jernbanesignaler). |
| **Supplier security** | Kræv evidens for sikker softwareudvikling og test hos leverandører. |
| **Logging og overvågning** | Overvåg kommunikation mellem trafiksystemer, sensorer og kontrolnetværk. |

---

## 🧾 Typiske artefakter og beviser

- Infrastrukturkort (signalnet, GPS, datalink-kommunikation)  
- Leverandørliste og due diligence-rapporter  
- Beredskabsplaner og kontaktpunkter  
- Change management-procedurer for trafiksoftware  
- Log- og overvågningspolitikker  
- Penetrationstest for ICS/OT-miljøer  

---

## ✈️ Eksempler på hændelser og konsekvenser

| Hændelsestype | Eksempel | Konsekvens |
|----------------|-----------|------------|
| Cyberangreb på havn | Maersk (2017) | Global logistikkæde lammet i flere dage. |
| Ransomware i jernbane | Tyskland (2022) | Togselskaber måtte genstarte signalsoftware manuelt. |
| GPS-jamming i Østersøen | 2023–2024 | Fly og skibe oplevede tab af navigation midt i flyruter. |
| DDoS mod lufthavnens booking | Flere europæiske lufthavne (2023) | Midlertidig nedetid og check-in afbrudt. |

---

## 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Risikostyring | A.6.1.2, A.8.2 | Risikoanalyse af OT-netværk i trafikstyring. |
| Adgangsstyring | A.9 | MFA for kontrolrum og vedligeholdelsesadgang. |
| Driftskontrol | A.12 | Segmentering og overvågning af SCADA. |
| Leverandørstyring | A.15 | Leverandørkontrakter med cybersikkerhedskrav. |
| Incident response | A.16 | Playbooks for ransomware og signalfejl. |
| Kontinuitet | A.17 | Backup og redundans for styringssystemer. |
| Teknisk sårbarhed | A.12.6 | Regelmæssige OT-sårbarhedsscanninger. |

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Transport Sector](https://nis2resources.eu/sectors/#transport)  
- [ENISA – Good Practices for Transport Cybersecurity](https://www.enisa.europa.eu/topics/critical-information-infrastructures-and-services/transport)  
- [EU Agency for Railways – Cybersecurity Guidance](https://www.era.europa.eu/)  
- [IMO Cyber Risk Management for Ships](https://www.imo.org/en/OurWork/Security/Pages/Cyber-security.aspx)  
- [ICAO Cybersecurity Strategy for Aviation](https://www.icao.int/cybersecurity)  

---

## ✅ Næste skridt
- Etabler sektoropdelte hændelses-playbooks (luft, sø, bane, vej).  
- Kortlæg alle eksterne datalinks (GPS, leverandører, cloud).  
- Implementér logkorrelation mellem trafiksystemer og IT-drift.  
- Planlæg årlig tabletop-øvelse for ransomware-scenarier.  
- Definér "critical dependencies" mellem IT og OT (fx mellem billet-, signal-, og kontrolsystemer).  

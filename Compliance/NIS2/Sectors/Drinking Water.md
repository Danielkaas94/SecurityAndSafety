#NIS2 #EssentialSector #DrinkingWater 

---
# 💧 Drinking Water Sector (Drikkevandssektoren)

**Kategori:** Essential Sector  
**Omfang:** Vandforsyningsanlæg, drikkevandsproduktion, distribution, SCADA/ICS-netværk og digitale overvågningssystemer.  
**Lovgrundlag:** NIS2 bilag I, punkt 2 (Energy & Water)  
**Tilsynsmyndighed (DK):** Forsyningstilsynet, Styrelsen for Dataforsyning og Infrastruktur, Center for Cybersikkerhed (CFCS)  

---

## 📋 Relevante NIS2-krav

**Artikel 21 – Sikkerhedsforanstaltninger**  
- Drikkevandssektoren skal beskytte mod både digitale og fysiske hændelser, der kan påvirke forsyningens kontinuitet.  
- Fokus på SCADA/ICS-sikkerhed, segmentering, fjernadgang og beredskab.  

**Artikel 23 – Hændelsesrapportering**  
- Krav om rapportering til relevante myndigheder inden 24 timer ved afbrydelser, sabotage eller kompromittering af driftskontrolsystemer.  

**Artikel 26 – Tilsyn og sanktioner**  
- Mulighed for bøder og påbud ved manglende sikring af netværk, kontrolsystemer eller beredskab.  

---

## 🧠 Sektorens karakteristika

Vandsektoren er en **af de mest kritiske infrastrukturer** i samfundet. Et cyberangreb kan medføre forurening, vandmangel, eller skade på sundheden for tusindvis af borgere.  
Sektoren er typisk kendetegnet ved:

- Mange små og decentrale forsyninger (ofte kommunale).  
- Gamle SCADA/PLC-systemer med lang levetid.  
- Begrænset cybersikkerhedsressourcer og få specialister.  
- Integration mellem IT og OT-netværk.  

---

## ⚠️ Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **SCADA/ICS kompromittering** | Manipulation af vandtryk, kemikalier eller pumpestyring. |
| **Ransomware** | Kryptering af kontrolservere, adgangstab til overvågningssystemer. |
| **Remote access exploits** | Uautoriseret fjernadgang via TeamViewer/VPN. |
| **Insider threats** | Forkert konfiguration eller bevidst sabotage. |
| **Supply chain** | Leverandører af kontrolsoftware kompromitteret. |
| **Legacy systems** | Uopdaterede PLC’er og HMI-software. |
| **Manglende logging/overvågning** | Ingen opdagelse af uautoriserede ændringer. |

---

## ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Network segmentation** | Adskil SCADA/ICS-netværk fra administrativ IT med firewalls. |
| **Zero Trust-principper** | Ingen implicit tillid mellem enheder – alt skal autentificeres. |
| **Access control** | 2FA og stram rollebaseret adgang for driftspersonale. |
| **Incident detection** | SIEM med fokus på OT-trafik og anomalier (Modbus, DNP3). |
| **Backup & recovery** | Offline backups af konfigurationer og kontrolsystemer. |
| **Physical security** | Adgangsbegrænsning til kontrolrum, pumper og brønde. |
| **Patch management** | Sikker test og planlagte opdateringer af PLC/HMI-software. |
| **OT asset inventory** | Overblik over alle SCADA-enheder og firmwareversioner. |
| **Remote access monitoring** | Logning og alarm ved uautoriserede forbindelser. |

---

## 🧾 Typiske artefakter og beviser

- Netværksdiagram over IT/OT-adskillelse  
- OT-asset register med ansvarlige ejere  
- Backup-plan for SCADA-konfigurationer  
- Adgangslog og audit trail for fjernstyring  
- Risikovurdering og trusselsbillede  
- Beredskabsplan ved cyberangreb eller forurening  
- Leverandørkontrakter med sikkerhedskrav  

---

## 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Adgangsstyring | A.9 | RBAC, 2FA, adgangslogning i SCADA. |
| Netværkssikkerhed | A.13 | Firewall mellem OT og IT, whitelisting. |
| Driftssikkerhed | A.12 | Dokumenteret ændringsstyring af kontrolsystemer. |
| Beredskab & genopretning | A.17 | Plan for hurtig genstart af pumper og kontrolsystemer. |
| Leverandørstyring | A.15 | Sikkerhedskrav i aftaler med vedligeholdelsesfirmaer. |
| Overvågning | A.12.4 | Central logning og detektion af afvigelser. |
| Fysisk sikkerhed | A.11 | Sikrede adgangspunkter til brønde og pumper. |

---

## 🧠 Eksempler på hændelser

| Hændelse | Eksempel | Konsekvens |
|-----------|-----------|------------|
| Oldsmar, Florida (2021) | Hacker forsøgte at øge natriumhydroxid-niveauet i vandet via fjernadgang. | Potentiel forgiftning – opdaget i tide. |
| Israel Water Authority (2020) | Koordinerede cyberangreb mod pumpestationer. | Midlertidig forstyrrelse af drift. |
| Danmark – mindre hændelser | Uautoriseret fjernlogin via TeamViewer (2019–2021). | Ingen skade, men alvorlige svagheder afdækket. |

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Water Sector](https://nis2resources.eu/sectors/#water)  
- [ENISA – Water Sector Cybersecurity](https://www.enisa.europa.eu/topics/water-sector)  
- [Danish Energy Agency – Vandforsyning og kritisk infrastruktur](https://ens.dk/)  
- [CFCS – Vejledning om ICS/SCADA-sikkerhed](https://cfcs.dk/)  
- [ISA/IEC 62443 – Industrial Control System Security Standard](https://www.isa.org/isa62443/)  

---

## ✅ Næste skridt

- Kortlæg SCADA-netværk og afhængigheder (IT/OT).  
- Etabler segmentering og kontrolleret fjernadgang.  
- Implementér central logning og overvågning af kontrolsystemer.  
- Lav tabletop-øvelse: “Ransomware mod pumpestation.”  
- Gennemgå leverandørkontrakter og adgangskrav.  

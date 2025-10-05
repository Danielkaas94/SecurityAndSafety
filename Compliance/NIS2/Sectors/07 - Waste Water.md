#NIS2 #EssentialSector #WasteWater 
# ♻️ Waste Water Sector (Spildevandssektoren)

**Kategori:** Essential Sector  
**Omfang:** Rensningsanlæg, kloaknet, pumpestationer, overvågningssystemer, SCADA/ICS-netværk og tilhørende IT-infrastruktur.  
**Lovgrundlag:** NIS2 bilag I, punkt 2 (Energy & Water)  
**Tilsynsmyndighed (DK):** Forsyningstilsynet, Miljøstyrelsen, Center for Cybersikkerhed (CFCS)  

---

## 📋 Relevante NIS2-krav

**Artikel 21 – Sikkerhedsforanstaltninger**  
- Operatører skal sikre både fysisk og digital drift, så miljøet og folkesundheden ikke bringes i fare.  
- Fokus på overvågning, adskillelse af IT/OT-netværk og sikring af fjernadgang.  

**Artikel 23 – Hændelsesrapportering**  
- Hændelser, der påvirker rensning, pumpestationer, sensornetværk eller miljøudledninger, skal rapporteres inden 24 timer.  

**Artikel 26 – Sanktioner**  
- Tilsynsmyndigheder kan udstede bøder og påbud ved manglende sikkerhedsforanstaltninger.  

---

## 🧠 Sektorens karakteristika

Spildevandssektoren udgør en **kritisk miljø- og sundhedsinfrastruktur**, hvor IT og OT smelter sammen i komplekse, geografisk spredte systemer.  
Den er kendetegnet ved:

- Mange automatiserede pumpestationer og sensorer.  
- SCADA/ICS-systemer med lang levetid og ofte proprietær software.  
- Behov for realtidsdata (tryk, flow, kemi).  
- Ofte kommunalt ejede selskaber med begrænsede ressourcer.  

---

## ⚠️ Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **SCADA-kompromittering** | Manipulation af pumpestyring, overløb eller kemikaliedosering. |
| **Ransomware** | Nedlukning af kontrolsystemer, tab af overvågning, miljøpåvirkning. |
| **IoT/OT-sårbarheder** | Eksponerede sensorer og PLC’er uden autentificering. |
| **Fjernadgang** | Uautoriserede VPN-forbindelser eller svag kryptering. |
| **Data-integritet** | Ændring eller tab af flowdata og alarmlogning. |
| **Miljøhændelser** | Sabotage eller fejl, der fører til forurening af vandløb/fjord. |
| **Supply chain** | Kompromitteret leverandørsoftware til SCADA/overvågning. |

---

## ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Network segmentation** | Streng adskillelse mellem SCADA og administrativ IT. |
| **Access control** | 2FA, individuelle konti, ingen delte logins til driftssystemer. |
| **OT asset management** | Inventarliste over PLC’er, HMI’er, sensorer og firmwareversioner. |
| **Monitoring** | Anomalidetektion i netværkstrafik (Modbus, OPC UA, MQTT). |
| **Patch management** | Koordineret patching i samarbejde med leverandører. |
| **Backup & recovery** | Offline kopier af SCADA-konfigurationer og alarmlogfiler. |
| **Physical security** | Adgangskontrol til pumpestationer, teknikbygninger og kontrolrum. |
| **Incident response (OT)** | Foruddefinerede procedurer for nedlukning og genstart. |
| **Environmental response** | Samarbejde med miljømyndigheder ved udledningshændelser. |

---

## 🧾 Typiske artefakter og beviser

- SCADA-topologi og kommunikationsdiagram  
- OT-asset register og opdateringshistorik  
- Backup- og genopretningsplaner  
- Audit logs for fjernadgang og ændringer  
- Leverandørkontrakter med cybersikkerhedskrav  
- Risikoanalyse for pumpestationer og sensornetværk  
- Miljøberedskabsplaner ved driftsstop eller forurening  

---

## 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Adgangsstyring | A.9 | RBAC for SCADA, fjernadgang via VPN med 2FA. |
| Netværkssikkerhed | A.13 | Firewall-regler mellem OT og IT. |
| Sikker drift | A.12 | Patching og ændringsstyring af kontrolsystemer. |
| Kontinuitet | A.17 | Beredskabsplan for afløb og pumpestationer. |
| Leverandørstyring | A.15 | Sikkerhed i SCADA-serviceaftaler. |
| Miljø og hændelser | A.18 | Krav om dataintegritet og ansvarlig rapportering. |
| Overvågning | A.12.4 | Logning og alarmering af systemændringer. |

---

## 🧠 Eksempler på hændelser

| Hændelse | Eksempel | Konsekvens |
|-----------|-----------|------------|
| Maroochy Shire (Australien, 2000) | Insider brugte stjålne credentials til at åbne ventiler. | 800.000 liter spildevand udledt i naturen. |
| Israel (2020) | Koordineret cyberangreb mod spildevandssystemer. | Forstyrrelse af pumpestationer. |
| Danmark (2021–2022) | Fjernadgang uden MFA og logning opdaget. | Potentiel risiko for manipulation – rettet efter audit. |

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Water Sector](https://nis2resources.eu/sectors/#water)  
- [ENISA – Cybersecurity in Water/Wastewater](https://www.enisa.europa.eu/topics/water-sector)  
- [CFCS – ICS/SCADA Security Guidance](https://cfcs.dk/)  
- [Miljøstyrelsen – Spildevandsanlæg og miljøregulering](https://mst.dk/)  
- [ISA/IEC 62443 – OT Security Standard](https://www.isa.org/isa62443/)  

---

## ✅ Næste skridt

- Gennemfør teknisk segmenteringsrevision (IT/OT).  
- Etabler sikker fjernadgang via MFA og VPN-logning.  
- Opbyg løbende overvågning (SIEM/SOC) af SCADA-netværk.  
- Udarbejd miljøberedskabsplan integreret med IR-playbook.  
- Test gendannelse af SCADA fra offline-backup.  

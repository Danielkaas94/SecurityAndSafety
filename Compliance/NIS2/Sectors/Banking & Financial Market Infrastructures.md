#NIS2 #EssentialSector #Banking #FinancialMarketInfrastructures

# 💰 Banking and Financial Market Infrastructures

**Kategori:** Essential Sector  
**Omfang:** Banker, kreditinstitutter, finansielle markedsinfrastrukturer (FMI’er) som børser, clearinghouses, og betalingssystemer.  
**Lovgrundlag:** NIS2 artikel 3 og bilag I, punkt 3 (Banking) og punkt 4 (Financial Market Infrastructures)  
**Tilsynsmyndighed (DK):** Finanstilsynet  

---

## 🏦 Del 1: Banking Sector

### 📋 Relevante NIS2-krav

- **Artikel 21 – Risikostyring:** Krav om robusthed i finansielle systemer, herunder sikring af data, transaktioner og betalingstjenester.  
- **Artikel 23 – Hændelsesrapportering:** Krav om rapportering til myndighed inden 24 timer (initial), 72 timer (detaljeret), og slutrapport ved afslutning.  
- **Artikel 26 – Sanktioner og tilsyn:** Dokumentation for hændelseshåndtering og risikostyring skal kunne fremvises til Finanstilsynet.  

---

### 🧠 Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **Ransomware og DDoS** | Forsøg på at lamme netbank eller kundeadgang. |
| **Phishing og social engineering** | Spear-phishing mod ansatte i netbank eller drift. |
| **Data integrity attacks** | Ændring af kundesaldi, transaktionshistorik eller renteværdier. |
| **Supply chain** | Angreb via tredjeparts fintech-leverandører eller cloud services. |
| **Credential theft / ATO (Account Takeover)** | Misbrug af kundelogin og svindel via mobilbank. |
| **Insider threats** | Illoyale medarbejdere med adgang til kundedata. |

---

### ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Strong authentication** | Krav om MFA og transaktionssignering (PSD2). |
| **Encryption** | Kryptering af data-at-rest og in-transit. |
| **Network segmentation** | Adskillelse af core banking, testmiljøer og interneteksponering. |
| **Fraud detection** | AI/ML-baseret anomali-detektion i realtid. |
| **Incident response** | Automatiserede playbooks til phishing og ransomware. |
| **Backup & recovery** | Krypterede, offline backups af finansielle databaser. |
| **Third-party risk management** | Sikkerhedsvurdering af leverandører (SOC2, ISO 27001). |

---

### 🧾 Typiske artefakter

- IT- og OT-risikovurdering  
- ISMS-dokumentation  
- Change management-procedurer  
- Leverandørrapporter og kontrolerklæringer  
- Beredskabsplaner og tabletop-øvelser  
- Log management- og SIEM-politikker  

---

### 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Risikostyring | A.6.1.2, A.8.2 | Risikovurdering af betalingssystemer. |
| Adgangsstyring | A.9 | RBAC og MFA for medarbejdere og kunder. |
| Hændelsesstyring | A.16 | Automatiseret loganalyse og alarmering. |
| Leverandørstyring | A.15 | SLA’er med sikkerhedskrav og testkrav. |
| Business continuity | A.17 | Øvelser for datagendannelse og netbank-drift. |
| Databeskyttelse | A.18 | GDPR- og finansdata-beskyttelse. |

---

### 📉 Eksempler på hændelser

| Hændelse | Eksempel | Konsekvens |
|-----------|-----------|------------|
| DDoS mod netbank | Nordea (2013) | Nedetid og utilgængelig online bank. |
| Credential phishing | SEB (2021) | Tusindvis af konti kompromitteret. |
| Cloud breach | Capital One (2019) | 100+ mio. kundedata lækket. |

---

## 🏛️ Del 2: Financial Market Infrastructures (FMI)

### 📋 Relevante NIS2-krav

- **Artikel 21 – Risikostyring:** FMI’er skal beskytte handels-, clearing- og betalingssystemer mod cyberangreb og driftsforstyrrelser.  
- **Artikel 23 – Hændelsesrapportering:** Kritiske hændelser skal rapporteres til Finanstilsynet og/eller Nationalbanken.  
- **Artikel 26 – Compliance:** Krav om teknisk og organisatorisk dokumentation samt revisioner.

---

### ⚙️ Typiske FMI-komponenter

- **Clearing & Settlement Systems** (fx VP Securities, Euroclear, TARGET2)  
- **Trading Platforms** (fx Nasdaq Nordic)  
- **Payment Gateways & Processors** (fx Nets, SWIFT)  
- **Liquidity Management Systems**  
- **Market Data Dissemination Systems**

---

### 🧠 Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **Operational disruption** | Nedetid i clearing-systemer, fx TARGET2-fejl. |
| **Integrity compromise** | Manipulation af transaktionsdata eller handelsordre. |
| **Systemic risk** | Kædereaktion i hele finanssektoren pga. fejl i FMI. |
| **Supply chain compromise** | Sårbarhed i tredjeparts softwaren, fx trading API’er. |
| **Insider threats** | Fejl eller sabotage i driftssystemer. |
| **Legacy systems** | Ældre mainframes uden moderne logning og patching. |

---

### ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Redundans og failover** | Replikering på tværs af datacentre og lande. |
| **High integrity logging** | Kryptografisk sikrede transaktionslogs. |
| **Network isolation** | Segmentering mellem clearing, market data og trading-systemer. |
| **Time synchronization** | GPS/NTP med validering for handelssekvens. |
| **Secure API management** | Signed API-requests og transaktionsvalidering. |
| **Penetration testing** | Årlige red team-øvelser (krav i mange FMI’er). |

---

### 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Risikostyring | A.6.1.2, A.8.2 | Analyse af systemiske afhængigheder. |
| Netværkssikkerhed | A.13 | Segmentering og IDS på handelsnetværk. |
| Sårbarhedsstyring | A.12.6 | OT/IT scanninger af trading- og clearing-systemer. |
| Hændelsesstyring | A.16 | Specifik FMI-incident response-plan. |
| Kontinuitet | A.17 | Backup i realtid og cold-site replication. |
| Logging og revision | A.12.4 | Audit trails med integritetssikring. |

---

### 🧾 Typiske artefakter

- Systemdiagrammer for trading, clearing og settlement  
- High Availability-planer og failover-tests  
- Sårbarhedsscanninger og red team-rapporter  
- Incident Response playbooks for markedsstop  
- Kommunikationsplaner mellem FMI’er og banker  

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Banking and Finance](https://nis2resources.eu/sectors/#banking)  
- [ENISA – Cybersecurity in Finance Sector](https://www.enisa.europa.eu/topics/finance-sector)  
- [EBA – Guidelines on ICT and Security Risk Management (EBA/GL/2019/04)](https://www.eba.europa.eu/)  
- [European Central Bank – Cyber Resilience Oversight Expectations (CROE)](https://www.ecb.europa.eu/paym/cyber-resilience/html/index.en.html)  
- [FS-ISAC – Financial Services Information Sharing and Analysis Center](https://www.fsisac.com/)  

---

## ✅ Næste skridt

- Udfør en fælles risikovurdering for bank og FMI-systemer (afhængigheder).  
- Etabler samarbejdsprocedurer mellem drift, compliance og finansiel regulering.  
- Implementér logkorrelation mellem bank- og FMI-systemer for tidlig detektion.  
- Planlæg tværsektoriel tabletop-øvelse (bank + FMI).  
- Formalisér rapporteringspipeline til Finanstilsynet/CFCS.  

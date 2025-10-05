#NIS2 #EssentialSector #DigitalInfrastructure  

# 🌐 Digital Infrastructure Sector (Digital Infrastruktur)

**Kategori:** Essential Sector  
**Omfang:** Internetudbydere (ISPs), datacentre, DNS-tjenester, TLD-registere, cloud-udbydere, IXPs (Internet Exchange Points), trust services (PKI/CA), samt udbydere af routing og backbone-infrastruktur.  
**Lovgrundlag:** NIS2 bilag I, punkt 8 (Digital Infrastructure)  
**Tilsynsmyndighed (DK):** Center for Cybersikkerhed (CFCS) og Energistyrelsen  

---

## 📋 Relevante NIS2-krav

**Artikel 21 – Sikkerhedsforanstaltninger**  
- Operatører skal dokumentere governance, risikostyring, adgangskontrol, systemovervågning og beredskab.  
- Krav om kontinuerlig tilgængelighed og robusthed i netværksinfrastruktur, DNS og cloud-services.  

**Artikel 23 – Hændelsesrapportering**  
- Sikkerhedshændelser, der påvirker tilgængelighed, integritet eller fortrolighed af essentielle tjenester, skal rapporteres inden 24 timer.  

**Artikel 26 – Sanktioner og tilsyn**  
- Tilsynsmyndigheder kan kræve audits, sikkerhedsrevisioner og dokumentation af compliance.  

---

## 🧠 Sektorens karakteristika

Den digitale infrastruktur er **rygraden i hele NIS2-regimet** – uden stabile netværk, DNS og cloud-platforme fungerer ingen andre sektorer.  
Derfor stilles der høje krav til **redundans, databeskyttelse, kontinuitet og cyberresiliens**.

Typiske aktører i sektoren:
- Internetudbydere (ISP’er og backbone-operatører)  
- Cloud service providers (IaaS, PaaS, SaaS)  
- Datacentre og hostingudbydere  
- DNS-tjenester og TLD-registere (.dk, .eu, .com osv.)  
- IXPs (Internet Exchange Points)  
- Certificate Authorities og trust service providers  

---

## ⚠️ Centrale risici

| Risikotype | Eksempler |
|-------------|------------|
| **DDoS-angreb** | Overbelastning af netværk, DNS eller cloud-tjenester. |
| **BGP hijacking** | Fejl eller bevidst manipulation af internet-routing. |
| **DNS manipulation** | Omdirigering af trafik, phishing, eller tab af tjeneste. |
| **Cloud misconfiguration** | Uautoriseret adgang til data eller VM’er. |
| **Supply chain exploits** | Afhængighed af tredjeparts datacentre og software. |
| **Credential theft** | Angreb mod administrative adgangskonti. |
| **Insider threats** | Sabotage eller læk af konfigurationsdata. |
| **Firmware exploits** | Kompromittering af netværksudstyr (routers, firewalls). |

---

## ⚙️ Sektor-specifikke kontroller

| Kravområde | Praktiske tiltag |
|-------------|-----------------|
| **Network resilience** | Redundant netværk, failover, DDoS-beskyttelse. |
| **DNSSEC** | Signering af DNS-zoner for at sikre dataintegritet. |
| **BGP security** | Implementér RPKI og route filtering. |
| **Access management** | MFA, just-in-time privilegier, SIEM integration. |
| **Segmentation** | Logisk adskillelse af kundedata, management-netværk og produktion. |
| **Patch management** | Sikker opdatering af routere, switches og hypervisors. |
| **Backup & disaster recovery** | Datacenter-redundans (N+1 eller bedre). |
| **Incident response** | Playbooks for DDoS, BGP hijack, og cloud compromise. |
| **Monitoring & telemetry** | 24/7 SOC-overvågning af netværk, DNS og cloud. |

---

## 🧾 Typiske artefakter og beviser

- Netværksarkitektur og redundansdiagram  
- DNSSEC-konfigurationsbeviser  
- Logning af administrative login og ændringer  
- Overvågningsrapporter (uptime, anomalidetektion)  
- IR-playbooks for netværkshændelser  
- Leverandør- og cloud-complianceaftaler (ISO 27001, SOC2, etc.)  
- Disaster recovery-plan med dokumenteret failover  

---

## 🧩 Mapping til ISO 27001 Annex A

| NIS2 tema | ISO 27001 Annex A kontroller | Eksempler |
|------------|-----------------------------|------------|
| Netværkssikkerhed | A.13 | BGP-filtering, DDoS-beskyttelse, trafiksegmentering. |
| Adgangsstyring | A.9 | MFA og privilegeret adgangskontrol. |
| Driftskontinuitet | A.17 | Datacenter-redundans, geografisk failover. |
| Kryptografi | A.10 | DNSSEC, TLS-certifikater, RPKI-signering. |
| Overvågning | A.12.4 | SIEM/SOC-analyse af netværksaktivitet. |
| Leverandørstyring | A.15 | SLA’er og sikkerhedsaftaler med datacenter- og cloud-partnere. |
| Hændelsesstyring | A.16 | Responsteam og kommunikationsplan ved nedbrud. |

---

## 🧠 Eksempler på hændelser

| Hændelse | Eksempel | Konsekvens |
|-----------|-----------|------------|
| Dyn DNS Attack (2016) | Massive DDoS via Mirai botnet. | Nedetid for store dele af internettet. |
| OVH Datacenter Fire (2021) | Brand i Strasbourg. | Tab af tjenester og kundedata. |
| CloudFlare outage (2020) | Fejl i BGP routing. | Global utilgængelighed i 27 minutter. |
| Route hijack (2022) | BGP-fejl hos russisk ISP. | Trafik rerouted via uautoriseret netværk. |

---

## 🔗 Nyttige ressourcer

- [NIS2Resources – Digital Infrastructure](https://nis2resources.eu/sectors/#digital-infrastructure)  
- [ENISA – Digital Infrastructure Security](https://www.enisa.europa.eu/topics/digital-infrastructure)  
- [CFCS – Netværkssikkerhed og resilient infrastruktur](https://cfcs.dk/)  
- [MANRS – Mutually Agreed Norms for Routing Security](https://www.manrs.org/)  
- [RIPE NCC – RPKI og BGP Security](https://www.ripe.net/)  
- [EU Cloud Code of Conduct](https://eucoc.cloud/en/home)  

---

## ✅ Næste skridt

- Kortlæg netværksinfrastruktur og afhængigheder.  
- Implementér DNSSEC og RPKI for sikker routing.  
- Etabler 24/7 overvågning og incident response-processer.  
- Test failover og disaster recovery-planer.  
- Formalisér SLA’er og sikkerhedskrav til leverandører og cloudpartnere.  

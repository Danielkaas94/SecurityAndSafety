#NIS2 #PublicAdministration #EssentialSector 

---

### 🏛 Public Administration

**Kategori:** Essential Sector
**Omfang:** Statlige, regionale og kommunale myndigheder samt visse offentligt ejede enheder, der udfører kritiske samfundsopgaver.

---

#### 📋 Relevante NIS2-krav

* **Artikel 21:** Sikkerhedsforanstaltninger og risikostyring

  * Krav om politikker for risikoanalyse, informationssikkerhed og leverandørstyring.
  * Fokus på *konfidentialitet, integritet, tilgængelighed og autenticitet* af information.
* **Artikel 23:** Rapportering af hændelser

  * Krav om *24-timers early warning* og *72-timers incident report* til CSIRT eller kompetent myndighed.
* **Artikel 26–27:** Opsyn, tilsyn og sanktioner

  * Offentlige myndigheder kan være både underlagt og udøvende af NIS2-tilsyn.

---

#### 🧠 Centrale risici

| Risikotype                            | Eksempler                                                              |
| ------------------------------------- | ---------------------------------------------------------------------- |
| **Phishing & social engineering**     | Offentlige medarbejdere er mål for credential theft.                   |
| **Ransomware**                        | Kommuner, regioner og ministerier er hyppige mål.                      |
| **Legacy-systemer**                   | Ældre fagsystemer og manglende patch management.                       |
| **Supply chain**                      | Afhængighed af leverandører (IT-drift, cloud, systemudvikling).        |
| **Data leakage**                      | Kombination af borgerdata og administrative systemer udgør høj risiko. |
| **Manglende logning og segmentering** | Særligt udbredt i mindre enheder og ældre netværk.                     |

---

#### 🧩 Sektor-specifikke kontroller (eksempler)

| Kravområde                  | Praktiske tiltag                                                                                           |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Governance & Policy**     | Etabler ISMS (evt. baseret på ISO 27001), udpeg ansvarlig CISO, implementér årlig risikovurdering.         |
| **Awareness & træning**     | Kræver løbende uddannelse af medarbejdere, herunder phishing-simuleringer.                                 |
| **Kontinuitet & beredskab** | Udarbejd forretnings- og IT-beredskabsplan (BCP/DRP) samt test mindst årligt.                              |
| **Incident Response**       | Formaliseret IR-plan med roller, eskalering, kontakt til CSIRT, og rapporteringsworkflow.                  |
| **Leverandørstyring**       | Kræv NIS2-compliance og dokumenterede sikkerhedskontroller hos leverandører.                               |
| **Tekniske kontroller**     | MFA på alle administrative konti, netværkssegmentering, EDR-løsninger, patch management, logning via SIEM. |

---

#### 🧾 Typiske artefakter i dokumentationen

* Informationssikkerhedspolitik og risikovurdering
* Leverandørregister med sikkerhedsvurderinger
* Incident Response-plan og beredskabsprocedurer
* Awareness-træningsplan
* Penetrationstest- og sårbarhedsrapporter
* Intern kontrolrapport (fx ISAE 3402 for leverandører)

---

#### ⚖️ Relaterede rammeværk og love

* **ISO 27001/27002** – klassisk ramme for styring af informationssikkerhed
* **GDPR** – overlap især i databeskyttelse og hændelsesrapportering
* **Danish NIS2 Implementation Act (forventet 2025)** – vil konkretisere myndigheders forpligtelser
* **NSIS og KL’s sikkerhedspolitikker** – danske retningslinjer for kommunal og statslig IT-sikkerhed

---

#### 🔗 Nyttige ressourcer

* [NIS2Resources.eu – Public Administration](https://nis2resources.eu/sectors/#public-administration)
* [Digitaliseringsstyrelsen – Informationssikkerhed i det offentlige](https://digst.dk/informationssikkerhed/)
* [Center for Cybersikkerhed (CFCS) – Vejledninger](https://cfcs.dk/da/vejledninger/)

---
---
---

Perfekt. Jeg fortsætter og laver en dybdegående mapping mellem NIS2-kravene for Public Administration og relevante ISO 27001 Annex A-kontroller, plus praktiske anbefalinger, artefakter, tjekliste, eksempler på kontraktklausuler og et forslag til et roadmap. Alt på dansk og uden em dash.

# Dybdegående mapping: Public Administration under NIS2 → ISO 27001 + praktisk implementering

## Kort forklaring

Målet er at vise, hvordan konkrete NIS2-krav for offentlige myndigheder kan dækkes af ISO 27001-kontroller og operationelle tiltag. For hver hovedkategori får du:

* Relevante ISO Annex A-kontroller
* Konkrete tekniske og organisatoriske tiltag
* Forslag til artefakter og beviser
* Prioritering og korte next steps

---

## 1) Governance, ledelsesansvar og politikker

**NIS2-krav/tema:** Ledelsen skal sikre risikostyring, ressourceallokering og ansvar for cybersikkerhed.

**ISO Annex A:** A.5 (Policies for information security), A.6 (Organisation of information security), A.18.1 (Compliance)

**Praktiske tiltag**

* Etabler en informationssikkerhedspolitik godkendt af direktionen eller borgmester/kommunalbestyrelse.
* Udpeg en ansvarlig (CISO/ansvarlig for cybersikkerhed) med definerede beføjelser og rapporteringslinjer.
* Lav governance-møder hver kvartal med beslutningslog.

**Artefakter / beviser**

* Signeret informationssikkerhedspolitik
* Organigram med ansvar og beføjelser
* Mødeprotokoller fra governance-møder

**Prioritet:** Høj

**Next steps**

1. Udarbejd politikskabelon og få formel godkendelse.
2. Dokumentér roller og ansvar i et RACI-diagram.

---

## 2) Risikovurdering og risikostyring

**NIS2-krav/tema:** Løbende risikovurdering af tjenesters sikkerhed og leverandør-relaterede risici.

**ISO Annex A:** A.6.1.2, A.8.2, A.18.2

**Praktiske tiltag**

* Implementér en standardiseret risikovurderingsmetode (fx ISO 27005 eller NIST SP 800-30).
* Klassificér systemer og data efter kritikalitet for borgerbetjening.
* Indfør risikoregister med ejerskab og behandlingsplaner.

**Artefakter / beviser**

* Risikomatrix og risikoregister
* Rapport fra gennemført risikovurdering
* Behandlingsplaner med deadlines og ejere

**Prioritet:** Høj

**Next steps**

1. Lav en kickoff-risikworkshop for de 10 mest kritiske applikationer.
2. Opret risikoregister i et delt dokument eller værktøj.

---

## 3) Incident response og rapportering

**NIS2-krav/tema:** Hurtig indberetning af sikkerhedshændelser til CSIRT/kompentent myndighed og intern håndtering.

**ISO Annex A:** A.16 (Information security incident management), A.12.4 (Logging and monitoring)

**Praktiske tiltag**

* Udarbejd IR-plan og playbooks for typiske hændelsestyper, fx ransomware, dataeksfiltration, DDoS.
* Definér processer for 24-timers early warning og 72-timers detaljeret rapport.
* Integrér kommunikationsplaner, både internt og eksternt (press statements, borgersupport).

**Artefakter / beviser**

* Incident Response-plan
* Playbooks per hændelsestype
* Test- og øvelsesrapporter (tabletop og tekniske øvelser)
* Eksempel på rapport til myndighed

**Prioritet:** Kritisk

**Next steps**

1. Skriv en simpel 24h- og 72h-rapportskabelon.
2. Kør tabletop-øvelse inden for 3 måneder.

**Eksempel: Indhold i en 72-timers rapport**

* Hændelses-ID, tidspunkt for opdagelse, aktuel status
* Omfang og påvirkede systemer
* Tiltag gennemført indtil rapporttidspunkt
* Behov for assistance fra myndigheder eller leverandører
* Kontaktperson og eskalationsliste

---

## 4) Kontinuitet og beredskab (BCP/DRP)

**NIS2-krav/tema:** Sikre fortsat levering af kritiske tjenester.

**ISO Annex A:** A.17 (Business continuity management)

**Praktiske tiltag**

* Udarbejd forretningskontinuitetsplaner, herunder RTO og RPO for kritiske systemer.
* Test recovery scenarier, herunder failover til backup-datacenter eller cloud.
* Identificér kritiske tredjepartsleverandører og krav til deres kontinuitetsplan.

**Artefakter / beviser**

* BCP og DRP-dokumenter
* Testplaner og resultater af DR-øvelser
* Backup-politikker og restaureringstests

**Prioritet:** Høj

**Next steps**

1. Fastlæg kritiske processer og sæt RTO/RPO.
2. Planlæg en fuld DR-test for mindst én kritisk tjeneste.

---

## 5) Supply chain og leverandørstyring

**NIS2-krav/tema:** Due diligence på leverandører, kontraktkrav og overvågning.

**ISO Annex A:** A.15 (Supplier relationships), A.14 (System acquisition, development and maintenance)

**Praktiske tiltag**

* Opret leverandørregister med klassificering efter kritikalitet.
* Indfør obligatoriske sikkerhedsklausuler i kontrakter for kritiske leverandører: retten til audit, rapportering af hændelser, SLA for patches.
* Kræv beviser for leverandørers sikkerhed, fx certificeringer eller rapporter.

**Artefakter / beviser**

* Leverandørregister
* Standardkontraktklausuler
* Tredjepartsrapporter og audits

**Prioritet:** Meget høj for tredjeparts-afhængige tjenester

**Next steps**

1. Udarbejd standard leverandørkrav og klausultekst.
2. Gennemfør tredjepartsrisikovurdering for top 20 leverandører.

**Eksempel på kontraktklausul (kort):**
"Leverandøren skal inden for 24 timer efter opdagelse underrette Kunden om sikkerhedshændelser, der påvirker Kundens data eller tjeneste, og give detaljerede oplysninger senest inden for 72 timer."

---

## 6) Adgangsstyring og identitetskontrol

**NIS2-krav/tema:** Stærke adgangsregler, least privilege og MFA.

**ISO Annex A:** A.9 (Access control), A.7.1 (Human resource security)

**Praktiske tiltag**

* Indfør centraliseret identitetsstyring, rollebaseret adgangskontrol og periodiske adgangsreviews.
* Påkræv MFA på administrative konti og for fjernadgang.
* Implementér just-in-time adgang for kritiske operationer hvor muligt.

**Artefakter / beviser**

* Access control policies
* Adgangsreview-logs
* MFA-implementationsrapporter

**Prioritet:** Kritisk

**Next steps**

1. Identificér administrative konti og tving MFA.
2. Kør en adgangsreview for kritiske systemer.

---

## 7) Logging, overvågning og detektion

**NIS2-krav/tema:** Effektiv logning for at kunne opdage og efterforske hændelser.

**ISO Annex A:** A.12.4 (Logging and monitoring), A.16

**Praktiske tiltag**

* Centraliser logs i SIEM eller log-management med passende retention og korrelation.
* Definér logging minimumsstandarder for kritiske applikationer og infrastruktur.
* Implementér overvågning af integritetsændringer i kritiske systemer.

**Artefakter / beviser**

* SIEM-opsætning og use-cases
* Alert playbooks
* Log retention-politik

**Prioritet:** Høj

**Next steps**

1. Lav en liste over hvilket logindhold der er kritisk for hver tjeneste.
2. Opret 3 prioriterede detektions-use-cases i SIEM.

---

## 8) Sikker udvikling og patch management

**NIS2-krav/tema:** Sikker udvikling, sårbarhedsstyring og rettidig patching.

**ISO Annex A:** A.14 (System acquisition, development and maintenance), A.12.6 (Technical vulnerability management)

**Praktiske tiltag**

* Kræv secure SDLC-aktiviteter ved nyudvikling og større ændringer: code review, SCA, CI pipeline scanning.
* Centraliser patch management med prioritering efter CVSS og business-impact.
* Udfør regelmæssige sårbarhedsscanninger og penetrationstest.

**Artefakter / beviser**

* Patch-log og deployment-rapporter
* SCA- og SAST-rapporter
* PT/VA-rapporter

**Prioritet:** Høj

**Next steps**

1. Definér SLAs for patching for kritiske systemer.
2. Planlæg månedlig eller kvartalsvis sårbarhedsscanning.

---

## 9) Awareness, træning og insider-risk

**NIS2-krav/tema:** Løbende cyber awareness for ansatte og risikominimering af insidertrusler.

**ISO Annex A:** A.7.2.2 (Awareness, education and training), A.7 (Human resource security)

**Praktiske tiltag**

* Årligt obligatorisk awareness-forløb, suppleret med kvartalsvise micro-modules.
* Gennemfør phishing-simuleringer og målbar opfølgning.
* Indfør processer for offboarding og adgangsrevokation ved medarbejderafgang.

**Artefakter / beviser**

* Kursusplan og deltagelseslister
* Phishing-simulationsrapporter
* Offboarding-checklist

**Prioritet:** Medium-høj

**Next steps**

1. Sæt opfølgnings KPI: phish click-rate og completion-rate for kurser.
2. Implementér offboarding-procedure i HR-proces.

---

## 10) Dokumentation, revision og bevis

**NIS2-krav/tema:** Krav om dokumentation og evne til at demonstrere compliance ved tilsyn.

**ISO Annex A:** A.18 (Compliance), A.5

**Praktiske tiltag**

* Oprethold central dokumentmappe med politikker, procedurer, rapporter og øvelsesdokumentation.
* Planlæg interne audits og eventuelt ekstern revision hvis relevant.
* Udarbejd gap-analyse mod NIS2 og opfølgningsplan.

**Artefakter / beviser**

* Dokumentbibliotek med versionsstyring
* Audit-rapporter og opfølgningsplaner
* Gap-analyse dokument

**Prioritet:** Høj

**Next steps**

1. Opret dokumentstruktur i repo eller SharePoint med adgangskontrol.
2. Planlæg intern audit hvert år.

---

# Praktisk tjekliste for Public Administration (kopiér ind i checklists.md)

* [ ] Informationssikkerhedspolitik godkendt af ledelsen
* [ ] Udpeget ansvarlig for cybersikkerhed (CISO eller tilsvarende)
* [ ] Risikovurdering gennemført for top 10 kritiske systemer
* [ ] Incident Response-plan med 24/72h rapportskabeloner
* [ ] Leverandørregister og standard sikkerhedsklausuler
* [ ] BCP/DRP for kritiske tjenester med testplan
* [ ] MFA for administrative konti og fjernadgang
* [ ] SIEM eller log-central med mindst 3 prioriterede detektions-use-cases
* [ ] Patch management SLA dokumenteret og implementeret
* [ ] Awareness-program med dokumenteret deltagelse
* [ ] Dokumentbibliotek klar til tilsyn

---

# Eksempel: Mindre incident response playbook (skabelon)

1. Titel: Ransomware på fagsystem X
2. Formål: Hurtig containment, minimal datatab, opfylde rapporteringsfrist
3. Roller og kontaktinfo: IR leder, IT-drift, kommunikationsansvarlig, juridisk, leverandørkontakt
4. Opdagelse: Hvad udløser playbook (alarmer, brugerrapport)
5. Initial containment: Isoler påvirkede hosts, deaktiver netværksadgang til backup-mål
6. Kommunikation: Internt, ekstern (borgerinfo), myndighedsnotifikation (24h)
7. Evidence preservation: Gem logs, skærmbilleder, snapshots
8. Recovery: Restaurer fra verificerede backups, verifikationstest før genstart
9. Lessons learned: Post-mortem, opdater playbooks og træningsplan

---

# Forslag til prioritets-roadmap 6-12 måneder

Måned 0-1:

* Signér sikkerhedspolitik og udpeg CISO
* Opret leverandørregister og indfør kontraktskabelon

Måned 1-3:

* Kickoff risikovurdering top 10 systemer
* Udform 24/72h rapportskabeloner
* MFA på administrative konti

Måned 3-6:

* Implementér SIEM / log central use-cases
* Gennemfør første tabletop IR-øvelse
* Definér RTO/RPO for kritiske systemer

Måned 6-12:

* Gennemfør DR-test for mindst én kritisk tjeneste
* Ekstern sårbarhedstest / penetrationstest
* Kør phishing-simulering og kør awareness-kursus

---
---




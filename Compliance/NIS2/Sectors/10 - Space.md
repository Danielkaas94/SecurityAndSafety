#NIS2 #EssentialSector #Space  

---

## 🛰️ Space Sector (Essentielle enheder)

### 1. Introduktion

Rummets domæne omfatter operatører, producenter og tjenesteudbydere, der er involveret i design, opsendelse, drift og anvendelse af rumteknologier og infrastrukturer.
Formålet med NIS2’s inddragelse af *Space* er at sikre kontinuitet, pålidelighed og beskyttelse af data og tjenester, som understøtter kritiske samfundsfunktioner på Jorden.

Eksempler på afhængige områder:

* GPS / Galileo / GNSS navigation
* Satellitbaseret kommunikation (fx militær, maritim, luftfart)
* Jordobservationsdata (klima, miljø, sikkerhed)
* Rumbaseret overvågning og forsvar

---

### 2. Typiske aktører

| Aktørtype                            | Eksempler                                                   |
| ------------------------------------ | ----------------------------------------------------------- |
| **Satellitoperatører**               | ESA, EUMETSAT, Airbus Defence & Space                       |
| **Bakkestationer / Mission Control** | DLR, Thales Alenia Space, private jordstationer             |
| **Leverandører og producenter**      | RUAG, OHB, SpaceX, GomSpace (DK)                            |
| **Tjenesteudbydere**                 | Navigationstjenester, kommunikationsudbydere, dataplatforme |

---

### 3. Centrale NIS2-krav og ISO 27001-mapping

| NIS2 Krav                   | Beskrivelse                                                                     | ISO 27001 Annex A Mapping |
| --------------------------- | ------------------------------------------------------------------------------- | ------------------------- |
| Risikostyring               | Identificér trusler mod satellitdata, signalintegritet og jordstationer.        | A.5.4, A.8.8, A.15.1      |
| Fysisk sikkerhed            | Beskyt opsendelsesfaciliteter, kontrolcentre og jordstationer.                  | A.7.4, A.11.1             |
| Sikker software og firmware | Verificér firmware og kommandointerfaces mod kompromittering.                   | A.8.29, A.8.31            |
| Leverandørstyring           | Håndtér underleverandører (raketfirmaer, datalink, antenneoperatører).          | A.5.19, A.5.20            |
| Kommunikationssikkerhed     | Kryptering af kommandolinks, uplink/downlink kontrol.                           | A.8.24, A.8.28            |
| Incident response           | Etabler rutiner for hændelser, fx tab af signal, uautoriserede kommandoer.      | A.5.23, A.5.25            |
| Business continuity         | Backup af mission control, redundante links, failover til andre bakkestationer. | A.5.29, A.5.30            |

---

### 4. Centrale trusler

* **Jamming & Spoofing** (forvrængning af signaler, især GNSS)
* **Cyberangreb mod kontrolsystemer** (command uplink kompromittering)
* **Supply chain attacks** (komponenter, software i satellitter og jordstationer)
* **Fysisk sabotage** (antenner, jordstationer, fiberlinjer)
* **Rumaffald og kollisioner** (indirekte risici for kritiske tjenester)

---

### 5. Eksempler på kontroller

* Krypteret telemetri og kommando-protokoller (fx CCSDS-standarder)
* Network segmentation mellem mission control og administrations-IT
* Kontinuerlig overvågning af signalintegritet (anti-jamming teknologi)
* Penetrationstests mod satellit-jord kommunikationskanaler
* Geo-fencing af kontrolkommandoer (kun tilladt fra bestemte steder/IP’er)

---

### 6. Ressourcer

* [NIS2Resources.eu – Space Sector](https://nis2resources.eu/sectors/space/)
* [ESA Security Framework](https://www.esa.int/Security)
* [ENISA – Space Cybersecurity](https://www.enisa.europa.eu/topics/space)
* [EU Agency for the Space Programme (EUSPA)](https://www.euspa.europa.eu/)
* [Galileo Signal Authentication](https://www.gsc-europa.eu/galileo-services/galileo-open-service)

---

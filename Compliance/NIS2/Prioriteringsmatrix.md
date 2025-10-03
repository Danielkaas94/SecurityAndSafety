#NIS2 #MFA #MultiFactorAuthentication #Matrix #Prioriteringsmatrix

Så bygger vi videre på øve-casen med en **prioriteringsmatrix**.
Formålet er at kunne vurdere hvilke gaps, der skal adresseres først (hurtige wins vs. store strategiske projekter).

Jeg tager de 7 gaps fra tabellen og placerer dem ud fra to akser:

* **Risiko** (Lav/Høj) → Hvor kritisk er det, hvis gappet ikke lukkes?
* **Indsats** (Lav/Høj) → Hvor mange ressourcer kræver det at lukke gappet?

---

## Prioriteringsmatrix (fiktivt eksempel)

### Hurtige gevinster (Lav indsats – Høj risiko)

* **Adgangskontrol (MFA)**: Kan implementeres relativt hurtigt, men risikoen er høj, hvis der sker kompromittering.
* **Incident Management (rapporteringsprocedurer)**: Procedurer kan laves på kort tid, men uden dem er risikoen for NIS2-brud meget høj.

### Strategiske investeringer (Høj indsats – Høj risiko)

* **Risikostyring**: At etablere en kommunedækkende proces kræver tid og ressourcer, men er centralt for NIS2.
* **Business Continuity/DRP**: At udvikle og teste en fuld plan er ressourcekrævende, men risikoen ved at mangle den er høj.

### Lavere prioritet / Vedligehold (Lav indsats – Lav risiko)

* **Awareness-træning**: Giver værdi, men konsekvensen af manglende træning er ikke lige så kritisk som fx manglende MFA.
* **Ledelsesansvar (rapporter til direktion/byråd)**: Kan hurtigt etableres, men risikoen er primært governance-relateret, ikke teknisk kritisk.

### Langsigtede forbedringer (Høj indsats – Lav/moderat risiko)

* **Forsyningskædesikkerhed**: Det kræver meget arbejde at ændre kontrakter og auditere leverandører. Risikoen er moderat, men stigende, da kommunen er afhængig af eksterne IT-leverandører.

---

📊 Hvis du skulle visualisere det i en 2x2 matrix, ville det se sådan ud:

```
                 Høj Risiko
                 ──────────────
                 | Hurtige     | Strategiske
      Lav indsats| gevinster   | investeringer
                 | (MFA,       | (Risikostyring,
                 | Incident Mg)| BCP/DRP)
────────────────────────────────────────────
                 | Lavere      | Langsigtede
                 | prioritet   | forbedringer
      Høj indsats| (Awareness, | (Forsyningskæde)
                 | Ledelse)    |
                 ──────────────
                 Lav Risiko
```

---


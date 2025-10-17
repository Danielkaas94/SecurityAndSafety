## CIS Control 02: Inventory and Control of Software Assets

### 🎯 Purpose

Actively manage (inventory, track, and correct) all **software assets** on enterprise systems to ensure that only authorized and supported software is installed and can execute, while unauthorized or unmanaged software is identified and prevented from installation or execution.

The goal is to reduce attack surfaces introduced by unapproved, outdated, or vulnerable software.

---

### 🧩 Key Principles

* **Visibility:** Know what software exists and where it runs.
* **Authorization:** Only approved software should be installed or executed.
* **Version Control:** Maintain updated and patched versions of all applications.
* **Automation:** Use tools to detect and remove unauthorized software automatically.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------- |
| **2.1** | Establish and maintain a detailed inventory of all authorized software within the organization.                       |
| **2.2** | Deploy automated tools (e.g., agents or scanners) to detect installed software and compare against the approved list. |
| **2.3** | Ensure all software has a documented business purpose and designated owner.                                           |
| **2.4** | Restrict the ability for users to install or execute unapproved software.                                             |
| **2.5** | Regularly review and reconcile software inventories to ensure accuracy.                                               |
| **2.6** | Remove or isolate unauthorized or unsupported software immediately.                                                   |

---

### 🧰 Example Tools

* **Software Inventory:** Lansweeper, GLPI, SCCM, Open-AudIT
* **Endpoint Management:** Microsoft Intune, Jamf, Ansible, Puppet
* **Application Whitelisting:** AppLocker, Carbon Black, OS native policies (Windows Defender Application Control, SELinux)

---

### 🧠 Best Practices

* Maintain a **Software Allowlist** and **Denylist** for consistent enforcement.
* Integrate your software inventory with **vulnerability scanners** (e.g., OpenVAS, Nessus) for version monitoring.
* Use **digital signatures** or **hash validation** to confirm software integrity.
* Periodically audit high-risk endpoints (e.g., developer machines, admin laptops).

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                                        |
| ---------------------- | ------------------------- | ---------------------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Asset and software management to ensure security of information systems.           |
| **ISO/IEC 27001:2022** | A.8.1 & A.8.7             | Inventory of assets and protection against malware, including software control.    |
| **NIST CSF**           | ID.AM-2 / PR.IP-1         | Software assets are inventoried and maintained; baselines established for systems. |

---

### 📊 Example Policy Snippet

```text
All software deployed on corporate systems must be approved, licensed, and documented in the enterprise software inventory.  
Unapproved software is prohibited and subject to immediate removal.  
Administrators must review software inventories monthly to ensure compliance with approved baselines.
```

---

### 📚 References

* [CIS Control 02 – Inventory and Control of Software Assets](https://www.cisecurity.org/controls/inventory-and-control-of-software-assets)
* [NIST SP 800-53 Rev.5 – CM-8 & CM-10](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 8.7](https://www.iso.org/standard/75652.html)

---

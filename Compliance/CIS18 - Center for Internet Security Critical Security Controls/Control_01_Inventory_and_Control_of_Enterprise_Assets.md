Excellent — here’s the draft for your first CIS control file:
`/compliance/CIS18/Control_01_Inventory_and_Control_of_Enterprise_Assets.md`

---

## CIS Control 01: Inventory and Control of Enterprise Assets

### 🎯 Purpose

Actively manage (inventory, track, and correct) all **enterprise assets** — including end-user devices, network devices, IoT, and servers — to ensure that only authorized devices are granted access, and unauthorized devices are identified and removed.

The goal is to maintain visibility and control over all assets that can connect to your organization’s network or handle business data.

---

### 🧩 Key Principles

* **Asset Visibility:** You can’t secure what you don’t know exists.
* **Authorization:** Each device must be explicitly approved before connecting to the enterprise network.
* **Continuous Monitoring:** Detect and respond to unauthorized or rogue assets.
* **Data Integrity:** Maintain accurate and up-to-date inventories to support patching, configuration, and incident response efforts.

---

### ⚙️ Implementation Steps

| Step    | Description                                                                                                                        |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **1.1** | Establish and maintain a detailed inventory of all enterprise assets (workstations, laptops, servers, network devices, IoT, etc.). |
| **1.2** | Utilize automated discovery tools to identify new or unknown devices connected to the network.                                     |
| **1.3** | Ensure asset inventory is updated automatically when assets are added, removed, or modified.                                       |
| **1.4** | Assign a unique identifier and owner for each asset.                                                                               |
| **1.5** | Implement network access control (NAC) or similar mechanisms to prevent unauthorized assets from connecting.                       |
| **1.6** | Regularly review and reconcile discovered assets with inventory records.                                                           |

---

### 🧰 Example Tools

* **Network Scanners:** Nmap, Angry IP Scanner, Advanced IP Scanner
* **Asset Management:** GLPI, OCS Inventory, Lansweeper, Snipe-IT
* **NAC Solutions:** Cisco ISE, Aruba ClearPass, pfSense packages

---

### 🧠 Best Practices

* Integrate inventory data with **vulnerability management** and **patching systems**.
* Use **tagging** or **naming conventions** to categorize assets by department, owner, or risk level.
* Include **virtual machines** and **cloud instances** (e.g., AWS EC2, Azure VMs) in your inventory.
* Validate that your asset management process is reflected in **incident response** and **change management** workflows.

---

### 🔒 Mappings to Other Frameworks

| Framework              | Reference                 | Description                                                             |
| ---------------------- | ------------------------- | ----------------------------------------------------------------------- |
| **NIS2**               | Annex I – Risk Management | Identification and management of network and information system assets. |
| **ISO/IEC 27001:2022** | A.5.9 & A.8.1             | Inventory of assets and acceptable use of assets.                       |
| **NIST CSF**           | ID.AM-1 / ID.AM-2         | Physical and software assets are inventoried and managed.               |

---

### 📊 Example Policy Snippet

```text
All devices that connect to the corporate network must be registered in the enterprise asset inventory system.  
Unauthorized devices are prohibited and will be automatically quarantined or disconnected.  
Asset inventories must be reviewed monthly for accuracy and completeness.
```

---

### 📚 References

* [CIS Control 01 – Inventory and Control of Enterprise Assets](https://www.cisecurity.org/controls/inventory-and-control-of-enterprise-assets)
* [NIST SP 800-53 Rev.5 – CM-8](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
* [ISO/IEC 27002:2022 – Clause 5.9](https://www.iso.org/standard/75652.html)

---


<div align="center">

## [How Denmark’s Welfare State Became a Surveillance Nightmare 📸📽️👹](https://www.wired.com/story/algorithms-welfare-state-politics/?bxid=632df0b6aff41e483d0f8f6e&cndid=70938262&esrc=MARTECH_ORDERFORM&mbid=mbid%3DCRMWIR012019%0A%0A&source=EDT_WIR_NEWSLETTER_0_DAILY_ZZ&utm_mailing=WIR_Daily_030723_Special_Suspicion_Machine)
## [The Cyber Threat Against Denmark 🧑‍💻](https://www.cfcs.dk/en/cybertruslen/threat-assessments/the-cyber-threat-against-denmark/)
## [💸💸 Forsikringsselskaber har undervurderet cybertruslen: Ransomware får priserne til at stige 💸💸](https://www.version2.dk/artikel/forsikringsselskaber-har-undervurderet-cybertruslen-ransomware-faar-priserne-til-stige)
## [🔥🌶️Dansk hostingselskab lagt ned af ransomware: Kunder har mistet al data 🌶️🔥](https://www.version2.dk/artikel/dansk-hostingselskab-lagt-ned-af-ransomware-kunder-har-mistet-al-data)

# 🔐 Security & Safety 🔐
SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY, SECURITY &amp; SAFETY

<img alt="Sad Phone User 🤳" src="https://github.com/Danielkaas94/SecurityAndSafety/blob/main/SadPhoneUser.gif?raw=true">

</div>

<hr>

<div align="center">

# [Download WireShark! 🔌🦈](https://www.wireshark.org/download.html)
# [Download PyCharm: Python IDE 🐍](https://www.jetbrains.com/pycharm/download/?section=windows)
# [Download Swiss Army knife for developers (DevToys) 🛠️](https://devtoys.app)
# [🍽️🍴🔪 CyberChef 🧑‍🍳👩‍🍳👨‍🍳](https://gchq.github.io/CyberChef/)
# [🛠️📉📈 Risk Assessment Tools: Oregon State University 📈📉🛠️](https://risk.oregonstate.edu/risk-assessment-tools)

</div>

As an novice whitehat hacker, there are several tasks you can perform using the Command Prompt (CMD) to enhance your cybersecurity knowledge and protect systems. It's important to note that whitehat hacking is focused on ethical and legal practices, ensuring the security and integrity of systems. Here are a few tasks you can explore:

1. Network Diagnostics: Use CMD commands like `ipconfig`, `ping`, and `tracert` to diagnose network issues, test connectivity, and troubleshoot network problems.

2. Security Auditing: Perform basic security audits using commands such as `netstat` to identify open ports, `tasklist` to list running processes, and `systeminfo` to gather system information for vulnerability assessment.

3. Password Auditing: Utilize tools like `net user` command to manage user accounts, `wmic` to retrieve password policy information, and `secedit` to analyze security policies for password auditing purposes.

4. Malware Analysis: Employ CMD tools like `dir`, `attrib`, and `tasklist` to investigate suspicious files, folders, and processes. Use tools such as `sfc` (System File Checker) to verify the integrity of system files.

5. Log Analysis: Analyze event logs using `eventvwr` to identify potential security incidents, system errors, or anomalies.

6. Scripting and Automation: Learn to write simple batch scripts (.bat files) using CMD commands for automating tasks, such as backups, system monitoring, or routine maintenance.

7. System Administration: Familiarize yourself with CMD commands for user management (`net user`), file and folder operations (`cd`, `copy`, `move`, etc.), and system configuration (`regedit`, `gpedit.msc`) to better understand system administration tasks.

It's important to note that while using CMD commands, always ensure you have proper authorization and adhere to legal and ethical guidelines. Continuous learning, research, and staying updated with cybersecurity best practices will help you advance your skills and responsibly contribute to maintaining system security.

```bat
REM To set up the remote computer to allow remote command executions
reg add HKLM\Software\Microsoft\windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f

:: Revert Changes
reg add HKLM\Software\Microsoft\windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 0 /f
```

### Enable WireShark with Darkmode by using this command: 🌑
```bat
-platform windows:darkmode=2
```


### Display filters 📺
```
arp.opcode == 2

eth.dst && !(eth.dst[1:2] == eth.dst[3:4] && eth.dst[1:2] == eth.dst[5:6])

// TLS Client Hello
tls.handshake.type == 1

// TLS Server Hello
tls.handshake.type == 2
```


### Basic tshark in action 🔡🦈
```bat
:: Using the wi-fi for 10 seconds, write it into the file "tshark.pcap"
C:\Program Files\WireShark>tshark -i "wi-fi" -a duration:10 -w tshark.pcap

:: Using the wi-fi for 10 seconds, capture filter is DNS write it into the file "dns.pcap"
C:\Program Files\WireShark>tshark -i "wi-fi" -f "src port 53" -a duration:15 -w dns.pcap

```




<!-- ## [CloudShark ☁🦈] -->

## [The Common Vulnerabilities and Exposures (CVE) Database 🔌📡](https://www.cve.org/)

## [🧑‍💻 MITRE ATT&CK® 👩‍💻](https://attack.mitre.org/)

## [Leet Translator & Generator 1️⃣3️⃣3️⃣7️⃣](https://md5decrypt.net/en/Leet-translator/)

## [PacketLife.net 🎁📦🧬💕](https://packetlife.net/captures/protocol/telnet/)

## [MALWARE-TRAFFIC-ANALYSIS.NET 🚦📉📈⛔](https://malware-traffic-analysis.net/2017/01/28/index.html)

## [Speedguide.net - Port 4️⃣4️⃣4️⃣4️⃣ Details](https://www.speedguide.net/port.php?port=4444)

## [Old School MS-DOS Viruses in Action (15 gifs) 🦠💀](https://imgur.com/gallery/uCGGi)

## [Cain and Abel (software)](https://en.wikipedia.org/wiki/Cain_and_Abel_(software))

## [Sample Captures 📻📡📺](https://tcpreplay.appneta.com/wiki/captures.html#smallflows-pcap.)

## [How to Get Email Headers 📧🤯](https://mxtoolbox.com/Public/Content/EmailHeaders/)

## [Domain-based Message Authentication, Reporting & Conformance - What is DMARC?](https://dmarc.org/)

## [The Anti Hacker Alliance (AHA) 👨‍💻](https://anti-hacker-alliance.com/)

## [Digital Attack MapTop daily DDoS attacks worldwide 🌎](https://www.digitalattackmap.com/#anim=1&color=0&country=ALL&list=0&time=16065&view=map)

## [🛑 Blocked Internet Ports List 🛑](https://xfinity.com/support/internet/list-of-blocked-ports)

## ["Bad" TCP/UDP Ports List](https://www.garykessler.net/library/bad_ports.html)

## [List of the Top 1️⃣0️⃣0️⃣0️⃣ Ports](https://thedatalist.com/portlist/)

## [VirusTotal - Analyse suspicious files 📄🤔](https://www.virustotal.com/gui/home/upload)

## [CYBERTHREAT REAL-TIME MAP 🌏](https://cybermap.kaspersky.com/)

## [Bug Hunter University 🐞🏹🏫](https://bughunters.google.com/learn)

## [👧👦🧒👵🎅 True People Search 👩👨🧑👴🧓](https://truepeoplesearch.net/)

## [RAMMap v1.61](https://learn.microsoft.com/en-us/sysinternals/downloads/rammap)

## [Fone Finder 📱📴📲📶🤳🤙📞](http://www.fonefinder.net/)

## [DistroWatch.com 👁️🖥️👁️](https://distrowatch.com/)

## [🔎🦠 VirusTotal 🦠🔍](https://www.virustotal.com/)

## [💀 ';--have i been pwned? 💀](https://haveibeenpwned.com/)

## [🧻📜 IT Governance ISO 27001 & ISO 27002 📜🧻](https://www.itgovernance.co.uk/iso27001-and-iso27002-2022-updates)

## [🔐 Let's Encrypt](https://letsencrypt.org/)

<br>


# OSI Layer Attacks

|   | **Layer**    | **Attack**                                                                  |
|---|--------------|-----------------------------------------------------------------------------|
| 7 | Application  | Buffer overflow, XSS, DDoS                                                  |
| 6 | Presentation | Unicode vulnerability, SSL strip                                            |
| 5 | Session      | Session hijacking, DNS poisoning                                            |
| 4 | Transport    | SYN flood, invalid TCP flags, UDP flood                                     |
| 3 | Network      | ICMP flood, OS fingerprinting, IP address spoofing, routing table poisoning |
| 2 | Data Link    | Sniffing, ARP cache poisoning, macof attack                                 |
| 1 | Physical     | Cutting cables, jamming, keystroke logging                                  |


<br>

# News 🆕📰🗞️

### [SECURITYWEEK NETWORK 🧑‍💻](https://www.securityweek.com/)
### [VERSION2️⃣](https://www.version2.dk/)
### [2️⃣4️⃣Tech.dk](https://24tech.dk/)
### [🖥️Dansk IT Sikkerhed 🖥️](https://www.dkits.dk/)
### [🔎 OSINTer - Todays News 🔍](https://osinter.dk/feed/day)
### [Best 160 Cybersecurity Groups On LinkedIn](https://www.cyberdb.co/best-160-linkedin-cybersecurity-groups-on/)

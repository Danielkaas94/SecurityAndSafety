#Cracking #Hash #Hashcat #Haiti #Hashid #JohnTheRipper 

# Crack The Hash Level 2

Advanced cracking hashes challenges and wordlist generation

Password cracking is part of the penetration tester job but is rarely taught on challenges platforms. In this room you will learn to how to crack hashes, identify hash types, create custom wordlists, find specific wordlists, create mutations rules, etc.

This room is a spiritual successor to [Crack the Hash](https://tryhackme.com/room/crackthehash).

I recommend you to have done the room [Crack the hash](https://tryhackme.com/room/crackthehash) before attempting this one, which is harder and will use more advanced techniques.

However this room include a course about hash cracking before you have to face the cracking challenges, it may be a good idea to read the course part before doing [Crack the hash](https://tryhackme.com/room/crackthehash) if you are a new comer.


---

## Task 2 - Walkthrough -  Hash identification - Haiti - _**HA**sh **I**den**T**if**I**er_

[Haiti](https://noraj.github.io/haiti/) is a CLI tool to identify the hash type of a given hash. [Install](https://noraj.github.io/haiti/#/pages/install) it.

- 641+ hash types detected
- Modern algorithms supported (SHA3, Keccak, Blake2, etc.)
- Hashcat and John the Ripper references
- CLI tool & library
- Hackable

```bash
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ gem install haiti-hash
Fetching paint-2.3.0.gem
Fetching haiti-hash-3.0.0.gem
Fetching docopt-0.6.1.gem
Defaulting to user installation because default installation directory (/var/lib/gems/3.3.0) is not writable.
Successfully installed paint-2.3.0
Defaulting to user installation because default installation directory (/var/lib/gems/3.3.0) is not writable.
Successfully installed docopt-0.6.1
Defaulting to user installation because default installation directory (/var/lib/gems/3.3.0) is not writable.
WARNING:  You don't have /home/kali/.local/share/gem/ruby/3.3.0/bin in your PATH,
          gem executables (haiti, haiti-fzf, haiti-parsable, haiti_console, hashcat-haiti, john-haiti) will not run.
Successfully installed haiti-hash-3.0.0
Parsing documentation for paint-2.3.0
Installing ri documentation for paint-2.3.0
Parsing documentation for docopt-0.6.1
Installing ri documentation for docopt-0.6.1
Parsing documentation for haiti-hash-3.0.0
Installing ri documentation for haiti-hash-3.0.0
Done installing documentation for paint, docopt, haiti-hash after 0 seconds
3 gems installed

```

```bash

# Well, it seems that I need sudo
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ sudo gem install haiti-hash                                                                
[sudo] password for kali: 
Fetching haiti-hash-3.0.0.gem
Fetching paint-2.3.0.gem
Fetching docopt-0.6.1.gem
Successfully installed paint-2.3.0
Successfully installed docopt-0.6.1
Successfully installed haiti-hash-3.0.0
Parsing documentation for paint-2.3.0
Installing ri documentation for paint-2.3.0
Parsing documentation for docopt-0.6.1
Installing ri documentation for docopt-0.6.1
Parsing documentation for haiti-hash-3.0.0
Installing ri documentation for haiti-hash-3.0.0
Done installing documentation for paint, docopt, haiti-hash after 0 seconds
3 gems installed

┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ haiti                                                                                 
Usage:
  haiti [options] list
  haiti samples (<ref> | <name>)
  haiti [options] <hash>
  haiti --ascii-art
  haiti -h | --help
  haiti --version
```



Launch Haiti on this hash:  
`741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853`

```bash
# Haiti
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ haiti 741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853
RIPEMD-320 [JtR: dynamic_150]
IPMI 2.0 RAKP HMAC-SHA1 [HC: 7300]
Umbraco HMAC-SHA1 [HC: 24800]
WPA-EAPOL-PBKDF2 [HC: 2500]
WPA-EAPOL-PMK [HC: 2501]

# hashid
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ hashid 741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853
Analyzing '741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853'
[+] RIPEMD-320
```

---


### By the way! Here is a tip! Shortcut to Move to the Beginning or Ending of a Command in Linux Terminal
The ``Ctrl+A`` key combination moves the pointer to the start of the command.
The ``Ctrl+E`` key combination moves the pointer to the end of the command.

Alternatively, you can use the `HOME` and `END` key on your keyboard.

If you have space in your commands, you can use the arrows `Ctrl+⬅️` and `Ctrl+➡️`, this also works with CMD/PowerShell



Launch Haiti on this hash:
`1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee`

```bash
# Haiti
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ haiti 1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee                 
SHA-256 [HC: 1400] [JtR: raw-sha256]
GOST R 34.11-94 [HC: 6900] [JtR: gost]
SHA3-256 [HC: 17400] [JtR: dynamic_380]
Keccak-256 [HC: 17800] [JtR: raw-keccak-256]
PANAMA [JtR: dynamic_320]
BLAKE2-256 (blake2b)
BLAKE2-256 (blake2s)
MD6-256
sm3
Shake-128 (256)
Shake-256 (256)
Shake-512 (256)
BLAKE3
Streebog-256
IPMI 2.0 RAKP HMAC-SHA1 [HC: 7300]
Umbraco HMAC-SHA1 [HC: 24800]
WPA-EAPOL-PBKDF2 [HC: 2500]
WPA-EAPOL-PMK [HC: 2501]
Snefru-256 [JtR: snefru-256]
RIPEMD-256 [JtR: dynamic_140]
Haval-256 (3 rounds) [JtR: haval-256-3]
Haval-256 (4 rounds) [JtR: dynamic_290]
Haval-256 (5 rounds) [JtR: dynamic_300]
GOST CryptoPro S-Box
Skein-256 [JtR: skein-256]
                                                                                                                       
# Hashid
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ hashid 1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee                
Analyzing '1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee'
[+] Snefru-256 
[+] SHA-256 
[+] RIPEMD-256 
[+] Haval-256 
[+] GOST R 34.11-94 
[+] GOST CryptoPro S-Box 
[+] SHA3-256 
[+] Skein-256 
[+] Skein-512(256)
```

### *As you can see, what is different with haiti, is that we also get the -m code for hashcat `[HC: 1400]` and the code for John the Ripper `[JtR: raw-sha256]`*


---
---


# Task 3 - Walkthrough - **Wordlists**


For hash cracking you will often need some custom or specialized dictionaries called wordlists.

[SecLists](https://github.com/danielmiessler/SecLists) is a collection of multiple types of lists used during security assessments, collected in one place. List types include usernames, passwords, URLs, sensitive data patterns, fuzzing payloads, web shells, and many more.

[wordlistctl](https://github.com/BlackArch/wordlistctl) is a script to fetch, install, update and search wordlist archives from websites offering wordlists with more than 6300 wordlists available.

[Rawsec's CyberSecurity Inventory](https://inventory.raw.pm/overview.html) is an inventory of tools and resources about CyberSecurity. The [Cracking](https://inventory.raw.pm/tools.html#title-tools-cracking) category will be especially useful to find wordlist generator tools.

**Note**: On the exercise below we will see how to use how to use wordlistctl to download a list, for the example I took rockyou which is a famous wordlist but if you use TryHackMe AttackBox or Kali Linux you should already have it under `/usr/share/wordlists/`, so you don't need to download it again, this is just an example to show you how wordlistctl works.


*This "walkthrough" can go suck a bag of dicks, the installation `pacman -S wordlistctl` is only working for BlackArch Linux and not Kali Linux... Moron...*

## [YouTube - How to use Wordlists in Kali Linux - FAQ's](https://www.youtube.com/watch?v=kA-eWYzjX8c)


---
---


### Answer the questions below

Depending of your distribution, the John configuration may be located at `/etc/john/john.conf` and/or `/usr/share/john/john.conf`. To locate the JtR install directory run locate `john.conf`, then create `john-local.conf` in the same directory (in my case`/usr/share/john/john-local.conf`) and create our rules in here.

---

Let's use the top 10 000 most used password list from [SecLists](https://github.com/danielmiessler/SecLists#install) (`/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt`) and generate a simple border mutation by appending all 2 digits combinations at the end of each password.  
Let's edit `/usr/share/john/john-local.conf` and add a new rule:  
```bash
[List.Rules:THM01]
$[0-9]$[0-9]
```


```bash
# Installing seclists - Pretty huge compared to rockyou.txt - This is going to be interesting!
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ sudo apt -y install seclists
[sudo] password for kali: 
Installing:                     
  seclists

Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 135
  Download size: 557 MB
  Space needed: 1970 MB / 30.2 GB available

Get:1 http://kali.download/kali kali-rolling/main amd64 seclists all 2025.2-0kali1 [557 MB]
Fetched 557 MB in 1min 10s (7920 kB/s)                                                                                                
Selecting previously unselected package seclists.
(Reading database ... 651363 files and directories currently installed.)
Preparing to unpack .../seclists_2025.2-0kali1_all.deb ...
Unpacking seclists (2025.2-0kali1) ...
Setting up seclists (2025.2-0kali1) ...
Processing triggers for kali-menu (2025.4.2) ...
Processing triggers for wordlists (2023.2.0) ...
                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ 

```

## ****usr = Unix System Resources****


Now let's crack the SHA1 hash `2d5c517a4f7a14dcb38329d228a7d18a3b78ce83`, we just have to write the hash in a text file and to specify the hash type, the wordlist and our rule name. `john hash.txt --format=raw-sha1 --wordlist=/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt --rules=THM01`

#### What was the password? `moonligh56` - hash type: SHA-1



```bash
# hashid
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ hashid hash1.txt                   
--File 'hash1.txt'--
Analyzing '2d5c517a4f7a14dcb38329d228a7d18a3b78ce83'
[+] SHA-1 
[+] Double SHA-1 
[+] RIPEMD-160 
[+] Haval-160 
[+] Tiger-160 
[+] HAS-160 
[+] LinkedIn 
[+] Skein-256(160) 
[+] Skein-512(160) 

# haiti - damn I love this! The references to hashcat and john the ripper
┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ haiti 2d5c517a4f7a14dcb38329d228a7d18a3b78ce83
SHA-1 [HC: 100] [JtR: raw-sha1]
RIPEMD-160 [HC: 6000] [JtR: ripemd-160]
Double SHA-1 [HC: 4500]
Ruby on Rails Restful Auth (one round, no sitekey) [HC: 27200]
MySQL5.x [HC: 300] [JtR: mysql-sha1]
MySQL4.1 [HC: 300] [JtR: mysql-sha1]
Umbraco HMAC-SHA1 [HC: 24800]
WPA-EAPOL-PBKDF2 [HC: 2500]
WPA-EAPOL-PMK [HC: 2501]
Haval-160 (3 rounds) [JtR: dynamic_190]
Haval-160 (4 rounds) [JtR: dynamic_200]
Haval-160 (5 rounds) [JtR: dynamic_210]
HAS-160
LinkedIn [HC: 190] [JtR: raw-sha1-linkedin]
Skein-256(160)
Skein-512(160)


# Proof of Concept in Hashcat
# Hybrid wordlist + mask
-a 6  
hashcat -m 100 hash1.txt -a 6 10k-most-common.txt ?d?d


┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ hashcat -m 100 hash1.txt -a 6 10k-most-common.txt ?d?d
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-13th Gen Intel(R) Core(TM) i7-13700HX, 2317/4634 MB (1024 MB allocatable), 8MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 514 MB (3824 MB free)

Dictionary cache built:
* Filename..: 10k-most-common.txt
* Passwords.: 10000
* Bytes.....: 73017
* Keyspace..: 1000000
* Runtime...: 0 secs

2d5c517a4f7a14dcb38329d228a7d18a3b78ce83:moonligh56       
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 100 (SHA1)
Hash.Target......: 2d5c517a4f7a14dcb38329d228a7d18a3b78ce83
Time.Started.....: Sun Nov  9 11:00:29 2025 (0 secs)
Time.Estimated...: Sun Nov  9 11:00:29 2025 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (10k-most-common.txt), Left Side
Guess.Mod........: Mask (?d?d) [2], Right Side
Guess.Queue.Base.: 1/1 (100.00%)
Guess.Queue.Mod..: 1/1 (100.00%)
Speed.#01........: 34938.5 kH/s (7.81ms) @ Accel:1024 Loops:64 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 524288/1000000 (52.43%)
Rejected.........: 0/524288 (0.00%)
Restore.Point....: 0/10000 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-64 Iteration:0-64
Candidate.Engine.: Device Generator
Candidates.#01...: password12 -> benz34
Hardware.Mon.#01.: Util:  7%

Started: Sun Nov  9 11:00:18 2025
Stopped: Sun Nov  9 11:00:31 2025

```

### Let's try with john the ripper

```bash
# Proof of concept
john hash.txt --format=raw-sha1 --wordlist=/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt --rules=THM01

john hash1.txt --format=raw-sha1 --wordlist=10k-most-common.txt --rules=THM01
john hash1.txt --format=raw-sha1 --wordlist=10k-most-common.txt --mask=?d?d # Not sure?
# Correct solution from ChatGPT
john --format=raw-sha1 --wordlist=10k-most-common.txt --mask='?d?d' hash1.txt
john hash1.txt --format=raw-sha1 --wordlist=10k-most-common.txt --mask='?d?d'

# Note to self - charset 1
john --wordlist=10k-most-common.txt --mask='?1?1' --mask-charset=1=aeiou hash1.txt



┌──(kali㉿kali)-[~/Desktop/Crack the hash 2]
└─$ john hash1.txt --format=raw-sha1 --wordlist=10k-most-common.txt --rules=THM01
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
Warning: no OpenMP support for this hash type, consider --fork=8
Press 'q' or Ctrl-C to abort, almost any other key for status
moonligh56       (?)     
1g 0:00:00:00 DONE (2025-11-09 11:08) 20.00g/s 11307Kp/s 11307Kc/s 11307KC/s hotrats56..jayhawks56
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed.
```
``

---
---
---
---

# Task 5 - Walkthrough - Custom wordlist generation

As I said in the previous task mangling rules avoid to waste storage space and time but there are some cases where generating a custom wordlist could be a better idea:

- You will often re-use the wordlist, generating one will save computation power rather than using a mangling rule
- You want to use the wordlist with several tools
- You want to use a tool that support wordlists but not mangling rules
- You find the custom rule syntax of John too complex

### Answer the questions below

Let's say we know the password we want to crack is about dogs. We can download a list of dog races `wordlistctl fetch -l dogs -d` (`/usr/share/wordlists/misc/dogs.txt`). Then we can use [Mentalist](https://github.com/sc0tfree/mentalist) to generate some mutations.


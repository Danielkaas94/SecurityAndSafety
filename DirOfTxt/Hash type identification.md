
[TryHackMe - Crack The Hash](https://tryhackme.com/room/crackthehash)

*How can I just look at at hash and know if it's sha MD4/MD5, etc.?*

48bb6e862e54f2a795ffc4e541caed4d 

CBFDAC6008F9CAB4083784CBD1874F76618D2A97

1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032 

$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom 

279412f945939ba78ce0758d3fd83daa

---

F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85 

1DFECA0C002AE40B8619ECF94819CC1B

---
---

Excellent question — identifying a hash type *by sight* is a classic skill in cybersecurity and CTFs.
You can often guess the algorithm **by length, character set, and prefix/suffix patterns**.

Let’s break down your examples one by one 👇

---

### 🔹 1️⃣ `48bb6e862e54f2a795ffc4e541caed4d`

* **Length:** 32 hex characters
* **Hex only (0–9, a–f)**
  ✅ **Likely:** **MD5** (128-bit = 32 hex chars)

---

### 🔹 2️⃣ `CBFDAC6008F9CAB4083784CBD1874F76618D2A97`

* **Length:** 40 hex characters
  ✅ **Likely:** **SHA-1** (160-bit = 40 hex chars)

---

### 🔹 3️⃣ `1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032`

* **Length:** 64 hex characters
  ✅ **Likely:** **SHA-256** (256-bit = 64 hex chars)

---

### 🔹 4️⃣ `$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom`

* **Prefix:** `$2y$`
  ✅ **Likely:** **bcrypt**

  * `$2a$`, `$2b$`, `$2y$` all indicate bcrypt
  * `12` = cost factor

---

### 🔹 5️⃣ `279412f945939ba78ce0758d3fd83daa`

* **Length:** 32 hex chars again
  ✅ **Likely:** **MD5**
  (could also be MD4 or NTLM, but NTLM usually **uppercase** hex)

---

### 🔹 6️⃣ `F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85`

* **Length:** 64 hex characters
  ✅ **Likely:** **SHA-256**

---

### 🔹 7️⃣ `1DFECA0C002AE40B8619ECF94819CC1B`

* **Length:** 32 hex characters (but *uppercase*)
  ✅ **Possibly:** **MD4** or **NTLM hash**

  * NTLM hashes are *uppercase* MD4 of the UTF-16 password.

---

### 🔹 8️⃣ `$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/...`

* **Prefix:** `$6$`
  ✅ **Likely:** **SHA-512 crypt** (used in `/etc/shadow` on Linux)

---

### 🔹 9️⃣ `e5d8870e5bdd26602cab8dbe07a942c8669e56d6`

* **Length:** 40 hex chars
  ✅ **Likely:** **SHA-1**

---

### 📘 Summary Table

| Example         | Length        | Clues         | Likely Algorithm |
| --------------- | ------------- | ------------- | ---------------- |
| `48bb6e862e...` | 32            | Hex           | MD5              |
| `CBFDAC6008...` | 40            | Hex           | SHA-1            |
| `1C8BFE8F80...` | 64            | Hex           | SHA-256          |
| `$2y$12$...`    | Prefix `$2y$` | bcrypt        | bcrypt           |
| `279412f945...` | 32            | Hex           | MD5              |
| `F09EDCB1FC...` | 64            | Hex           | SHA-256          |
| `1DFECA0C00...` | 32            | Uppercase hex | NTLM / MD4       |
| `$6$aReally...` | Prefix `$6$`  | SHA-512 crypt |                  |
| `e5d8870e5b...` | 40            | Hex           | SHA-1            |

---

### 🧠 Quick Recognition Tips

| Hash Type     | Length   | Charset                | Example Prefix      |
| ------------- | -------- | ---------------------- | ------------------- |
| MD5           | 32       | hex                    | —                   |
| MD4 / NTLM    | 32       | uppercase hex          | —                   |
| SHA-1         | 40       | hex                    | —                   |
| SHA-256       | 64       | hex                    | —                   |
| SHA-512       | 128      | hex                    | —                   |
| bcrypt        | 60       | `$2a$`, `$2b$`, `$2y$` | bcrypt              |
| SHA-512 crypt | variable | `$6$`                  | Linux `/etc/shadow` |
| MD5 crypt     | variable | `$1$`                  | Linux `/etc/shadow` |

---
---

*The best tool is to use hashcat? what if I already know that the password has to be 4 in length and I use the wordlist from rock you.txt?*

Short answer: **Yes — hashcat is an excellent tool** for this.
But if you *already know the password length is exactly 4*, don’t feed hashcat a huge wordlist like `rockyou.txt` as-is — use a **mask attack** (fast, tiny keyspace) or pre-filter `rockyou` to only 4-char entries. Below I give practical, copy-paste commands plus tips for common hash types.

---

## Quick facts

* Mask attacks (`-a 3`) generate candidate passwords on the GPU/CPU and are **far faster** for known fixed lengths than running a big dictionary. ([hashcat.net][1])
* If you prefer dictionaries, filter the dictionary to length 4 first (so hashcat wastes no time).
* Some hash types (bcrypt, sha512crypt) are intentionally slow — brute forcing them is much slower and may be impractical. ([GitHub][2])

---

## Useful commands

Assume `hash.txt` contains your hash (one per line). Replace `-m <mode>` with the correct hashcat mode for your hash (examples below).

### 1) Mask attack (recommended for fixed length = 4)

Only lowercase letters:

```bash
hashcat -m <mode> -a 3 hash.txt ?l?l?l?l
```

Lowercase+digits:

```bash
hashcat -m <mode> -a 3 hash.txt ?l?l?l?d
```

Any printable ASCII (bigger keyspace; slower):

```bash
hashcat -m <mode> -a 3 hash.txt ?a?a?a?a
```

( `?l` = lower, `?u` = upper, `?d` = digit, `?s` = special, `?a` = all printable ) — mask docs. ([hashcat.net][1])

### 2) Use rockyou **but only 4-char entries** (dictionary mode)

Create a filtered file:

```bash
awk 'length($0)==4' /usr/share/wordlists/rockyou.txt > rockyou-4.txt
# or (if you want to allow spaces, use): awk 'length($0)==4' RS='\n' ORS='\n' rockyou.txt > rockyou-4.txt
```

Then run:

```bash
hashcat -m <mode> -a 0 hash.txt rockyou-4.txt
```

This is useful if you *know* the password is one of rockyou’s existing 4-char entries.

### 3) Hybrid mode (dictionary + mask) — rarely needed for exact length 4

Append 0–3 brute characters to each dictionary word, etc. Example (not common for exactly 4):

```bash
# append one digit to each word from rockyou
hashcat -m <mode> -a 6 hash.txt rockyou-4.txt ?d
```

Docs: hybrid/combinator overview. ([hashcat.net][1])

### 4) Output & tuning

* Show cracked: `hashcat --show -m <mode> hash.txt -o found.txt`
* Use optimized kernels for fast short-password work: `-O` (but this limits max password length).
* Workload profile: `-w 3`.
* Keep `--potfile-path` in mind if reusing potfiles.

---

## Common hashcat `-m` mode numbers (examples)

(Use the exact `-m` for your hash; wrong mode → errors / no cracks.)

* MD5 = `-m 0` (raw MD5). ([hashcat.net][3])
* SHA1 = `-m 100`. ([hashcat.net][3])
* MD4 = `-m 900`. ([Black Hills Information Security, Inc.][4])
* NTLM = `-m 1000`. ([Black Hills Information Security, Inc.][4])
* SHA256 = `-m 1400`. ([Black Hills Information Security, Inc.][4])
* SHA512 = `-m 1700` (raw). ([Black Hills Information Security, Inc.][4])
* bcrypt (`$2y$`, `$2a$`) = `-m 3200` — **very slow compared to MD5**. ([GitHub][2])
* sha512crypt (`$6$` shadow format) = `-m 1800`. ([Black Hills Information Security, Inc.][5])

If you aren’t sure which mode to use, use a hash identifier tool (e.g., `hashid`, `hash-identifier`) or visually check prefixes (`$2y$`, `$6$` etc.) — hashes without a prefix need size/length identification. Example hashes page on the hashcat wiki is useful. ([hashcat.net][3])

---

## Which is *faster*: rockyou filtered vs mask?

* If you know **exactly** 4 characters and the charset (e.g., lowercase only), the **mask** `?l?l?l?l` is faster: it enumerates only the needed keyspace internally on GPU/P\nCPU.
  Example keyspace sizes:

  * `?l?l?l?l` = 26⁴ = 456,976 candidates → trivial.
  * `rockyou.txt` has ~14M lines; filtering to only 4-char lines might be much smaller, but still likely larger than the small mask.
    So: **mask** first; if that fails, try filtered rockyou (or rules on rockyou).

---

## Special note on bcrypt & other slow hashes

If the hash is bcrypt (`$2y$...`) or sha512crypt (`$6$...`), cracking even a 4-char password will be **orders of magnitude slower** than raw MD5. It may still be feasible for 4 chars (small keyspace), but expect far fewer attempts/second — check hashcat benchmarking to estimate time. ([GitHub][2])

---

## Example end-to-end: MD5, 4 lowercase letters

1. Put the hash in `hash.txt` (no extra characters).
2. Run:

```bash
hashcat -m 0 -a 3 -w 3 hash.txt ?l?l?l?l -O -o cracked.txt
```

3. After it runs, check:

```bash
hashcat --show -m 0 hash.txt
```

---

## Final tips

* Always confirm **hash type** first (prefixes like `$2y$` or `$6$` help; when in doubt use a hash identifier). ([hashcat.net][3])
* For fixed, small lengths — **mask** is your fastest route. ([hashcat.net][1])
* If you *must* use rockyou, **filter** it to the exact length to avoid wasting time.
* Respect legality and ethics: only crack hashes you own or are authorized to test.

---

If you want, tell me the **hash type** (or paste one hash and its prefix), and I’ll give the exact hashcat `-m` number and the exact command you'd run (mask vs filtered rockyou), plus an estimated keyspace and a realistic time/speed note based on hash type.

[1]: https://hashcat.net/wiki/doku.php?id=hybrid_attack&utm_source=chatgpt.com "Hybrid Attack"
[2]: https://github.com/hashcat/hashcat/issues/2490?utm_source=chatgpt.com "Hashmode: 3200 - bcrypt $2*$, Blowfish (Unix)"
[3]: https://hashcat.net/wiki/doku.php?id=example_hashes&utm_source=chatgpt.com "example_hashes [hashcat wiki]"
[4]: https://www.blackhillsinfosec.com/wp-content/uploads/2020/09/HashcatCheatSheet.v2018.1b.pdf?utm_source=chatgpt.com "hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask"
[5]: https://www.blackhillsinfosec.com/hashcat-cheatsheet/?utm_source=chatgpt.com "Hashcat Cheatsheet"

# Lektion 1

## Tilfældige tal

[En simpel algoritme](http://gugl.dk/rand1.html)


##### [Wikipedia - Linear congruential generator (LCG)](https://en.wikipedia.org/wiki/Linear_congruential_generator)


##### [Python - random() 🐍](https://docs.python.org/3/library/random.html)

Python uses the Mersenne Twister as the core generator. It produces 53-bit 
precision floats and has a period of 2**19937-1. The underlying implementation in 
C is both fast and threadsafe. The Mersenne Twister is one of the most extensively 
tested random number generators in existence. However, being completely 
deterministic, it is not suitable for all purposes, and is completely unsuitable for 
cryptographic purposes.


##### [True Random](http://gugl.dk/truerandom.html)
```javascript
var count = 0;
 var totalcount = 0;
 function counting() {
    count++;
    setTimeout(counting,0);  // put back in run queue
 }
 function printbinary() { … }
 var interval;
 interval = setInterval(printbinary,1000)    // 1 second
 counting();
```


##### [Click Random](http://gugl.dk/click.html)


##### [Linux Commands - /dev/random vs /dev/urandom and are they secure?](https://linuxhint.com/dev_random_vs_dev_urandom/)

```python
c = [0]*256
with open("/dev/random", 'rb') as f:
    b = f.read(256000)
    for a in b:
        c[int(a)] += 1
min = 10000000
max = 0

for cc in c:
    if cc>max: max=cc
    if cc<min: min=cc

 print("min: ",min,"max: ",max)
```



## SQL Injection



##### [Wordpress - Source Code](https://wordpress.org/download/source/)

`git clone git://develop.git.wordpress.org/`

`grep -ir mysqli`


##### [Definition - legacy system (legacy application)](https://www.techtarget.com/searchitoperations/definition/legacy-application)

---
- Escaping
- Prepared statements
- Object Relational Mapping (ORM)
---


<br>

---
---

# Lektion 2

## XXS - Cross Site Scripting ✝️

##### [Wikipedia - Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)

- `< til &lt;`
- `> til &gt;`
- `& til &amp;`
- `" til &quot;`

---

#### [Søg på dr.dk - Horsens](https://www.dr.dk/soeg?query=horsens)


#### [Søg på dr.dk - <script>alert(7);</script>](https://www.dr.dk/soeg?query=%3Cscript%3Ealert(7);%3C/script%3E)

---

#### [reflected1](http://gugl.dk/xss/reflected1/)
#### [reflected2](http://gugl.dk/xss/reflected2/)


#### [stored1](http://gugl.dk/xss/stored1/)
#### [stored2](http://gugl.dk/xss/stored2/)

---


#### [OWASP - DOM Based XSS](https://owasp.org/www-community/attacks/DOM_Based_XSS)

#### [StackOverflow - HTML-encoding lost when attribute read from input field](https://stackoverflow.com/questions/1219860/html-encoding-lost-when-attribute-read-from-input-field)

#### [StackOverflow - Unescape HTML entities in JavaScript?](https://stackoverflow.com/questions/1912501/unescape-html-entities-in-javascript/34064434#34064434)

#### [StackOverflow - HTML-encoding lost when attribute read from input field](https://stackoverflow.com/questions/1219860/html-encoding-lost-when-attribute-read-from-input-field)

#### [xssdemo](http://gugl.dk/xssdemo/)

#### [Dev - Mozilla - Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)


---
---
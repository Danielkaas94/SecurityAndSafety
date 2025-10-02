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

# Lektion 3

## Inputvalidering

- regex

[Regex to validate date formats dd/mm/YYYY, dd-mm-YYYY, dd.mm.YYYY, dd mmm YYYY, dd-mmm-YYYY, dd/mmm/YYYY, dd.mmm.YYYY with Leap Year Support - Stack Overflow](https://stackoverflow.com/questions/15491894/regex-to-validate-date-formats-dd-mm-yyyy-dd-mm-yyyy-dd-mm-yyyy-dd-mmm-yyyy)


```python
import datetime
 import re
 def validatedate(inputdate):
  m = re.match('^(\d\d)-(\d\d)-(\d\d\d\d)$',inputdate)
  if not m:
    return False
  try:
    dd = int(m.group(1))
    mm = int(m.group(2))
    yyyy = int(m.group(3))
    result = datetime.date(yyyy,mm,dd)
    return True
  except ValueError:
    return False
```

```python
(?x) # modifier x: free spacing mode (for comments)
 # verify date dd/mm/yyyy; possible separators: -.,/ 
# valid year range: 0000-9999
 ^ # start anchor 
# precheck xx-xx-xxxx,... add new separators here 
(?=\d{2}([-.,\/])\d{2}\1\d{4}$)
 (?: # day-check: non caturing group 
  # days 01-28 
  0[1-9]|1\d|[2][0-8]| 
  # february 29d check for leap year: all 4y / 00 years: only each 400 # 0400,0800,1200,1600,2000,... 
  29 
    (?!.02. # not if feb: if not ... 
       (?! # 00 years: exclude !0 %400 years 
           (?!(?:[02468][1-35-79]|[13579][0-13-57-9])00) 
           # 00,04,08,12,... 
           \d{2}(?:[02468][048]|[13579][26]) ) )|
```


```C#
<%@ language="C#" %>
 <form id="form1" runat="server">
    <asp:TextBox ID="txtName" runat="server"/>
    <asp:Button ID="btnSubmit" runat="server" Text="Submit" />
    <asp:RegularExpressionValidator ID="regexpName" runat="server"     
                    ErrorMessage="This expression does not validate." 
                    ControlToValidate="txtName"
                    ValidationExpression="^[a-zA-Z'.\s]{1,40}$" />
 </form>
```


[Part 9, add validation to an ASP.NET Core MVC app | Microsoft Learn](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/validation?view=aspnetcore-8.0)


---

[Ng-Pattern Examples - LearnKode](https://www.learnkode.com/Examples/Angular/Ng-Pattern)


```html
<ng-form name="mailForm">
    Email: <input type="text" ng-model="mail" name="mail" ng-pattern="re" /><br />
    </ng-form>
    <script>
    var app = angular.module("app", []);
    app.controller('controllerName', ['$scope', function ($scope) {
        $scope.mail = "visrosoftware@gmail.com";
        $scope.re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    }]);
 </script>
 </body>
```

---

### HTML 5

```html
<form action="/action_page.php">
 Country code: <input type="text" name="country_code"
  pattern="[A-Za-z]{3}" title="Three letter country code">
 <input type="submit">
 </form>
```

### Positive lookahead

- `^(?=.*[a-z]) (?=.*[A-Z]) (?=.*[0-9]) (?=.{8,})`

---


[Noget med datoer (gugl.dk)](http://gugl.dk/date.html)

#### Klient og/eller server?

Man bør inputvalidere på klient.
Man skal inputvalidere på server.

På klienten kan man give hurtigt feedback, og aflaste serveren. På serveren 
skal der inputvalideres, for man kan ikke stole på hvad der kommer fra 
klienten.

De to valideringer, klient og server, behøver ikke være lavet på samme måde. 

---
---


import re 
from time import time
from colorama import init, Fore, Back, Style

# A - regex True
# B - regex False

# C - regex precompiled True
# D - regex precompiled False

# E - programming True
# F - programming False

def check1(d):
  m = re.match(r'^\d\d\d\d-\d\d-\d\d$',d)
  if m:
    return True
  else:
    return False

t = time()
count = 0
for i in range(1000000):
  if check1('9999-99-99'):
     count = count+1
print('A',count, time()-t, Fore.BLUE + " regex True")

t = time()
count = 0
for i in range(1000000):
  if not check1('999x-99-99'):
     count = count+1
print('B',count, time()-t, Fore.RED + " regex False")


def check2(d):
  m = prog.match(d)
  if m:
    return True
  else:
    return False

t = time()
prog = re.compile(r'^\d\d\d\d-\d\d-\d\d$')
count = 0
for i in range(1000000):
  if check2('9999-99-99'):
     count = count+1
print('C',count, time()-t, Fore.LIGHTBLUE_EX + " regex precompiled True")

t = time()
prog = re.compile(r'^\d\d\d\d-\d\d-\d\d$')
count = 0
for i in range(1000000):
  if not check2('999x-99-99'):
     count = count+1
print('D',count, time()-t, Fore.LIGHTRED_EX + " regex precompiled False")

def checkdigits(s):
 for c in s: 
 #  print(c)
   if (c>='0' and c<='9'):
     pass
   else:
     return False
 return True
 


def check3(d):
  d = d.strip();
  a = d.split("-")

  if len(a)!=3:
    return False;

  if not checkdigits(a[0]):
    return False;

  if len(a[0])!=4:
    return False
         
  if not checkdigits(a[1]):
    return False;

  if len(a[1])!=2:
    return False
         
  if not checkdigits(a[2]):
    return False;

  if len(a[2])!=2:
    return False
         
  return True

t = time()
count = 0
for i in range(1000000):
  if check3('9999-99-99'):
     count = count+1
print('E',count, time()-t, Fore.LIGHTCYAN_EX + " programming True")


# 
t = time()
count = 0
for i in range(1000000):
  if not check3('999x-99-99'):
     count = count+1
print('F',count, time()-t, Fore.LIGHTMAGENTA_EX + " programming False")
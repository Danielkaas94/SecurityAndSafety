#!/usr/bin/python3
import hashlib
from time import sleep

PASSWORD_MD5HASH="973cc08c6aa6d171ed0ebf31675517ae"
BLOCK_01="ymca"
BLOCK_03="mmdk"

CHAR_SET="abcdefghijklmnopqrstuvxyz0123456789"

for char1 in CHAR_SET:
    for char2 in CHAR_SET:
        for char3 in CHAR_SET:
            for char4 in CHAR_SET:
                BLOCK_02 = char1+char2+char3+char4

                PASSWORD_TEST = BLOCK_01+BLOCK_02+BLOCK_03
                HASH_TEST = hashlib.md5(PASSWORD_TEST.encode('utf-8')).hexdigest()
                print(HASH_TEST)

                if HASH_TEST == PASSWORD_MD5HASH:
                    print('GOT IT')
                    print(f'PASSWORD ER {PASSWORD_TEST} og md5 hash er {HASH_TEST}')
                    sleep(2)
                    break


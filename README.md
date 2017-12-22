ENCRYPT / DECRYPT FILES WITH PYCRYPTODOME
=========================================

Most of the code is readable in **crypt.py** script. Using AES symmetrical
encryption logic, based on 128-bits only (check for strong encryption, with 256
or more).

**AESCipher.py** is just a simple class to encrypt / decrypt one line of
strings. TODO: try to convert it as a file encrypt / decrypt tool?

Most of those code comes from:

An old exemple, not working at this time:
(https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto)[https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto]

A re-writing of the previous version here, working fine:
(https://forum.level1techs.com/t/the-knights-of-python-ep-1-0-crypto-simple-file-encryption/110068)[https://forum.level1techs.com/t/the-knights-of-python-ep-1-0-crypto-simple-file-encryption/110068]



Some librairies available on Pypy:

- Kryptonite: (https://github.com/gilsho/kryptonite)[https://github.com/gilsho/kryptonite]
- SimpleAES: (https://github.com/NilayKulkarni/SimpleAES)[https://github.com/NilayKulkarni/SimpleAES]

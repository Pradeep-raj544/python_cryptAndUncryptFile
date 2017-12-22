# FROM: https://forum.level1techs.com/t/the-knights-of-python-ep-1-0-crypto-simple-file-encryption/110068

from hashlib import sha256
import os, random, struct

from Crypto import Random
from Crypto.Cipher import AES

CHUNKSIZE = 64*1024


def set_pwd(password):
    return sha256(password.encode('utf-8')).digest()


def encrypt(key, infile, outfile=None, chunksize=CHUNKSIZE):
    if not outfile:
        outfile = infile + '.enc'
        #IV = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        #IV = bytes(IV, encoding='utf-8')
    filesize = str(os.path.getsize(infile)).zfill(16)
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(infile, 'rb') as f_in:
        with open(outfile, 'wb') as f_out:
            #f_out.write(struct.pack('<Q', filesize))
            f_out.write(filesize.encode('utf-8'))
            f_out.write(IV)

            while True:
                chunk = f_in.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    #chunk += bytes(' ' * (16 - len(chunk) % 16),
                    #               encoding='utf-8')
                    chunk += b' ' * (16 - (len(chunk) % 16))
                f_out.write(encryptor.encrypt(chunk))

def decrypt(key, infile, outfile=None, chunksize=CHUNKSIZE):
    if not outfile:
        filepath, ext = os.path.splitext(infile)
        filename = filepath.split('/')[-1]
        outfile = f"decrypted-{filename}{ext}"

    with open(infile, 'rb') as f_in:
        #something = f_in.read(struct.calcsize("Q"))
        filesize = int(f_in.read(16))
        IV = f_in.read(16)
        #origsize = struct.pack('<Q', something)[0]
        #IV = f_in.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outfile, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunksize)
                if len(chunk) == 0:
                    break
                f_out.write(decryptor.decrypt(chunk))

            f_out.truncate(filesize)


if __name__ == '__main__':
    ask = input("Password: ")
    pwd = set_pwd(ask)

    choice = input("(E)ncrypt or (D)ecrypt? ")
    if choice == 'E':
        ask_file = input("What file? ")
        encrypt(pwd, ask_file)
        print("Done.")

    elif choice == 'D':
        ask_file = input("Decrypt what file? ")
        decrypt(pwd, ask_file)
        print("Done.")

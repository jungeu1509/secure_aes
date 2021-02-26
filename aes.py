import base64
import hashlib
import time
import sys
import binascii
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

#padding size
BS = 16
#padding
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
#unpadding
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def usage():
    print("How to use "+sys.argv[0])
    print("=========================================================================")
    print(sys.argv[0]+", decode/encode, mode, key, iv, input_file, output_filename")
    print("-------------------------------------------------------------------------")
    print("- Decode : dec / Encode : enc")
    print("- Mode : CBC, CTR")
    print("-------------------------------------------------------------------------")
    print("-h or --help : print how to use")

class AESCipher:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt_CBC(self, raw):
        #padding
        raw = pad(raw)
        #encrypt with cbc
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw.encode('utf-8')))
    
    def decrypt_CBC(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(enc))

    def encrypt_CTR(self, raw):
        iv_int = int(binascii.hexlify(self.iv), 16)
        ctr = Counter.new(128, initial_value=iv_int)
        cipher = AES.new(self.key, AES.MODE_CTR, counter = ctr)
        return cipher.encrypt(raw.encode('utf-8'))
    
    def decrypt_CTR(self, enc):
       # enc = base64.b64decode(enc)
        iv_int = int(binascii.hexlify(self.iv), 16)
        ctr = Counter.new(128, initial_value=iv_int)
        cipher = AES.new(self.key, AES.MODE_CTR, counter = ctr)
        #return unpad(cipher.decrypt(enc[16:]))
        return cipher.decrypt(enc)

def main():

    if sys.argv[1]=="-h" or sys.argv[1]=="--help":
        print("welcome")
        usage()
        return
    elif len(sys.argv) != 7:
        print("please input 7 arguments")
        usage()
        return

    if sys.argv[1]=="enc" or sys.argv[1]=="ENC" or sys.argv[1]=="encrypt":
        key_f = open(sys.argv[3], 'rb')
        key = key_f.read()
        key_f.close()
        iv_f = open(sys.argv[4], 'rb')
        iv = iv_f.read()
        iv_f.close()
        input_f = open(sys.argv[5], 'r')
        data = input_f.read()
        input_f.close()

        if sys.argv[2]=="CBC" or sys.argv[2]=="cbc":
            encrypted_data = AESCipher(bytes(key),bytes(iv)).encrypt_CBC(data)
        elif sys.argv[2]=="CTR" or sys.argv[2]=="ctr":
            encrypted_data = AESCipher(bytes(key),bytes(iv)).encrypt_CTR(data)
        else:
            usage()
            print(sys.argv[2])
            return
        
        output_f = open(sys.argv[6], 'wb+')
        output_f.write(encrypted_data)
        output_f.close()
    elif sys.argv[1]=="dec" or sys.argv[1]=="DEC" or sys.argv[1]=="decrypt":
        key_f = open(sys.argv[3], 'rb')
        key = key_f.read()
        key_f.close()
        iv_f = open(sys.argv[4], 'rb')
        iv = iv_f.read()
        iv_f.close()
        input_f = open(sys.argv[5], 'rb')
        data = input_f.read()
        input_f.close()

        if sys.argv[2]=="CBC" or sys.argv[2]=="cbc":
            decrypted_data = AESCipher(bytes(key),bytes(iv)).decrypt_CBC(data)
        elif sys.argv[2]=="CTR" or sys.argv[2]=="ctr":
            decrypted_data = AESCipher(bytes(key),bytes(iv)).decrypt_CTR(data)
        else:
            usage()
            print(sys.argv[2])
            return
 
        output_f = open(sys.argv[6], 'w+')
        output_f.write(str(decrypted_data.decode('utf-8')))
        output_f.close()
    else:
        usage()
        print(sys.argv[1])
        return

if __name__ == "__main__":
    main()

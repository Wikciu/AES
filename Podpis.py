from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

with open("private_key.der", "rb") as f:
    private_key = RSA.import_key(f.read())

with open("C:\\Users\\wikto\\OneDrive\\Desktop\\Test_AES.txt", "rb") as f:
    data = f.read()

hash = SHA256.new(data)
signature = pss.new(private_key).sign(hash)


with open("signature.sig", "wb") as f:
    f.write(signature)




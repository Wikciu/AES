from Crypto.PublicKey import RSA

key = RSA.generate(2048)

with open("private_key.der", "wb") as f:
    f.write(key.export_key())





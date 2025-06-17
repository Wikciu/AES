from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256

with open("C:\\Users\\wikto\\OneDrive\\Desktop\\Test_AES.txt", "rb") as f:
    data = f.read()

aes_key = get_random_bytes(16)
hmac_key = get_random_bytes(16)


cipher = AES.new(aes_key, AES.MODE_CTR)
ciphertext = cipher.encrypt(data)

hmac = HMAC.new(hmac_key, digestmod=SHA256)
tag = hmac.update(cipher.nonce + ciphertext).digest()


with open("C:\\Users\\wikto\\OneDrive\\Desktop\\Output.txt", "wb") as f:
    f.write(tag)
    f.write(cipher.nonce)
    f.write(ciphertext)

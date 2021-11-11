# OAEP for enc
#PSS for digital signature
from Crypto.PublicKey.RSA import generate

def generate_RSA(bits=1024):
    #generate in pem format
    print(generate(bits))
print(generate_RSA())

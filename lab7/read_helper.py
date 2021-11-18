import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

pubkey = open('mykey.pem.pub','r')
rsakey = RSA.importKey(pubkey.read())
rsa_d = rsakey.e
n = rsakey.n
#print(n,"\n")

#private key
priv_key = open('mykey.pem.priv','r')
rsa_priv = RSA.importKey(priv_key.read())
rsa_e = rsa_priv.d
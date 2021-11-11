from Crypto.Hash import SHA256, hashalgo

from ex2 import enc,dec,int_to_bytes
from read_helper import n, rsa_d,rsa_e
from sq_mult import square_multiply

#step 1

#prime number 1
int_to_enc = 100
y = enc(int_to_enc,rsa_d,n)

#step 2
s = 2

#prime number 2
ys =  enc(s,rsa_d,n)
m = y * ys

decrypted_rsa = dec(m,rsa_e,n)

print("Part II-------------\n")
print(f"Encrypting:  {int_to_enc}")

print("Result:\n")
print(m)

print(f"Decrypted:    {decrypted_rsa}")
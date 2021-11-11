import random

from read_helper import rsa_d, n
from sq_mult import square_multiply
from ex2 import enc

#alice
s = random.getrandbits(1024)
message = square_multiply(s,rsa_d,n)

#attack
attack = (message,s)

#bob
x_prime = enc(s,rsa_d,n)

# check
print(f"Does x == x_prime? {x_prime == message}")
if (x_prime == message):
    print(f"Bob has accepted {attack}")
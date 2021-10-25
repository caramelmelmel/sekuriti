# 50.042 FCS Lab 6 template
# Year 2021

#from lab6.primes import square_multiply
from primes import (square_multiply,gen_prime_nbits)
import random
import present_with_ecb
import os


def dhke_setup(nb):
    p = gen_prime_nbits(nb)
    alpha = random.randint(2,p-2)
    return p, alpha 


def gen_priv_key(p):
    private_alice = random.randint(2,p-2)
    #private_bob = random.randint(2,p-2)
    return private_alice


def get_pub_key(alpha, a, p):
    pub_key = square_multiply(alpha,a,p)
    #pub_key = (alpha ** a) % p 
    return pub_key


def get_shared_key(keypub, keypriv, p):
    shared_key = square_multiply(keypub,keypriv,p)
    return shared_key
    #return (keypub ** keypriv)%p


if __name__ == "__main__":
    p, alpha = dhke_setup(80)
    print("Generate P and alpha:")
    print("P:", p)
    print("alpha:", alpha)
    print()
    a = gen_priv_key(p)
    b = gen_priv_key(p)
    print("My private key is: ", a)
    print("Test other private key is: ", b)
    print()
    A = get_pub_key(alpha, a, p)
    B = get_pub_key(alpha, b, p)
    print("My public key is: ", A)
    print("Test other public key is: ", B)
    print()
    sharedKeyA = get_shared_key(B, a, p)
    sharedKeyB = get_shared_key(A, b, p)
    print("My shared key is: ", sharedKeyA)
    print("Test other shared key is: ", sharedKeyB)
    print("Length of key is %d bits." % sharedKeyA.bit_length())
    #extend the file
    #pass shared key into shared_key_p2.txt
    if os.path.exists('shared_key_p2.txt'):
        os.remove('shared_key_p2.txt')
        os.remove('complain_enc.txt')
        os.remove('complain_dec.txt')
    #convert to hex
    key_file = open('shared_key_p2.txt',mode='w')
    key_file.write(hex(sharedKeyA).lstrip('0x'))
    key_file.close()
    key_file = open('shared_key_p2.txt', 'r')
    keyfile_content = key_file.read()
    keyfile_content = keyfile_content.rstrip()
    present_with_ecb.ecb('complain.txt','complain_enc.txt',int(keyfile_content,16),'E')
    #open the enc file
    encrypted = open('complain_enc.txt','rb')
    #print(f"the encrypted text is {encrypted.readlines()}")
    present_with_ecb.ecb('complain_enc.txt','complain_dec.txt',int(keyfile_content,16),'D')
    decrypted_file = open('complain_dec.txt','r')
    plaintext = open('complain.txt','r')
    print(f'The plaintext is : {plaintext.read()}')
    print(f'The encrypted text is {encrypted.read()}')
    print(f'The decrypted text is : {decrypted_file.read()}')
    encrypted.close()
    decrypted_file.close()
    key_file.close()

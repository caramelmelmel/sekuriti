from Crypto.Hash import SHA256

from sq_mult import square_multiply
from read_helper import rsa_e, rsa_d, n


def enc(msg,priv,mod_p):
    return square_multiply(msg,priv,mod_p)

def dec(cipher,pub,mod_p):
    return square_multiply(cipher,pub,mod_p)

# convert from int to hash
def int_to_bytes(integer):
     return integer.to_bytes((integer.bit_length()+7)//8,'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes,'big')

def string_to_bytes(string):
    return bytes(string,'utf-8')

# plaintext
plaintext = open('196673.txt','r')
hash_algo = SHA256.new()
hashed_txt = hash_algo.update(plaintext.read().encode())
message_digest = hash_algo.hexdigest()

# check if x' == hashed plain
message_digest_int = int_from_bytes(string_to_bytes(message_digest))
encrypted_digest = enc(message_digest_int,rsa_e,n)
dec_digest = dec(encrypted_digest,rsa_d,n)

#convert int to the hash
hashed_res = int_to_bytes(dec_digest).decode()

print("plain:")
print(message_digest,'\n')
print("decrypted:")
print(hashed_res,'\n')

if (message_digest == hashed_res):
    print('The decrypted and the original matches!')
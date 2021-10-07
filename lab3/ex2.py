import time
import os
import hashlib
import itertools

start_time = time.time()

hash_file = open("hash5.txt","r")

if os.path.exists("ex2_hash.txt"):
    os.remove("ex2_hash.txt")

file_output = open("ex2_hash.txt","w")

#generate permutations according to given hint
possible_characters = list("abcdefghijklmnopqrstuvwxyz0123456789")

def possible_answers(given_combi):
    string_possibilities = []
    for item in itertools.product(given_combi, repeat=5):
        string_possibilities.append("".join(item))
    return string_possibilities


read_hash = hash_file.readlines()

plaintext_possibilities = []
resultant_hashed_plaintext = {}
final_words = ""

plaintext_possibilities = possible_answers(possible_characters)

#loop through hash and store in dictionary
for plaintext in plaintext_possibilities:
    result = hashlib.md5(plaintext.encode())
    result = result.hexdigest()
    resultant_hashed_plaintext[result] = plaintext
#read each line
print("generated all the plaintext")

for line in read_hash:
    #determine if needa use md5
    #MD5 has a fixed length of 32 word string
    line = line.strip("\n")

    if len(line) == 32:
        print("We need to break the MD5 hash")
    
    final_words += resultant_hashed_plaintext[line] + "\n"

file_output.write(final_words)

#close those file pointers pick them up!!!!
file_output.close()
hash_file.close()    

print(f"The execution time is {time.time()-start_time}")
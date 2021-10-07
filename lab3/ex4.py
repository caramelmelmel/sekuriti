import os
import hashlib
import random
import string

if os.path.exists("salted6.txt"):
    os.remove("salted6.txt")

if os.path.exists("plain6.txt"):
    os.remove("plain6.txt")

#generate possible ans


def random_alphabet_gen():
    return str(random.choices(string.ascii_lowercase,k=1)[0])


#hash function
def hash_with_md5(input_string):
    result = hashlib.md5(input_string.encode())
    result = result.hexdigest()
    return result

#open all file pointers
hash_load = open("ex2_hash.txt","r") 
write_to = open("plain6.txt","w")
write_hash_to = open("salted6.txt","w")

#do all the readline
write_to_file_string = ""
write_hash = ""

for line in hash_load.readlines():
    line = line.strip("\n")
    line = line + random_alphabet_gen()
    write_to_file_string += line + "\n"
    write_hash += hash_with_md5(line) + "\n"

write_to.write(write_to_file_string)
write_hash_to.write(write_hash)

print("writing has finished")
write_to.close()
write_hash_to.close()




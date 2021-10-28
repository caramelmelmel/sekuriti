# 50.042 FCS Lab 6 template
# Year 2021
#code adapted: https://medium.com/asecuritysite-when-bob-met-alice/baby-step-giant-step-solving-discrete-logarithms-and-why-its-a-hard-problem-to-solve-62b11bbe3088

import math
import os
import primes

#calculate m 
#p is the order of the cyclic group G
def calculate_m(p):
    return int(math.ceil(math.sqrt(p-1)))

#alpha is the generator 
# beta is the element
#ouput of the babystep_giantstep is that of x satisfying alpha ^x = beta
#fname is the filename
def baby_step(alpha, beta, p, fname):
    file_babystep = open(fname,mode='w')
    #compute to a hash table
    m =  calculate_m(p)
    store_values = {}
    for j in range(0,m):
        store_values[j] = (beta * (alpha ** j))%p
    file_babystep.write(str(store_values))
    file_babystep.close()
    return store_values


def giant_step(alpha, p, fname):
    file_giant_step = open(fname,mode='w')
    m = calculate_m(p)
    stored_value = {}
    for x_g in range(0,m):
        stored_value[x_g] = primes.square_multiply(alpha,m * x_g,p)
    file_giant_step.write(str(stored_value))
    file_giant_step.close()
    return stored_value


def baby_giant(alpha, beta, p):
    m = calculate_m(p)
    #baby step
    if os.path.exists('baby_step.txt'):
        os.remove('baby_step.txt')
        os.remove('giant_step.txt')

    baby_step_dict = baby_step(alpha,beta,p,'baby_step.txt')
    giant_step_dict = giant_step(alpha,p,'giant_step.txt')

    #convert both to dict
    for key in baby_step_dict.keys():
        if baby_step_dict[key] in giant_step_dict.values():
            giant_key = list(giant_step_dict.keys())[list(giant_step_dict.values()).index(baby_step_dict[key])]
            return (giant_key * m)- key 



if __name__ == "__main__":
    """
    test 1
    My private key is:  264
    Test other private key is:  7265
    """
    p = 17851
    alpha = 17511
    A = 2945
    B = 11844
    sharedkey = 1671
    a = baby_giant(alpha, A, p)
    b = baby_giant(alpha, B, p)
    guesskey1 = primes.square_multiply(A, b, p)
    guesskey2 = primes.square_multiply(B, a, p)
    print("Guess key 1:", guesskey1)
    print("Guess key 2:", guesskey2)
    print("Actual shared key :", sharedkey)

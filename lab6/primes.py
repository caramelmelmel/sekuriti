# 50.042 FCS Lab 6 template
# Year 2021

import random
def square_multiply(a,x,n):
    y = 1

    #number of bits in x
    #num_bits = x.bit_length()

    #convert the integer x into a lit of bits
    x_in_bits = list("{0:b}".format(x))

    for i in x_in_bits:
        y = (y ** 2) % n 
        if i == '1':
            y = y* a %n
    return y 


def single_test(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
        
    if square_multiply(a, exp, n) == 1:
        return True
        
    while exp < n - 1:
        if square_multiply(a, exp, n) == n - 1:
            return True
            
        exp <<= 1
        
    return False
    
def miller_rabin(n, k):
    for i in range(k):
        a = random.randrange(2, n - 1)
        if not single_test(n, a):
            return False
            
    return True

def gen_prime_nbits(n):
    pass

if __name__=="__main__":
    #print(square_multiply(16,12,1))
    print('Is 561 a prime?')
    print(miller_rabin(561,2))
    print('Is 27 a prime?')
    print(miller_rabin(27,2))
    print('Is 61 a prime?')
    print(miller_rabin(61,2))

    print('Random number (100 bits):')
    print(gen_prime_nbits(100))
    print('Random number (80 bits):')
    print(gen_prime_nbits(80))

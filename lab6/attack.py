import dhke
import babygiant
import primes
import time
#from lab6.dhke import gen_priv_key, get_pub_key
#from lab6.dhke import dhke_setup

for i in range(16,9000000):

    #get the inputs to the baby step giant step
    start_timer = time.time()
    p,alpha = dhke.dhke_setup(i)
    priv_key = dhke.gen_priv_key(p)
    beta = dhke.get_pub_key(alpha,priv_key,p)

    #algo
    x = babygiant.baby_giant(alpha,beta,p)
    guess_shared = primes.square_multiply(beta,x,p)
    end_time = time.time()
    real_shared = dhke.get_shared_key(beta,priv_key,p)
    print(f"The key size is {i}")
    print(f"The guess of the shared key is {guess_shared}")
    print(f"The real shared key is {real_shared}")
    print(f"Time taken is {end_time-start_timer}")







def SieveOfAtkin(limit):
    #for 2 and 3
    if (limit > 2): 
        print(2 , end = " ") 
    if (limit > 3): 
        print(3 , end = " ")
    #intialize sieve
    sieve = [False] * limit 
    for i in range( 0 , limit ): 
        sieve[i] = False # here we are intializing each number as non-prime.
    #for step 3
    x = 1
    while(x * x < limit ) : 
        y = 1
        while(y * y < limit ) : 
        #main part
            n = (4 * x * x) + (y * y) 
            if (n <= limit and (n % 12 == 1 or 
                            n % 12 == 5)):
                sieve[n] ^= True # changing status to prime.
            n = (3 * x * x) + (y * y) 
            if (n <= limit and n % 12 == 7): 
                sieve[n] ^= True # changing status to prime.
            n = (3 * x * x) - (y * y) 
            if (x > y and n <= limit and 
                        n % 12 == 11): 
                sieve[n] ^= True # changing status to prime.
            y += 1
        x += 1
        #mark all multiples of square as non-prime
        r = 5
        while(r * r < limit) : 
            if (sieve[r]) : 
                for i in range(r * r, limit, r * r): 
                    sieve[i] = False # here we are changing status to non-prime and ignoring it.
        # Print primes 
    for a in range(5 , limit ): 
        if (sieve[a]): 
            print(a , end = " ") 

limit = 20
SieveOfAtkin(limit) 
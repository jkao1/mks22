def fred(q):
    return q**2 - 3

def sumFredWhile(n):
    summ = 0
    n -= 1
    while n >= 0:
        summ += fred(n)
        n -= 1
    return(summ)
sumFredWhile(3)

def sumFredFor(n):
    summ = 0
    for i in range(n):
        summ += fred(i)
    return(summ)
sumFredFor(3)

def sumFredBetween(low,high):
    print(sumFredWhile(high) - sumFredWhile(low))
sumFredBetween(0,3)

def sumFredBetween2(a,b):
    print(abs(sumFredWhile(high) - sumFredFor(low)))
sumFredBetween(0,3)

def factorPairs(n):
    for i in range(1,int(n/2 + 1)):
        if n % i == 0:
            print(i)
factorPairs(36)

import math

def is_prime(x):
    hi = 0
    if x<2:  
        hi = False  
    elif x == 2:  
        hi = True  
    else:  
        for n in range(2, x):  
            if x%n==0:  
                hi = False  
    print(hi)
is_prime(23)
is_prime(50)

def largestPrimeFactor(n):
    prime_factors = []
    for i in range(1,int(n**(1/2) + 1)):
        if n % i == 0 and isPrime(i):
            factors.append(i)

    print(max(prime_factors))
    

is_prime(98767)
is_prime(987127)
is_prime(135797533)
is_prime(2345678911)
is_prime(12345677654381)



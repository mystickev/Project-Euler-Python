# -*- coding: utf-8 -*-
"""
Project Euler #10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million
"""
"""
import math
import numpy

def prime6(upto):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2:(upto-1)/2:factor]=0
    return numpy.insert(primes[isprime],0,2)
    
upto = input("Enter a number: ")
print("List of primes <"),upto
print sum(prime6(upto))
"""
import itertools as it
def erat2a( ):
    D = {  }
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D:
                x += 2*p
            D[x] = p
            
primes = erat2a()
for i in range(1,100):
    print primes
# -*- coding: utf-8 -*-
"""
Circular primes Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from Prime import prime_sieve
from Prime import is_prime
from math import factorial, sqrt
import time

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True

def cycles_of(s):
    list_of_cycles = []
    s = str(s)
    n = str(s)
    """
    shifts the sequence to the left to cycle them
    """
    for i in range(0,len(n)):
        n = n[1:] + n[0]
        if is_prime(int(n)):
            list_of_cycles.append(n)
        else: return False
    if len(list_of_cycles) == len(str(s)):
        return list_of_cycles
    else: return False

start = time.time()
count = 0
for prime in prime_sieve(1000000):
    if cycles_of(prime):
        print prime, cycles_of(prime)
        count += 1
print "Done! With", count, "found in", time.time() - start, "seconds"
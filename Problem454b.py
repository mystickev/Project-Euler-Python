# -*- coding: utf-8 -*-

"""
Diophantine reciprocals III
Problem 454

Observations: there are no primes possible for y
x < y <= L so values of x run up to y and are limited to divisors of x

"""
from fractions import gcd
from math import floor
from Prime import primefactor
from Prime import is_prime
from itertools import combinations
import time
import math

# --- generator pair that tests values and return only those in the sequence ------------
def divisorGen(n):
    factors = list(primefactor(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def isA005279(num):
    divs = [x for x in divisorGen(num)]
    for d in range(1, len(divs)-1):
        for e in range(d+1, len(divs)):
            if divs[e] < 2*divs[d]:
                return True

def A005279(): # generator function
    num = 5
    while True:
        if isA005279(num):
            yield num
        num += 1

# -----------------------------------------------------------------------------------------
starttime = time.time()
sequence = A005279()
for n in range(6, 37):
    print n, sequence.next()
print "Done! In", time.time() - starttime, "seconds"



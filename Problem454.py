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
from Prime import primefactor
import math
from math import sqrt, floor, ceil
import time

def divisors(tuple):
    count = 1
    for si in tuple:
        count *= (si[1] + 1)
    return count

def print_factors(tuple, num):
    list_of_factors = []
    for pi_si in tuple:
        multiplier = 1
        while pi_si[0] * multiplier <= num:
            # somehow remove even/even combinations? Odd/odd, etc.
            list_of_factors.append(pi_si[0] * multiplier)

            multiplier += 1
    return list(set(list_of_factors))




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
    for d in xrange(1, len(divs)-1):
        for e in xrange(d+1, len(divs)):
            if divs[e] < 2*divs[d]:
                return True

def A005279(): # generator function
    num = 5
    while True:
        if isA005279(num):
            yield num
        num += 1

def count_divisors(list, num):
    result = []
    for integer in list:
        if integer < num:
            if num*integer % (num + integer) == 0:
                result.append(integer)
    return len(result)
# -----------------------------------------------------------------------------------------
starttime = time.time()
sequence = A005279()
y = sequence.next()

print "-----------------------------------"
sumtotal = 0
while y < 100002:
    numsq = y**2
    lower_limit = int(floor(math.sqrt(y)))
    count = 0
    for n in xrange(lower_limit, y/2):
        if numsq % (y - n) == 0:
            count += 1
            sumtotal += 1
    y = sequence.next()
print "Finished with", sumtotal, "in", time.time() - starttime, "seconds"

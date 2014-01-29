#Euler 108

#KeyZero Conversation approach
"""
#1/x + 1/y = 1/n
#using algebra, we solve for y in terms of x and n
# y = nx/(x-n)
# let d = (x-n)
# y = nx/d
# x = d+n
# y = n(d+n) / d
# y = (nd + n^2)/d
# y = n + n^2/d
# so for y to be integer, we need to find divisors d of n^2
# then backsubstitute
# x, y (with the constraints that n < x <= 2n)

# number of solutions for n is (divisors(n^2)+1)/2

# number of divisors of an integer are product of powers of prime factor + 1.
# i.e. 24 is 2^3 * 3^1. The powers are 3 and 1.  The product of (3+1) and (1+1)
# is 8, so there are eight divisors.

# reduce the search space.  We want to find any value n where n^2 has at least
# 2000 divisors.

# assume that it is made up of squares of small prime numbers
# 2^2 * 3^2 * 5^2 *7^2 *11^2 * 13^2  (this is six different factors all raised to the
# power of 2).  Also, this is (2*3*5*7*11*13)^2, or 30030^2.
# So number of divisors is (2+1)^6, or 729.  This is too low, but we can start here

# If we go to 7 different factors, we get to
# (2*3*5*7*11*13*17)^2, or 510510^2.
# Number of divisors is (2+1)^7, or 2187.  This is greater than 2000, so this could be it.
"""

import math
import operator
import time
t0 = time.time()

#generate sieve

import math

def sieve(n):
    initSieve = []
    maxNum = int(math.sqrt(n))+1
    for i in range(2,n):
        initSieve.append(True)
    j = 2
    while j <= maxNum:
        if initSieve[j-2]:
            for k in range(j*j, n, j):
                initSieve[k-2] = False
        j += 1
    outputList = [x+2 for x in range(len(initSieve)) if initSieve[x]]
    return outputList

topSieve = 50
primes = sieve(topSieve)  #prime factors less than

print primes
lenP = len(primes)   #length of primes
print lenP

def divisors(n, primes):   # factorizes a number using small primes
    tempN = n
    t = [0 for x in range(len(primes))]
    idx = 0
    while idx < len(t):
        while tempN > 1 and tempN % primes[idx] == 0:
            t[idx] += 1
            tempN /= primes[idx]
        if tempN == 1:
            return True, t, tempN
        idx += 1
    return False, t, tempN

# our divisors function takes a number n,
# sees if we can factorize it using prime numbers within our sieve
# so within our search space - we will take a number n, try to factorize it,
# only using these prime factors.
# if the number can be factorized using these prime factors, then we get a True


def sumDiv(takesList):   # takes our factorization list, returns number of divisors
    c = 1
    for i in takesList:
        if i > 0:
            c *= (i+1)
    return c

# this is the product of the first 6 primes
start = 2 * 3 * 5 * 7 * 11 * 13
# another way to get this is
s2 = reduce(operator.mul, [primes[x] for x in range(6)])

incr = s2

testNum = start

def isSquare(possibleAnswer):  #takes as input list of exponents
    f = [int(math.pow(primes[i], possibleAnswer[i])) for i in range(lenP)]
    test = reduce(operator.mul, f)
    r = int(math.sqrt(test))
    if r*r == test:
        return True, test, r
    else:
        return False, test, r

while True:
    a, b, c = divisors(testNum, primes)
    if a:   #this should always be true, since we're incrementing by s2
        d = sumDiv(b)
        if d > 2000:
            e, f, g = isSquare(b)
            if e:
                print a, b, c
                print f, g
                print "the answer n is", g
                break
    testNum += incr

t1 = time.time()
print t1 - t0, "seconds"

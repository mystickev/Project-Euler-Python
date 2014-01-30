# -*- coding: utf-8 -*-
"""
Project Euler #10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million
"""


#
# This solution uses an optimized version of the "Sieve of Eratosthenes"
# to find all prime numbers below a certain input value.  The found primes
# are then summed to give the solution.
#

import itertools as it
import time

#
# uses a generator function called erat2a()
#

def erat2a():
    #
    # This is a generator function, holds state in memory and
    # returns the next value when the erat2a.next() method is called
    #
    D = {}

    yield 2 # this is the yield at first run

    for q in it.islice(it.count(3), 0, None, 2):

        p = D.pop(q, None)

        if p is None:

            D[q*q] = q

            yield q # return the next prime

        else:

            x = q + 2*p

            while x in D:

                x += 2*p

            D[x] = p

#
# set variables
#

starttime = time.time()
sum = 0

primes = erat2a() # fire up the generator function and assign to variable primes

#
# The while loop will run, generating primes, and summing them, until the next
# prime is > 2,000,000.  At that point the while loop terminates.

while primes.next() < 2000000:

    sum += primes.next()

#
# Return the answer and the timing
# The answer is 71458417057
# Found in 1.50534510612 seconds
#

print "The answer is", sum
print "Found in", time.time() - starttime, "seconds"
"""
Project Euler Problem 454
"""
# grab functions from my Project Euler 454 library module
from E454tools import factorize, divisors_from_factors, A005279
import time
import math
from math import sqrt, floor
from fractions import gcd


# set initial conditions, including count of solutions, y and y**2
# y is the only required input

count = 0
sequence = A005279()
y = sequence.next()
starttime = time.time()

count = 0

while y < 1001:
    y_sq = y**2  # square the value for y

    # next we're going to get a list of divisors of y**2 from its prime factorization

    # first we factorize y_sq using divisors from factors function
    # next, we produce a list of divisors using divisors from factors function
    # finally, we assign the result to list_of_divisors_of_y_sq variable

    divisor_a = divisors_from_factors(factorize(y_sq))
    divisor_b = divisor_a

    for a in divisor_a:
        for b in divisor_b:
            if gcd(a, b) == 1:
                count += 1

    y = sequence.next()

print "Found", count, "solutions in", time.time() - starttime, "seconds"
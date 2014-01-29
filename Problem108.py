# -*- coding: utf-8 -*-
"""
Diophantine reciprocals I Problem 108
In the following equation x, y, and n are positive integers.

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

d(m) = products of pi ^ si from i = 1 to r
number of divisors comes from the exponents of the prime factorization

Answer is n = 180180 [2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 7, 7, 11, 11, 13, 13]
result 32464832400 has >2,000 divisors
"""

from Euler_Utils import factor
import time
"""
Minimize search space: we’re looking for a highly composite solution for n^2 somewhere between
2^2 * 3^2 * 5^2 * 7^2 * 11^2 * 13^2 = 30030 (So number of divisors is (2+1)^6, or 729)
and 2^2 * 3^2 * 5^2 * 7^2 * 11^2 * 13^2 * 17^2 = 510510^2 (Number of divisors is (2+1)^7, or 2187)
"""
start = time.time()

for input_val in xrange(30030, 510510, 2):
    num_factors = 1
    # the number of divisors is going to be high when the number is a product /
    # of a large number of small primes (highly composite number)
    factors_of_input_val = factor(input_val)
    for tuple in factors_of_input_val:
        num_factors *= (2*tuple[-1] + 1) #grab the exponent of si
    if num_factors > 1999:
        print "n of", input_val, "has", num_factors, "divisors"  # non-distinct divisors (repeats)
        break
print "Done! In", time.time() - start, "seconds"
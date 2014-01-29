# -*- coding: utf-8 -*-
"""
Diophantine reciprocals II Problem 110

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for
which the total number of distinct solutions exceeds one hundred. What is the least value of n for which the
number of distinct solutions exceeds four million? NOTE: This problem is a much more difficult version of problem 108
and as it is well beyond the limitations of a brute force approach it requires a clever implementation.

Function d(n) returns a count of divisors, and the math is d(n) = (s1 + 1)*(s2 + 1)* ... *(sn + 1)
where p1 ... pn is the prime factorization and s1 ... sn are the coefficients. If n^2 then
D(n^2) = (2*s1 + 1)*(2*s2 + 1)* ... *(2*sn + 1)

If all sn's are the same, reduces to
(sn + 1)^m which for sn = 2 and m = 4 (2^2*3^2*5^2*7^2 = 44,100)
(2+1)^4 = 81 works!

So where is (2 + 1)^m > 8,000,000? Note: unknown number of terms (but prime terms are known)
log10((2+1)^m)) = log10(8,000,000)
m log10 (3) = log10(8,000,000)
m = 14.46820890645068 times (at si = 2 14 is too few, 15 prime terms is too many)

Answer:
n = 9350130049860600
exponents = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

"""

def return_factors(factors_of_input_val):
    num_factors = 1
    for tuple in factors_of_input_val:
        num_factors *= (2*tuple[-1] + 1) # iterate over the tuple & grab the exponent of si
        # the math is d(n) = (s1 + 1)*(s2 + 1)* ... *(sn + 1) where d(n) returns the count of divisors
        # D(n^2) + 1 = (2s1 + 1)*(2s2 + 1)* ... *(2sn + 1)
    return num_factors/2 - 1 # divide by 2 and subtract 1 to get number of unique solutions


def prime_product(factors_of_input_val):
    prime_product = 1
    for tuple in factors_of_input_val:
        prime_product *= (tuple[0]**tuple[1]) # iterate over the tuple & return prime product
    return prime_product

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
exponents = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

prime_tuples = zip(primes, exponents)

print "Answer n =", prime_product(prime_tuples), "has", return_factors(prime_tuples), "unique factors"


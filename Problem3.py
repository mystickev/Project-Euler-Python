# -*- coding: utf-8 -*-
"""
Project Euler Problem #3
Created on Fri Dec 13 16:42:30 2013 @author: pante_000

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
# My naive prime factorization algorithm in function factor(int)
# utilizes Sieve of Eratosthenes
def factor(x):

    factors = []

    i = 2

    while x > 1:

        if x % i == 0:

            x = x / i

            factors.append(i)

        else:

            i += 1

    return factors

num = input("Input an integer: ")

print factor(num)

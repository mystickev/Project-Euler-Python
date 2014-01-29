# -*- coding: utf-8 -*-
"""
Project Euler #3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
# prime factorization algorithm
def factor(x):
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else: 
            if i+1 % 2 == 0:
                i += 2
            else:
                i += 1
    return factors

num = input("Input a number to factor: ")
print factor(num)

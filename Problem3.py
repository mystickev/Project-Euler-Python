# -*- coding: utf-8 -*-
"""
Project Euler Problem #3 - Created on Fri Dec 13 16:42:30 2013 @author: pante_000

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

#
# My naive prime factorization algorithm in function factor(int)
# tries all values from 2 to input value and checks for divisibility.
# By the fundamental Theorem of Arithmetic, all numbers have a
# prime factorization (can be decomposed into multiples of prime numbers).
# Let's start at the first prime factor and check for divisibility using the
# modulo operator. If the number is divisible by 2 (even), then let's divide
# by 2 and try again.  For example, 16 decomposes as [2, 2, 2, 2] = 2**4.
#
# When we have a remainder not evenly divisible by the divisor,
# increment up to the next divisor (2 > 3, etc).
#
# Even with a large number, this algorithm is very fast in Python.
#

import time

def factor(x):

    factors = [] # a variable (list) to hold the prime factors

    i = 2 # start from the first prime, 2

    while x > 1:
        #
        # check for divisibility (no remainder)
        # if divisible by i, add to the list and
        # divide through.
        #
        if x % i == 0:

            x = x / i

            factors.append(i)

        else:
            #
            # try the next value of i up to the input value
            #
            i += 1

    return factors

# let's define the variable num to hold the value 600851475143

num = 600851475143

#
# By the way the function was written, when we run it, it returns a list of prime factors.
# Since we only want the largest, let's find the result using slice syntax (e.g., [-1] returns
# the last element in a Python list.
#

starttime = time.time()

print "The largest prime factor of", num, "is", factor(num)[-1]  # [-1] is slice syntax for last item
print "Finished in", time.time() - starttime, "seconds"

# -*- coding: utf-8 -*-
"""
Project Euler 451
"""
from fractions import gcd
import fractions
import random
import math
from math import ceil
from math import sqrt
    
_mrpt_num_trials = 5 # number of bases to test

def prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
    return True # no base tested showed n as composite
    
def is_square(n):
  return sqrt(n).is_integer()
    
def fermatfactor(N):
  if N <= 0: 
    return N
  if N%2 == 0: # is N even?
    return (2, N/2) # return 2 and N/2 as factors
  a = ceil(sqrt(N)) # round up the square root of N (Fermat's method)
  while not is_square(a**2 - N): # there is a faster way to do this ... see pdf
    a = a + 1 # increment up and keep going until a square is found
  b = sqrt(a**2 - N) # at the final a value, pass the value to b
  return int(a - b), int(a + b) # complete the square 


def isodd(num):
    if num % 2 == 0:
        return 0
    else: 
        return 1
        
def phi(n):
    if n == 1: return 1
    return sum(d * mobius(n / d) for d in range(1, n+1) if n % d == 0)
    
def mobius(n):
    result, i = 1, 2
    while n >= i:
        if n % i == 0:
            n = n / i
            if n % i == 0:
                return 0
            result = -result
        i = i + 1
    return result

"""
print list
result = []
for i in range(2,100):
    result.append(i * 7 % 15)
print sorted(set(result))


"""
mod = 48
list = []
i = 1
if prime(mod):
    #totient = 1
    list.append(mod)
else:
    while i < mod:
        if pow(mod-i,2,mod) == 1:
            list.append(i)
            i += 1
        else:
            i += 1
print list

"""

Euler's Criterion a**((p-1)/2)=(a:p) mod p 
(here (a:p) is the Legendre symbol). 
a^(Phi(m) - 1) === a^-1 (a inverse) mod m


In number theory, an integer q is called a quadratic residue modulo n if it 
is congruent to a perfect square modulo n

 if p === 1 mod 4, then p|m2 + 1

 By Fermat’s little theorem, if 
 n < p then n^p−1 === 1 (mod p)
 14 < 15 then 14^(15-1) === 1 mod 15
 
 which means that its square root, n^((p−1)/2), is congruent to ±1 (mod p)
 14^(14/2) mod 15 === 14 (-1 mod p)

14**2 === 1 mod 15
11**2 === 1 mod 15

a^2 === (n-a)^2 mod n

http://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n

Groups and generators

Cyclic decomposition of Z/nZ

quadratic residues
http://en.wikipedia.org/wiki/Quadratic_residue

9218751**2 mod 10000000

Because a2 ≡ (n − a)2 (mod n)

Start at the top and work way down
Check to see if a number is prime = only 1 and number are coprime

353453 is prime, and 353452 is coprime (n-1) but is also n**2 % 353453 === 1

Is the square of some number, coprime to z, also coprime mod z?

For a given z, how many residues are coprime to z? Which of these residues
when squared, is congruent to 1 mod z?
    
"""
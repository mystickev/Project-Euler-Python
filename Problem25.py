# Project Euler #25
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

import math # to count digits

fibcache = {} # build a cache of Fibonacci numbers

# -------------- Fibonacci number generator
def fib(num):
    if num in fibcache:
        return fibcache[num]
    else:
       fibcache[num] = num if num < 2 else fib(num-1) + fib(num-2)
    return fibcache[num]

# initial conditions
n = 1 #seed value
digits = 0 # initialize counter

# the loop
while digits <= 999: # as soon as it gets to 1000 digits, kick out
    result = fib(n)
    digits = int(math.log10(result))+1 # count the digits
    n = n+1 # try the next seed value (1, 2, 3, 4 ... some big number)
    
# print the results    
print ("The answer is: "),result
print ("Place number: "),n-1
print ("Digits: "),digits


# Notes
# Fibonacci terms converge to (n)*Phi=(n+1), where Phi is the Golden Ratio (1+sqrt5)/2.
# Saying that a number contains 1000 digits is the same as saying that it's greater than 10**999
# 10**2 has 3 digits, 10**3 has 4 digits, 10**4 has 5 digits, etc...
# 10**999 has 1000 digits
# 10**1000 has 1,001 digits ... 
# The nth Fibonacci number is [phi**n / sqrt(5)], where the
# brackets denote "nearest integer". 
# So we need phi**n/sqrt(5) > 10**999
# n * log(phi) - log(5)/2 > 999 * log(10)
# n * log(phi) > 999 * log(10) + log(5)/2
# n > (999 * log(10) + log(5) / 2) / log(phi)

# A handheld calculator shows the right hand side to be
# 4781.8593, so 4782 is the first integer n with the desired property.

# -------
#another solution
#
# a,b,c = 0,1,1
# while True:
#	a,b,c=b,a+b,c+1
#	if b >= 10**999:
#		print c
#		break
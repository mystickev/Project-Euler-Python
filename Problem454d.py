#!/usr/local/bin/python2.7
import math
from math import sqrt, floor, ceil
import fractions
from fractions import gcd
import time

starttime = time.time()

L = 100000000
a, b= 1, 1
a_upper_bound = int(floor(math.sqrt(L)))
b_upper_bound = int(floor(math.sqrt(L)))+1
count = 0

for a in range(1, a_upper_bound):
    for b in range(a+1, b_upper_bound):

        if gcd(a, b) == 1:
            count += L/(b*(a+b))

print "Count is", count
print "Finished in", time.time() - starttime, "seconds"

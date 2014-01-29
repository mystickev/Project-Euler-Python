# -*- coding: utf-8 -*-
"""
Created on Sun Jan 05 11:46:23 2014

@author: pante_000
"""
sum = 0
num = 2**1000
print num
for i in str(num):
    sum += int(i)
print sum

print reduce(lambda x, y: x+y, str(2**1000))

"""
reduce() can be used to find Least common multiple for 3 or more numbers:
def lcmm(*args):
    return reduce(lcm, args)

>>> lcmm(100, 23, 98)
112700
>>> lcmm(*range(1, 20))
232792560
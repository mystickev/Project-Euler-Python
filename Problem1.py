# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:42:30 2013

@author: pante_000
"""

# Project Euler Problem #1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 
# and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
three = 3
five = 5
i = 1
j = 1
data = [] # a list
    
num = input("pick a number: ")

while three*i < num:
    data.append(three*i) # add multiples of 3 < num
    i+=1
while five*j < num:
    data.append(five*j) # add multiples of 5 < num
    j += 1
    
print list(set(data)) # a "set" is guaranteed to not have duplicates
print sum(list(set(data))) # sum up the set

# could have also used modulo solution //

#to_sum = [x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]
#result = 0
#for n in to_sum:
#    result += n
    
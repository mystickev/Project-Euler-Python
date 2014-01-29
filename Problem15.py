"""
problem 15 - Starting in the top left corner of a 2x2 grid, and 
only being able to move to the right and down, there are exactly 6 routes 
to the bottom right corner. How many such routes are there through a 
20x20 grid?

The value of the binomial expansion (m+n n) is given by the expression
(factorial(m+n)/(factorial(n)*factorial(m)))

Checking for 2x2 yields four choose two or (4,2) = 6
20x20 yields forty choose twenty or (40, 20) = 137846528820

"""
from math import factorial

def fact(n,k):
    result = (factorial(n+k))/(factorial(k)*factorial(n))
    return result

print fact(20,20) # m x n grid

"""
could also be given by factorial(40)/factorial(20)**2

40! / 20! ^ 2

"""
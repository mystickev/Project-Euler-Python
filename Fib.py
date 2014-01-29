# -------------------------------------------------------------------------
# The Fibonacci numbers are the integer sequence 0, 1, 1, 2, 3, 5, 8, 13, 21 ... 
# in which each item is formed by adding the previous two. 
# The sequence can be defined recursively by: 
# starting conditions 0 for n=0, 1 for n=1,then 
# F(n) = F(n-1)+F(n-2) for n>1

# -------------------------------------------------------------------------
def recur_fib1(n): # simple example using recursion
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return recur_fib1(n-1) + recur_fib1(n-2) # note this method is very SLOW (tree recursion)
  
# -------------------------------------------------------------------------      
# To calculate the nth Fibonacci number in only n steps
# we can also start with 0 and 1 and iteratively add up items n times 
  
def iter_fib(n): # example using iteration
    terms = [0,1] #seed value stored in a list
    i = 2
    while i <= n:
        terms.append(terms[i-1]+terms[i-2])
        i=i+1
        #print terms[-1] 
        #The some_list[-n] syntax gets the nth-to-last element. 
        #So some_list[-1] gets the last element, some_list[-2] gets the 
        #second to last, etc, all the way down to some_list[-len(some_list)], 
        #which gives you the first element.
    return terms[n]
    
# -------------------------------------------------------------------------
def next_fib(n): # example using iteration
    a = 0 # initial conditions
    b = 1
    for i in range(n):
        a, b = b, a + b 

    return a
    
    
# -------------------------------------------------------------------------
# Example with memoization - although the recursive implementation given above is elegant and 
# close to the mathematical definition it is not very practical. 
# Calculating fib(n) requires calculating two smaller Fibonacci numbers, 
# which in turn require two additional recursive calls each, and so on until all branches reach 1. 
# As a consequence, the time required to calculate fib(n) is exponential in n 
# (it is about Φn, where Φ is the golden ratio). To remedy this, we can employ memoization 
# to cache previous computations. The memoization cache is a dictionary consisting of entries 
# composed of a key n and a corresponding value fib(n). We initialize the dictionary 
# with the first two Fibonacci numbers (0,1).
# The memoized fib function recursively computes and stores the value of fib(n) 
# if it hasn't been previously stored in the memo dictionary. 
# Otherwise it simply returns the memoized value of fib(n). 

def fib_memo(n):
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]
    
# -------------------------------------------------------------------------
#Implementation of Binet's formula
#All sequences defined by linear recurrence have an associated closed-form expression for the nth number.
#Because of floating-point rounding errors, this will however only give the right result for n < 70. 
    
phi = (1 + 5**0.5) / 2

def Binet(n):
    return int(round((phi**n - (1-phi)**n) / 5**0.5))

#another Binet formula
from math import log
def fibinv(f):
    if f < 2:
        return f
    return int(round(log(f * 5**0.5) / log(phi)))
    
# -------------------------------------------------------------------------
#An example using matrices
def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]

# -------------------------------------------------------------------------
#Using Lucas numbers
def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

def fib_lucas(n):
    return powLF(n)[1]

# -------------------------------------------------------------------------
#main code 
n = input("Enter a number: ")

print fib_lucas(n)

#--- find the nth Fibonacci number---------------------------------------------------------------
def fibonacci(n):
    """
    Find the nth number in the Fibonacci series.
    Fast doubling Fibonacci algorithm
    """
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]

# Returns a tuple (F(n), F(n+1))
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
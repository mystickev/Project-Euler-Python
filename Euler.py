# -*- coding: utf-8 -*-
"""
A list of tools for solving Project Euler problems in Python

"""
import math
import numpy
import itertools
import random
from fractions import gcd

#--- Count number of divisors for a given number--------------------------------------
def count_divs(input_val):

    num_factors = 1

    # number of divisors comes from the exponents of the prime factorization /
    # the number of divisors is going to be high when the number is a product /
    # of a large number of small primes (e.g., a highly composite number)

    factors_of_input_val = primefactor(input_val) # grab the prime factors as a list of tuples

    for tuple in factors_of_input_val:
        num_factors *= (tuple[-1] + 1) # iterate over the tuple & grab the exponent of si
        # the math is d(n) = (s1 + 1)*(s2 + 1)* ... *(sn + 1) where d(n) returns the count of divisors

    return num_factors

#--- Factorial stuff------------------------------------------------------------------
# fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

def factorial(n):
    return reduce(lambda x, y:x*y, range(1,n+1), 1)

def sof_digits(n):
    # sum of factorial's digits
    s = 0
    while n > 0:
        s, n = s + fact[n % 10], n // 10
    return s

def sos_digits2(n):
    s = 0
    while n > 0:
        s, n = s + (n % 10)**2, n // 10
    return s

#--- Combinations, Permutations and Pandigitalism ------------------------------------
def is_perm(a,b):
    return sorted(str(a)) == sorted(str(b))

def perm(n, s):
    """
    requires function factorial()
    Find the nth permutation of the string s. Example:
    perm(30, 'abcde')
    bcade
    """
    if len(s)==1:
        return s
    q, r = divmod(n, factorial(len(s) - 1))
    return s[q] + perm(r, s[:q] + s[q + 1:])

def is_palindromic(n):
    return str(n)==str(n)[::-1]

def pal_list(k):
    # Create a list of all palindromic numbers with k digits
    if k == 1:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in range(1,10)
            for ys in itertools.product(range(10), repeat=k/2-1)
            for z in (range(10) if k%2 else (None,))]

def pandigital(n):
  #bitwise check for pandigitalism, works for any sequence
  count = 0
  num = 0
  digit = 0
  while n > 0:
    if n % 10 == 0:
      return False
    num = digit
    digit |= 1 << (n % 10 - 1)
    if num == digit:
      return False
    count += 1
    n /= 10
  if digit == (1 << count) - 1:
    return True
  else:
    return False


#--- greatest common divisor----------------------------------------------------------------------
def easy_gcd(a, b):
    # Computes the greatest common divisor of a and b. Examples:
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    while b != 0:
        (a, b) = (b, a%b)
    return a

def gcd(a,b):
    while a: # loop
            a, b = b%a, a # sets a = b mod a, and b = a
    return b # return GCD

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def xeuclid(a, b):
    """ return gcd(a,b), x and y in 'gcd(a,b) = ax + by'.
    """
    x = [1, 0]
    y = [0, 1]
    sign = 1

    while b:
        q, r = divmod(a, b)
        a, b = b, r
        x[1], x[0] = q*x[1] + x[0], x[1]
        y[1], y[0] = q*y[1] + y[0], y[1]
        sign = -sign

    x = sign * x[0]
    y = -sign * y[0]
    return a, x, y

#--- Euler's Totient or Phi function ----------------------------------------------------------------------

def euler_phi_function(phi):
    number_of_gcds_equal_to_1 = 0

    for positive_integers_less_than_phi in range(phi - 1,0,-1): # range(start,stop,decrement)
        the_gcd = gcd(phi,positive_integers_less_than_phi) # call gcd function
        if the_gcd == 1:
            number_of_gcds_equal_to_1 += 1

    return number_of_gcds_equal_to_1

def chinese_remainder(a, m):
    """
    return x in ' x = a mod m'
    requires xeuclid(a,b) to run
    """
    modulus = reduce(lambda a,b: a*b, m)

    multipliers = []
    for m_i in m:
        M = modulus / m_i
        gcd, inverse, y = xeuclid(M, m_i)
        multipliers.append(inverse * M % modulus)

    result = 0
    for multi, a_i in zip(multipliers, a):
        result = (result + multi * a_i) % modulus
    return result


#--- binomial coefficients-----------------------------------------------------------------------
def binomial(n, k):
    """
    Calculate C(n,k) or (n choose k) the number of ways can k be chosen from n. Example:

    >>>binomial(30,12)
    86493225
    """
    nt = 1
    for t in range(min(k, n-k)):
        nt = nt * (n-t) // (t+1)
    return nt


#--- catalan number------------------------------------------------------------------------------
def catalan_number(n):
    """
    Calculate the nth Catalan number. Example:

    >>> catalan_number(10)
    16796
    """
    nm = dm = 1
    for k in range(2, n+1):
        nm, dm = (nm*(n+k), dm*k)
    return nm / dm




#--- bezout coefficients--------------------------------------------------------------------------
def bezout(a,b):
    """
    Bézout coefficients (u,v) of (a,b) as:

        a*u + b*v = gcd(a,b)

    Result is the tuple: (u, v, gcd(a,b)). Examples:

    >>> bezout(7*3, 15*3)
    (-2, 1, 3)
    >>> bezout(24157817, 39088169)    #sequential Fibonacci numbers
    (-14930352, 9227465, 1)

    Algorithm source: Pierre L. Douillet
    http://www.douillet.info/~douillet/working_papers/bezout/node2.html
    """
    u,   v,  s,  t = 1, 0, 0, 1
    while b !=0:
        q, r = divmod(a,b)
        a, b = b, r
        u, s = s, u - q*s
        v, t = t, v - q*t

    return (u, v, a)



def legendre(a, p):
        if a == 0:
            return 0
        x, y, L = a, p, 1
        while 1:
            if x > (y >> 1):
                x = y - x
                if y & 3 == 3:
                    L = -L
            while x & 3 == 0:
                x = x >> 2
            if x & 1 == 0:
                x = x >> 1
                if y & 7 == 3 or y & 7 == 5: L = -L
            if x == 1:
                return L
            if x & 3 == 3 and y & 3 == 3: L = -L
            x, y = y % x, x

def is_square(n):
    root = math.sqrt(n)
    return root % 1 == 0  # '4.0' will pass, '4.1212' won't

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


from math import ceil, sqrt

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

#--- check n for prime--------------------------------------------------------------------------
def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

#--- generate prime numbers----------------------------------------------------------------------
def prime_sieve(n):
    """
    Function returns a list of prime numbers from 2 to a prime < n

    Example: prime_sieve(25) returns [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


#--- Miller-Rabin primality test----------------------------------------------------------------
def miller_rabin(n):
    """
    Check n for primalty:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:
    http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)
    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

#--- Prime factorization algorithms----------------------------------------------------------------------

def fetch_prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        """
        Easy to make it run in O(sqrt(n)) time, just stop the loop when d*d > n
        and if n > 1 at this point then its value should be appended to
        the list of prime factors.
        """
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors # returns a list of prime factors

# prime factorization algorithm
def naive_prime_factor(x):
    """ naive prime factorization algorithm"""

    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    return factors

#--- factor a number into primes and frequency----------------------------------------------------
def primefactor(n):
    """ find the prime factors of n along with their frequencies.

    primefactor(786456) will return a list of tuples [(2,3), (3,3), (11,1), (331,1)] whose corresponding
    prime factors pi and exponents si can be accessed by using slice notation.
    """
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = perform_trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1; n /= p
        F.append((p, e))
    F.sort()
    return F


def perform_trial_division(n, bound = None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n % p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m * m <= n:
        if n % m == 0:
            return m
        m += dif[i % 8]
        i += 1
    return n

def factors(n):
    gaps = [1,2,2,4,2,4,2,4,6,2,6]
    length, cycle = 11, 3
    f, fs, next = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[next]
        next += 1
        if next == length:
            next = cycle
    if n > 1: fs.append(n)
    return fs

def primes_upto(upto):
    # returns a list of primes up to the input value
    primes = numpy.arange(3,upto+1,2)
    isprime = numpy.ones((upto - 1) / 2, dtype = bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor - 2) / 2]: isprime[(factor * 3 - 2) / 2:(upto - 1) / 2 : factor] = 0
    return numpy.insert(primes[isprime], 0, 2)
    # will truncate output with ... and return only last 3 values if list is huge
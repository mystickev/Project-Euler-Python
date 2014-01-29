"""
Collection of tools for Project Euler 454

"""

from Prime import primefactor
import math
import time

def print_factors(tuple, num):
    list_of_factors = []
    for pi_si in tuple:
        multiplier = 1
        while pi_si[0] * multiplier <= num:
            # somehow remove even/even combinations? Odd/odd, etc.
            list_of_factors.append(pi_si[0] * multiplier)

            multiplier += 1
    return list(set(list_of_factors))




# --- generator pair that tests values and return only those in the sequence ------------
def divisorGen(n):
    factors = list(primefactor(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def isA005279(num):
    divs = [x for x in divisorGen(num)]
    for d in xrange(1, len(divs)-1):
        for e in xrange(d+1, len(divs)):
            if divs[e] < 2*divs[d]:
                return True

def A005279(): # generator function
    num = 5
    while True:
        if isA005279(num):
            yield num
        num += 1

def count_divisors(list, num):
    result = []
    for integer in list:
        if integer < num:
            if num*integer % (num + integer) == 0:
                result.append(integer)
    return len(result)

def factorize(n):
   if n < -1: return [[-1, 1]] + factorize(-n)
   elif n == -1: return [[-1, 1]]
   elif n == 0: return [[0, 1]]
   elif n == 1: return [[1, 1]]
   else:
      def factor_out(n, divisor):
         power = 0
         while (n % divisor) == 0:
            n //= divisor
            power += 1
         return (n, power)
      factors = []
      n, power = factor_out(n, 2)
      if power > 0:
         factors.append([2, power])
      divisor = 3
      while divisor * divisor <= n:
         n, power = factor_out(n, divisor)
         if power > 0:
            factors.append([divisor, power])
         divisor += 2
      if n > 1:
         factors.append([n, 1])
      return factors

def divisors_from_factors(factors):
   def unsorted_divisors_from_factors(factors):
      if not factors: return [1]
      else:
         base = factors[0][0]
         if base == -1: return unsorted_divisors_from_factors(factors[1:])
         elif base == 0: return []
         elif base == 1: return unsorted_divisors_from_factors(factors[1:])
         else:
            divs = unsorted_divisors_from_factors(factors[1:])
            alldivs = []
            for power in xrange(0, factors[0][1]+1):
               alldivs += map(lambda x: x * base ** power, divs)
            return alldivs
   alldivs = unsorted_divisors_from_factors(factors)
   alldivs.sort()
   return alldivs

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

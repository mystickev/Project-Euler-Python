# -*- coding: utf-8 -*-
"""
RSA decryption
"""
from math import sqrt, ceil
from fractions import gcd
N = long(N)
N = input("Enter N: ")
e = input("Enter e: ")

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
  
def euler_phi_function(phi):
  number_of_gcds_equal_to_1 = 0
  for positive_integers_less_than_phi in xrange(phi - 1,0,-1):
     the_gcd = gcd(phi,positive_integers_less_than_phi)
     if the_gcd == 1:
          number_of_gcds_equal_to_1 += 1
  return number_of_gcds_equal_to_1

fac1, fac2 = fermatfactor(N)
T = (fac1 - 1)*(fac2 - 1)
Tphi = T
Tphi = euler_phi_function(Tphi)
print "Tphi: ", Tphi
print "Tphi - 1: ", Tphi -1, "is the decryption key"
print "T: ", T
d = (e**(Tphi- 1))%T
print "d: ", d
print "-----------------"
print "To decrypt, we raise each block of four digits to the power", Tphi - 1, "mod", N
print "-----------------"
digits = input("Enter up to 4 digits: ")
answer = (digits**d)%N
print answer
"""
RSA encryption example
"""
from fractions import gcd 

def euclid(a, b): # Euclid's GCD algorithm
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

p = 11
q = 13
N = p*q # modulus
Tphi = (p - 1)*(q - 1) # Euler's totient phi function
# Let's find an e that is coprime to T
e = long(2) # PUBLIC encryption KEY
while e < Tphi:
    if gcd(e, Tphi) == 1: # coprime!
        break
    else:
        e = e + 1 # try the next one

def extended_euclid(a, b):
    if b == 0:
        return [a, 1, 0]
    else:
        previous_d, previous_x, previous_y = extended_euclid(b, a % b)
        d, x, y = (previous_d, previous_y, previous_x - a // b * previous_y)
        return [d, x, y]

dd, x, y = extended_euclid(Tphi, e) # satisfy Bezout's identity
if y > 0:
    d = y # take the positive portion
else:
    d = y % Tphi # or take the modulus of the other, which should be positive
    
print "-----------------" 
print "N = ", N
print "e = ", e
print "maximum message value is: ", N-2
print "-----------------"

text = 9
print "message: ", text
cypher = (text**e)%N

print "cyphertext: ", cypher
    # To decrypt the code, "81," we can use N and d as follows: 81^d = (81)^131 mod 323 = 123
print " ....."
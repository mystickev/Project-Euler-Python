"""
RSA encryption example
"""
from fractions import gcd 

def euclid(a, b): # Euclid's GCD algorithm
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

p = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541 
q = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233 
N = p*q # modulus
Tphi = (p - 1)*(q - 1) # Euler's totient phi function
# Let's find an e that is coprime to T
e = 65537 # PUBLIC encryption KEY

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
print "-----------------"

text = 1976620216402300889624482718775150 
print "message: ", text
cypher = (text**e)%N

print "cyphertext: ", cypher
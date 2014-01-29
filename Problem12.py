"""
Numbers such that d(n), the number of divisors of n, is greater than for 
any smaller n are called highly composite numbers. If n is a triangular 
number then it can be termed as Highly Composite Triangular Number . For 
example 28 is a triangular number and d(28) = 6 . Number of divisors 
of all triangular numbers less than 28 is less than 6. So 28 is a 
Highly Composite Triangular number.

If N=2^(a_2)3^(a_3)...p^(a_p) is the prime factorization of a highly composite number: 
1. The primes 2, 3, ..., p form a string of consecutive primes, 
2. The exponents are nonincreasing, so a_2>=a_3>=...>=a_p, and 
3. The final exponent a_p is always 1, except for the two cases N=4=2^2 
and N=36=2^2*3^2, where it is 2. 

"""
import collections

def prime_fac(n): #Returns all the prime factors of a positive integer
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def triangle_num(Tn): # generates triangle numbers
    Tn = Tn*(Tn+1)/2
    return Tn
       
def count_divs(Tn):
    prime = prime_fac(Tn)
    counter=collections.Counter(prime)
    # here's the magic bit d(n)=(v1+1)(v2+1)...(vk+1)
    sum = (counter[2]+1)*(counter[5]+1)*(counter[3]+1)*(counter[7]+1)*(counter[11]+1)*(counter[13]+1)*(counter[17]+1)*(counter[19]+1)*(counter[23]+1)
    return sum
    
Tn = 6000
while count_divs(triangle_num(Tn)) < 500:
    Tn += 1
print triangle_num(Tn), "has", count_divs(triangle_num(Tn)), "divisors"
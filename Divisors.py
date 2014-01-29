from math import sqrt
import time
import itertools
from fractions import gcd

##############################################################
### cartesian product of lists ##################################
##############################################################

def appendEs2Sequences(sequences,es):
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result


def cartesianproduct(lists):
    """
    given a list of lists,
    returns all the possible combinations taking one element from each list
    The list does not have to be of equal length
    """
    return reduce(appendEs2Sequences,lists,[])

##############################################################
### prime factors of a natural ##################################
##############################################################

def primefactors(n):
    '''lists prime factors, from greatest to smallest'''  
    i = 2
    while i<=sqrt(n):
        if n%i==0:
            l = primefactors(n/i)
            l.append(i)
            return l
        i+=1
    return [n]      # n is prime


##############################################################
### factorization of a natural ##################################
##############################################################

def factorGenerator(n):
    p = primefactors(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def divisors(n):
    factors = factorGenerator(n)
    divisors=[]
    listexponents=[map(lambda x:k**x,range(0,factors[k]+1)) for k in factors.keys()]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors

starttime = time.time()
count = 0
num = 60
divisor_list = divisors(num)[::-1]
newlist = []
for n in range(1, len(divisor_list)):
    multiple = 2
    while multiple * divisor_list[n] < num:
        if (multiple * num * divisor_list[n]) % (num + (multiple * divisor_list[n])) == 0:
            if (multiple * divisor_list[n]) not in newlist:
                newlist.append(multiple * divisor_list[n])
        multiple += 1
count += len(newlist)
print "Found", count
print newlist
print "Finished in", time.time() - starttime, "seconds"


"""

starttime = time.time()
count = 0
for num in range(6,1001):
    divisor_list = divisors(num)[::-1]
    newlist = []
    for n in range(1, len(divisor_list)):
        multiple = 2
        while multiple * divisor_list[n] < num:
            if (multiple * num * divisor_list[n]) % (num + (multiple * divisor_list[n])) == 0:
                if (multiple * divisor_list[n]) not in newlist:
                    newlist.append(multiple * divisor_list[n])
            multiple += 1
    count += len(newlist)
print "Found", count
print "Finished in", time.time() - starttime, "seconds"


Testvals:
6499223 = 12807816

square root of 12807816 is 3578
12807816 has 48 divisors
y 12807816 x 1829688 n 1600977 a 11206839 b 228711 ab 2563127354529 n**2 2563127354529
y 12807816 x 2134636 n 1829688 a 10978128 b 304948 ab 3347758177344 n**2 3347758177344
y 12807816 x 4269272 n 3201954 a 9605862 b 1067318 ab 10252509418116 n**2 10252509418116
y 12807816 x 6403908 n 4269272 a 8538544 b 2134636 ab 18226683409984 n**2 18226683409984
y 12807816 x 9148440 n 5336590 a 7471226 b 3811850 ab 28479192828100 n**2 28479192828100
y 12807816 x 9605862 n 5489064 a 7318752 b 4116798 ab 30129823596096 n**2 30129823596096

Problems: for 1000, 600 is not a divisor of 1000. There is no 3 in the prime factorization of 1000.

for 176 (in sequence) there are x divisors, and solutions appear at:
x = 66 (n = 48)
x = 80 (n = 55)

"""
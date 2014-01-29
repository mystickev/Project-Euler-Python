"""
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

def count_divs(tuple):
    count = 1
    for pi_si in tuple:
        count *= (pi_si[1] + 1)
    return count

starttime = time.time()
num = 10**12
for i in range(1, num):
    if (i * num) % (i + num) == 0:
        print "y = ", num, "x = ", i, "n = ", (i * num) / (i + num), "a = ", num - ((i * num) / (i + num)), \
            "b = ", i - ((i * num) / (i + num)), "ab = ", (num - ((i * num) / (i + num)))*(i - ((i * num) / (i + num))), \
            "n**2 = ", ((i * num) / (i + num))**2
print "finished in", time.time() - starttime, "seconds"

print "-----------------------------------"
y = 15**6
numsq = y**2
starttime = time.time()
for n in range(2,y):
    if numsq % (y - n) == 0 and n < y/2:
        print "y = ", y, "n =", n
print "finished in", time.time() - starttime, "seconds"


"""

from Prime import primefactor
import math
from math import sqrt, floor, ceil
import time


print "-----------------------------------"
sumtotal = 0
for y in range(6, 1001):
    numsq = y**2
    lower_limit = int(floor(math.sqrt(y)))
    starttime = time.time()
    count = 0
    for n in xrange(lower_limit, y/2):
        if numsq % (y - n) == 0:
            count += 1
            sumtotal += 1
    if count >= 1:
        print y, count, sumtotal
print "finished in", time.time() - starttime, "seconds"


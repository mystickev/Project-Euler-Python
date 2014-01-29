"""
Problem 14 - The following iterative sequence is defined for the set of positive integers:

n > n/2 (n is even)
n > 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all 
starting numbers finish at 1. 

Which starting number, under one million, produces 
the longest chain? NOTE: Once the chain starts the terms are allowed to go above 
one million.
"""

def gen_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:   
            n = n // 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence

max_len = 0  
for i in xrange(800000,1000001):
    if len(gen_sequence(i)) > max_len:
        max_len = len(gen_sequence(i))
        max_i = i
print "seed", max_i, "yields", max_len, "numbers"

"""
lim = 1000000; chain = {1:1}; maxL = 1

def collatz(i):
   if i not in chain: chain[i] = 1 + collatz(i/2 if i%2==0 else 3*i+1)
   return chain[i]
for i in range(1, lim): maxL = i if (collatz(i) > chain[maxL]) else maxL 
print "collatz chain of {} is {} terms long.".format(maxL, collatz(maxL))
"""


# -*- coding: utf-8 -*-
"""
Project Euler #47 Distinct Prime Factors

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
from Prime import primefactor # re-using this function, I built it into a Module Prime with other Euler prime-related stuff
import time # see how long it takes to execute code

"""
Note: my primefactor(n) function will return a list of tuples [(pi, si), ..., (pn, sn)] where the whose corresponding
prime factors pi and exponents si can be accessed by using slice notation.  For example, primefactor(644) will return a
list of tuples [(2,2), (7,1), (23,1)].

I'm going to use this function on a range of inputs n and check to see if consecutive values of n have the same
list length (list of tuples); if so, return those values.
"""
starttime = time.time()

for n in range(600, 600000):

    if len(primefactor(n)) == len(primefactor(n + 1)) == len(primefactor(n+2)) == len(primefactor(n+3)) == 4:

        """
        check to see if we get 4 in a row with 4 prime factors, skip others.  I tested this on length 3
        and it worked perfectly (n, n+1, n+2 == 3)  If it works, print "got one" followed by the n and its
        prime factorization list of tuples
        """

        print "got one", n, primefactor(n)
        print "got two", n+1, primefactor(n+1)
        print "got three", n+2, primefactor(n+2)
        print "got four", n+2, primefactor(n+3)
        break # exit if we find one

print "Done! Finished in", time.time() - starttime, "seconds"

"""
Answer:
got one 134043 [(3, 1), (7, 1), (13, 1), (491, 1)]
got two 134044 [(2, 2), (23, 1), (31, 1), (47, 1)]
got three 134045 [(5, 1), (17, 1), (19, 1), (83, 1)]
got four 134045 [(2, 1), (3, 2), (11, 1), (677, 1)]
Done! Finished in 4.51472806931 seconds
"""
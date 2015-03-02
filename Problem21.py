# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def proper_divisors(number):
    """ Return a list of the divisors of a number """
    divisor_list = []
    for i in range(1, number//2 + 1):
        if number % i == 0:
            divisor_list.append(i)

    return divisor_list

def d(list_of_numbers):
    """ sum the list of numbers """

    return sum(list_of_numbers)

amicable_total = 0
for i in range(1,10001):
    test = d(proper_divisors(d(proper_divisors(i))))
    if test == i and i != d(proper_divisors(i)):
        print(i)
        amicable_total += i

print(amicable_total)

""" Results:

220
284
1184
1210
2620
2924
5020
5564
6232

Sum = 31626
"""
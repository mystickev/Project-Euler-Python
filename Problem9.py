# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def generate_pythagorean_triple(m, n):
    """ Generates a pythagorean triple using Euclid's method.

    Given two starting integers m and n, return a pythagorean triple as a tuple of integers (a, b, c).

    No coding required if you use Euclid's method of finding Pythagorean Triples.
    Euclid's method says that given an arbitrary pair of positive integers m and n,
    with m > n, the integers a, b and c form a Pythagorean triple as follows:

    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2

    If you take a + b + c = 1000, you'll find that m(m+ n) = 500; m^2 = 400 and m*n = 100; and
    from there it's pretty easy to find two integers m = 20 and n = 5.  From there, the
    results are a = 375; b = 200; and c = 425 and the product of these results is 31,875,000.
    """

    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2

    return a, b, c
    # returns a tuple of integers

# iterate over a range of m and n values
for i in range(1, 22):
    for j in range(1, 22):
        if sum(generate_pythagorean_triple(i, j)) == 1000:
            a1, b1, c1 = generate_pythagorean_triple(i, j)
            print('m is: ', i)
            print('n is: ', j)
            print(generate_pythagorean_triple(i, j))
            print('triple product:', a1 * b1 * c1)
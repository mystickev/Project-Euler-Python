#--- check n for prime--------------------------------------------------------------------------
def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

#--- generate prime numbers----------------------------------------------------------------------
def prime_sieve(n):
    """
    Function returns a list of prime numbers from 2 to a prime < n

    Example: prime_sieve(25) returns [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


#--- Miller-Rabin primality test----------------------------------------------------------------
def miller_rabin(n):
    """
    Check n for primalty:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:
    http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)
    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

#--- Prime factorization algorithms----------------------------------------------------------------------

def fetch_prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        """
        Easy to make it run in O(sqrt(n)) time, just stop the loop when d*d > n
        and if n > 1 at this point then its value should be appended to
        the list of prime factors.
        """
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors # returns a list of prime factors

# prime factorization algorithm
def naive_prime_factor(x): # naive prime factorization algorithm
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    return factors

#--- factor a number into primes and frequency----------------------------------------------------
def primefactor(n):
    """
    find the prime factors of n along with their frequencies, for example:

    primefactor(786456) will return a list of tuples [(2,3), (3,3), (11,1), (331,1)] whose corresponding
    prime factors pi and exponents si can be accessed by using slice notation.
    """
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = perform_trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1; n /= p
        F.append((p, e))
    F.sort()
    return F


def perform_trial_division(n, bound = None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n % p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m * m <= n:
        if n % m == 0:
            return m
        m += dif[i % 8]
        i += 1
    return n

def factors(n):
    gaps = [1,2,2,4,2,4,2,4,6,2,6]
    length, cycle = 11, 3
    f, fs, next = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[next]
        next += 1
        if next == length:
            next = cycle
    if n > 1: fs.append(n)
    return fs

def primes_upto(upto):
    # returns a list of primes up to the input value
    primes = numpy.arange(3,upto+1,2)
    isprime = numpy.ones((upto - 1) / 2, dtype = bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor - 2) / 2]: isprime[(factor * 3 - 2) / 2:(upto - 1) / 2 : factor] = 0
    return numpy.insert(primes[isprime], 0, 2)
    # will truncate output with ... and return only last 3 values if list is huge
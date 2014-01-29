def pandigital(n):
  #bitwise check for pandigitalism
  count = 0
  num = 0
  digit = 0
  while n > 0:
    if n % 10 == 0:
      return False
    num = digit
    digit |= 1 << (n % 10 - 1)
    if num == digit:
      return False
    count += 1
    n /= 10
  if digit == (1 << count) - 1:
    return True
  else:
    return False

products = []
summation = 0
# lets limit the search space
# 2x2 product does not yield a 9-digit number
# only conditions that work are 1x4 and 2x3
for m in range(2,100):
  if m > 9:
    nbegin = 123
  else:
    nbegin = 1234
  nend = 10000 / m + 1
  for n in range(nbegin, nend):
    if n % 10 == 0: continue # remove
    if m % 10 == 0: continue # remove
    prod = m * n
    if prod % 10 == 0: continue # remove
    compiled = sorted(str(prod) + str(n) + str(m))
    result = int(''.join(compiled))
    if len(str(result)) == 9: # check for 9 digits (some have less)
      if pandigital(result):
        print result, "from m", m, "n", n, "and prod", prod
        summation += prod
        products.append(prod)
print "Result is", summation, "but let's remove duplicates using set and sum"
print "The final result is", sum(set(products))

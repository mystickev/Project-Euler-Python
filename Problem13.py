"""
Problem 13: Work out the first ten digits of the sum of the 
following one-hundred 50-digit numbers.
"""

array = []
sum = 0
with open("input13.txt", "r") as f:
  for line in f:
    array.append(line)
    sum = sum + int(line)
print str(sum)[0:10]
f.close()
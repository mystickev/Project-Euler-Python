"""
Project Euler Problem 13:
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(external data file)

"""
import time
starttime = time.time()

array = [] # opening an empty list "array" in Python is easy
sum = 0

#
# open the file "input13.txt" for reading using Python's
# open-as method
#

with open("input13.txt", "r") as f:
    #
    # use a for loop to iterate over each line
    # convert each line to an integer
    # then store the sum in sum
    #
    for line in f:

        array.append(line)

        sum = sum + int(line)

#
# To get the answer, let's use Python's "slice" syntax
# to grab the first 10 digits.  First convert the sum to
# a string.
#
print str(sum)[0:10]
print "Finished in", time.time() - starttime, "seconds"
#
# Close the file for reading
#
f.close()
# -*- coding: utf-8 -*-
"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers
from 1 to 1000 (one thousand) inclusive were written out in words, how many 
letters would be used? 

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""
import math 

numbers = dict()
numbers[0] = ''
numbers[1] = 'one'
numbers[2] = 'two'
numbers[3] = 'three'
numbers[4] = 'four'
numbers[5] = 'five'
numbers[6] = 'six'
numbers[7] = 'seven'
numbers[8] = 'eight'
numbers[9] = 'nine'
numbers[10] = 'ten'
numbers[11] = 'eleven'
numbers[12] = 'twelve'
numbers[13] = 'thirteen'
numbers[14] = 'fourteen'
numbers[15] = 'fifteen'
numbers[16] = 'sixteen'
numbers[17] = 'seventeen'
numbers[18] = 'eighteen'
numbers[19] = 'nineteen'
numbers[20] = 'twenty'
numbers[30] = 'thirty'
numbers[40] = 'forty'
numbers[50] = 'fifty'
numbers[60] = 'sixty'
numbers[70] = 'seventy'
numbers[80] = 'eighty'
numbers[90] = 'ninety'

def printnum(num):
    result = ''
    val = num
    hunds = (int(math.floor(num/100)) % 10)
    tens = (int(math.floor(num/10)) % 10) * 10
    ones = (int(math.floor(num % 10)))
    if tens < 20:
        num -= hunds*100
        tens = num
        ones = 0
    if val == 1000:
        result = 'one thousand'
        return result
    else: 
        if val > 19 and val < 100:
            result = numbers[tens]
            result += numbers[ones]
        if val > 99:
            result = numbers[hunds]
            result += "hundred"
            if tens > 0:
                result += "and"
                result += numbers[tens]
                result += numbers[ones]
            else:
                print ""
        if val < 20:
            result = numbers[tens]
            result += numbers[ones]
    return result

def count_letters(word):
    return len(word) - word.count(' ')
    
counter = 0
for i in range (1,1001):
    print printnum(i), count_letters(printnum(i))
    counter += count_letters(printnum(i))
print "result is:", counter    


    

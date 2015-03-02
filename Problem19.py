
# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one,Saving February alone, which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import calendar

week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8:'August',
         9: 'September', 10: 'October', 11: 'November', 12: 'December'}

counter = 0
for year in range (1901, 2001):
    month_increment = 1
    while month_increment < 13:
        if week[calendar.weekday(year, month_increment, 1)] == 'Sunday':
            print('Found', month[month_increment], '1st', year, 'was a Sunday')
            counter += 1
        month_increment += 1

print('\nFound', counter, 'total Sundays that start on the first of a month')
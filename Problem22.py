"""
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv

letter_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                 'Z': 26}

def name_split(name):
    """ Split a name into a list of letters for mapping
    """
    return list(name)

list_of_names = []
reader = csv.reader(open('p022_names.txt'))
for row in reader:
    for i in range(len(row)):
        list_of_names.append(row[i])

total_of_all_names = 0
for name_pos, name in enumerate(sorted(list_of_names)):
    name_string = name_split(name)
    sum_of_letters = 0
    for letter in name_string:
        sum_of_letters += letter_map[letter]
    print(name_pos+1, name, sum_of_letters, (name_pos+1) * sum_of_letters)
    total_of_all_names += (name_pos+1) * sum_of_letters

print('The answer is:', total_of_all_names)

"""Results:
1 AARON 49 49
2 ABBEY 35 70
3 ABBIE 19 57
...
5162 ZULEMA 78 402636
5163 ZULMA 73 376899
The answer is: 871198282
"""
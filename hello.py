# -*- coding: utf-8 -*-
"""
Python Practice file
Created and updated as required

@author: MasukuCM
"""

# New Scrap File for Trying out stuff

import sys

import re


def Cat(filename):
    f = open(filename, 'r')
#    for line in f:
#        print(line)
#    lines = f.readlines()    #creating a list of lines
#    print(lines)
    text = f.read()           # just reads the file
    print(text)
    f.close()


def Hello(name):
    if name == 'Alice':
        print('Alice Mode')
    else:
        print('Else Case')
    name = name + '!!!!'
    print('Hello',name)


# Regular Expressions

def Find(pat, text):
    match = re.search(pat, text)
    if match:
        print(match.group())
    else:
        print('Not found')



# Define a main() function that prints a little greeting.
def main():
    Hello(sys.argv[1])
    print('Welcome to the practice doc!')
#    print(sys.argv[1])
    Cat(sys.argv[1])

    Find('ig', 'called piiig')


# Reviewed up to end of Part 2, next session is Part 3

# Now onto lists and dictionaries


# lists
    li = [2, 4, 6]
    a = [4, 2, 1, 6]
    b = ['ccc', 'aaaa', 'd', 'bb']
    c = sorted(b, key=len)
    for num in b:
        print(num)
    print(c)

# example of a loop


# join method, split method
    d = ':'.join(b)
    print(d.split(':'))


# next thing is tuples
# immutable, fixed size

    tu = (2, 3, 5)

# list of tuples
    litu = [(1,'b'), (2,'a'), (1,'a')]
    print(sorted(litu))


# Using dictionaries
    d = {'user':'bozo', 'pswd':1234}
    print(d['pswd'])

# look at creating an empty dictionary and adding content sequentially

# need a section on adding to a dictionary



# next section coming soon


    # scrap notes
    # Not important


# Day 2 Part 1
# Start with Regular Expressions



# Next is Day 2 Part 2
# Utilities

    
# Info from Google's Python Class
# PyQuick - Basic Python


# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    main()


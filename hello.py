<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Python Practice file
Created and updated as required

@author: MasukuCM
"""

# New Scrap File for Trying out stuff

import sys
import os
import re

import subprocess             # this has replaced the commands module from python 2

import math                   # just for fun

def Cat(filename):
#    f = open(filename, 'r')
#    for line in f:
#        print(line)
#    lines = f.readlines()    #creating a list of lines
#    print(lines)

# handling exceptions
    try:
        f = open(filename)
        text = f.read()           # just reads the file
        print('---', filename)
        print(text)
    except IO Error:
        print('IO Error', filename)

# the exception doesn't work well

#    f.close()

 def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))

# most parts of this code has changed a lot from Python 2 to 3


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

# Utilities: OS and Commands
# Didn't do much on this

# Utilities: URLs and HTTP, Exceptions

# Modularity
# Command line flags


# List comprehension


# Define a main() function that prints a little greeting.
def main():
    Hello(sys.argv[1])
#    print('Welcome to the practice doc!')
#    print(sys.argv[1])
#    Cat(sys.argv[1])
#    List(sys.argv[1])
    args = sys.argv[1:]
    for arg in args:
        Cat(arg)

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

# Review with repetition


# Day 2 Part 1
# Start with Regular Expressions


# Next is Day 2 Part 2
# Utilities

# Day 2 Part 3
# Utilities: URLs and HTTP, Exceptions

    
# Info from Google's Python Class
# PyQuick - Basic Python


# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    main()

=======
# -*- coding: utf-8 -*-
"""
Python Practice file
Created and updated as required

@author: MasukuCM
"""

# New Scrap File for Trying out stuff

import sys
import os
import re

import subprocess             # this has replaced the commands module from python 2

import math                   # just for fun

def Cat(filename):
#    f = open(filename, 'r')
#    for line in f:
#        print(line)
#    lines = f.readlines()    #creating a list of lines
#    print(lines)

# handling exceptions
    try:
        f = open(filename)
        text = f.read()           # just reads the file
        print('---', filename)
        print(text)
    except IO Error:
        print('IO Error', filename)

# the exception doesn't work well

#    f.close()

 def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))

# most parts of this code has changed a lot from Python 2 to 3


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

# Utilities: OS and Commands
# Didn't do much on this

# Utilities: URLs and HTTP, Exceptions

# Modularity
# Command line flags


# List comprehension


# Define a main() function that prints a little greeting.
def main():
    Hello(sys.argv[1])
#    print('Welcome to the practice doc!')
#    print(sys.argv[1])
#    Cat(sys.argv[1])
#    List(sys.argv[1])
    args = sys.argv[1:]
    for arg in args:
        Cat(arg)

    Find('ig', 'called piiig')


# Reviewed up to end of Part 2, next session is Part 3

# Restart the review

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

# Review with repetition

# New Revision after a long time

# Day 2 Part 1
# Start with Regular Expressions


# Next is Day 2 Part 2
# Utilities

# Day 2 Part 3
# Utilities: URLs and HTTP, Exceptions

    
# Info from Google's Python Class
# PyQuick - Basic Python


# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    main()

>>>>>>> caf9d8f3ed137fb70f45a8313fd299b8223f5b2b

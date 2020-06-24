# -*- coding: utf-8 -*-
"""
Python Practice file
Created and updated as required

@author: MasukuCM
"""

# New Scrap File for Trying out stuff

import sys

# def Cat(filename):
#    f = open(filename)
#    for line in f:
#        print(line)

def Hello(name):
    if name == 'Alice':
        print('Alice Mode')
    else:
        print('Else Case')
    name = name + '!!!!'
    print('Hello',name)


# Define a main() function that prints a little greeting.
def main():
    Hello(sys.argv[1])
    print('Welcome to the practice doc!')
#    print(sys.argv[1])
#    Cat(sys.argv[1])

# Reviewed up to end of Part 1, next session is Part 2

# Now onto lists and dictionaries


# lists
    li = [2, 4, 6]
    a = [4, 2, 1, 6]
    b = ['ccc', 'aaaa', 'd', 'bb']
    c = sorted(b, key=len)
#    print(b)
    for num in b:
        print(num)
    print(c)

# example of a loop



# Using dictionaries
    d = {'user':'bozo', 'pswd':1234}
    print(d['pswd'])


# next thing is tuples
# next section coming soon


    # scrap notes
    # Not important

    
# Info from Google's Python Class
# PyQuick - Basic Python


# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    main()


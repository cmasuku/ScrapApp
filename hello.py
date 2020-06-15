# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:26:52 2019

@author: MasukuCM
"""

# New Scrap File for Trying out stuff

import sys

def Cat(filename):
    f = open(filename)
    for line in f:
        print(line)


# Define a main() function that prints a little greeting.
def main():
    print('Welcome to the practice doc!')
    Cat(sys.argv[1])
    

# Using dictionaries
    d = {'user':'bozo', 'pswd':1234}
    print(d['pswd'])

# compare with lists
    li = [2, 4, 6]
    a = [4, 2, 1, 6]
    b = ['ccc', 'aaaa', 'd', 'bb']
    c = sorted(b, key=len)
    print(b)
    print(c)

# next thing is tuples
# next section coming soon


    # scrap notes
    # Not important

    
# Info from Google's Python Class
# PyQuick - Basic Python


# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    main()


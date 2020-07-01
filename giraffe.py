# -*- coding: utf-8 -*-
"""
Scrap Python file for trying out random code
Created on Tue Jun 30 2020
From watching Free Courses on YouTube
By: freeCodeCamp.org
Title: Learn Python -- Full Course for Beginners [Tutorial]
@author: MasukuCM
"""
# Preferred Editor/IDE PyCharm but I use Spyder

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2*np.pi*x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2,1,2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

# There's some exponential term that I did not see


# Unrelated code
character_name = 'George'
character_age = 35


# New Info from some Online course

## Programming for Everybody





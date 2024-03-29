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

import math
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
# to be fixed soon
# still waiting for the fix

# Unrelated code
character_name = 'George'
character_age = 35

# part of this code will be fixed soon
# most part of it should be fixed


# New Info from some Online course

## Programming for Everybody


# get all the import statements correct

## New info for fun

########################################

## Pyomo imports to be included
#from pyomo.environ import *
#
## PYOMO code
#model = ConcreteModel()
#model.r = Var()
#model.h = Var()
#
#def surf_area_obj_rule(m):
#  return 2 * pi * m.r * (m.r + m.h)
#model.surf_area_obj = Objective(rule=surf_area_obj_rule)
#
#def vol_con_rule(m):
#  return pi * m.h * m.r** == 355
#model.vol_con = Constraint(rule=vol_con_rule)

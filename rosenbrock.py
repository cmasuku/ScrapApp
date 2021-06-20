# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:10:09 2020
This is just a simple PYOMO file
The code runs by:
$ pyomo solve rosenbrock.py --solver=ipopt --summary

From a Pyomo book
"""

# Rosenbrock test function

from pyomo.environ import *

model = ConcreteModel()

# model.x = Var( initialize=-1.2, bounds=(-2, 2) )
# model.y = Var( initialize= 1.0, bounds=(-2, 2) )

# model.obj = Objective( expr= (1-model.x)**2 + 100*(model.y-model.x**2)**2, sense= minimize )

# Edited for fun
# These edits will be deleted afterwards
model.x = Var()
model.y = Var()
def rosenbrock(m):
    return (1.0 - m.x)**2 + 100.0*(m.y - m.x**2)**2
model.obj = Objective(rule=rosenbrock, sense=minimize)

solver = SolverFactory('ipopt')
solver.solve(model, tee=True)

print()
print('*** Solution ***:')
print('x:', value(model.x))
print('y:', value(model.y))

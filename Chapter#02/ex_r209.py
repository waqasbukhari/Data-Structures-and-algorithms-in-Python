#!/usr/bin/env python3

"""
method __sub__() is added to the Vector class. 
The changes are enclosed within comments specifying it to be part of R-2.9.
"""

from Vector import Vector

v = Vector([0,1,2,8, 8]) # Vector(list(range(5)))
u = Vector([0,1,2,3, 8]) # Vector(list(range(5)))
w = v - u

print(w)
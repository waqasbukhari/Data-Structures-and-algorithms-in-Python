#!/usr/bin/env python3

"""
method __neg__() is added to the Vector class. 
The changes are enclosed within comments specifying it to be part of R-2.10.
"""

from Vector import Vector

u = Vector([0,1,2,8, 8]) 
v = u + list(range(5,10)) # Note a list can be added to an instance of class Vector. polymorphism. 
print(v)
w = list(range(5,10)) + u # Note that a vector cannot be added to a list instance. 
print(w)
# We can added __radd__() that would enable the computation of w. 
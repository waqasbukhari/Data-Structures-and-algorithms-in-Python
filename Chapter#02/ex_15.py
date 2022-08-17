#!/usr/bin/env python3

"""
modified method __init__() to enable initialization either with an int or with a sequence type. 
The changes are enclosed within comments specifying it to be part of R-2.15.
"""

from Vector import Vector

u = Vector([0,1,2,8, 8]) # initialized with a sequence
v = Vector(5)            # initialized with an int
print(v * u)

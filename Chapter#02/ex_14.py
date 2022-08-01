#!/usr/bin/env python3

"""
modified method __mul__() to enable vector multiplication to compute dot product. 
The changes are enclosed within comments specifying it to be part of R-2.13.
"""

from Vector import Vector

u = Vector([0,1,2,8, 8]) 
v = Vector([3,4,5,11, 12]) 
print(v * u)

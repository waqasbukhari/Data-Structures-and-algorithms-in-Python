#!/usr/bin/env python3

"""
method __rmul__() is added to the Vector class. 
The changes are enclosed within comments specifying it to be part of R-2.13.
"""

from Vector import Vector

u = Vector([0,1,2,8, 8]) 
print(3 * u)

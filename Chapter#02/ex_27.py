#!/usr/bin/env python3

"""
method __contains__() is added to the Range class. 
The changes are enclosed within comments specifying it to be part of C-2.27.
"""

from Range import Range
from time import time


max_number = int(1e12)
repetitions = 100000


r = Range(5,max_number,4)
t = time()
for _ in range(repetitions):
    a = 0 in r
print(time() - t)
t = time()
for _ in range(repetitions):
    a = -10 in r
print(time() - t)
t = time()
for _ in range(repetitions):
    b = (max_number - 1) in r
print(time() - t)

print()
r = range(5,max_number,4)
t = time()
for _ in range(repetitions):
    a = 0 in r
print(time() - t)
t = time()
for _ in range(repetitions):
    a = -10 in r
print(time() - t)
t = time()
for _ in range(repetitions):
    b = (max_number - 1) in r
print(time() - t)



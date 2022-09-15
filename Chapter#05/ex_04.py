#!/usr/bin/env python3

"""
Modification is made to method __getitem__ of DynamicArray class. 
Changes are enclosed within comments, specifying ex R-5.4
"""

from DynamicArray import DynamicArray

print("populating dynamic array. ")
A = DynamicArray()
for i in range(20):
    A.append(i)
print("array is populated. ")
for i in range(-20,0,1):
    print(i, A[i])
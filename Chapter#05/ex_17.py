#!/usr/bin/env python3

"""
On class DynamicArray. 
n append operations are "amortized" O(n)
n pop operations are "amortized" O(n) because pop is inverse of append and has same cost. 
Hence, a series of n append and n pop operations take O(n).
"""
#!/usr/bin/env python3
"""
O(n) algorithm. 
find 5 repeated elements; all elements are from 1 to n-5. n is hte size of the array/list. 
"""

def repeated_elements(seq):
    n = len(seq)
    B = [None] * (n-5) # place 1 at B[0] and t at B[t-1]
    for s in seq:
        if B[s-1] is not None:
            yield s
        B[s-1 ] = s

if __name__ == "__main__":
    s = list(range(1,500)) + [5,71,200,300,450]
    for t in repeated_elements(s):
        print(t)

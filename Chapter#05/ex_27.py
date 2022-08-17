#!/usr/bin/env python3
"""
Taking xor between all the n-bit elements would result in a zero. 
xor of all the n-bit elements would yield a number (if it is non-zero) is one of the missing. 
let 3 is missing in a 2-bit integers, taking 0 xor 1 xor 2 = 3
"""

def missing_k_bit_element(seq):
    result = 0
    for s in seq:
        result = result ^ s

    return result

if __name__ == "__main__":
    s = list(range(32))
    print(missing_k_bit_element(s))

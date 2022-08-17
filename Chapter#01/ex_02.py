#!/usr/bin/env python3

def is_even(k):
    """ This function uses bit-wise operator to implement to determine
    whether a function is even or odd
    As an example consider 41 and its 8-bit binary representation.
    also consder for 1
    41 ~ 00101001
    01 ~ 00000001
    Taking bit-wise and would zero-out all other bits except the least
    significant bit.
    This LSB can determine whether a number is odd or even since it would 1
    if the number is odd     """
    

    
    return not (k & 1)

if __name__ == '__main__':
    print(is_even(41))
    print(is_even(410))
    print(is_even(24))
    print(is_even(0))
    print(dir(is_even))
    print(is_even.__doc__)

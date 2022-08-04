#!/usr/bin/env python3

from random import randrange

""" Implement shuffle using only randrange(n) that spits a number from 0 to n-1 inclusive. """
def shuffle(seq):
    """
    Logic:
    i) keep a number to track the end of array, lets call it j, which initially would be n-1. 
    ii) pick a random number from 1 to j, inclusive randrange(j). 
    iii) picked number should be appended to shuffled array, and is placed at the end and j is decrementd. 
    iv) repeat ii) and iii) until j =-1, or len(shuffled_array) = len(seq)
    """
    n = len(seq)
    shuffled_array = []
    j = n-1 # track the last index, elements placed in shuffled array should be after this. 
    while j > -1: # len(shuffled_array) < n:
        idx = randrange(j + 1) # +1 because end number is also a candidate. 
        shuffled_array.append(seq[idx])
        seq[idx], seq[j] = seq[j], seq[idx]
        j -= 1

    return shuffled_array

if __name__ == '__main__':

    arr = list(range(50))
    print(shuffle(arr))

    print(len(set(arr)))

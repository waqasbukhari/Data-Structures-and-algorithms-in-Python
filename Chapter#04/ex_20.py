#!/usr/bin/env python3

from random import shuffle
def rearrange_around_k(seq, k, start=None, end=None):
    """
    in each recursive run.
    i) if len(seq) < 2, base case.  
    ii) if start >= end, base case. 
    iii) iterate start until it reaches a value (>k). If start does not reach such a value, base case. 
    iv) iterate end backwards until it reaches a value (<=k). If end does not reach such a value, base case. 
    v) if the base case iii) and iv) is not reached, replace the contents of start and end and return a subsequent recursive call with appropriate start and end. 
    """
    # # base case
    if len(seq) < 2:
        return seq

    # in the first recursive run. 
    if start is None:
        start, end = 0, len(seq)-1

    if start >= end:
        return seq

    for st_index in range(start, end+1): # iterate to find index with odd value. 
        if seq[st_index] > k :
            break

    if st_index == end: # base case iii) odd value is reached at end, => nothing to replace. 
        return seq

    start = st_index

    for en_index in range(end, start-1, -1): # iterate to find index with odd value. 
        if seq[en_index] < k:
            break

    if en_index == start: # base case iv) even value is reached at start, => nothing to replace. 
        return seq

    end = en_index

    seq[start], seq[end] = seq[end], seq[start]

    return rearrange_around_k(seq, k, start=st_index+1, end=en_index-1)
    
if __name__ == "__main__":
    print()
    a = list(range(1))
    print(rearrange_around_k(a, 5))

    print()
    a = list(range(2))
    print(rearrange_around_k(a, 5))

    print()
    a = list(range(100))
    shuffle(a)
    print(rearrange_around_k(a, 25))

    print()
    a = [1,3,5,7,9,11,13,15]
    shuffle(a)
    print(rearrange_around_k(a, 10))

    print()
    a = list(range(2,200,2))
    shuffle(a)
    print(rearrange_around_k(a, 105))


#!/usr/bin/env python3
from random import shuffle, randint
def my_shuffle(seq):
    perm_idx = []
    while len(perm_idx) < len(seq):
        idx = randint(0, len(seq)-1)
        if idx not in perm_idx:
            perm_idx.append(idx)
    return [seq[numb] for numb in perm_idx]
    

# print([chr(numb_rep_chr) for numb_rep_chr in range(ord('a'), ord('z') + 1)])

if __name__ == '__main__':
    lst = list(range(10))
    print(my_shuffle(lst))
    

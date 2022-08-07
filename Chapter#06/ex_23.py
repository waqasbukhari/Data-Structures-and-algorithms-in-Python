#!/usr/bin/env python3

from Stack import ArrayStack

# Using lists very similar to Stacks. i.e., using append for push and pop for pop

def reorder_stacks(R, S, T):
    n, m = len(S), len(T)
    while S:
        R.append(S.pop())
    while T:
        R.append(T.pop())
        
    for _ in range(m):
        S.append(R.pop())
        
    for _ in range(n):
        S.append(R.pop())
        
        
        
    

if __name__ == "__main__":
    R = [1,2,3]
    S = [4,5]
    T = [6,7,8,9]
    reorder_stacks(R, S, T)
    print(R)
    print(S)
    print(T)
    
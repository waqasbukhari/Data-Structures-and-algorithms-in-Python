def unique(S, start, stop):
    if stop-start<=1: return True
    elif not unique(S, start, stop-1): return False
    elif not unique(S, start+1, stop): return False
    else: return S[start] != S[stop] 



"""
unique[n]
n = 1   ->   1 operation(if statement)      ->  1  = 2^0
n = 2   ->  IF AND ESE STATEMENTS           ->   2 OPERATIONS
n = 3   ->  n2+n2   ->   2+2  ->   4        -> 2^2
n = 4   ->  n3+n3   ->   2^2+2^2  ->   8    -> 2^3
n = 5   ->  n4+n4   ->   2^3+2^3  ->   16   ->2^4
n = 5   ->  n(5-1)+n(5-1)  ->  2^(5-2)+ 2^(5-2)    ->   2^(n-1)
.
.
.
.
n = n   ->  n(n-1)+n(n-1)    ->  2^(n-2) + 2^(n-2)   ->   2^(n-1)


so overall runtime is
1+2+4+8+16+.....+2^n-1     ->   exponentiol runtime

"""


def unique1 (S):
    if len (S)<=1: return "unique"
    
    for i in range(len(S)):
        for j in range(1,len(S)):
            if S[i] ==  S[j]:
                print('unique')
    print('unique') 


S = [0,1]
unique1(S)

"""

unique[n]
n = 1   ->   1 operation(if statement)      ->  1  = 2^0
n = 2   ->  i=2 elements & j = 1 element           ->   2 OPERATIONS
n = 3   ->  i=3 elements & j = 2 element           ->   6 OPERATIONS
n = 4   ->  i=4 elements & j = 3 element           ->   12 OPERATIONS
n = 5   ->  i=5 elements & j = 4 element           ->   20 OPERATIONS
n = 5   ->  i=6 elements & j = 5 element           ->   30 OPERATIONS
.
.
.
.
n = n   ->  i=n elements & j = n-1 element           ->   n(n-1) OPERATIONS
                                                     ->   n^2-n operations
                                                     -> runtime is  O(n^2)


so overall runtime is
n^2     ->   quadratic runtime

"""


            
ZZZZZZZZZZZZZZZZ

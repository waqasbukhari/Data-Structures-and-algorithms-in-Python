# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    
    if n == 0:
        return
    else:
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

n = 5

TowerOfHanoi(n, 'A', 'C', 'B')

##############runtime explanation#############
"""
TowerOfHanoi[n]
n = 1   ->   1 print  ->  1  = 2^0
n = 2   ->  1 print+ TowerOfHanoi[1] +1 print   ->   1+1+1=3 = 2^2  - 1
n = 3   ->  1 print+TowerOfHanoi[2]+1 print + TowerOfHanoi[1] +1 print
        ->     1    +    3     +   1   + 1    + 1 = 7 = 2^3  - 1


n = 4   ->  1 print  +  TowerOfHanoi[3]  + 1 print + TowerOfHanoi[2] + 1 print
            +TowerOfHanoi[1] +1 print

        -> 1 + 7 + 1+ 3+1+1+1 = 15 = 2^4 - 1

n = n = 1 print +TowerOfHanoi[n-1]+1 print+.......+ 1 print  +  TowerOfHanoi[3]  + 1 print + TowerOfHanoi[2] + 1 print
            +TowerOfHanoi[1] +1 print
        1 + 2^n-1 -1 + 1 + .....+1+1+1 = 2^n - 1


So, tower of hanoi has time complexity of O(2^n)
"""

#!/usr/bin/env python3

def factors_2(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k
            
def factors_3(n):
    k = 1
    rem_factors = []
    while k * k < n:
        if n % k == 0:
            yield k
            rem_factors.append(n //k)
        k += 1
    if k * k == n:
        rem_factors.append(k)

    while rem_factors:
        yield rem_factors.pop()
            
if __name__ =='__main__':
    gen2 = factors_2(100)
    for factor in gen2:
        print(factor)

    print('\n')
    
    gen3 = factors_3(100)
    for factor in gen3:
        print(factor)
    
    

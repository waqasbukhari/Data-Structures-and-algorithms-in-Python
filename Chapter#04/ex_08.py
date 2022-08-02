#!/usr/bin/env python3

"""
if n is a power of 2. 
then repeatedly doing A to B would make the last array with a length of 1 and 
all the intermediate arrays would have a length that would be power of 2. 

Directly summing up the array involves n additions. 

In the proposed method, every step invols additions that are half the size of the array. 
so, the total additions would be n/2 + n/4 + ..... + 1 (chain of length log n ) for any n (length of the initial array. )
mathematically, it is 

summation from i=0 to log(n) -1 {2^i} -- this mathematical expression is a sum of a geometric series. 


applying the sum of finite geometric series formulat, we get. 

1 - 2^(log n) / 1 - 2

2^log n = n

(1-n)/(1-2) = n. 
so, it is O(n)
"""
#!/usr/bin/env python3


"""
Number of lines printed in draw_interval(c). 
c = 1, lines = 1... 1 line with 1 dash
c = 2, lines = 1 (line with 2 dash) + 2 (line with 1 dash) = 3
c = 3, lines = 1 (line with 3 dash) + 2 (line with 2 dash) + 4 (line with 1 dash) = 7


Generalizing. 
c = 4, lines = 2^0 (line with 4 dash) + 2^1 (line with 3 dash) + 2^2 (line with 2 dash.) + 2^3 (line with 1 dash.)  = 15
c = n, lines = 2^0 + 2^1 + 2^2 + ... + 2^(n-1) 

we know that. 2^n = 1 + summation from i=0 to i=n-1 {2^i}

so, 
c = n, lines = 2^n - 1 

"""

"""
Now, how many number of dashes are printed in draw_interval(c). 
c = 1, lines = 1... 1 line with 1 dash, dashes = 1
c = 2, lines = 1 (line with 2 dash) + 2 (line with 1 dash) = 3, dashes = 4
c = 3, lines = 1 (line with 3 dash) + 2 (line with 2 dash) + 4 (line with 1 dash) = 7, dashes = 11


Generalizing. 
c = 4, lines = 2^0 (line with 4 dash) + 2^1 (line with 3 dash) + 2^2 (line with 2 dash.) + 2^3 (line with 1 dash.)  = 15, dashes = 26
c = n, lines = 2^0 + 2^1 + 2^2 + ... + 2^(n-1), 
      dashes = (n-0)*2^0 + (n-1)*2^1 + (n-2)*2^2 + ... + (n-(n-1))*2^(n-1)

dashes = 2^0*n + 2^1*(n-1) + 2^2*(n-2) + .... + 2^(n-1)*(n-(n-1))
dashes = 1*2^(n-1) + 2*2^(n-2)  + 3*2^(n-3)  + ... + (n-1)*2^1 + n*2^0 .... (1)
dashes = 2^n (1/2 + 2/2^2 + 3/2^3 + 4/2^4 + 5/2^5 + .... + n/2^n)

so, dashes is summation from i=1 to i=n {i/2^i}   .... (2)

reference: https://www.youtube.com/watch?v=5KQozlnAWuo for below.... 

(2) can written as a double summation. 

{summation from i=1 to i=n} {summation from k=0 to k=i} {1/2^i} 
Note the second summation caters for i in the numerator. 
interchanging the summation order. 
{summation from k=0 to k=n} {summation from i=k to i=n} {1/2^i} 
Applying geometric sum. 
{summation from k=0 to k=n} (1-(1/2)^n+1) / (1-(1/2)) - (1-(1/2)^k+1) / (1-(1/2))






"""
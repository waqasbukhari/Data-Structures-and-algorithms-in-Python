"""

let, we have a function d(n) with running time O(f(n)) and a function e(n)
with running time O(g(n))

d(n) = O(f(n))
e(n) = O(g(n))

d(n) - e(n) != O(f(n))  -  O(g(n))

because,


the subtraction of 2 running times may cancel the highest order terms
which are necessary for the running time analysis of an algorithm  since
the Big-Oh notation suggests the running time to be proportional to the
highest odered term in the function equation.



"""

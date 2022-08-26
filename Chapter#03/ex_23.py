def example1(S):
    n = len(S)          # 1 operation
    total = 0
    for j in range(n):  # for loop completes in n operations
      total += S[j]     # adding elements total n operations
    return total


"""

following the comments gives us 1+n+n= 2n +1
So this function is O(n) ignoring constant terms for big oh notation


"""

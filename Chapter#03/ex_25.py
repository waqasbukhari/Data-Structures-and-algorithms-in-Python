def example3(S):
    n = len(S)          # 1 operation
    total = 0
    for j in range(n):  # total n operations
        # each new value of j makes inner loop
        # to run for 1 extra time as compared to the last time
        # i.e. 1+2+3+...+n-1 = (n(n+1))/2 operations =>(n^2+n)/2
        for k in range (j+1):
          total += S[j]     # adding elements total n operations
    return total

"""

keeping in view the comments
we have
        1+ n + n^2/2 + n/2 + n = n^2/2 + 5n/2 +  1
        ignoring consttant and lower order terms gives:
        n^2/2


        So, big oh  notation for this example is O(n^2)



"""

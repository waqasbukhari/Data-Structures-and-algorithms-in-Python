def summ(seq,n):
    if n == 0:
        res = 0
    if n>=1:
        res += summ(seq,n)
    return res
    




A = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]

n = len(A)
for i in range(len(A)):
    res.append(summ(A[i],n))
    print(res)
        

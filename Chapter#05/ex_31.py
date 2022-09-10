def summ(seq,n):
    if n == 0:
        return (seq[n])
    if n>=1:
        return (seq[n]+summ(seq,n-1))





A = [[2,2,2,2],[3,3,3,3],[1,1,1,1],[4,4,4,4]]

n = len(A)
res = []
for i in range(len(A)):   
    res.append(summ(A[i],n-1))       
print(res)
result = summ(res,n-1)
print(result)




print(summ(A,3))

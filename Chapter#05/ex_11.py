#standard control structures for finding sum of 2d array

def summ(A,n):
    sumation = 0
    for i in range(n):
        for j in range(n):
            sumation += A[i][j]
    return sumation




A = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]

n = len(A)
result = summ(A,n)
print(result)

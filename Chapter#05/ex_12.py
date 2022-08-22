#list comprehension for finding sum of 2d array

A = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]

n = len(A)
summ = sum([sum (x) for x in A])
print(summ)

def find_duplicate(A):
    B = set()
    dup = []
    for i in range(len(A)):
        if  A[i] in B:
            dup.append(A[i])
            print(A[i],' is already contained in the set and set cannot have duplicates')
            return dup

        B.add(A[i])

        
    


A = [1,2,3,4,1]
duplicates = find_duplicate(A)
print(duplicates,'are duplicate items in given list')


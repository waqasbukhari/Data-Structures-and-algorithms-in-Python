L = list(range(100))
for i in range(len(L)):
    if L[i] == 101:
        print('found')
        break
print(' this block of code runs in O(n) time ') 

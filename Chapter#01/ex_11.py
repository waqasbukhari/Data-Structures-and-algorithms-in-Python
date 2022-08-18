a = []
a += [1]
print(a)
for i in range(1,10,1):
    a += [a[i-1]*2]
a += [[a[i-1]*2] for i in range(1,10,1)]
print(a)

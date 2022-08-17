import sys
data = []
size = [0]
for k in range (1,27):
    a = len(data)
    b = sys.getsizeof(data)
    #print(b)
    size.append(b)
    if b !=  size[k-1]:
        print('length is {} and size is {}'.format( a,b))
        #print('Length is {0:3d}; Size in Bytes is {0:4d}'.format(a,b))
    data.append(None)


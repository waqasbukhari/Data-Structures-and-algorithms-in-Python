import sys
data = []
size = [0]
for k in range (1,27):
    a = len(data)
    b = sys.getsizeof(data)
    size.append(b)
    print('length is {} and size is {}'.format( a,b))
    data.append(None)

import sys # provides getsizeof function
data = [ ]
n = 25
for k in range(n):
    a = len(data) # number of elements
    b = sys.getsizeof(data) - sys.getsizeof([])# actual size in bytes
    data.append(None) # increase length by one
    print( 'Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))

    
print('Array size is being shrinked')
while data:
    a = len(data) # number of elements
    b = sys.getsizeof(data) - sys.getsizeof([])# actual size in bytes
    data.pop()
    print( 'Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))

    

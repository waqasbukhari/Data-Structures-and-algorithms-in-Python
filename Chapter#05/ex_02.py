import sys # provides getsizeof function
data = [ ]
n = 260
for k in range(n):
    a = len(data) # number of elements
    b = sys.getsizeof(data) - sys.getsizeof([])# actual size in bytes
    array_capacity = int(b / 4)
    if a == array_capacity:
        print( 'Length: {0:3d}; Size in bytes: {1:4d}' .format(a, array_capacity))
        
    data.append(None) # increase length by one

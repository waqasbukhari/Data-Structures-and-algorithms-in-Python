import sys # provides getsizeof function
data = [ ]
n = 26
for k in range(n):
    a = len(data) # number of elements
    b = sys.getsizeof(data) - sys.getsizeof([])# actual size in bytes
    print( 'Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))
    data.append(None) # increase length by one

    

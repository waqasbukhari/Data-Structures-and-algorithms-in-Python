'''
yes the sequence of values gets changed with varying initial lengths of arrays
'''
import sys
data = [[0],[1,2],[3,4,9],[5,6,7,8]]

for j  in range(len(data)):
    size = data[j]
    for k in range(10):
        a = len(data[j])
        b = sys.getsizeof(data[j])
        size.append(b)
        print('length is {} and size is {}'.format( a,b))
        data.append(None)
    print('#################next###############')

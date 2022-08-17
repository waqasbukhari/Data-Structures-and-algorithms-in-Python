import sys
data = []
size = [0]
for k in range (1,27):
    a = len(data)
    b = sys.getsizeof(data)
    size.append(b)
    print('length is {} and size is {}'.format( a,b))
    data.append(None)
print('**********************************************')
print('popping elements 1 by 1 to view how the size of the data shrinks')
for j in range(len(data)):
    data.pop()
    b = sys.getsizeof(data)
    print('length is {} and size is {}'.format( a,b))

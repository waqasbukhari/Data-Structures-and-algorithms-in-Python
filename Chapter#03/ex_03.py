import math
for i in range(1,100):
    a = 2*i*i*i
    b = 40*i*i
    if b>a:
        print (b)
        print(a)
        print('n0 for B greater than A is = ', i+1)
        break

import time
A = []
n = [10000,100000,1000000,10000000,100000000]
t_app = []
for i in range(len(n)):
    t1 = time.time()
    for j in range(n[i]):
        A.append(None)
    t2 = time.time()
    t = t2-t1
    t_app.append(t)

list_ext = [[None]*(n[0]),[None]*(n[1]),[None]*(n[2]),[None]*(n[3]),[None]*(n[4])]

A = []

t_ext = []
for i in range(len(list_ext)):
    t3 = time.time()
    A.extend(list_ext[i])
    t4 = time. time()
    t = t4-t3
    t_ext.append(t)
print('time for APPEND operation for n = 10^3,10^4,10^5,10^6,10^7 is given as follows')
print(t_app)
print('time for EXTEND operation for n = 10^3,10^4,10^5,10^6,10^7 is given as follows')
print(t_ext)
print('clearly shows that extend operation is efficient than append operation')

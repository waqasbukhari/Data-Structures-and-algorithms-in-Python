x =(input("enter num sequence without delimiters"))
x= list(x)
a = len(x)+1
print(x)
b = []
y = []
for i in range(-1,-a,-1):
    x[i] = int(x[i])
    y.append(x[i])
    print(i)
    b.append(x[i])
y.reverse()
y.reverse()
print(y)
print(b)

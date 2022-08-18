x =(input("enter num sequence without delimiters"))

x = list(x)
print(x)
count = 0
y = []
for i in range(len(x)):
    x[i] = int(x[i])
    y.append(x[i])
print(y)
for i in range(len(y)):
    for j in range(len(y)):
        b = y[i]*y[j]
        if b%2 !=0:
            print(y[i],y[j])
            print("pair of numbers with odd product found")
            count+=1
print(count)

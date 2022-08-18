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
        if y[i] ==y[j]:
            print(y[i],y[j])
            print("pair of numbers with valus found")
            count+=1
print(count)

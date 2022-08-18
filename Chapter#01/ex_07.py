n = int(input("enter n"))
sums = 0
sums = sum([i*i for i in range(n) if i%2!=0])
print (sums)

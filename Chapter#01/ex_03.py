n = int(input("how many numbers do you want to enter"))
numlist = []
for i in range(n):
    data =int(input("enter next num"))
    numlist.append(data)
biggest = numlist[0]
for val in numlist:
    if val>biggest:
        biggest = val



print(biggest)


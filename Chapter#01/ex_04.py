n = int(input("enter num"))
def smsq(n):
    result = []
    sums = 0
    for i in range(n):
        sums+=i*i
    return sums
sums = smsq(n)
print (sums)

n = int(input("enter n"))
def sumoddint(n):
    sums = 0
    for i in range (n):
        if i%2 !=0:
            sums += i*i

    return sums

result = print(sumoddint(n))

n = int(input("enter n"))
m = int(input("enter m"))
def is_multiple(n,m):
    if n%m == 0:
        x= True
    else:
        x = False
    return x
result = print(is_multiple(n,m))

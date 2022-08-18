k = int(input("enter k"))

def iseven(k):
    a = divmod(k,2)
    if a[1] == 0:
        return True
    else:
        return False


print(iseven(k))

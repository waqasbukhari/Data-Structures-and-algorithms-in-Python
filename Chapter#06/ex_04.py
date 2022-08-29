def remove_recurr(S,n):
    if n<=0:
        return ('stack emptied')
    else:
        S.pop()
        return remove_recurr(S,n-1)
        
    




S =  list(range(10))
n = len(S)
T = remove_recurr(S,n)
print(T)

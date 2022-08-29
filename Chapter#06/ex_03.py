from Stack import ArrayStack
S = list(range(10))
T = ArrayStack()
def transfer(S,T):
    [T.push (S[-i]) for i in range(1,len(S))]
    T.push(S[0])
    return T
    
T = transfer(S,T)

print(T)

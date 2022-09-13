from Stack import ArrayStack
S = ArrayStack()
for i in range(10):
    S.push(i)
T = ArrayStack()
def transfer(S,T):
    [T.push (S.pop()) for i in range(len(S))]
    #T.push(S.pop())
    return T
    
T = transfer(S,T)

print(T)

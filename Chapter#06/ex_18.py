from Stack import ArrayStack

def transfer(S,T):
    [T.push (S[i]) for i in range(len(S))]

    S = []
    [S.append(T.pop()) for i in range(1,len(T))]

    return S
S = list(range(10))
T = ArrayStack()
S = transfer(S,T)
print(S, 'Final Stack')

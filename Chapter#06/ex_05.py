from Stack import ArrayStack
def transfer(S,T):
    [T.push(S[i]) for i in range(len(S))]
    S = [T.pop() for i in range(len(T))]

    return S,T


S = list(range(10))
T = ArrayStack()
S,T = transfer(S,T)


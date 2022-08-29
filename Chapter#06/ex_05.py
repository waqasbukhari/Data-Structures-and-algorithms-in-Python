def transfer(S,T):
    T = [S[i] for i in range(len(S))]
    S = [S.pop() for i in range(len(S))]
    S = [T[-i] for i in range(1,len(T))]+[T[0]]
    
    return S,T



S = list(range(10))
A = []
n = len(S)
print('Initial Stack ', S)
S,T = transfer(S,A)
print('intermediate list ',T)
print('Final Stack ',S)

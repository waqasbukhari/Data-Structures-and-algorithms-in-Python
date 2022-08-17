from collections import deque 
from Stack import ArrayStack

D = deque(list(range(1,9)))
S = ArrayStack()


print(D)

S.push(D.pop())
S.push(D.pop())
S.push(D.pop())
S.push(D.pop())
D.appendleft(D.pop())
D.append(S.pop())
D.append(D.popleft())
D.append(S.pop())
D.append(S.pop())
D.append(S.pop())

print(D)

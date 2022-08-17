from collections import deque 
from Queue import ArrayQueue

D = deque(list(range(1,9)))
Q = ArrayQueue()


print(D)

D.appendleft(D.pop())
D.appendleft(D.pop())
D.appendleft(D.pop())
Q.enqueue(D.pop())
Q.enqueue(D.pop())
D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(D.popleft())
D.append(D.popleft())
D.append(D.popleft())

print(D)

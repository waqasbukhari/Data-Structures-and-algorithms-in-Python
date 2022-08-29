"""
find a certain element in S containing n elements
constraint is... put back the elements in S as in original order
"""

from Stack import ArrayStack
from ArrayQueue import ArrayQueue
S = ArrayStack()
for i in range(10):
    S.push(i)
#sprint(S)

Q = ArrayQueue()

num2find = 6
for i in range(len(S)):
    ans = S.pop()
    if ans == num2find:
        Q.enqueue(ans)
        print('num found at stacks',i+1,' element')
    else:  Q.enqueue(ans)
print(Q)
print(len(Q))

print(Q.dequeue())
for i in range(len(Q)):
    print(i)
    print(S.push(Q.dequeue()))
print(S)

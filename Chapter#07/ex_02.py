from LinkStack import LinkedStack

L = LinkedStack()
M = LinkedStack()

for i in range(10):
    L.push(i)

for i in range(11,20):
    M.push(i)

def concat(L,M):
    L1 = LinkedStack()
    while not M.is_empty():
        L1._head = L1._Node(M._head._element,M._head)
        M.pop()
    while not L.is_empty():
        L1._head = L1._Node(L._head._element,M._head)
        L.pop()
    return L1

concList = concat(L,M)
print(concList)

from LinkeQueue import LinkedQueue

LQ = LinkedQueue()
for i in range(10):
    LQ.enqueue(i)
Q2 = LinkedQueue()
for i in range(10,20):
    Q2.enqueue(i)
def concat(LQ,Q2):
    for j in range(len(Q2)):
        LQ.enqueue(Q2.dequeue())
    return Q2, LQ

Q2,LQ = concat(LQ,Q2)


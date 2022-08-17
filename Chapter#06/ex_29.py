#!/usr/bin/env python3

"""
method rotate() is added to ArrayQueue class in Queue. 
"""
from Queue import ArrayQueue

Q = ArrayQueue()
Q.enqueue(2)
Q.rotate()
Q.enqueue(12)
Q.rotate()
Q.enqueue(24)


print(Q.first())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
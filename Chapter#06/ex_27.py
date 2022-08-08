#!/usr/bin/env python3

from Stack import ArrayStack
from Queue import ArrayQueue

# Using Queue to scan a Stack. 

def stack_scan_with_queue():
    'Scan for an element in Stack and then put it back in stack in the same order. '
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in range(10):
        stack.push(i)

    to_search = 2
    found = False
    while stack:
        e = stack.pop()
        if e == to_search:
            found = True
        queue.enqueue(e)

    while queue:
        stack.push(queue.dequeue())

    while stack:
        queue.enqueue(stack.pop())

    while queue:
        stack.push(queue.dequeue())

    print(stack.top()==i)

    return found

    
if __name__ == '__main__':
    stack_scan_with_queue()

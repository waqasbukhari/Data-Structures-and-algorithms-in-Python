#!/usr/bin/env python3

class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

# Stack using a single Queue. 
from Queue import ArrayQueue

# push is O(1)
# pop is O(n)

class ArrayStack:

    def __init__(self, maxlen=None):
        self._queue = ArrayQueue()
        self._top_element = None
            

    def __len__(self):
        return len(self._queue)
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def push(self, e):
        self._queue.enqueue(e)
        self._top_element = e

    def top(self):
        if self._top_element is None:
            raise Empty("The stack is empty")
        return self._top_element

    def pop(self):
        if self._top_element is None:
            raise Empty("The stack is empty")
            
        # Iterate over the queue n-1 times. 
        # Each iteration is about dequeue and then enqueue. 
        # nth element is one that need to be popped. 
        for _ in range(len(self._queue)-1):
            self._queue.enqueue(self._queue.dequeue())
            
        return self._queue.dequeue()
    

if __name__ == '__main__':

    S = ArrayStack( ) # contents: [ ]
    S.push(5) # contents: [5]
    S.push(3) # contents: [5, 3]
    print(len(S)) # contents: [5, 3]; outputs 2
    print(S.pop( )) # contents: [5]; outputs 3
    print(S.is_empty()) # contents: [5]; outputs False
    print(S.pop( )) # contents: [ ]; outputs 5
    print(S.is_empty()) # contents: [ ]; outputs True
    S.push(7) # contents: [7]
    S.push(9) # contents: [7, 9]
    print(S.top( )) # contents: [7, 9]; outputs 9
    S.push(4) # contents: [7, 9, 4]
    print(len(S)) # contents: [7, 9, 4]; outputs 3
    print(S.pop( )) # contents: [7, 9]; outputs 4
    S.push(6) # contents: [7, 9, 6]
    
        
        
    

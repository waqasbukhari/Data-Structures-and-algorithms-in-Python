#!/usr/bin/env python3

class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

# Queue using two stacks. 
from Stack import ArrayStack

# enqueue is O(1)
# dequeue is O(n)
from Stack import Empty

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._primary_stack = ArrayStack() # To keep the data. 
        self._secondary_stack = ArrayStack() # To help primary stack in doing dequeue operation. 
        self._first = None
        
    def __len__(self):
        return len(self._primary_stack) + len(self._secondary_stack)
        
    def is_empty(self):
        return len(self) == 0
        
    def first(self):
        if self._first==None:
            raise Empty("Queue is empty. ")
            
        return self._first
    
    def dequeue2(self):
        if self._first==None:
            raise Empty("Queue is empty. ")
            
        # Transfer all data from primary to secondary queue to get the element 
        # that is to be dequeued. 
        while self._primary_stack:
            self._secondary_stack.push(self._primary_stack.pop()) 
            
        # Now the first element of secondary element is one that should be popped. 
        answer = self._secondary_stack.pop()
        # Now put all data back to primary stack. 
        self._first = self._secondary_stack.top()
        while self._secondary_stack:
            self._primary_stack.push(self._secondary_stack.pop()) 
            
            
        return answer
    def dequeue(self):
        if self._first==None:
            raise Empty("Queue is empty. ")
            
        # Transfer all data from primary to secondary queue to get the element 
        # that is to be dequeued. 
        while True:
            if self._secondary_stack:
                answer = self._secondary_stack.pop()                
                break
            else:
                while self._primary_stack:
                    self._secondary_stack.push(self._primary_stack.pop()) 
                    
        # Similar code to assigne self._first. 
        while True:
            if self._secondary_stack:
                self._first = self._secondary_stack.top()                
                break
            elif self._primary_stack:
                while self._primary_stack:
                    self._secondary_stack.push(self._primary_stack.pop()) 
                    
            else:
                self._first = None
                
        return answer
                    
                    
            
    
    def enqueue(self, e):
        self._primary_stack.push(e)
        if self._first == None:
            self._first = e
   
    
if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    print(Q.dequeue())
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    print(Q.dequeue())
    Q.enqueue(8)
    Q.enqueue(9)
    print(Q.dequeue())
    Q.enqueue(10)
    Q.enqueue(20)
    Q.enqueue(30)
    Q.enqueue(40)
    print(len(Q))
    print(Q.dequeue( ))
    Q.enqueue(11)
    #### resizing. 
    Q.enqueue(12)
    Q.enqueue(13)
    Q.enqueue(14)
    Q.enqueue(15)
    print(Q.dequeue( ))
    print(Q.dequeue( ))
    Q.enqueue(7)
    Q.enqueue(9)
    print(Q.first())
    Q.enqueue(4)
    print(len(Q))
    print(Q.dequeue( ))
    Q.enqueue(12)
    Q.enqueue(13)
    Q.enqueue(14)
    Q.enqueue(15)
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    print(Q.first())
    print(len(Q))

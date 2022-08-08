#!/usr/bin/env python3


# double-ended Queue using two stacks. 
from Stack import ArrayStack

# add_first is O(1)
# add_last is O(n)
# delete_first is O(1)
# delete_last is O(n)

from Stack import Empty

class DoubleQueue:
    def __init__(self):
        self._primary_stack = ArrayStack() # To keep the data. 
        self._secondary_stack = ArrayStack() # To help primary stack in doing dequeue operation. 
        self._first = None
        self._last = None
        
    def __len__(self):
        return len(self._primary_stack) + len(self._secondary_stack)
        
    def is_empty(self):
        return len(self) == 0
        
    def first(self):
        if self._first==None:
            raise Empty("Queue is empty. ")
            
        return self._first
    
    def last(self):
        if self._last==None:
            raise Empty("Queue is empty. ")
            
        return self._last
    
    def add_first(self, e):
        self._primary_stack.push(e)
        if not self._first:
            
            self._first=e
            self._last=e
            
        else:
            self._first = e
            
    def add_last(self, e):
        while self._primary_stack:
            self._secondary_stack.push(self._primary_stack.pop())
        # Add last
        self._secondary_stack.push(e)
        # keep data back in primary. 
        while self._secondary_stack:
            self._primary_stack.push(self._secondary_stack.pop())
            
        if self._first==None:
            self._first=e
            self._last=e
            
        else:
            self._last = e
            
    def delete_first(self):
        if self._first==None:
            raise Empty("Queue is empty. ")
            
        # simply pop primary. 
        answer = self._primary_stack.pop()
        if self._primary_stack:
            self._first = self._primary_stack.top()
        else:
            self._first=None
            self._last=None
        return answer
                    
                    
    def delete_last(self):
        if self._last==None:
            raise Empty("Queue is empty. ")
            
        # traversing.             
        while self._primary_stack:
            self._secondary_stack.push(self._primary_stack.pop())
            
        # simply pop primary. 
        answer = self._secondary_stack.pop()
        if self._secondary_stack:
            self._last = self._secondary_stack.top()
        else:
            self._first=None
            self._last=None
        
        # keep data back in primary. 
        while self._secondary_stack:
            self._primary_stack.push(self._secondary_stack.pop())
        
        return answer
                    
                    
            
   
    
if __name__ == '__main__':
    D = DoubleQueue()
    D.add_first(1)
    D.add_first(2)
    D.delete_last()
    D.delete_last()
    print(D.first())
    print(D.last())
    print(len(D))

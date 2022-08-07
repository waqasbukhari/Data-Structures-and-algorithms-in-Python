from collections import deque 
from Stack import Empty

class Queue:
    def __init__(self):
        self._data = deque()
        
    def __len__(self):
        return len(self._data)
        
    def is_empty(self):
        return len(self) ==0
        
    def first(self):
        if not len(self):
            raise Empty("Queue is empty. ")
            
        return self._data[0]
        
    def dequeue(self):
        if not len(self):
            raise Empty("Queue is empty. ")
            
        return self._data.popleft()
        
    def enqueue(self, e):
        self._data.append(e)
    
if __name__ == "__main__":    
    pass 
    
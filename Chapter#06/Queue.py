from Stack import Empty

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    """ This class implements queue using Python list as an Adapter Pattern.

        Methods to implement for realizing Stack.
        i)  enqueue(e)
        ii) dequeue()

        Accessor methods.
        i)    first ~ return top element
        ii)   is_empty ~ returns True if the stack is empty.
        iii)  len ~ returns length of the Stack.

    """
    def __init__(self):
        self._capacity = ArrayQueue.DEFAULT_CAPACITY
        self._data = [None] * self._capacity
        self._size = 0
        self._front = 0 # current index where element has to be pushed. 
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0
        
    def first(self):
        if self._size == 0:
            raise Empty("Queue is empty. ")
            
        return self._data[self._front]
    
    def dequeue(self):
        if self._size == 0:
            raise Empty("Queue is empty. ")
            
        front = self._data[self._front]
        self._data[self._front] = None
        # In case self._frong was at index len(self._data) -1 then adding 1 would make it len(self._data)
        # which is beyond the indexes. so, to move it to 0, we use modulus operator. 
        
        self._front =  (self._front + 1) % self._capacity
        self._size -= 1
        
        return front
    
    def enqueue(self, e):
        if len(self) == self._capacity: 
            self._resize(2*self._capacity)
            
        idx = (self._front + self._size) % len(self._data)
        self._data[idx ] = e
        self._size += 1
        
    
    def _resize(self, capacity):
        
    
        B = [None] * capacity
        for i in range(self._size): 
            idx = (self._front + i ) % len(self)
            B[i] = self._data[idx]
            
        self._front = 0
        self._data = B
        self._capacity = capacity
        
        print(self._data    )
        
        
    
    
if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.dequeue()
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.dequeue()
    Q.enqueue(8)
    Q.enqueue(9)
    Q.dequeue()
    Q.enqueue(10)
    Q.enqueue(20)
    Q.enqueue(30)
    Q.enqueue(40)
    print(len(Q))
    print(Q._size)
    print(Q._front)
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
    print(Q._data)
    print(Q.first())
    Q.enqueue(4)
    print(len(Q))
    print(Q.dequeue( ))
    Q.enqueue(12)
    Q.enqueue(13)
    Q.enqueue(14)
    Q.enqueue(15)
    print(Q._front)
    print(Q._size)
    print(Q._data)
    Q.enqueue(1)
    Q.enqueue(2)
    print(Q._front)
    print(Q._size)
    print(Q._data)
    Q.enqueue(3)
    print(Q._front)
    print(Q._size)
    print(Q._data)
    print(ses)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    print(Q._data)
    print(Q.first())
    print(len(Q))

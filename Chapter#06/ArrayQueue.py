class Empty(Exception):
    pass
#C28
class Full(Exception):
    pass

class ArrayQueue:
    

    DEFAULT_CAPACITY = 10


    def __init__(self):
        self._data = [None] *ArrayQueue. DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):

        return self._size


    def is_empty():
        return self._size == 0

    def first(self):
        if self. is_empty:
            raise Empty('queue is empty')
        return self._data[self._front]


    def dequeue(self):

        if self.is_empty:
            raise Empty('queue is empty')
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (1+self._front)% (len(self._data))
        self._size -= 1

        return answer
    def __str__(self):

        return(str(self._data))

        
    def enqueue(self,e):
        #C28
        if self.size == maxlen:
            raise Full('queue is full')
            
        if self._size == len(self._data):
            self._resize (2 * len(self._data))
            
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1



    def _resize (self,cap):
        old = self._data
        self._data = [None] *cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)

        self._front = 0
        
    #C29
    def rotate():
        ele = self.dequeue(e)
        self.enqueue(ele)
        

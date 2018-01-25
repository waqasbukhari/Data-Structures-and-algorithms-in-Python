class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

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
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0 # Number of elements in the queue
        self._front = 0 # index of the first element that is to be removed

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)

        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize( 2*len(self._data))

        index = (self._front + self._size) % len(self._data)
        self._data[index] = e
        self._size += 1

    def _resize(self, new_capacity):
        B = [None] * new_capacity
        for idx in range(self._size):
            B[idx] = self._data[self._front]
            self._front = (self._front + 1) % len(self._data)

        self._data = B
        self._front = 0

    
    
if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(8)
    Q.enqueue(9)
    Q.enqueue(10)
    print(Q.dequeue( ))
    Q.enqueue(11)
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

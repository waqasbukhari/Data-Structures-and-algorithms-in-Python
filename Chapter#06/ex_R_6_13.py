class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

from collections import deque
class ArrayQueue:
    """ This class implements stack using deque as an Adapter Pattern.

        Methods to implement for realizing Stack.
        i)  enqueue(e)
        ii) dequeue()

        Accessor methods.
        i)    first ~ return top element
        ii)   is_empty ~ returns True if the stack is empty.
        iii)  len ~ returns length of the Stack.

    """

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        return self._data.popleft()
    
    def enqueue(self, e):
        self._data.append(e)


if __name__ == '__main__':
    D = deque()
    
    D.append(1)
    D.append(2)
    D.append(3)
    D.append(4)
    D.append(5)
    D.append(6)
    D.append(7)
    D.append(8)

    # 1 2 3 5 4 6 7 8

    Q = ArrayQueue()
    Q.enqueue(D.popleft())
    Q.enqueue(D.popleft())
    Q.enqueue(D.popleft())
    Q.enqueue(D[1])
    D.remove(D[1])
    Q.enqueue(D.popleft())
    Q.enqueue(D.popleft())
    Q.enqueue(D.popleft())
    Q.enqueue(D.popleft())
    print(Q._data)
    

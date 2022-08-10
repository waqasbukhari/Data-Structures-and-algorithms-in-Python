class Empty(Exception):
    pass

class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'  # it is a memory optimization tool.
        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None 
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        'return element to be dequeued, so, it is hea.d'
        if self.is_empty():
            raise Empty("list is empty. ")

        return self._head._element

    def dequeue(self):
        "dequeue from head. because you wouldn't be able to assign new head if you dequeue from tail since tail doesn't hold reference in a singly linked list. "
        'return element to be dequeued, so, it is hea.d'
        if self.is_empty():
            raise Empty("list is empty. ")

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

        return answer
        
    def enqueue(self, e):
        'enqueue from tail. '
        node = self._Node(e, None)
        if self.is_empty():
            self._head = node
        else:
            self._tail._next = node

        self._size += 1
        self._tail = node
        
    def rotate(self):
        if self.is_empty():
            raise Empty("list is empty. ")

        # it is enqueue(dequeue())
        # since the dequeue() is from head. 
        new_tail = self._head # save head as a node. 
        self._head = new_tail._next # assign next of head to be new head. 
        new_tail._next = None # since old head need to be tail, set its _next to None. 

        self._tail._next = new_tail # set _next of hte old tail to the old head
        self._tail = new_tail # set tail. 


if __name__ == '__main__':
    D = LinkedQueue()

    D.enqueue(1)
    D.enqueue(2)
    
    
    print(D._head,D._tail)
    print(D.dequeue())
    print(D._head,D._tail)
    print(D.dequeue())
    print(D._head,D._tail)
    
    

class Empty(Exception):
    pass

class CircularQueue:
    # implement queue wiht a circular linked list. 
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        # keep a reference to tail. because tail's next is head. 
        self._tail = None
        self._size =0 

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        'element to be dequeued is head'
        if self.is_empty():
            raise Empty("list is empty. ")

        return self._tail._next._element

    def dequeue(self):
        'element to be dequeued is head'
        if self.is_empty():
            raise Empty("list is empty. ")

        answer = self._tail._next._element
        self._size -= 1
        if self.is_empty():
            self._tail = None
        else:
            self._tail._next = self._tail._next._next

        return answer
    
    def enqueue(self, e):
        new_tail = self._Node(e, None)
        if self.is_empty():
            new_tail._next = new_tail # self._tail # head n tail are same and point to itself. 
        else:
            new_tail._next = self._tail._next
            self._tail._next = new_tail

        self._tail = new_tail
        self._size == 1

    def rotate(self):
        'it is enqueue(dequeue()) i.e., move tail to the head. '
        if self._size > 0:
            self._tail = self._tail._next

if __name__ == '__main__':
    D = CircularQueue()

    D.enqueue(1)
    D.enqueue(2)
    D.enqueue(3)
    
    
    print(D.dequeue())
    print(D.first())
    print(D.dequeue())
    
    

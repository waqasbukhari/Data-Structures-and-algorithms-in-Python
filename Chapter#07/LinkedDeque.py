class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation."""
    class _Node:
        __slots__ = '_element' , '_prev' , '_next' # streamline memory
        def __init__(self, element, prev, next): # initialize node’s fields
            self._element = element # user’s element
            self._prev = prev # previous node reference
            self._next = next # next node reference

    # MAIN METHODS
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer # trailer is after header
        self._trailer._prev = self._header # header is before trailer
        self._size = 0 # number of elements

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor) # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element # record deleted element
        node._prev = node._next = node._element = None # deprecate node
        return element # return deleted element

class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance
    """ Double-ended queue implementation based on a doubly linked list."""
    def first(self):
        if self.is_empty( ):
            raise Empty("Deque is empty")
        return self._header._next._element # real item just after header

    def last(self):
        if self.is_empty( ):
            raise Empty("Deque is empty")
        return self._trailer._prev._element # real item just before trailer

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next) # after header

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

    def delete_first(self):
        if self.is_empty( ):
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next) # use inherited method
    
    def delete_last(self):
        if self.is_empty( ):
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev) # use inherited method
    
    def print_all(self):
        first = self._header._next
        for i in range(len(self)):
            print(first._element)
            first = first._next
            
    def print_all2(self):
        last = self._trailer._prev
        for i in range(len(self)):
            print(last._element)
            last = last._prev
            
        
if __name__ == '__main__':
    D = LinkedDeque()
    D.insert_last(1)
    D.insert_last(2)
    D.insert_last(3)
    D.insert_last(4)
    D.insert_last(5)
    D.insert_last(6)
    D.insert_last(7)
    D.insert_last(8)
    D.insert_last(9)

    D.print_all()
    print('\n')
    print('\n')
    D.print_all2()

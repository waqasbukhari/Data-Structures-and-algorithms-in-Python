from copy import copy , deepcopy
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

    def find_middle(self):
        head = D._header
        tail = D._trailer

        while True:
            # In case of array with even numnber of elements
            if head._next is tail and tail._prev is head:
                return 'Middle elements are {},{}'.format(head._element,tail._element)
            # In case of array with odd numnber of elements
            if head._next is tail._prev:
                return 'Middle elements is {}'.format(head._next._element)
            head, tail = head._next, tail._prev


    def combine_lists(self, other):
        # Difference between shallow copy and deep copy
        
        # A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
        # A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

        # In this problem, shallow copy suffices since copying reference to the new varialbe suffice and we can make changes in the new variable
        # without affecting the old variables. However, it would affect the trailer of self. That can be problematic.
        # Therefore, make a deepcopy
        
        new_self = deepcopy(self)# .copy() # it just creats an alias of self. 
        last_node = new_self._trailer._prev        
        new_self._trailer = None

        first_node = other._header._next
        other._header = None

        last_node._next = first_node
        first_node._prev = last_node

        new_self._size = self._size + other._size

        return new_self
    
if __name__ == '__main__':
    D = LinkedDeque()
    
    D.insert_first(7)
    D.insert_first(6)
    D.insert_first(5)
    D.insert_first(4)
    D.insert_first(4)
    D.insert_first(3)
    D.insert_first(2)
    D.insert_first(1)
    
    print('\n')
    print('List 1')
    D.print_all()

    L = LinkedDeque()
    
    L.insert_first(15)
    L.insert_first(14)
    L.insert_first(13)
    L.insert_first(12)
    L.insert_first(11)
    L.insert_first(10)
    L.insert_first(9)
    L.insert_first(8)
    
    print('\n')
    print('List 2')
    L.print_all()


    new_D = D.combine_lists(L)

    
    print('\n')
    print('new list ')
    #L_n.print_all()
    new_D.print_all()


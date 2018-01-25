class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class LinkedQueue:
    """ This class implements Queue using singly linked list as an Adapter Pattern.

        Methods to implement for realizing Stack.
        i)  enqueue(e)
        ii) dequeue()

        Accessor methods.
        i)    first ~ return top element
        ii)   is_empty ~ returns True if the stack is empty.
        iii)  len ~ returns length of the Stack.

    """

    class _Node:
        """ Lightweight, nonpublic class to for storing a node in a singly linked list.
            Note that a node in a singly linked list contains an element and a reference to the next element.           
        """

        """ By default Python uses a dict to store an object’s instance attributes.
            This is really helpful as it allows setting arbitrary new attributes at runtime.
            There are classes whose attributes are fixed and there is no need for setting new attributes.
            In such a case, memory can be saved.

            __slots__ tells python interpreter that the list of attributes described here are the only attributes this class would ever need.
            Therefore, there is not need of a dynamic dictionary to manage references to other objects with
        """
        # 

        __slots__ = '_element', '_next'  # it is a memory optimization tool.
        def __init__(self, element, next):
            self._element = element
            self._next = next


    ###### Queue methods.            
    def __init__(self):
        self._head = None # we dequeue from head
        self._tail = None # we enqueue from head
        self._size = 0    # We maintain the size. 
        pass

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Except('Array is empty')
        return self._head._element

    # tail and head point to the same node if the linked list contains 1 element.
    

    def dequeue(self):
        if self.is_empty():
            raise Except('Array is empty')
        
        answer = self._head._element
        # node pointed by _next of the current _head becomes the _head. 
        self._head = self._head._next
        self._size -= 1

        # In case, the linked list has just one element then the tail reference is
        if self.is_empty():
            self._tail = None
        
        return answer
        
    def enqueue(self, e):
        node = self._Node(e, None)
        # If the array is initially empty. then enqueue would make the following changes.
        # _head and _tail pointer starts pointing to the same node

        # If the array was not empty, then _next of the existing _tail points to the added node
        # and then the _tail becomes the added node
        if self.is_empty(): 
            self._head = node
        else:
            self._tail._next = node
        self._tail = node

        self._size += 1

    def rotate(self):

        self._tail._next = self._head
        self._tail = self._head
        
        self._head = self._head._next

        
        self._tail._next = None


    def print_array(self):
        node = self._head
        while node is not None:
            print(node._element)
            node = node._next


if __name__ == '__main__':
    D = LinkedQueue()

    D.enqueue(1)
    D.enqueue(2)
    D.enqueue(3)
    D.enqueue(4)
    D.enqueue(5)
    D.enqueue(6)

    D.print_array()
    print('\n')
    D.rotate()
    print('\n')
    D.print_array()

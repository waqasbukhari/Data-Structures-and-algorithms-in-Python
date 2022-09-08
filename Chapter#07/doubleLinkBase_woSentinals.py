class Empty (Exception):
    pass

class Full (Exception):
    pass



class _DoublyLinkedWOSBase:
    class _Node:
        __slots__ = '_element','_prev', '_next'

        def __init__(self,element,prev, next):

            self._element = element

            self._prev = prev

            self._next = next

    def __init__(self):

        self.head = None

        self._size = 0


    def __len__ (self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def _insert_between(self,e,predecessor,successor):

        newest = self._Node(e,predecessor,successor)
        
        predecessor._next = newest
        
        successor._prev = newest
        
        self._size += 1

        return newest

    def _delete_node(self,node):
        
        predecessor = node._prev
        
        successor = node._next
        
        predecessor._next = node._next
        
        successor._prev = node.prev

        self._size -= 1

        element = node._element

        node._prev = node._next = node._element = None

        return element
    

    
    

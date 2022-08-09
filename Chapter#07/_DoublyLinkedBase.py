class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation. 

    """
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev

    ######### Methods for DoublyLinkedBase.

    def __init__(self):
         # create sentinels
        self._head = self._Node(None, None, None) # create sentinels
        self._tail = self._Node(None, self._head, None) # Initiall prev of tail points to head
        self._head._next = self._tail # Initiall next of head points to tail

        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0


    def _insert_between(self, e, preceeding_node, following_node):
        new_node = self._Node(e, following_node, preceeding_node)
        preceeding_node._next = new_node
        following_node._prev = new_node

        self._size += 1

        return new_node

        
    def _delete_node(self, node):
        preceeding_node = node._prev
        following_node = node._next

        preceeding_node._next, following_node._prev = following_node, preceeding_node
        self._size -= 1
        answer = node._element

        node._element = node._next = node._prev = None

        return answer
        
if __name__ == '__main__':
    D = _DoublyLinkedBase()

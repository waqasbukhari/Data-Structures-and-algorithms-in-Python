from _DoublyLinkedBase import _DoublyLinkedBase, Empty

class LinkedDeque(_DoublyLinkedBase):  # LinkedDeque is a subclass of _DoublyLinkedBase
    """ Double-ended queue implementation based on a doubly linked list
    """
    def first(self):
        if self.is_empty():
            raise Empty('The empty')
        return self._head._next._element

    def last(self):
        if self.is_empty():
            raise Empty('The empty')
        return self._tail._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._head, self._head._next)

    def insert_last(self,e):
        self._insert_between(e, self._tail._prev, self._tail)
    
    def delete_first(self):
        if self.is_empty():
            raise Empty('The empty')
        self._delete_node(self._head._next)
        pass

    def delete_last(self):
        if self.is_empty():
            raise Empty('The empty')
        self._delete_node(self._tail._prev)
        pass
    
    
        
if __name__ == '__main__':
    D = LinkedDeque()
    D.insert_first(1)
    D.insert_first(2)
    D.insert_first(3)
    D.insert_first(4)
    D.insert_last(5)
    D.insert_last(6)
    D.insert_last(7)
    

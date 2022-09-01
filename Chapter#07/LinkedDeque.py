from DoublyLinkedList import _DoublyLinkedBase

class LinkedDequeue(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty('Dequeueis Empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Dequeueis Empty')
        return self._trailer._prev._element

    def insert_first(self,e):

        self._insert_between(e, self._header.self._header._next)


    def insert_last(self,e):

        self._insert_between(e, self._trailer._prev,self._trailer)


    def delete_first(self):

        if self.is_empty():
            raise Empty('Dequeueis Empty')

        return self._delete_node(self._header._next)
    def delete_last(self):

        if self.is_empty():
            raise Empty('Dequeueis Empty')

        return self._delete_node(self._trailer._prev)

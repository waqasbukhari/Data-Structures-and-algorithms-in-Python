
"""
positional list ADT without sentinals
"""
from DoublyLinkedList_woSentinals import _DoublyLinkedWOSBase

class PositionalListWOS(_DoublyLinkedWOSBase):

    class Position:

        
        def __init__(self,container,node):

            self._container = container
            self._node = node

        def element(self):
            
            return self._node._element

        def __eq__(self,other):

            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):

            return not(self == other)

    def _validate(self,p):

        if not isinstance(p,self.Position):

            raise TypeError('p must be proper position type')

        if p._container is not self:
                
            raise ValueError('p is not contatined in this container')


        if p._node._next is None:

            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self,node):
            if self._size == 0:
                self._head = self.Position(self,node))

            return self.Position(self, node)


    def first(self):

        return self._make_position(self._head)


    def before(self,p):

        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):

        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):

        cursor = self.first()
        while cursor is not None:
            yield (cursor.element())
            cursor = self.after(cursor)
    #R15
    def reverse(self):

        cursor = self.last()

        while cursor is not None:
            yield (cursor.element())
            cursor = self.before(cursor)

    #C34

    def swap (self,p,q):
        node1 = self._validate(p)
        node2 = self._validate(q)

        node1prevold = self.node1._prev
        node1nextold = self.node1._next

        node2prevold = self.node2._prev
        node2nextold = self.node2._next

        self.node1._prev = node2prevold
        self.node1._next = node2nextold

        self.node2._prev = node1prevold
        self.node2._next = node1nextold

        return self

        



        
    def _insert_between(self,e,predecessor,successor):

        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        oldfirst = self._head

        return self._insert_between(e, self._head,oldfirst)
    
    

    def add_before(self,p,e):

        original = self._validate(p)
        
        return self._insert_between(e, original._prev,original)

    def add_after(self,p,e):

        original = self._validate(p)
        
        return self._insert_between(e, original,original._next)

    def delete(self,p):

        original = self._validate(p)

        return self._delete_node(original)

    def replace(self,p,e):

        original = self._validate(p)
        old_value = original._element
        original.element = e

        return old_value
    #R12
    def max_ele(self):
        max_element = 0
        for x in self:
            if x > max_element:
                max_element = x

        return max_element
    #R13 
    def find(self,e):

        for x in self:
            if x == e:
                return ('found first occurrence of ',e)
    
    #R17


    def move2front(self,p):

        if 1 <= p <= len(self):

            raise ValueError ('Illegal value of p')
        
        temp = PositionalList()
        for item in self:
            temp.add_last(item)

        for j in range(p):

            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value

            temp.delete(highPos)



            
    
    




    


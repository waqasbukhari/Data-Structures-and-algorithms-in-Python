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


class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access."""
    #-------------------------- nested Position class --------------------------
    class Position:
        """ An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            """ Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """ Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """ Return True if other does not represent the same location."""
            return not (self == other) # opposite of eq
    #-------------------------- End of nested Position class --------------------
    #------------------------------- utility method -------------------------------
    def _validate(self, p):
        """ Return position s node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None: # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    #------------------------------- utility method -------------------------------
    def _make_position(self, node):
        """ Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None # boundary violation
        else:
            return self.Position(self, node) # legitimate position

    #------------------------------- accessors -------------------------------
    def first(self):
        """ Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """ Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """ Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """ Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list."""
        cursor = self.first( )
        while cursor is not None:
            yield cursor.element( )
            cursor = self.after(cursor)

    #------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """ Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """" Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """ Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """ Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """ Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """ Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original) # inherited method returns element

    def replace(self, p, e):
        """ Replace the element at Position p with e.
            Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element # temporarily store old element
        original._element = e # replace with new element
        return old_value # return the old element value

    def max(self):
        if len(self) == 0:
            raise ValueError('The list is empty')

        max_element = None # first_position.element
        for element in self:
            if max_element is None or element > max_element:
                max_element = element
        return max_element

    def find(self, e):
        if len(self) == 0:
            raise ValueError('The list is empty')
        position = self.first()
        while position is not None:
            element = position.element()
            if element == e:
                return position
            position = self.after(position)
        


if __name__ == '__main__':
    D = PositionalList()
    D.add_first(1)
    D.add_first(2)
    D.add_first(3)
    D.add_first(4)
    D.add_first(28)
    D.add_first(11)
    D.add_first(4)
    D.add_last(5)
    D.add_last(6)
    D.add_last(7)

    # L.add_before(L.first(), e) would have to do the following.
    # i) L.first() returns a position
    # ii) L.add_before(L.first(), e) would convert position from L.first() back to the node.
    # iii) and then _insert_between() would be called.
    # whereas.
    # L.add_first(self, e) would avoid i) and ii) operations L.add_before(L.first(), e) and only iii) operation suffice.

    # similar argument holds for L.add_last(e) and L.add_after(L.last(), e)


    pos = D.find(28)
    print(pos.element())

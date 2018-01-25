class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """ Create an empty stack."""
        self._data = [ ] # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """ Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """ Add element e to the top of the stack."""
        self._data.append(e) # new item stored at end of list

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty("Stack is empty ")
        return self._data[-1] # the last item in the list

    def pop(self):
        """ Return (but do not remove) the element at the top of the stack.
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty("Stack is empty ")
        return self._data.pop( ) # remove last item from list

S = ArrayStack( ) # contents: [ ]
S.push(5) # contents: [5]
S.push(3) # contents: [5, 3]
print(len(S)) # contents: [5, 3]; outputs 2
print(S.pop( )) # contents: [5]; outputs 3

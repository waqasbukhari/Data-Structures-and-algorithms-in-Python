class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class Full(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class ArrayStack:
    """ This class implements stack using Python list as an Adapter Pattern.

        Methods to implement for realizing Stack.
        i)  push(e)
        ii) pop()

        Accessor methods.
        i)    top ~ return top element
        ii)   is_empty ~ returns True if the stack is empty.
        iii)  len ~ returns length of the Stack.

    """

    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        self._size = 0
        self._data = [None] * 0
        if self._maxlen:
            self._data = [None] * self._maxlen
            

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        ####
        # C-6.16        
        if len(self) == self._maxlen:
            raise Full("Stack capacity is full. ")
        ####
        if self._maxlen:
            self._data[self._size] = e
        else:
            self._data.append(e)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self._data[ - 1]

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")
            
        if self._maxlen:
            answer = self._data[-1]
            self._data[-1] = None
        else:
            answer = self._data.pop()
        self._size -= 1
        return answer

    

if __name__ == '__main__':

    S = ArrayStack( ) # contents: [ ]
    S.push(5) # contents: [5]
    S.push(3) # contents: [5, 3]
    print(len(S)) # contents: [5, 3]; outputs 2
    print(S.pop( )) # contents: [5]; outputs 3
    print(S.is_empty()) # contents: [5]; outputs False
    print(S.pop( )) # contents: [ ]; outputs 5
    print(S.is_empty()) # contents: [ ]; outputs True
    S.push(7) # contents: [7]
    S.push(9) # contents: [7, 9]
    print(S.top( )) # contents: [7, 9]; outputs 9
    S.push(4) # contents: [7, 9, 4]
    print(len(S)) # contents: [7, 9, 4]; outputs 3
    print(S.pop( )) # contents: [7, 9]; outputs 4
    S.push(6) # contents: [7, 9, 6]
    

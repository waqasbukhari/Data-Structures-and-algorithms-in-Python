class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class Full(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class ArrayStack:
    def __init__(self, maxlen):
        self._size = 0
        self._data = [None] * maxlen
        self._last_item_idx = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        if len(self) == len(self._data):
            self._data[self._last_item_idx] = None
            self._last_item_idx = (self._last_item_idx + 1) % len(self._data)
            self._size -= 1

        self._data[(self._last_item_idx + self._size) % len(self._data)] = e
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self._data[(self._last_item_idx + self._size -1) % len(self._data)]

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")

        answer = self._data[(self._last_item_idx + self._size - 1) % len(self._data)]
        self._data[(self._last_item_idx + self._size - 1) % len(self._data)] = None
        self._size -= 1
        return answer
    

if __name__ == '__main__':

    S = ArrayStack(4) # contents: [ ]
    S.push(5) # contents: [5]
    S.push(3) # contents: [5, 3]
    S.push(7) # contents: [7]
    S.push(9) # contents: [7, 9]
    S.push(11) # contents: [7, 9]
    print(S.top( )) # contents: [7, 9]; outputs 9
    S.push(4) # contents: [7, 9, 4]
    print(len(S)) # contents: [7, 9, 4]; outputs 3
    print(S.pop( )) # contents: [7, 9]; outputs 4
    S.push(6) # contents: 7, 9, 11, 6
    print(S.pop())
    print(S.pop())
    print(S.pop())
    print(S.pop())
    

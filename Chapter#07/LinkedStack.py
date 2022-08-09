class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class LinkedStack:

    class _Node:
        """ 
            __slots__ tells python interpreter that the list of attributes described here are the only attributes this class would ever need.
            Therefore, there is not need of a dynamic dictionary to manage references to other objects with
        """
        # 

        __slots__ = '_element', '_next'  # it is a memory optimization tool.
        def __init__(self, element, next):
            self._element = element
            self._next = next


    ###### Stack methods.            
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("list is empty. ")
        return self._head._element
        
    def pop(self):
        if self.is_empty():
            raise Empty("list is empty. ")

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        return answer
        


if __name__ == '__main__':
    D = LinkedStack()
    
    D.push(1)
    D.push(2)
    D.push(3)
    D.push(4)
    D.push(5)
    D.push(6)

    print(D.pop())
    print(D.pop())
    print(D.pop())
    print(D.pop())
    print(D.pop())
    print(D.pop())
    print(D.pop())



















    

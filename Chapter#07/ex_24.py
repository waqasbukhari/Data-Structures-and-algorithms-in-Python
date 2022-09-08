class Empty (Exception):
    pass

class Full (Exception):
    pass
class HeaderLinkedStack:
    class _node:
        __slots__ = 'element','next'
        def __init__(element,next):
            self._element = element
            self._next = next
    

    def __init__(self):

        self._header = self._node(None,None)
        self._header._next = None
        self._size = 0

    def is_empty(self):

        return self._size == 0


    def __len__(self):
        return self._size
        
    def push(self,e):

        self._header._next = self._node(e,None)
        self._size += 1

    def pop(self):

        if self._header._next == None:
            raise Empty('Stack in Empty')
        answer = self._header._next._element()
        newtop = self.header._next._next._element()
        self._header._next = newtop
        return answer
                

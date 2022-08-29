class Full(Exception):
    pass

class Empty (Exception):
    pass

class ArrayStack:
    def __init__(self, maxlen = None):
        

        #R16
        if not maxlen == None:
            self._capacity = maxlen
            
        else: self._capacity = 30


        
        self._data = [None] *maxlen


    def __len__(self):

        return len(self._data)

    def is_empty(self):

        return len(self._data)== 0


    def push(self,e):

        if self._len(self._data) == self._capacity:
            raise Full('stack is full')

        self._data.append(e)
        


    def top (self):

        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]


    def pop(self):

        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()
    

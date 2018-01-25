class Empty(Exception):
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

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self._data[ - 1]

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self._data.pop()

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    """ This class implements stack using Python list as an Adapter Pattern.

        Methods to implement for realizing Stack.
        i)  enqueue(e)
        ii) dequeue()

        Accessor methods.
        i)    first ~ return top element
        ii)   is_empty ~ returns True if the stack is empty.
        iii)  len ~ returns length of the Stack.

    """

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0 # Number of elements in the queue
        self._front = 0 # index of the first element that is to be removed

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)

        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize( 2*len(self._data))

        index = (self._front + self._size) % len(self._data)
        self._data[index] = e
        self._size += 1

    def _resize(self, new_capacity):
        B = [None] * new_capacity
        for idx in range(self._size):
            B[idx] = self._data[self._front]
            self._front = (self._front + 1) % len(self._data)

        self._data = B
        self._front = 0
    

def transfer(S, T):
    """ Transfer elements from stack S to stack T.
        such that the  top elements in S are the first ones to
        be pushed onto T.
    """

    for i in range(len(S)):
        element_S = S.pop() # extract the top element
        T.push(element_S) # push to the lowers

    return T

def rec_pop(S):
    """ This function recursively pops out the elements from S.
    """
    if S.is_empty():
        return
    print(S.pop())
    return rec_pop(S)

def list_reversal(lst):
    """ This function reverses the contents of lst
    """
    S = ArrayStack()
    for i in range(len(lst)):
        S.push(lst[i])
        

    lst = []
    while not S.is_empty():
        e = S.pop()
        lst.append(e)
        
    return lst        

if __name__ == '__main__':
    lst = list(range(20))
    print(list_reversal(lst))
    


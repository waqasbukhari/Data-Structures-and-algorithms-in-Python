import ctypes

class DynamicArray():
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._size

    def __getitem__(self, k):
        if not (0<= k < self._size):
            raise IndexError("Invalid index")

        return self._A[k]

    def append(self, e):
        if self._size == self._capacity:
            self._resize(2*self._capacity)

        self._A[self._size] = e
        self._size += 1
        
    def insert(self, k, value):
        "Insert value at index k. "
        if self._size == self._capacity:
            self._resize(2*self._capacity)
            
        for i in range(self._size-1, k-1, -1):
            self._A[i+1] = self._A[i]
            
        self._A[k] = value
        self._size += 1
        
    def remove(self, value):
        # remove first occurrence of the value. 
        for i in range(self._size):
            if self._A[i]==value:
                for j in range(i, self._size-1):
                    self._A[j] = self._A[j+1]
                self._size -= 1
                self._A[self._size] = None
                return
                
        raise ValueError('Value not found. ')
                
                
        

    def _resize(self, capacity):
        B = self._make_array(capacity)
        for i in range(self._size):
            B[i] = self._A[i]

        self._A = B
        self._capacity = 2*self._capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    A = DynamicArray()
    for i in range(10):
        A.append(i)
        
    A.insert(0,25)
    A.insert(5,25)
    A.remove(6)
    A.remove(9)
    A.remove(25)
    
    
    for a in A:
        print(a)

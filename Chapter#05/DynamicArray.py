import ctypes
class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_Array(self._capacity)


    def __len__(self):

        return self._n


    def __getitem__(self,k):

        #R04
        if -self._n <= k <0:
            k = k+self._n+1
        #R04
        return self._A[k]


    def append(self,obj):

        if self._n == self._capacity:
            self._resize(self._capacity+0.25*self._capacity)
            self._A[self._n] = obj
            self._n =+ 1

    def insert(self,k,val):

        if self._n == self._capacity:
            B = self._make_array((self._capacity+0.25*self._capacity))
        for i in range(0,k):
            B[i] = A[i]
        B[k] = val
        for j in range(k+1,self._n):
            B[j] = A[j-1]
        self._n += 1
        
    def remove_all(self,val):
        count = 0
        for i in range(len(self._A)):
            if self._A[i]==value:
                count += 1
        for i in range(len(data)-count+1):
            if self._A[i]==value: 
                del(self._A[i])
        self._n -= count
        
                
        
    def _resize(self,c):

        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):

        return (c*ctypes.py_object)()

    #R16
    def pop(self):
        self._A = self._A.pop()
        self._size -= 1
        if self._size <= self._capacity //4:
            self._resize(self._capacity // 2)




        

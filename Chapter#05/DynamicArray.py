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
            self._resize()

        self._A[self._size] = e
        self._size += 1

    def _resize(self):
        B = self._make_array(2 * self._capacity)
        self._capacity = len(B)
        for i in range(self._size):
            B[i] = self._A[i]

        self._A = B
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    A = DynamicArray()
    for i in range(10):
        print(len(A))

        A.append(i)

print(len(A))

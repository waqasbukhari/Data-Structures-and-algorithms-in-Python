#!/usr/bin/env python3

"""
Implement double-ended queue, ArrayDeque
"""
from Stack import Empty
class ArrayDeque:
    def __init__(self, maxlen):
        self._data = [None] * maxlen
        self._capacity = len(self._data)
        self._size = 0
        self._first_idx = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if not len(self):
            raise Empty("Deque is empty. ")

        return self._data[self._first_idx]

    def last(self):
        if not len(self):
            raise Empty("Deque is empty. ")

        return self._data[(self._first_idx + self._size - 1) % self._capacity]


    def add_first(self, e):
        if self._size == len(self._data): # no more elements can be added. so, delete one from the other end. 
            self.delete_last()

        self._first_idx = (self._first_idx - 1) % self._capacity
        self._data[self._first_idx] = e
        self._size += 1

    def delete_first(self):
        if not len(self):
            raise Empty("Deque is empty. ")
        self._data[self._first_idx] = None
        self._first_idx = (self._first_idx + 1) % self._capacity
        self._size -= 1


    def add_last(self, e):
        if self._size == len(self._data): # no more elements can be added. so, delete one from the other end. 
            self.delete_first()

        self._data[(self._first_idx + self._size) % self._capacity] = e
        self._size += 1
 
    def delete_last(self):
        if not len(self):
            raise Empty("Deque is empty. ")
        self._data[(self._first_idx + self._size - 1) % self._capacity] = None
        self._size -= 1




    def _resize(self, capacity): 
        B = [None] * capacity
        for i in range(self._first_idx, self._first_idx + self._size):
            B[i - self._first_idx] = self._data[i % len(self._data)]

        self._data = B
        self._capacity = capacity
        self._first_idx = 0


if __name__ == "__main__":
    D = ArrayDeque(5)
    D.add_first(1)
    D.add_last(2)
    D.add_last(3)  
    D.delete_first()
    D.add_last(4)
    D.add_last(5)  # 25 14 13 12 11 6 2 3 4 5 8
    D.add_first(6)
    D.add_first(7)
    D.add_last(8)
    D.add_last(9)
    D.add_last(10)
    D.delete_first()
    D.add_first(11)
    D.add_first(12)   # 14 13 12
    D.delete_last()
    D.add_first(13)
    D.add_first(14)
    D.delete_last()
    print(D.first())
    print(D.last())
    D.add_first(24)
    D.delete_last()
    D.delete_first()
    print(D.first())
    print(D.last())
    pass 

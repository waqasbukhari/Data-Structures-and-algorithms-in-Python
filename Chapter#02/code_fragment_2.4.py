#!/usr/bin/env python3

class Vector:
    def __init__(self, seq=[], dim=0):
        if seq:
            self._coords = list(seq)
            self._dim = len(seq)
        if dim and not seq:
            self._coords = [0] * dim
            self._dim = dim
            
    def __len__(self):
        return len(self._coords)
        
    def __getitem__(self, j):
        return self._coords[j]
        
    def __setitem__(self, j, val):
        self._coords[j] = val
            
    def __str__(self):
        str_representation = '<' + ', '.join([str(a) for a in self._coords]) + '>'
        return str_representation
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectos to be added should have equal length. ')
            
        c = Vector(self._coords)
        for i in range(len(self)):
            c[i] += other[i]   
            
        return c
        
    def __eq__(self, other):
    
        return self._coords == other._coords
    
        

if __name__ == '__main__':
    a = Vector([0,1,2,3, 8])
    print(a[2])
    a[2] = 5
    print(a[2])
    b = Vector(range(4,9))
    print(a)
    print(a+b)
    c = Vector(dim=2)
    print(c)
    # print(a+c)
    c = Vector([0,1,5,3, 8])
    print(a==c)
    print(a!=c)

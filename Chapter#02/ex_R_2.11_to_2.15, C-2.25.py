#!/usr/bin/env python3

"""
R-2.11 
We can check other in __add__(self, other), we can check instance type of other;
and if isinstance(other, Vector) is False, we can raise ValueError. 
"""
class Vector:
    def __init__(self, seq=[], dim=0):
        # R-2.15 - a constructor that adds in a sequence. 
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
        
    # R-2.12, we can use __mul__() to implement 3*v. 
    def __mul__(self, other):
        # R-2.14
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('Vectors should have same lenght. ')
            return sum([self._coords[i]*other._coords[i] for i in range(len(self))])
            
        c = Vector(self._coords)
        for j in range(len(c)):
            c[j] *= other
            
        return c
        
        
    # R-2.13, we can use __mul__() to implement 3*v. 
    def __rmul__(self, factor):
        c = Vector(self._coords)
        for j in range(len(c)):
            c[j] *= factor
            
        return c
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectos to be added should have equal length. ')
            
        c = Vector(self._coords)
        for i in range(len(self)):
            c[i] += other[i]   
            
        return c
    
    # R-2.11, we can use __radd__() to let list add to vector.     
    def __radd__(self, other):
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
    b = list(range(5))
    
    print(a)
     
    print(a+b) # Let u add vector to a list.  __add__
    print(b+a) # list cannot add to vector  __radd__
    print(a*3) # __mul__
    print(3*a) # __rmul__
    
    print(a*(a+b))

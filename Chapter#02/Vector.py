#!/usr/bin/env python3

class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._dim = d
            self._coords = [0] * d
        else:
            self._coords = list(d)
            self._dim = len(d)
            
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
    
    ####
    # R-2.9
    def __sub__(self, other): ## lets you use == operator
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self._coords[i] - other._coords[i]

        return result
    ####
        
    ####
    # R-2.10
    def __neg__(self): ## This special method let you use -inst 
        """Produce string representation of vector."""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = - self._coords[i]

        return result
    ####
    
    ####
    # R-2.12, we can use __mul__() to implement 3*v. 
    # C-2.25
    def __mul__(self, other):
        # R-2.14
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('Vectors should have same lenght. ')
            return sum([self._coords[i]*other._coords[i] for i in range(len(self))])
        # R-2.12
        c = Vector(self._coords)
        for j in range(len(c)):
            c[j] *= other
            
        return c
    ####

    ####
    # R-2.13, we can use __mul__() to implement 3*v. 
    def __rmul__(self, factor):
        c = Vector(self._coords)
        for j in range(len(c)):
            c[j] *= factor
            
        return c
    ####
        

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
    
    # Since a implements __len__ and __getitem__, it becomes an implicit iterator. 
    for ii in a:
        print(ii)

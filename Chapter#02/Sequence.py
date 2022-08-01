#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod # need these definitions

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
    """Return the length of the sequence."""
    
    @abstractmethod
    def __getitem__(self, j):
    """Return the element at index j of the sequence."""
    
    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val: # found match
            return True
        return False
        
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val: # leftmost match
                return j
        raise ValueError( value not in sequence ) # never found a match
        
    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val: # found a match
                k += 1
        return k
    ####
    # R-2.22    
    def __eq__(self, other):
        if len(self) == len(other):
            for a,b in zip(self, other):
                if a >= b:
                    return False
                    
        else:
            raise ValueError("Sequences to compare should have equal lengths. ")
            
        return True
    ####
        
    ####
    # R-2.23
    def __lt__(self, other):
        if len(self) == len(other):
            for a,b in zip(self, other):
                if a != b:
                    return False
                    
        else:
            raise ValueError("Sequences to compare should have equal lengths. ")
            
        return True
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

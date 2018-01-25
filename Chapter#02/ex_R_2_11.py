class Vector:
    """ Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """ Create d-dimensional vector of zeros. """
        self._coords = [0] * d

    def __len__(self): # This special method allows finding length of class instance using len(inst) style . 
        """ Return the dimension of the vector. """
        return len(self._coords)

    def __getitem__(self, j): ## This special method let you get the value using square bracket notation. like inst[j]
        """ Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val): ## This special method let you set the value using square bracket notation. like inst[j] = 10
        """ Set jth coordinate of vector to given value."""
        self._coords[j] = val

    ## offers a.__add__(b) and a is self and b is other.
    def __add__(self, other): ## lets you use + operator
        """ Return sum of two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result
            
    ## offers b.__add__(a) and a is self and b is other.
    def __radd__(self, other): ## lets you use + operator
        """ Return sum of two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result
            
    def __mul__(self, other): ## lets you use * operator
        """ Return sum of two vectors."""
        result = 0
        if len(self) == len(other): # relies on len method
            for j in range(len(self)):
                result += other[j] * self[j]
            return result

        elif isinstance(other, int):
            result = Vector(len(self)) # start with vector of zeros
            for j in range(len(self)):
                result[j] = factor * self[j]

            return result
            
    def __rmul__(self, factor): ## lets you use * operator
        """ Return sum of two vectors."""
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = factor * self[j]

        return result
            
##    def __add__(self, other): ## lets you use + operator
##        """ This class offers __len__ and __getitem__ methods and thus a default iteration is constructed
##            we can make an iterator out of an instance by iter(instance)
##            and can create a list since an instance of this class is an iterable.        
##        """
##        """ Return sum of two vectors."""
##        if len(self) != len(other): # relies on len method
##            raise ValueError("dimensions must agree")
##        
##        result = Vector(len(self)) # start with vector of zeros
##        self_list = list(self)
##        other_list = list(other)
##        
##        for j in range(len(self)):
##            result[j] = self_list[j] + other_list[j]
##            
##        return result

    def __eq__(self, other): ## lets you use == operator
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __sub__(self, other): ## lets you use == operator
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        
        """Return True if vector has same coordinates as other."""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self._coords[i] - other._coords[i]

        return result


            
    def __neg__(self): ## This special method let you use -inst 
        """Produce string representation of vector."""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = - self._coords[i]

        return result


    def __ne__(self, other): ## lets you use != operator
        """ Return True if vector differs from other."""
        return not self == other # rely on existing eq definition

    def __str__(self): ## This special method let you use print() function to print a representation of the class instance.
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation


if __name__ == '__main__':
    vec1 = Vector(3)
    vec1[0] = 10

    vec2 = Vector(3)
    vec2[1] = 10

    print(vec1 + [1,2,3])
    print([1,2,3] + vec1)
    
    print(vec1 * 5)
    print(5 * vec1)

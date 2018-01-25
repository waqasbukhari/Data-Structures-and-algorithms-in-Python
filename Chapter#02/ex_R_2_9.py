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

    def __add__(self, other): ## lets you use + operator
        """ Return sum of two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
            
        return result

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

    print(vec2)
    print(-vec2)

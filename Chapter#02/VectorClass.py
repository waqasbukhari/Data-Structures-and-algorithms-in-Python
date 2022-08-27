class Vector:
    def __init__(self,d):
        
        self._coords = [0]*d
        
    def __len__(self):
        
        return len(self._coords)
    
    def __getitem__(self,j):
        
        return self._coords[j]
    
    def __setitem__(self,j,val):
        
        self._coords[j] = val
        
    def __add__(self,other):
        
        if len(self)!=len(other):
            raise ValueError ('dimensions must agree')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self,other):
        
        return self._coords==other.coords

    def __ne__(self, other):
        
        return not self == other

    def __str__(self):
        
        return '<' +str(self._coords)[1:-1]+'>'
    #R09   
    def __sub__ (self,other):

        if len(self)!=len(other):

            raise ValueError ('dimensions must agree')

        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result
    #R10
    def __neg__(self):

        self._coords[j] = -1 * self._coords[j]

    #R12
    def __mul__ (self):
        for j in range(len(self)):
            self._coords[j] = self._coords[j] *3

    #R13

    def __rmul__ (self):
        for j in range(len(self)):
            self._coords[j] = 3*self._coords[j]

    #R22
    def __eq__(self,other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    #R23
    def __It__(self,other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        for i in range(len(self)):
            if self[i] < other[i]:
                return '1st seq is less than 2nd'
        return '2nd seq is less than 1st'

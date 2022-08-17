from abc import ABCMeta, abstractmethod
class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """ """
    @abstractmethod
    def __getitem__(self,j):
        """ """

    def __contains__(self,val):

        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def index(self,val):
        
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value is not in sequence')

    def count(self,val):

        k=0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    def __eq__(self,other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
    

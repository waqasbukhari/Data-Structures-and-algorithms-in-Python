from FavouritesList import FavouritesList

class FavouritesListMTF:

    def _move_up(self,p):

        if p != self._data.first():

            self._data.add_first(self._data.delete(p))


    def top(self,k):

        
        if 1 <= k <= len(self):

            raise ValueError ('Illegal value of k')

        temp = PositionalList()

        for item in self._data:

            temp.add_last(item)

        for j in range(k):

            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value

            temp.delete(highPos)
        

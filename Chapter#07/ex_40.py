class favouritesInFavouritesMTF(FavouritesList,FavouritesListMTF):

    def __init__(self, n):
        #n represents the how many turns you
        #consider before removing aan item from fav list
        self._favInfav = PositionalList()
        self._n = n


    def access(self,e):

        p = self._find_position(e)

        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)
        n += 1
        p = self._make_position(e)
        if p is None:
            p = self._favInfav.add_last(self._Item(e))
        if n == n:
            self._data = self._favInfav

        while self._favInfav not self.is_empty:
            self._favInfav.delete_first()
            

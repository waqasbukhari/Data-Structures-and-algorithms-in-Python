class Range:
    def __init__(self,start=0,stop=None,step=1):
        self._start = start
        self._stop = stop
        self._step = step
        self._lenlist = max(int(0, (stop-start+step-1)//step))
        self._k = -1

        def __len__(self):
            return self._length

        def __next__(self):
            self._k += 1
            if 0 <= k < self._lenlist:
                return self._start + (self._k*self._step)
                


        def __getitem__(self,k):
            if 0 <= k < self._lenlist:
                return self._start + (self._k*self._step)
            else:
                raise IndexError('index not in range')

        def __iter__(self):

            return self



            
        def __str__(self):
            return str(self.__class__)+ ": " + str(self.__dict__)



if __name__ == '__main__':
    print(Range(5,20,3))
    
    

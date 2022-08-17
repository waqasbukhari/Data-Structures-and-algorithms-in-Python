class ReverseSeqIterator:
    def __init__ (self, seq):

        self._seq = seq

        self._k = len(seq)

    def __next__(self):

        self._k -= 1
        if self._k >=0:
            return (self._seq(k))
        else:
            raise StopIteration()

    def __iter__ (self):

        return self




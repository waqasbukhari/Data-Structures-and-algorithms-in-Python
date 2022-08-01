#!/usr/bin/env python3

class SequenceIterator:
    def __init__(self, seq=[]):
        self._seq = seq
        self._item_to_return = len(self._seq) - 1
        
    def __next__(self):
        if self._item_to_return == -1:
            raise StopIteration()
            
        _tmp_item = self._seq[self._item_to_return]
        self._item_to_return -= 1
            
        return _tmp_item
        
    def __iter__(self):
        return self
        

if __name__ == '__main__':
    A = SequenceIterator([0,1,2,3, 8])
    for a in A:
        print(a)
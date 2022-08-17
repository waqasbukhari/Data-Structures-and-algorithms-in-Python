#!/usr/bin/env python3

import random
class Range:
    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        if len(args) == 2:
            start, stop, step = args[0], args[1], 1
        if len(args) == 3:
            start, stop, step = args[0], args[1], args[2]
            
        self._start = start
        self._stop = stop
        self._step = step
        self._item_to_return = start
        
    def __next__(self):
        
        if self._item_to_return >= self._stop:
            raise StopIteration()
            
        _tmp_item = self._item_to_return
        self._item_to_return += self._step
            
        return _tmp_item
        
        
    def __len__(self):
        start, stop, step = self._start, self._stop, self._step
        length = (stop - start - 1) // step + 1
        self._length = length
        
        return self._length
        
    def __iter__(self):
        return self
        
        
def test_range():        
    a = random.randint(0,100)
    b = random.randint(a, 100)
    try:
        c = random.randint(1, b-a)
    except: 
        return 
    print(a,b,c)
    B = range(a,b,c)
    C = Range(a,b,c)
    for a, b in zip(B, C):
        if a!=b:
            print(a,b,c)
            raise ValueError('there is an error. ')
        
    if len(B) != len(C):
        print(a,b,c)
        print(len(B), len(C))
        raise ValueError('Lengths are not equal.')
        
    return a,b,c
        
    
if __name__ == '__main__':
    for _ in range(10000):
        test_range()
        


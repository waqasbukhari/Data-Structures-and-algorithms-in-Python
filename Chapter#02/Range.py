# !/usr/bin/env python3

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
        
    def __contains__(self, val):
        """
        C-2.27. 
        An iterator implicitly implements __contains__ 
        but it has to run through all the values in a sequence. 
        So, it becomes O(n) operation. 
        
        Implement an efficient O(1) operation. 
        """    
        # Check if the val is within the range. 
        if self._start <= val < self._stop : 
            diff_from_start = val - self._start
            q,r = divmod(diff_from_start , self._step)
            if r==0: # meaning val is part of the Range. 
                return True
        
        else:
            return False # Even val is not within the range. 
        
        
        
        
        
        
        
        
def test_range():        
    a = random.randint(0,100)
    b = random.randint(a, 100)
    try:
        c = random.randint(1, b-a)
    except: 
        return 
    print(a,b,c)
    
    B = range(a,b,c) # built-in range
    C = Range(a,b,c) # defined range
    
    # Test elements of the range. 
    for e_A, e_B in zip(B, C):
        if random.randint(0,1): # check contains
            # An element is know to be in the range. 
            if e_A not in C:
                raise ValueError('Element no found but element is there. ')
                
            # element not known to be in the array. 
            tmp_element = random.randint(a,b-1)
            if ((tmp_element in B) ^ (tmp_element in C)):
                print(a,b,c)
                raise ValueError("__contains__ implementation is wrong. ")
            
        if e_A!=e_B:
            print(a,b,c)
            raise ValueError('there is an error. ')
        
    # Test length
    if len(B) != len(C):
        print(a,b,c)
        print(len(B), len(C))
        raise ValueError('Lengths are not equal.')
        
    return a,b,c
        
    
if __name__ == '__main__':

    for _ in range(10000):
        test_range()

# !/usr/bin/env python3

from Range import Range
       
        
        
        
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

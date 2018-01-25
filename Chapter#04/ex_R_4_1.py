import time
from random import shuffle

def find_max(S):
    len_sq = len(S)
    if len_sq == 1:
        return S[0],S[0]

    mid_pt = len_sq // 2

    low_max = find_max(S[:mid_pt])
    up_max = find_max(S[mid_pt:])
    
    def combiner(a, b):
        max_ele = a[0] if a[0] >=b[0] else b[0]
        min_ele = a[1] if a[1] <=b[1] else b[1]
        
        return max_ele, min_ele
    
    return combiner(low_max, up_max)

def find_max_nonrec(S):
    max_element, min_element = S[0],S[0]
    type(max_element)
    for s in S:
        if s > max_element:
            max_element = s
        if s < min_element:
            min_element = s

    return max_element, min_element
            

if __name__ == '__main__':

    S = list(range(100000))
    shuffle(S)
    
    t = time.time()    
    print(find_max(S))
    print(time.time() - t)
    
    t = time.time()    
    print(find_max_nonrec(S))
    print(time.time() - t)
    

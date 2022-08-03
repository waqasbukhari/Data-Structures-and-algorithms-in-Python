#!/usr/bin/env python3


def rearrange(seq):
    h = even_first(seq)
    return h[0] + h[1]
    
def even_first(seq):
    # print(seq)
    if len(seq) == 1:
        print([seq[0]],[] if seq[0]%2==0 else [],[seq[0]])
        return [seq[0]],[] if seq[0]%2==0 else [],[seq[0]]
        
    mid_pt = len(seq) // 2        
    h1 = even_first(seq[:mid_pt])
    h2 = even_first(seq[mid_pt:])
    
    h = h1[0] + h2[0], h1[1] + h2[1]
    
    return h
    
    
if __name__ == "__main__":
    a = list(range(15))
    print(rearrange(a))

import time
from random import shuffle

# ex-C-4.9
def find_max(S):
    len_sq = len(S)
    
    if len(S) ==0 :
        return
    if len(S) == 1:
        return S[0]

    mid_pt = len_sq // 2

    low_max = find_max(S[:mid_pt])
    up_max = find_max(S[mid_pt:])
    
    seq_max = low_max if low_max > up_max else up_max
    
    return seq_max
    
def find_max_nonrec(S):
    seq_max = -float("inf")
    for s in S:
        seq_max = seq_max if s<seq_max else s
        
        
    return seq_max
        







if __name__ == '__main__':

    S = list(range(10000000))
    shuffle(S)
    
    t = time.time()    
    rec_max = find_max(S)
    print(time.time() - t)
    
    t = time.time()    
    nonrec_max = find_max_nonrec(S)
    print(time.time() - t)
    
    if rec_max != nonrec_max:
        raise ValueError("Results of the functions are different. ")
    

from time import time
from random import shuffle

def element_uniqueness(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):

            if seq[i] == seq[j]:
                return False

    return True

##def element_uniqueness_recur(seq):
##    len_seq = len(seq)
##    half_len_seq = len_seq // 2
##
##    left_seq = seq[:half_len_seq]
##    right_seq = seq[half_len_seq:]
##
##    def cross_element_uniqueness(seq1, seq2):
##        """ This function finds if an element in seq1 is in seq2.          
##        """
##
##        for el_seq1 in seq1:
##            for el_seq2 in seq2:
##                if el_seq1 == el_seq2:
##                    return False
##
##        return True
##                
##
##
##    res1 = element_uniqueness(left_seq)
##    if not res1:
##        return False        
##    res2 = cross_element_uniqueness(left_seq, right_seq)
##    if not res2:
##        return False
##    res3 = cross_element_uniqueness(right_seq, left_seq)
##    if not res3:
##        return False
##    res4 = element_uniqueness(right_seq)
##    if not res4:
##        return False
##
##    return True

def element_uniqueness_recur(seq):
    len_seq = len(seq)
    if len_seq == 1:
        return seq#[0]
    
    half_len_seq = len_seq // 2

    left_seq = element_uniqueness_recur(seq[:half_len_seq])
    right_seq = element_uniqueness_recur(seq[half_len_seq:])

    if bool(left_seq) + bool(right_seq) < 2:
        return False


    for el_seq1 in left_seq:
        for el_seq2 in right_seq:
            if el_seq1 == el_seq2:
                return False
            
    return left_seq + right_seq
            

    
if __name__ == '__main__':
    seq = list(range(10800))
    shuffle(seq)
    # seq += [1]

    t= time()
    print(element_uniqueness(seq))
    print(time() - t)
    
    t= time()
    print(bool(element_uniqueness_recur(seq)))
    print(time() - t)
    

#!/usr/bin/env python3

def seq_reverse(seq):
    """ This function takes in a squence
    and returns another sequence with opposite order  """
    # This function makes another sequence and populates taht. 
    seq = seq.copy() # make a local copy. 
    sec_seq = []
    while seq:
        last_item = seq.pop()
        sec_seq.append(last_item)
    return sec_seq

def seq_reverse_inplace(seq):
    # This function reverses a sequence inplace
    seq = seq.copy() # make a local copy.
    
    seq2 = [seq[-(i+1)] for i in range(len(seq))]

    

    print('dfd',seq)
    print('second seq',seq2)
    return seq2

if __name__ == '__main__':

    lst_numbers = list(range(10))
    print("another array", seq_reverse(lst_numbers))
    print("inplace ", seq_reverse_inplace(lst_numbers))
    # print(lst_numbers.reverse())
    # print(lst_numbers)

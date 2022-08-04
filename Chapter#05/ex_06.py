#!/usr/bin/env python3

def find_repeated(seq):
    """
    there are 1 to n-1 elements with exactly 1 repeated. 
    summation over the entire sequence minus the summation from 1 to n-1 would reveal the repeated number. 
    sum from 1 to n-1 is (n-1)(n-2)/2
    """
    n = len(seq)
    sum_1_n_ = 0.5 * (n-1) * (n-2)
    return int(sum(seq) - sum_1_n_)
    
if __name__ == "__main__":
    a = list(range(22)) + [7]
    print(find_repeated(a))
    a = list(range(205)) + [25]
    print(find_repeated(a))
    a = list(range(105)) + [30]
    print(find_repeated(a))
    a = list(range(225)) + [75]
    print(find_repeated(a))
    
#!/usr/bin/env python3

# from binary_search import binary_search as bs

def binary_search(data, target, low=None, high=None):
    """
    code fragment 4.3
    """
    if low is None:
        low =0
        high = len(data) - 1
    # # base case
    if low > high:
        return -1
    else:
        mid = (low+high) //2
        if target ==data[mid]:
            return mid
        elif target<data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


def find_pair(seq, k):
    for s in seq:
        idx = binary_search(seq, k-s)
        if idx>-1:
            return s, seq[idx]
        
    
if __name__ == "__main__":
    s = list(range(50))
    print(find_pair(s, 87))

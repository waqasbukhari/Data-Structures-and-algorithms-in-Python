#!/usr/bin/env python3

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

    
if __name__ == "__main__":
    print()

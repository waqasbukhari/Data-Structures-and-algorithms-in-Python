#!/usr/bin/env python3

# nonrecursive version of code fragment 4.12. power(x,n) with log n

def power(x,n):
    """
    code fragment 4.3
    """
    traces = []
    while n != 0: 
        n, r = divmod(n, 2)
        traces.append(r)

    value = 1
    while traces:
        e = traces.pop()
        value = value ** 2  
        value = value if e==0 else x*value

    return value

    
if __name__ == "__main__":
    print(power(8,4))

#!/usr/bin/env python3

def int_log_rec(n, base = 2):
    if n < base:
        return 0
    else:
        return 1 + int_log_rec(n // base, base)
    
if __name__ == '__main__':
    value = 17; base = 2

    print(int_log(value, base))

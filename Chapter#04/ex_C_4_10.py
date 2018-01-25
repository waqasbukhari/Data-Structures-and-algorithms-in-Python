from time import time
def int_log(n, base = 2):
    b = 0
    while n >= base:
        n /= base
        b += 1
    return b

def int_log_rec(n, base = 2):
    if n < base:
        return 0
    else:
        return 1 + int_log_rec(n / base, base)
    
if __name__ == '__main__':
    value = 1028; base = 2

    t= time()
    print(int_log(value, base))
    print(time() - t)
    
    t= time()
    print(int_log_rec(value, base))
    print(time() - t)

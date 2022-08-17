import sys
sys.setrecursionlimit(100000)

def harmonic_num(n):
    if n==1:
        return 1
    
    return 1/n + harmonic_num(n-1)
    
if __name__ == '__main__':

    print(harmonic_num(1))    
    print(harmonic_num(2))
    print(harmonic_num(3))
    print(harmonic_num(4))
    print(harmonic_num(5))
    print(harmonic_num(6))
    print(harmonic_num(7))
    print(harmonic_num(8))
    print(harmonic_num(1000))
    
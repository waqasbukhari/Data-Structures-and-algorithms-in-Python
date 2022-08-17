import sys
sys.setrecursionlimit(100000)

def string2int(S, base = 0):
    if len(S) == 0:
        return 0
    if len(S) == 1:
        return int(S[-1]) * 10 ** base
        
    return int(S[-1]) * 10 ** base + string2int(S[:-1], base+1)
    
if __name__ == '__main__':
    print(string2int('12345'))
    print(string2int('2345'))
    print(string2int('454926'))
    print(string2int('123412585'))
    print(string2int('8769542'))
    print(string2int('598267'))
    print(string2int('4573951'))
    
import time
def find_max(S):
    len_sq = len(S)
    if len_sq == 1:
        return S[0]

    mid_pt = len_sq // 2

    low_max = find_max(S[:mid_pt])
    up_max = find_max(S[mid_pt:])
    
    def combiner(a, b):
        return a if a >=b else b
    
    return combiner(low_max, up_max)

def find_max_nonrec(S):
    max_element = S[0]
    for s in S:
        if s > max_element:
            max_element = s

    return max_element
            

if __name__ == '__main__':

    t = time.time()    
    S = [1,2,3,4,5,6,8]
    print(find_max(S))
    print(time.time() - t)
    
    t = time.time()    
    S = [1,2,3,4,5,6,8]
    print(find_max_nonrec(S))
    print(time.time() - t)
    

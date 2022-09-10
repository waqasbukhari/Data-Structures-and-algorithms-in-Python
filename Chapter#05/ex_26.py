

     
def findmissing(Arr):
    n = max(Arr)+1
    res = [None]* n
    for j in range (n):
        for i in Arr:
            res[i] = i
    missing = []
    for k in range(len(res)):
        if res[k] == None:
            missing.append(k)
    
    return missing

if __name__ == '__main__':
    Arr = [1,3,5,6,7,9,11,13,14,15,16,17,18,19,20]
    result = findmissing(Arr)
    print(result)


def lostFound(seq):
    result = 0
    for i in range(len(seq)):
        result = result ^ seq[i]
    return result
                
if __name__ == "__main__":
    s2 = [0,2,3]
    print(s2)
    print((lostFound(s2)))

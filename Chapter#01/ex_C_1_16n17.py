#!/usr/bin/env python3
def scale_idx(data, factor):
    for j in range(len(data)):
        data[j] *= factor

def scale_val(data, factor):
    for val in data:
        val *= factor

if __name__ == '__main__':
    data = list(range(5))
    scale_idx(data, 10)
    print(data)
    
    data = list(range(5))
    scale_val(data, 10)

    print(data)
    
        

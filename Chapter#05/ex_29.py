#!/usr/bin/env python3
"""
"""

def natural_join(A, B):
    dict_a = {y:x for x,y in A}
    dict_b = {y:z for y,z in B}

    dict_join = []
    for y in dict_a.keys():
        if y in dict_b:
            tmp = (dict_a[y], y, dict_b[y])
            dict_join.append(tmp)

    return dict_join

if __name__ == "__main__":
    A = [(1,1),(2,2),(3,3),(4,4)]
    B = [(1,5),(2,6),(3,73),(4,8),(5,9)]

    print(natural_join(A, B))

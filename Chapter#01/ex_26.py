#!/usr/bin/env python3
import sys
def numb_vowels(in_str):
    vowel_list = set(['a','e','i','o','u'])
    
    count = 0    
    for ch in list(in_str):
        if ch in vowel_list:
            count += 1

    return count

def numb_vowels_list(in_str):
    vowel_list = ['a','e','i','o','u']
    
    count = 0    
    for ch in list(in_str):
        if ch in vowel_list:
            count += 1

    return count

if __name__ =='__main__':
    numbers = sys.stdin.read()
    a,b,c = numbers.split()
    a,b,c = int(a), int(b), int(c)
    if a + b == c:
        print('{} + {} = {}'.format(a,b,c))
    if a == b - c:
        print('{} = {} - {}'.format(a,b,c))
    if a * b == c:
        print('{} * {} = {}'.format(a,b,c))

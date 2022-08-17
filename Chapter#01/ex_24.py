#!/usr/bin/env python3
import sys
import time
    

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
    t1 = time.time()
    print(numb_vowels('how are you. I am good'))
    print(time.time() - t1)
    
    t2 = time.time()
    print(numb_vowels_list('how are you. I am good'))
    print(time.time() - t2)
    

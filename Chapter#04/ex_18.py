#!/usr/bin/env python3

VOWELS = set(list('aeiou'))

def more_vowels(string):
    more_vowels = more_vowels_than_consonants(string)
    print(more_vowels)
    return True if more_vowels > 0 else False

def more_vowels_than_consonants(string):
    if len(string) == 0:
        return 0
        
    if len(string) ==1:
        return 1 if string in VOWELS else -1
        
    mid_pt = len(string) // 2
        
    more_vowels_1 = more_vowels_than_consonants(string[:mid_pt])
    more_vowels_2 = more_vowels_than_consonants(string[mid_pt:])
    
    return more_vowels_1 + more_vowels_2
    
        
    
if __name__ == "__main__":
    a = 'abacus'
    print(more_vowels(a))
    a = 'palindrome'
    print(more_vowels(a))
    a = 'racecar'
    print(more_vowels(a))
    a = 'gohangasalamiimalasagnahog'
    print(more_vowels(a))
    a = 'aeiou'
    print(more_vowels(a))

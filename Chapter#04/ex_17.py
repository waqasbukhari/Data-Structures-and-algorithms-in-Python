#!/usr/bin/env python3

def is_palindrome(string):
    if len(string) < 2:
        return True
        
    if string[0] != string[-1]:
        return False
        
    return is_palindrome(string[1:-1])
    
if __name__ == "__main__":
    a = 'abacus'
    print(is_palindrome(a))
    a = 'palindrome'
    print(is_palindrome(a))
    a = 'racecar'
    print(is_palindrome(a))
    a = 'gohangasalamiimalasagnahog'
    print(is_palindrome(a))

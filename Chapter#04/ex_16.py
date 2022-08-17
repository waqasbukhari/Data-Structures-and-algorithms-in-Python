#!/usr/bin/env python3

def reverse(string):
    if len(string) < 2:
        return string
        
    mid_point = len(string) // 2
    
    # reverse first half
    reverse_1 = reverse(string[:mid_point])
    # reverse first half
    reverse_2 = reverse(string[mid_point:])
    # combine
    string = reverse_2 + reverse_1
    return string
    
if __name__ == "__main__":
    a = 'abacus'
    print(reverse(a))
    a = 'palindrome'
    print(reverse(a))

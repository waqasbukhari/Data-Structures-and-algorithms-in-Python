'''
let n be the total elements to be added to the list

A = []
n = number of elements to be appended
n append operations take O(n) time
n pop operations also take O(n) time
after every n/4 decrease in elements 1 resize operation
also takes place which make total of 4 operations
total time = n+n+4
           = 2n+4
So this takes O(n) time

'''

#!/usr/bin/env python3


##my_list = []
##for i in range(10):
##    numb = 2*i if len(my_list) == 0 else 2*i + my_list[i-1]
##    my_list.append(numb)
##
##print(my_list)
##        
##        
    
my_list = [2*sum(list(range(i+1))) for i in range(10)]
print(my_list)

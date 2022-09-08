"""
lets assume the initial capacity is c for a dynamic array
and also there is arithmatic increase of 10 at every over flow.
which means that after every 10 append operations there is a copy
operation that grows as follows

at 1st overflow there is a copy operation of cost   -> c
at 2nd overflow there is a copy operation of cost   ->  2c
                                                        (c+c = 2c elements)

at 3rd overflow there is a copy operation of cost   -> 3c
                                                        2c+c = 3c elements

.
.
.
.
.
.
at nth overflow there is a copy operation of cost   -> nc
                                                        (n-1)c+c = nc elements

                                                        
this pattern gives birth to the following:

    c+c append operations+2c+ c append operations +3c+ c append operations
    4c+c append operations+5c+c append operations+....+nc = c((n(n+1))/2)

    c+c+2c+c+3c+c+4c+....+c+nc = nc+(c((n^2 + n)/2))
                         = c((n^2 + n)/2)+nc
                         = c/2(n^2 + n)+nc
                         = c(n^2)/2 +cn +cn
                         = c(n^2)/2 + 2cn
                         = O(n^2) runtime
"""




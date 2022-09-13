#R08
"""
total 32 enque operations    -> 32 elements added
10 first operations          -> checking 1st element doesnt increase/decrease size
15 deque operations,5 go waste if all were during dequeue
                             -> 32-10 = 22 elements at the end

if 5 empty errors were during first operations then final length will be
                            -> 32-15 = 17 elements

So the final length of queue will be between 17 and 22
                            

"""



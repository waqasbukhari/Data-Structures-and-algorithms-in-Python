from Stack import ArrayStack
from random import randint
"""
Implemented in Stack,
changes enclosed within comments, specifying to be part of C-6.17
"""


if __name__ == "__main__":
    S = ArrayStack(100)
    for _ in range(500):
        print(_)
        a = randint(0,4)
        if a==0: # 20% prob of pop. 
            S.pop()
        else:
            S.push(randint(1,50))
            
            

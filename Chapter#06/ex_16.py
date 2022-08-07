from Stack import ArrayStack

"""
Implemented in Stack,
changes enclosed within comments, specifying to be part of C-6.16
"""


if __name__ == "__main__":
    S = ArrayStack(5)
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.push(5)
    S.push(6) # It will throw Full exception. 

from Stack import ArrayStack
from random import randint

def largest():
    S = ArrayStack()
    numbers = [randint(0,1500) for _ in range(3)]
    [S.push(c) for c in numbers]
    
    correct = max(numbers)
    x = S.pop() 
    x = x if x>S.top() else S.top()
    
    return x==correct
    
    
def experiment():
    REP = 20000
    return sum([largest() for _ in range(REP)]) / REP


if __name__ == "__main__":
    print(experiment())
#!/usr/bin/env python3

from Stack import ArrayStack


def eval_postfix(elements):
    # push all to a Stack. 
    S1 = ArrayStack()
    [S1.push(e) for e in elements]
    
    S2 = ArrayStack()
    
    while S1: # as long as there are elements in S1.
        e = S1.pop()
        if e in list('+-*/'):
            S2.push(e)
            print(e)
        else: # a number. 
            # if top in S1 is a number and top in S2 is an operator.
            if S1 and (S1.top() not in list('+-*/')) and (S2.top() in list('+-*/')): # next is a number. 
                e2 = S1.pop() # pull the next number. 
                op = S2.pop() # pull the operator from S2
                result = eval(e2+op+e)
                if not S2 and not S1:
                    return result
                S2.push(str(result))
                print(result)
            else: # but the next is an operator. 
                S2.push(e)
                print(e)
                
        if not S1:
            if len(S2) < 3:
                raise ValueError('expression is not correct')
            while S2:
                S1.push(S2.pop())
                
            


if __name__ == "__main__":
    elements = "5 2 + 8 3 - * 4 / 2 / 8 *".split()
    elements = "5 2 8 3 - * 4 1 2 3 4 6 6 / 8 2 / 8 * + - - - * + + +".split()
    elements = "10 +".split()
    elements = "5 2 + 8 3 - * 4 + 1 2 3 4 6 6 / 8 2 / 8 * + - - - + + +".split()
    print(eval_postfix(elements))

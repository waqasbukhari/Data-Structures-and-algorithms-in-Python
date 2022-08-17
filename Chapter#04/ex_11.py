from time import time
from random import shuffle


def are_elements_unique(S):
    # base case. 
    if len(S) <= 1:
        return True
        
    # first n-1 elements are unique.
    first_result = are_elements_unique(S[:-1])
    # last n-1 elements are unique.
    second_result = are_elements_unique(S[1:])
    # Ensure first and last elements are different
    third_result = S[0] != S[-1]
    
    return first_result and second_result and third_result
    
def are_elements_unique_savings(S, results={}):
    # Check if the result is already computed. 
    str_repr = S.__str__()
    if str_repr in results:
        return results[str_repr]
        
    # base case. 
    if len(S) <= 1:
        return True
        
    # first n-1 elements are unique.
    first_result = are_elements_unique_savings(S[:-1])
    results[S[:-1].__str__()] = first_result
    # last n-1 elements are unique.
    second_result = are_elements_unique_savings(S[1:])
    results[S[1:].__str__()] = second_result
    # Ensure first and last elements are different
    third_result = S[0] != S[-1]
    
    return first_result and second_result and third_result
    

    
if __name__ == '__main__':

    seq = list(range(26))
    shuffle(seq)

    t= time()
    print(are_elements_unique(seq))
    print(time() - t)
    
    t= time()
    print(bool(are_elements_unique_savings(seq)))
    print(time() - t)
    

from time import sleep

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
    
if __name__ == "__main__":
    S = list('abccde')
    print(are_elements_unique(S))
    S = list('a')
    print(are_elements_unique(S))
    S = list('abcdefghijklmnopqrstuvwxyz')
    print(are_elements_unique(S))
    S = []
    print(are_elements_unique(S))
    

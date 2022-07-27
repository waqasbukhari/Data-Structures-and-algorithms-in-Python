def reverse(S):
    # base case
    if len(S) <= 1:
        return S
        
    mid_pt = len(S) // 2
    reverse_first_half = reverse(S[:mid_pt])
    reverse_second_half = reverse(S[mid_pt:])
    
    return reverse_second_half + reverse_first_half
    



if __name__ == "__main__":
    S = list(range(10))
    print(reverse(S))
    S = list(range(1))
    print(reverse(S))
    S = list(range(2))
    print(reverse(S))
    S = list(range(100))
    print(reverse(S))
    S = list(range(0))
    print(reverse(S))

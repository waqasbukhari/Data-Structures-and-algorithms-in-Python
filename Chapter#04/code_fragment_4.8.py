def bad_fibonacci(n):
    # base case
    if n<=1:
        return n
        
    return bad_fibonacci(n-1) + bad_fibonacci(n-2) 
    
    
    
def fibonacci(n):
    result = good_fibonacci(n)
    return result[0]
    
    
def good_fibonacci(n):
    if n<=1:
        return n,0
        
    prev_result = good_fibonacci(n-1)
    result = prev_result[0] + prev_result[1]
    
    return result, prev_result[0]
if __name__ == "__main__":
    n = 4
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 5
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 6
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 7
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 8
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 9
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 10
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 11
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))
    n = 12
    print(n, fibonacci(n))
    print(n, bad_fibonacci(n))

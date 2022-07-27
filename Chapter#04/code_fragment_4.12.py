def power(x, n):
    # base case
    if n == 0:
        return 1
        
    q, r = divmod(n, 2)
    
    half_power = power(x, q)
    
    return (x ** r) * (half_power ** 2)

if __name__ == "__main__":
    x ,n = 5,4
    print(power(x, n))

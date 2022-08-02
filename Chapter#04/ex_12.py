def product(m,n):
    if m==1 or n==1:
        return m if n==1 else n
    if m==0 or n==0:
        return 0
        
    return m + product(m, n-1) if n<=m else n + product(m-1, n)
        
if __name__ == '__main__':
    m, n = 289,50
    print(product(m,n))
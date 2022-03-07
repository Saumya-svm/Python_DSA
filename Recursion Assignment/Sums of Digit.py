def sumofdigits(n):
    if n==0:
        return 0
    add=n%10
    n=(n-add)/10
    s=sumofdigits(n)
    return add+s
    
    
n=int(input())
print(int(sumofdigits(n)))
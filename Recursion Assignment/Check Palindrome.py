def is_palindrome(a,ns,si):
    if si>=len(a):
        return ""
    
    ns=is_palindrome(a,ns,si+1)
    if ns+a[si]==a and si==0:
        return 'true'
    elif si==0 and ns+a[si]!=a:
        return 'false'
    return ns+a[si]

s=input()
print(is_palindrome(s,"",0))
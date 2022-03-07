def geosum(n):
    if n==0:
        return 1
    s=geosum(n-1)
    return (1)/(2**n)+s


n=int(input())
sum=geosum(n)
print("%.5f"%sum)
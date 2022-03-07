def towerofhanoi(n,src,helper,des):
    if n==1:
        print(src+" "+des)
        return
    towerofhanoi(n-1,src,des,helper)
    print(src+" "+des)
    towerofhanoi(n-1,helper,src,des)

n=int(input())
towerofhanoi(n,'a','b','c')
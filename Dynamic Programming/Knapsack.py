def knapsack(weights,values,weight,n,i=0):
    if i==n:
        return 0
    if weights[i]>weight:
        ans = knapsack(weights,values,weight,n,i+1)
    else:
        ans1 = knapsack(weights,values,weight,n,i+1)
        ans2 = knapsack(weights,values,weight-weights[i],n,i+1)+values[i]
        ans = max(ans1,ans2)
    return ans

def takeInput():
    n = int(input())
    if n==0:
        return [],[],0,n

    weights = list(map(int,input().split()))
    values = list(map(int,input().split()))
    weight = int(input())
    return weights,values,weight,n

weights,values,weight,n = takeInput()
print(knapsack(weights,values,weight,n))
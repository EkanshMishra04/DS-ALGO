# top-down approch as i am building solution from bigger problem to smaller(base case) problem
# recursive solution time complexity O(2^n) and space O(1)
# still need of memoizing

def knapsack(w,n,v,wt):
    if(w==0 or n==0):
        return 0
    elif(wt[n-1]>w):
        return 0
    else:
        return max(v[n-1]+knapsack(w-wt[n-1],n-1,v,wt),knapsack(w,n-1,v,wt))
w=60
n=3
v=[100,280,120]
wt=[10,40,20]
profit=knapsack(w,n,v,wt)
print(profit)
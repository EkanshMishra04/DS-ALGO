def subsetSumPartition(arr,n,TargetSum):
    if(n==0):                               # NO ITEM IN ARRAY
        t[n][TargetSum]=False
        return t[n][TargetSum]
    if(TargetSum==0):                       # NO SUM TO MAKE SO ALWAYS RETURN EMPTY SET
        t[n][TargetSum]=True
        return t[n][TargetSum]

    if(arr[n-1]>TargetSum):                 # ARRAY ITEM GREATER TARGET_SUM NOT POSSIBLE TO ADD IT TO SUBSET
        t[n-1][TargetSum]=subsetSumPartition(arr,n-1,TargetSum)
        return t[n][TargetSum]

    else:                                   # CODING OF CHOICE DIAGRAM
        t[n-1][TargetSum]=subsetSumPartition(arr,n-1,TargetSum-arr[n-1]) or subsetSumPartition(arr,n-1,TargetSum)
        return t[n][TargetSum]
n=6
arr=[3,34,4,12,5,2]
TargetSum=17
t=[[-1]*(TargetSum+1)]*(n+1)
print(subsetSumPartition(arr,n,TargetSum))
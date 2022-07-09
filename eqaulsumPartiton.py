def subsetsum(arr,n,target):
    if(n==0):
        return False
    if(target==0):
        return True
    if(arr[n-1]>target):
        return subsetsum(arr,n-1,target)
    else:
         return subsetsum(arr,n-1,target) or subsetsum(arr,n-1,target-arr[n-1])
def equalsumPartition(arr,n):
    arr_sum=sum(arr)
    if(arr_sum%2!=0):
        return False
    else:
        target=arr_sum//2
        return subsetsum(arr,n,target)
n=6
arr=[8,7,6,12,4,5]
print(equalsumPartition(arr,n))
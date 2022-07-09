import time
# def binarysearch(array,low,high,key):
#     if(low==high):
#         return
#     mid=(low+high)//2
#     if(array[mid]==key):
#         global index
#         index=mid
#         return
#     elif(array[mid]<key):
#         binarysearch(array,mid+1,high,key)
#     elif(array[mid]>key):
#         binarysearch(array,low,mid-1,key)
def binarysearch(array,low,high,key):
    while(low<=high):
        mid=(low+high)//2
        if(array[mid]==key):
            return mid
        elif(array[mid]>key):
            high=mid-1
        elif(array[mid]<key):
            low=mid+1
    return "not found"

begin=time.time()
key=100
array=[10,12,20,22,30,32,40,90,98,100]
array.sort()
a=binarysearch(array,0,9,key)
print(a)
end=time.time()
print("Elasped time was ",begin-end)
# key=40
# index=-1
# array=[10,12,20,22,30,32,40,90,98,100]
# array.sort()
# binarysearch(array,0,9,key)
# if index==-1:
#     print("element not in array")
# else:
#     print("element found at index-->>  ",index)
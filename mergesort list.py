import math
def merge(a,b):
    lena=len(a)
    lenb=len(b)
    lst=[]
    if(not a or not b):
        return
    else:
        i=0
        j=0
        while(i<lena and j<lenb):
            if(a[i]<a[j]):
                lst.append(a[i])
                i+=1
            elif(a[j]<a[i]):
                lst.append(a[j])
                j+=1
        if(i!=lena):
            while(i!=lena):
                lst.append(a[i])
                i+=1
        if(j!=lenb):
            while(j!=lenb):
                lst.append(a[j])
                j+=1
        print(lst)
        return




def mergesort(lst,low,high):
    indexlow=lst.index(low)
    indexhigh=lst.index(high)
    if(low>=high):
        return
    elif(low<high):



# lst=list(map(int,input().split()))
lst=[98,87,65,54,32,21]
n=len(lst)
low=lst[0]
high=lst=[n-1]
mergesort(lst,low,high)

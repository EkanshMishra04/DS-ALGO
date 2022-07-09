# def LinearSearch(lst,key):
#     flag=0
#     for i in lst:
#         if(i==key):
#             print("found element at index",lst.index(i))
#             flag=1
#             break
#     if(flag==0):
#         print("not found")



#recursive
def LinearSearch(lst,i,key):
    if(i>=len(lst)):
        print("NotFound")
        return
    else:
        if(lst[i]==key):
            print("found ",i)
        else:
            LinearSearch(lst,i+1,key)


key=13
lst=[90,98,100,10,12,20,22,30,32,40]
LinearSearch(lst,0,key)

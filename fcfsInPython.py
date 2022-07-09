def prepareGhantt(dict1):
    #key=[at,bt]
    n=len(dict1)
    at=[]
    bt=[]
    for i in dict1.keys():
        a=dict1[i]
        at.append(a[0])
        bt.append(a[1])
    c=at
    at.sort()
    newbt=[0]*n
    for i in c:
        k=at.index(i)
        newbt[k]=bt[c.index(i)]
    print(at)
    print(newbt)
    pass






# n=int(input())
n=3
dict1={} #process no as key and lst of bust time and arival time
# for i in range(n):
#     key=i+1
#     value=[]
#     at=int(input("Arrival time"))
#     bt=int(input("burst time"))
#     value.append(at)
#     value.append(bt)
#     dict1[key]=value
# # print(dict1)
at=[5,1,0]
bt=[2,4,3]
value=[[5,2],[1,4],[0,3]]
for i in range(n):
    dict1[i+1]=value[i]
print(dict1)
prepareGhantt(dict1)

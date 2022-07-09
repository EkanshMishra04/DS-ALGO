def createAdjacencyList(n):
    g=[]
    for i in range(n):
        # a=[]
        a=list(map(int,input().split()))
        g.append(a)
    return g

def printNeighbour(g):
    row=0
    addmat=[]
    for i in g:
        row+=1
        addrow=[]
        # print(f"neighbour of {row} ==>>",end="")
        vertexno=0
        for j in i:
            vertexno+=1
            if(j==1):
                addrow.append(vertexno)
        #         print(vertexno,end=" ")
        # print()
        addmat.append(addrow)
    return addmat
# def validateStep(a):
#     return False
# def applybfs(a):
#     flag=False
#     steps=["U","L","D","R"]
#     queue=[""]
#     print(queue)
#     for i in queue:
#
#         a=queue.remove(i)
#         for j in steps:
#             a=str(a)+j
#             flag=validateStep(a)
#             if(flag==True):
#                 queue.append(a)


def bfs(g):
    visted=[]
    queue=[]
    # for i in range(len(g)):
    queue.append(1)
    visted.append(1)
    while(len(queue)!=0):
        a=queue.pop(0)
        # print(a,end="=>")
        for j in g[a-1]:
            if(j not in visted):
                queue.append(j)
                visted.append(j)
    print("queue",queue)
    print("visted",visted)
                # print(j,end=" ")
            # print()

# n=6
# g= [[0,0,0,0,1,1],
#     [0,0,0,0,1,1],
#     [0,0,0,1,0,1],
#     [0,0,1,0,1,0],
#     [1,1,0,1,0,0],
#     [1,1,1,0,0,0]]
n=5
g=[[0,1,1,1,0],
   [1,0,0,1,1],
   [1,0,0,1,0],
   [1,1,1,0,1],
   [0,1,0,1,0]]
print(g)
a=printNeighbour(g)
print(a)
# bfs(a)


# n=int(input("no of vertices = "))
# g=createAdjacencyList(n)

# applybfs(a)
# for i in a:
#     print(i)


# 0 0 0 0 1 1
# 0 0 0 0 1 1
# 0 0 0 1 0 1
# 0 0 1 0 1 0
# 1 1 0 1 0 0
# 1 1 1 0 0 0
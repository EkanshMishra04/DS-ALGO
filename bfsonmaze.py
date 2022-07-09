def create_maze():
    lst=[]
    lst.append(["#","#","#","#","#","#","#","#"])
    lst.append(["#"," "," "," ","#","X","#","#"])
    lst.append(["#"," ","#"," ","#"," ","#","#"])
    lst.append(["#"," ","#"," "," "," ","#","#"])
    lst.append(["#"," "," ","#","#","#","#","#"])
    lst.append(["#","#"," ","#","#"," "," ","#"])
    lst.append(["#","#","O","#","#"," "," ","#"])
    lst.append(["#","#","#","#","#","#","#","#"])
    return lst


def implement_bfs():
    pass

a=create_maze()
for i in range(8):
    for j in range(8):
        if(a[i][j]=='O'):
            print("O is at index ",i,j)
        if(a[i][j]=='X'):
            print("X is at ",i,j)
    # print()
for i in range(8):
    for j in range(8):
        print(a[i][j],end=" ")
    print()
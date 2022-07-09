class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def InsertLast(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

    def Printer(self):
        if (self.start == None):
            print("Lst is empty")
        else:
            temp = self.start
            while (temp):
                print(temp.data, end="---->>>")
                temp = temp.next
            print("None")
    def sortll(self):
        if(not self.start):
            print("already sorted list")
        else:
            cpt=self.start
            while(cpt):
                fpt=cpt.next
                while(fpt):
                    if(cpt.data>fpt.data):
                        cpt.data,fpt.data=fpt.data,cpt.data
                    fpt=fpt.next
                cpt=cpt.next




mylist = LinkedList()
mylist.InsertLast(120)
mylist.InsertLast(90)
mylist.InsertLast(60)
mylist.InsertLast(30)
print("before sort")
mylist.Printer()
mylist.sortll()
print("after sort")
mylist.Printer()
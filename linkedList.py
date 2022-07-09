class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next



class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, data):
        newNode = node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # def printLL(self):
    #     current = self.head
    #     while(current):
    #         print(current.data)
    #         current = current.next
    def printNode(self):
        if(self.head==None):
            return
        else:
            curr = self.head
            while(curr!=None):
                print(curr.data,end="-->")
                curr=curr.next
            print("NULL")
        # print(self.head,self.head.next)
    def reverse(self):
        curr=self.head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        # print(count)
        curr=self.head
        first=self.head
        sec=first.next
        c=count
        count=count//2
        while(count>=0 and curr.next):
            prev=curr
            curr=curr.next
            count-=1
        print(curr.data,prev.data)




l1=LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.insert(6)
l1.insert(7)
l1.insert(8)
l1.printNode()
l1.reverse()
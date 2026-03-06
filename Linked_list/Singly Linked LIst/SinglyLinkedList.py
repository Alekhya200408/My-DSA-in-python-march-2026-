class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def InsertatMid(self,value,x):
        temp=Node(value)
        t1=self.head

        while(t1!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
                return
            else:
                t1=t1.next


    def InsertatBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
    def InsertatEnd(self,value):
        temp=Node(value)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next  
            t1.next=temp
        else:
            self.head=temp
    
    def printLL(self):
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                print(t1.data)
                t1=t1.next
            print(t1.data)
obj=SinglyLinkedList()
obj.InsertatEnd(10)
obj.InsertatEnd(20)
obj.InsertatMid(30,20)
obj.InsertatEnd(40)
obj.InsertatBeg(5)    
obj.InsertatBeg(2)
obj.printLL()

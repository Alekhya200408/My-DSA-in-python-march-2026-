class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None
        self.prev=None
    
class DoublyLL:
    def __init__(self):
        self.head=None

    def insertatEnd(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        
        t=self.head
        while(t.next!=None):
            t=t.next
        
        t.next=temp
        temp.prev=t
    
    def insertatbeg(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp #for doublyLL
        self.head=temp

    def insertatMid(self,value,x):
        temp=Node(value)
        t=self.head

        while(t.next!=None):
            if(t.data==x):
                break
            else:
                t=t.next
        
        temp.next=t.next
        t.next.prev=temp
        t.next=temp
        temp.prev=t

    def deleteDLL(self,value):
        if(self.head==None):
            print("LinkList is Empty")
            return

        #for beg deletion
        t=self.head
        if(t.data==value):
            self.head=t.next
            self.head.prev=None
            return
    #from middle deletion
        while(t.next!=None):
            if(t.data==value):
                t.prev.next=t.next
                t.next.prev=t.prev
                return
            else:
                t=t.next
        # deletion from end
        if(t.data==value):
            t.prev.next=None


    def printDLL(self):
        if(self.head!=None):
            t1=self.head
        while(t1.next!=None):
            print(t1.data, end="  <--> ")
            t1=t1.next
        print(t1.data) #for printing the last location

obj=DoublyLL()
obj.insertatEnd(10)
obj.insertatEnd(20)
obj.insertatEnd(30)
obj.insertatEnd(40)
obj.insertatbeg(5)
obj.insertatMid(50,20)
obj.deleteDLL(5)
obj.deleteDLL(50)
obj.deleteDLL(40)
obj.printDLL()

# while(t.next!=None):
#     if(t.data==x):
#        break
#     else:
#       t=t.next
# this iis the searching method
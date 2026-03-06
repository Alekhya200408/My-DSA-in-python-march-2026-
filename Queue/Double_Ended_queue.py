# for other languages like C
# Dequeue(Double Ended Queue )
# Insert at Front
#  if (front>0)
# front=front-1

# for deletion
# rear=rear-1

# In python
# insertion at the front we call insert(0 for beginning,value)
# for deletion at end item.pop() automaically it deletes from the end

class Dequeue:
    def __init__(self):
        self.items=[] #initialize the list
    
    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtFront(self):
        if(self.isEmpty()):
            raise Exception("Queue is empty")
        else:
            return self.items.pop(0) #always 1st index

    def insertAtBeginning(self,value):
        self.items.insert(0,value)
    
    def deleteAtEnd(self):
      if(self.isEmpty()):
            raise Exception("Queue is empty")
      else:
        return self.items.pop()

q=Dequeue()

q.insertAtBeginning(10)
q.insertAtBeginning(20)
q.insertAtBeginning(30)
q.insertAtEnd(50)
q.insertAtEnd(60)


print(q.deleteAtFront())
print(q.deleteAtFront())
print(q.deleteAtFront())
print(q.deleteAtFront())
print(q.deleteAtFront())




# FIFO
# when we insert an element (First element) we should change the front and rear to 0 from -1
# in next insertion  put rear=rear+1 (check overflow)
# for deletion front=front+1(check underflow)

# this all for other languages
# we use queue with lists ,we do  not check the front and rear (append it it insert at the end )
# use pop (0) index of front

class Queue:
    def __init__(self):
        self.items=[]

    def isempty(self):
        return len(self.items)==0
    
    # for insertion
    def insert(self,value):
        self.items.append(value)

    def delete(self):
        if(self.isempty()):
            raise Exception("Queue is empty")
        else:
            return self.items.pop(0) #always 1st index

q=Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete()
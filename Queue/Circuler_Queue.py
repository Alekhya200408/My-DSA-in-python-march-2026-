# we have to create a fix size array or list .....and circuler queue's benifit is to use the vacant space in the list at the beginning
# we will use modulo operater 
# for insert => rear=(rear+1)%size of queue
# for delete => front=(front+1)%size of queue

class CirculerQueue:
    def __init__(self,size): #defining the size of the list
        self.size=size
        self.items=[None]*size #it defines that it makes a size of array which is mentioned and all are none values in it
        self.front=self.rear=-1
    
    def enqueue(self,value):
        if((self.rear+1)%self.size==self.front):
            print("Queue is full")
        elif self.front==-1:
            self.front=self.rear=0
            self.items[self.rear]=value
        else:
            self.rear=(self.rear+1)%self.size
            self.items[self.rear]=value
    
    def dequeue(self):
        if(self.front==-1):
            print("queue is empty")
        elif self.front==self.rear:
            print(self.items[self.front])
            self.front=self.rear=-1
        else:
            print(self.items[self.front])
            self.front=(self.front+1)%self.size


cq=CirculerQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
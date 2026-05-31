class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None


def insert(root,value):
        if(root==None):
            return Node(value)
        if(root.data==value):
            return root
        if(root.data>value):
           root.left= insert(root.left,value)
        else:
           root.right= insert(root.right,value)
        return root  
 
def Search(root,value): 
        if(root==None):
            print("Element is not found ",end='\n')
            return 
        if(root.data==value):
            print("Element Found ",end='\n')
            return 
        if(root.data>value):
           Search(root.left,value)
        else:
            Search(root.right,value)
        return root   

def InOrder(root):
    if(root!=None):
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)

# root=Node(20)
# root.left=Node(15)
# root.right=Node(30)
# root.left.left=Node(12)
# root.left.right=Node(18)

root=insert(None,20) #atfirst Root should be none 
root=insert(root,12)
root=insert(root,33)
root=insert(root,7)
root=insert(root,30)
root=insert(root,21)
root=insert(root,27)
root=insert(root,46)

Search(root,27)
Search(root,100)

InOrder(root)


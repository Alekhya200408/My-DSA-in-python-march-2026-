# Traversal
arr=[1,2,3,4,5,6]

def traversal(x):
    for i in range (0,len(x)):
        print(x[i],end=" ")

traversal(arr)
print('\n')

# Insert an element in an array
def insert (arr,value):
    arr.append(value)
    return arr


print(insert(arr,7))

# Delete an element from an array

def delete(arr,value):
    arr.remove(value)
    return arr

print(delete(arr,3))

# Search an element in an array (Linear Search)
def search(arr,value):
    for i in arr:
        if(i==value):
            print("Element Found")
            return
    
    print("Element not Found")

search(arr,3)

# Finding the Largest Element in the array
def largest(arr):
    max=arr[0]

    for i in arr:
        if(i>max):
            max=i
    
    return max

print(largest(arr))

# Reverse an Array
def reverse(arr):
    arr.reverse()
    return arr

print(reverse(arr))
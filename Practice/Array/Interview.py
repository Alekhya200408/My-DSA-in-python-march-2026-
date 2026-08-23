# count even numbers
arr = [10, 15, 20, 25, 30]

def count_even(arr):
    count=0
    for i in arr:
        if(i%2==0):
            count+=1
            print(i,end=" ")
    return count
    

print(count_even(arr),)

# Sum all elements
def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

print(sum(arr))

# find the second largest element
def second_largest(arr):
    max=arr[0]
    second_largest=arr[0]
    for i in arr:
        if(i>max):
            second_largest=max
            max=i
        elif i>second_largest and i<max:
            second_largest=i
    return second_largest
print(second_largest(arr))

# best for 2nd largest chatgpt 
# def second_largest(arr):

#     if len(arr) < 2:
#         return "No second largest element"

#     largest = float('-inf')
#     second = float('-inf')

#     for i in arr:

#         if i > largest:
#             second = largest
#             largest = i

#         elif i > second and i != largest:
#             second = i

#     if second == float('-inf'):
#         return "No second largest element"

#     return second
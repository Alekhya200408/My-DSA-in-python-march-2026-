arr = [10, 20, 30, 40, 50]

# max
def maximum(arr):
    max=arr[0]

    for i in arr:
        if(i>max):
            max=i

    return max

print(maximum(arr))

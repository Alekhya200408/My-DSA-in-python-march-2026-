def kadanes(arr):
    max=arr[0]
    sum=0

    for i in range(len(arr)):
        sum=sum+arr[i]

        if(sum>max):
            max=sum
        if(sum<0):
            sum=0
    return sum

arr=[-2,-3,4,-1,-2,1,5,-3,4]
print(kadanes(arr))
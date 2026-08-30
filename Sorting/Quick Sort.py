arr=[4,6,2,5,7,9,1,3]
n=len(arr)-1
def quick_Sort(arr,low,high):
    if (low<high):
        pIndex=f(arr,low,high)
        quick_Sort(arr,low,pIndex-1)
        quick_Sort(arr,pIndex+1,high)

def f(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high):
            i+=1
        while (arr[j]>pivot and j>=low):
            j-=1
        if(i<j):
            arr[i],arr[j]=(arr[j],arr[i])
    arr[low],arr[j]=(arr[j],arr[low])
    return j

quick_Sort(arr,0,n)
print(arr)
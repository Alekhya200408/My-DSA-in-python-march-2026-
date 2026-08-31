class Solution:
    def Swap(self,arr,low,high):
        arr[low],arr[high]=(arr[high],arr[low])


    def sortZeroOneTwo(self, arr):
        n=len(arr)
        low=0
        mid=0
        high=n-1
        while(mid<=high):
            if (arr[mid]==0):
                self.Swap(arr,low,mid)
                low+=1
                mid+=1
            elif (arr[mid]==1):
                mid+=1
            elif (arr[mid]==2):
                self.Swap(arr,mid,high)
                high-=1

        return arr
# Its just the logical part of online coding part
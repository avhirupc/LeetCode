class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr=sorted(arr)
        count=0
        itr=0
        while(itr<len(arr)):
            no=arr[itr]
            j=itr+1
            while(j <len(arr) and arr[j]==no):
                j+=1
            while(j <len(arr) and arr[j]==no+1):
                count+=1
                break
            itr+=1
        return count
class Solution(object):
    def binary_search(self,arr,target):
        if len(arr)==0:
            return -1
        mid=len(arr)//2
        print(mid,arr,target)
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return self.binary_search(arr[:mid],target)
        ind=self.binary_search(arr[mid+1:],target)
        return ind+mid+1 if ind!=-1 else -1
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]!=target:
                return -1
            else:
                return 0
        
        break_point=nums.index(min(nums))
        arr1=nums[:break_point]
        arr2=nums[break_point:]
        if len(arr1)>0 and arr1[0]<=target<=arr1[-1]:
            #bin search
            return self.binary_search(arr1,target)
        else:
            ind=self.binary_search(arr2,target)
            return -1 if ind==-1 else ind+break_point
        
        
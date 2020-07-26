class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        if len(nums)==1:
            return len(nums)
        while(i<len(nums)-1):
            if nums[i]==nums[j]:
                nums.pop(j)
                continue
            i+=1
            j+=1
        return len(nums)
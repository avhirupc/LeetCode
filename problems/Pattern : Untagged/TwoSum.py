class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _set = {v:i for i,v in enumerate(nums)}
        for i,v in enumerate(nums):
            rem=target-v
            if rem in _set and _set[rem] != i:
                return sorted([i,_set[rem]])
            
                
        
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums):
                if n1+n2==target and i!=j:
                    return [i,j]

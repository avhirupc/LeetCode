"""TLE"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets={}
        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums):
                for k,n3 in enumerate(nums):
                    if i<j<k:
                        if n1+n2+n3==0:
                            triplets[str(sorted([n1,n2,n3]))]=[n1,n2,n3]
        return list(triplets.values())
        
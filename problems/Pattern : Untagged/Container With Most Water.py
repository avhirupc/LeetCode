"""TLE"""
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


"""Correct"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        l_ptr=0
        r_ptr=len(height)-1
        while(r_ptr>l_ptr):
            curr_area=abs(r_ptr-l_ptr)*min(height[l_ptr],height[r_ptr])
            max_area=max(max_area,curr_area)
            if height[l_ptr]>height[r_ptr]:
                r_ptr=r_ptr-1
            else:
                l_ptr=l_ptr+1
        return max_area
            
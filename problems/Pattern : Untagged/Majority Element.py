from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min_cnt=len(nums)//2
        nums=Counter(nums)
        for k,v in nums.items():
            if v > min_cnt:
                return k

        
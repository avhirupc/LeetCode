from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_time_number=0
        return reduce(lambda a,b: a^b,nums)
        
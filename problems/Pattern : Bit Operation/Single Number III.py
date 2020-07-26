"""HashMap Approach"""


from collections import Counter
class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		nums=filter(lambda x: x[1]==1,
			   Counter(nums).items())
		return [x[0] for x in list(nums)]
		

"""Bit Operation """
class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		bitmask=0
		for num in nums:
			bitmask ^= num

		rmb = bitmask & (- bitmask)
		x = 0
		for num in nums:
			if num & rmb :
				x = x^num
		return [x, bitmask^x]


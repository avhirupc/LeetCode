class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_=max(candies)
        can_be_max=[]
        for candy in candies:
            if candy+extraCandies>=max_:
                can_be_max.append(True)
            else:
                can_be_max.append(False)
        return can_be_max
        
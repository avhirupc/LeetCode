"""Basic"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_diff=0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j>i and ((prices[j] -prices[i])>max_diff):
                    max_diff=(prices[j] -prices[i])
        return max_diff
        
""" Min Cost Climbing Stairs"""

"Recursive Solution"
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        top_pos=len(cost)
        return min(self.minCostUtil(cost,top_pos-1),self.minCostUtil(cost,top_pos-2))
    
    def minCostUtil(self,cost,pos):
        if pos==0 or pos==1:
            return cost[pos]
        return min(cost[pos]+self.minCostUtil(cost,pos-1),cost[pos]+self.minCostUtil(cost,pos-2))
"""DP Dolution"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N=(len(cost))
        min_cost=[-1]*(N+1)
        min_cost[0]=cost[0]
        min_cost[1]=cost[1]
        for i in range(2,N+1):
            if i==N:
                return min(min_cost[i-1],min_cost[i-2])
            min_cost[i]=min(cost[i]+min_cost[i-1],cost[i]+min_cost[i-2])
        return min_cost[N]
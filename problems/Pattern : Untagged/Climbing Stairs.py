class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        combinations=[-1]*(n+1)
        combinations[0]=1
        combinations[1]=1
        for i in range(2,n+1):
            combinations[i]=combinations[i-1]+combinations[i-2]
        return combinations[n]
        
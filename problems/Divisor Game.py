class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp=[0]*(N+1)
        dp[0]=0
        dp[1]=0
        for i in range(2,N+1):
            for j in range(1,int(math.sqrt(i))+1):
                if i%j==0 and dp[i-j]==0:
                    dp[i]=1
        return dp[N]
        
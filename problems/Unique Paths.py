class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory=[[1]*n]*m
        for row in range(1,m):
            for col in range(1,n):
                memory[row][col]=memory[row-1][col]+memory[row][col-1]
        return memory[m-1][n-1]
        
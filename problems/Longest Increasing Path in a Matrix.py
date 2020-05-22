class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows,columns=len(matrix),len(matrix[0])
        dp=[[0 for col in range(columns)] for row in range(rows)]
        res=0
        for row_itr in range(rows):
            for col_itr in range(columns):
                l=self.dfs(matrix,row_itr,col_itr,dp,float("-inf")) 
                res=max(res,l)
        return res
    
    def dfs(self,matrix, row,col,dp,prev):
        if row<0 or row>len(matrix)-1 or col<0 or col>len(matrix[0])-1:
            return 0
        if  matrix[row][col]<=prev:
            return 0
        
        if dp[row][col]!=0:
            return dp[row][col]
        
        #left,right,up,down
        left=self.dfs(matrix, row,col-1,dp,matrix[row][col])
        right=self.dfs(matrix, row,col+1,dp,matrix[row][col])
        up=self.dfs(matrix, row-1,col,dp,matrix[row][col])
        down=self.dfs(matrix, row+1,col,dp,matrix[row][col])
        
        dp[row][col]=max(left,right,up,down)+1
        
        return dp[row][col]
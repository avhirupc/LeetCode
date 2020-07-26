class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        mem_grid=[[1]*cols]*rows
        mem_grid[0][0]= 0 if obstacleGrid[0][0]==1 else 1
        #suppose only one row
        for col in range(1,cols):
            if obstacleGrid[0][col]==1 or mem_grid[0][col-1]==0:
                mem_grid[0][col]=0
        #suppose only one col
        for row in range(1,rows):
            if obstacleGrid[row][0]==1 or mem_grid[row-1][0]==0:
                mem_grid[row][0]=0
                
        for row in range(1,rows):
            for col in range(1,cols):
                if obstacleGrid[row][col]==1:
                    mem_grid[row][col]=0
                    continue
                mem_grid[row][col]=mem_grid[row-1][col]+mem_grid[row][col-1]
        
        return mem_grid[rows-1][cols-1]
                    
        
        
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        #changing values assuming only one row
        _sum=0
        for col in range(cols):
            grid[0][col]+=_sum
            _sum=grid[0][col]
        #changing values assuming only one row
        _sum=0
        for row in range(rows):
            grid[row][0]+=_sum
            _sum=grid[row][0]
        
        for row in range(1,rows):
            for col in range(1,cols):
                grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
        return grid[rows-1][cols-1]
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid)==0:
            return 0
        rows,columns=len(grid),len(grid[0])
        island_count=0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=='1':
                    self.blast_island(grid,row,column)
                    island_count+=1
        return island_count
    
    def blast_island(self,grid,row,column):
        if (row<0 or column< 0 or row>=len(grid) or column>=len(grid[row])):
            return
        if grid[row][column]=='0':
            return
        grid[row][column]='0'
        self.blast_island(grid,row-1,column)
        self.blast_island(grid,row+1,column)
        self.blast_island(grid,row,column-1)
        self.blast_island(grid,row,column+1)
        return 
        
        
            
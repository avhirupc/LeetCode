from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten_set=deque([])
        rows,columns=len(grid),len(grid[0])
        level=0
        #get intial rotten set
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]==2:
                    rotten_set.append((row,column,0))
        #perform bfs, and keeping rotten oranges together, go all direction
        while(rotten_set):
            #iterate through all rotten and rot neighbours
            r,c,level=rotten_set.popleft()
            if r-1>=0 and grid[r-1][c]==1:
                grid[r-1][c]=2
                rotten_set.append((r-1,c,level+1))
            if r+1<rows and grid[r+1][c]==1:
                grid[r+1][c]=2
                rotten_set.append((r+1,c,level+1))
            if c-1>=0 and grid[r][c-1]==1:
                grid[r][c-1]=2
                rotten_set.append((r,c-1,level+1))
            if c+1<columns and grid[r][c+1]==1:
                grid[r][c+1]=2
                rotten_set.append((r,c+1,level+1))
        
        #check any of oranges are still fresh
        if any([1 in row for row in grid]):
            return -1
            
        return level

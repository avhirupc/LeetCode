"""TLE"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minutes_elapsed=0
        rows,columns=len(grid),len(grid[0])
        fresh_set,rotten_set=[],[]
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]==1:
                    fresh_set.append((row,column))
                elif grid[row][column]==2:
                    rotten_set.append((row,column))
        counter=0
        while(len(fresh_set)!=0):
            #iterate through all rotten and rot neighbours
            fresh_set_copy=fresh_set[:]
            for rot_o in rotten_set[:]:
                if (rot_o[0]-1,rot_o[1]) in fresh_set_copy:
                    rotten_set.append((rot_o[0]-1,rot_o[1]))
                    fresh_set.remove((rot_o[0]-1,rot_o[1]))
                elif (rot_o[0]+1,rot_o[1]) in fresh_set_copy:
                    rotten_set.append((rot_o[0]+1,rot_o[1]))
                    fresh_set.remove((rot_o[0]+1,rot_o[1]))
                elif (rot_o[0],rot_o[1]-1) in fresh_set_copy:
                    rotten_set.append((rot_o[0],rot_o[1]-1))
                    fresh_set.remove((rot_o[0],rot_o[1]-1))
                elif (rot_o[0],rot_o[1]+1) in fresh_set_copy:
                    rotten_set.append((rot_o[0],rot_o[1]+1))
                    fresh_set.remove((rot_o[0],rot_o[1]+1))
            counter+=1
        return counter
        
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten_set=deque([])
        rows,columns=len(grid),len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]==2:
                    rotten_set.append((row,column,0))
        while(rotten_set):
            #iterate through all rotten and rot neighbours
            r,c,level=rotten_set.popleft()
            if r-1>=0 and grid[r-1][c]==1:
                grid[r-1][c]=2
                rotten_set.append((row-1,column,level+1))
            elif r+1<rows and grid[r+1][c]==1:
                grid[r+1][c]=2
                rotten_set.append((row+1,column,level+1))
            elif c-1>=0 and grid[r][c-1]==1:
                grid[r][c-1]=2
                rotten_set.append((row,column-1,level+1))
            elif c+1<columns and grid[r][c+1]==1:
                grid[r][c+1]=2
                rotten_set.append((row,column+1,level+1))

        if any([1 in row for row in grid]):
            return -1
            
        return level

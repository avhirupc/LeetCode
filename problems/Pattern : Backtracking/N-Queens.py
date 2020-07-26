class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows,columns = n, n 
        board=[['.' for col in range(columns)] for row in range(rows)]
        solutions=[]
        queens_remaining = n
        #smallest unit in this problem
        self.solveNQueenUtil(board,0,queens_remaining,solutions)
        return solutions
    
    def solveNQueenUtil(self, board, row, queens_remaining, solutions):
        # goal
        if queens_remaining == 0:
            print(board)
            solutions.append(board)
            return 
        
        if row >=len(board):
            return 
        
        #all the choices . thats all the columns
        for col in range(len(board[0])):
            
            if self.validateBoard(board,row, col, len(board)):
                board[row][col]='Q'
                self.solveNQueenUtil(board, row+1, queens_remaining-1, solutions)
                
            board[row][col]='.'
            
        return 
        
    def validateBoard(self,board, row, col, N): 

        # Check this row on left side 
        for i in range(col): 
            if board[row][i] == "Q": 
                return False

        # Check upper diagonal on left side 
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
            if board[i][j] == "Q": 
                return False

        # Check lower diagonal on left side 
        for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
            if board[i][j] == "Q": 
                return False
        return True



class Solution(object):
    
    def isValid(self, location, queens):
        row, col = location
        for queen in queens:
            x, y = queen
            if abs(row - x) == abs(col - y):
                return False
            if row == x or col == y:
                return False
        return True
    
    def solve(self, grid, n, col, queens, solution):
        if col >= n:
            solution.append([''.join(reversed(row)) for row in grid])
            return True
        
        for i in range(n):
            r = False
            if self.isValid((i, col), queens):
                grid[i][col] = 'Q'
                queens.append((i, col))
                r = self.solve(grid, n, col + 1, queens, solution) or r
                grid[i][col] = '.'
                queens.remove((i, col))
        return r
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = []
        grid = [['.' for i1 in range(n)] for i2 in range(n)]
        solution = []
        self.solve(grid, n, 0, queens, solution)
        
        return solution
        
        
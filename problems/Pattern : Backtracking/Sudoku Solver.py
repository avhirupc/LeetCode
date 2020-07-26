class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows,columns=len(board),len(board[0])
        
        self.solveSudokuUtil(board,0,0,rows,columns)
        
        
    def solveSudokuUtil(self,board,row,column,rows,columns):
        # goal
        if column == columns:
            if row == rows:
                return True
            else:
                return self.solveSudokuUtil(board,row+1,0, rows,columns)
        if row==rows:
            return True
        if board[row][column]!='.':
            return self.solveSudokuUtil(board,row,column+1, rows,columns)
        
        #explore / choices
        for choice in range(1,10):
            if str(choice) in board[row]:
                continue
            if str(choice) in [board[r][column] for r in range(9)]:
                continue
            board[row][column]=str(choice)
            #constraint
            if self.isValidSudoku(board):
                if self.solveSudokuUtil(board,row,column+1,rows,columns):
                    return True
                
        board[row][column]='.'
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    sudoku += ((i, c), (c, j), (i//3, j//3, c))
        return len(sudoku) == len(set(sudoku))    
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_found=[]
        #iterate through each word 
        #sanitary checks
        if not board:
            return []
        if len(words)==0:
            return []
        for word in words:
            if self.wordPresent(word,board):
                words_found.insert(0,word)
        
        return words_found
    
    def wordPresent(self,word,board):
        rows,columns=len(board),len(board[0])
        for row in range(rows):
            for col in range(columns):
                if board[row][col]==word[0]:
                    visited=[[False for col in range(columns)] for row in range(rows)]
                    pr=False
                    if self.dfs(board,row,col,word,visited,pr):
                        return True
        return False
    
    def dfs(self,board,row,col,word,visited,pr):
        if row < 0 or row>=len(board):
            return False
        if col < 0 or col>=len(board[0]):
            return False
        if pr and len(word)<10:
            print(row,col,word,visited[row][col])
        if visited[row][col]:
            return False
        if board[row][col]!=word[0]:
            return False
        if board[row][col]==word[0] and len(word)==1:
            return True
        
        visited[row][col]=True
        left=self.dfs(board,row,col-1,word[1:],visited,pr)
        right=self.dfs(board,row,col+1,word[1:],visited,pr)
        top=self.dfs(board,row-1,col,word[1:],visited,pr)
        bottom=self.dfs(board,row+1,col,word[1:],visited,pr)
        
        return any([left,right,top,bottom])

        
        
        
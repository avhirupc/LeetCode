class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_total=0
        memory=[]
        for row in triangle:
            memory.append([0]*len(row))
        rows=len(triangle)
        #first col
        memory[0][0]=triangle[0][0]
        for row in range(1,rows):
            memory[row][0]=memory[row-1][0]+triangle[row][0]
        for row in range(1,rows):
            memory[row][-1]=memory[row-1][-1]+triangle[row][-1]
        
        for row in range(1,rows):
            cols=len(triangle[row])
            for col in range(1,cols-1):
                memory[row][col]=min(memory[row-1][col],memory[row-1][col-1])+triangle[row][col]
        return min(memory[-1])
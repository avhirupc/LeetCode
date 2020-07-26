
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows,cols=len(matrix),len(matrix[0])
        mem= [[0 for c in range(cols)] for r in range(rows)]
        max_s=0
        #fill first row
        for c in range(cols):
            mem[0][c]=int(matrix[0][c])
            max_s=max(max_s,mem[0][c])
        #fill first col
        for r in range(rows):
            mem[r][0]=int(matrix[r][0])
            max_s=max(max_s,mem[r][0])
        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c]=="0":
                    continue
                mem[r][c]=min(int(mem[r-1][c-1])
                              ,int(mem[r][c-1]),
                              int(mem[r-1][c]))+1
                max_s=max(max_s,mem[r][c])
        
        return max_s*max_s
        



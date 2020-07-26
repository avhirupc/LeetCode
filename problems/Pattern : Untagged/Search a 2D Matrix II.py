import numpy as np
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bol
        """
        print(matrix)
        if len(matrix)==0:
            return False
        matrix=np.array(matrix)
        rows,columns=matrix.shape
        if not(rows>2 and columns>2):
            matrix=matrix.flatten().tolist()
            return target in matrix
        if matrix[0][0]>target and target>matrix[rows-1][columns-1]:
            return False
        
        # divide logic
        mid=rows//2,columns//2
        if target==matrix[mid[0]][mid[1]]:
            return True
        elif target< matrix[mid[0]][mid[1]]:
            lmatrix=matrix[:mid[0]+1,:mid[1]+1]
            rmatrix=matrix[:mid[0]+1,mid[1]:]
            return self.searchMatrix(lmatrix,target) or self.searchMatrix(rmatrix,target)
        lmatrix=matrix[mid[0]:,:mid[1]+1]
        rmatrix=matrix[mid[0]:,mid[1]:]
        return self.searchMatrix(lmatrix,target) or self.searchMatrix(rmatrix,target)


import numpy as np
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bol
        """
        tgt_row=[]
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        for row_n,row in enumerate(matrix):
            if row[0]<=target<=row[-1]:
                tgt_row.append(row_n)
        for rn in tgt_row:
            if self.search(matrix[rn],target):
                return True
        return False
    
    def search(self,row,target):
        if len(row)==0:
            return False
        mid=len(row)//2
        
        if row[mid]==target:
            return True
        elif row[mid]>target:
            return self.search(row[:mid],target)
        return self.search(row[mid+1:],target)
    
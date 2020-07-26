"""
Learnings:
Slow and steady
copy paste code is prone to mistakes
think problem through
test 2 cases and think of corner cases
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        rows,columns=len(matrix),len(matrix[0])
        row_counter,column_counter=len(matrix),len(matrix[0])
        no_of_elements=rows*columns
        ritr,citr,flg=0,0,0
        spiral=[]
        while(row_counter!=0 and column_counter!=0):
            if flg==0:#traversing l to r 
                no_of_iter=column_counter
                for iteration in range(no_of_iter):
                    spiral.append(matrix[ritr][citr])
                    citr+=1
                    no_of_elements-=1
                    
                flg=1
                row_counter-=1
                ritr+=1
                citr-=1
                
            elif flg==1: # traversing top to down
                no_of_iter=row_counter
                for iteration  in range(no_of_iter):
                    spiral.append(matrix[ritr][citr])
                    ritr+=1
                    no_of_elements-=1
                
                flg=2
                column_counter-=1
                citr-=1
                ritr-=1
            elif flg==2: # traversing r to l
                no_of_iter=column_counter
                for iteration in range(no_of_iter):
                    spiral.append(matrix[ritr][citr])
                    citr-=1
                    no_of_elements-=1
                
                flg=3
                row_counter-=1
                ritr-=1
                citr+=1
            else: # traversing down to up
                no_of_iter=row_counter
                for iteration in range(no_of_iter):
                    spiral.append(matrix[ritr][citr])
                    ritr-=1
                    no_of_elements-=1
                
                flg=0
                column_counter-=1
                citr+=1
                ritr+=1

        return spiral
                
                
                
                
                
        
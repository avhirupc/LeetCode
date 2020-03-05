class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        max_sp=0
        for ind,el in enumerate(A):
            sp=self.rightSpecialValue(A,ind+1,el)*self.leftSpecialValue(A,ind-1,el)
            if sp>max_sp:
                max_sp=sp
        return max_sp%1000000007
    
    def rightSpecialValue(self,A,ind,pivot):
        lenA=len(A)
        while (ind!=lenA) and (A[ind]<=pivot) :
            ind+=1
        if ind==lenA:
            return 0
        return ind
            

    def leftSpecialValue(self,A,ind,pivot):
        while (ind!=-1) and (A[ind]<=pivot) :
            ind-=1
        if ind==-1:
            return 0
        return ind
            
    
            

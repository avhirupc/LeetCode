class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N==0:
            return "0"
        result=""
        while(N!=0):
            rem=N%-2
            q=N//-2
            if rem<0:
                rem+=2
                q+=1
            result=str(rem)+result
            N=q
        return result
    
    def decimal(self,N):
        decimal=0
        for pos,dig in enumerate(N[::-1]):
            decimal+=(dig*((-2)**pos))
        return decimal
    
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        n1=self.decimal(arr1)
        n2=self.decimal(arr2)
        n3=self.baseNeg2(n1+n2)
        return [i for i in n3]
        
        
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

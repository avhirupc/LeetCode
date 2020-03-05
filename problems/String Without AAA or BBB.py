class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result=""
        rem_a=A
        rem_b=B
        
        while(rem_a>0 and rem_b>0):
            if rem_a>=rem_b:
                if result[-2:]!="aa":
                    result+="a"
                    rem_a-=1
                else:
                    result+="b"
                    rem_b-=1
            else:
                if result[-2:]!="bb":
                    result+="b"
                    rem_b-=1
                else:
                    result+="a"
                    rem_a-=1
        while(rem_a>0):
            result+="a"
            rem_a-=1
        while(rem_b>0):
            result+="b"
            rem_b-=1
        return result

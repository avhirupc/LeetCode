class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=1
        sum=0
        while(sum<num):
            sum+=n
            if sum==num:
                return True
            n+=2
        return False
        
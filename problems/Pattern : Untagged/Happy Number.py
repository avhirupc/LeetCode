from math import pow
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n==4:
            return False
        sum_of_sq_d=0
        while(n!=0):
            sum_of_sq_d+=(pow(n%10,2))
            n=n//10
        return self.isHappy(sum_of_sq_d)
        
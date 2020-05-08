import math

def factorial(n,fact):
    if n==1:
        fact[n]=1
        return
    factorial(n-1,fact)
    fact[n]=n*fact[n-1]

    
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact={}
        factorial(n,fact)
        nums=list(range(1,n+1))
        res=self.get_perm(nums,k,fact)
        return res
    
    def get_perm(self,nums,k,fact):
        if len(nums)==0:
            return ""
        if len(nums)==1:
            return str(nums[0])
        n=len(nums)
        index=math.ceil(k/fact[n-1])-1
        k=k%fact[n-1]
        char=nums[index]
        nums.remove(char)
        return str(char)+self.get_perm(nums,k,fact)
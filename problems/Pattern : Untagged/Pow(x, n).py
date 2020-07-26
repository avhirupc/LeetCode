def get_pow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    tmp=get_pow(x,n//2)
    if n%2==0:
        return tmp*tmp
    return tmp*tmp*x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_n_positive = n>=0
        res=1
        n=abs(n)
        res=get_pow(x,n)
        return res if is_n_positive else 1/res
    

            
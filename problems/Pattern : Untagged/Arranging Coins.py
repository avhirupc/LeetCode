"""o(n)"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt=0
        st_size=1
        while(n>=st_size):
            cnt+=1
            n-=st_size
            st_size+=1
        return cnt
        
"""O(logn)"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right=0,n
        while(left<=right):
            k=(left+right)//2
            sum=(k*(k+1))//2
            if n==sum:
                return k
            if n>sum:
                left=k+1
            else:
                right=k-1
        return right
        
        

    
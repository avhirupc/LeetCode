# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start=1
        end=n+1
        return self.firstBadVersionUtil(start,end)
        
    def firstBadVersionUtil(self,start,end):
        mid=(end-start)//2+start
        if not isBadVersion(mid):
            return self.firstBadVersionUtil(mid,end)
        # if mid bad version
        if isBadVersion(mid-1):
            return self.firstBadVersionUtil(start,mid)
        return mid
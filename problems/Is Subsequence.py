"""Is Subsequence"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s==t:
            return True
        if len(s)==len(t):
            return False
        return any([self.isSubsequence(s,remove_at(i,t)) for i in range(0,len(t))])

"""Non DP Solution"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        for char in s:
            new = t[(i):].find(char)
            if new == -1:
                return False
            i = i+1+new       
        return True
            
            

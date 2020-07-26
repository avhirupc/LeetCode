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

"""DP Solution """
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sptr,tptr=0,0
        char_encountered=[0]*len(t)
        if s=="" :
            return True
        if t=="":
            return False
            
        
        if s[sptr]==t[tptr]:
            char_encountered[tptr]=1
            sptr+=1
            tptr+=1
        else:
            tptr+=1
        
        while(sptr<len(s) and tptr<len(t)):
            if s[sptr]==t[tptr]:
                char_encountered[tptr]=char_encountered[tptr-1]+1
                sptr+=1
            else:
                char_encountered[tptr]=char_encountered[tptr-1]
            tptr+=1
        
        if char_encountered[-1]==len(s):
            return True
        else:
            return False
            
            

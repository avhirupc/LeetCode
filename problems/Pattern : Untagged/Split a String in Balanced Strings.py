class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcnt,rcnt=0,0
        ssplits=0
        for itr in range(len(s)):
            if s[itr] == 'L':
                lcnt+=1
            else:
                rcnt+=1
            if lcnt==rcnt:
                ssplits+=1
                lcnt,rcnt=0,0
        return ssplits
                
        
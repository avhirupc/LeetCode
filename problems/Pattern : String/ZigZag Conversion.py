from collections import deque
from itertools import cycle

class Solution(object):
    def convert(self, s, numRows):
        rows = deque([])
        level = cycle(list(range(numRows))+list(range(numRows-2,0,-1)))
        itr=0
        while(itr<len(s)):
            rows.append((s[itr],next(level)))
            itr+=1
        
        result_set=[]        
        for level in range(numRows):
            result_set.extend(
                list(map(lambda x: x[0],
                filter(lambda x: x[1] == level, rows))))
                        
                              
        return "".join(result_set)
        
from collections import deque
from itertools import cycle

class Solution(object):
    def convert(self, s, numRows):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if numRows ==1 or numRows >= len(s):
            return s
        
        result_set =[""]* numRows
        
        index, step=0,1
        
        for c in s:
            result_set[index] += c
            if index==0:
                step = 1
            if index == numRows-1:
                step = -1
            
            index += step
                              
        return "".join(result_set)
        
        
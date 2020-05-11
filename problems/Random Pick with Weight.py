# TLE
import random
class Solution:

    def __init__(self, w: List[int]):
        ind_itr=0
        w_itr=0
        indexes=[]
        while(w_itr<len(w)):
            i_itr=0
            while(i_itr<w[w_itr]):
                indexes.append(ind_itr)
                i_itr+=1
            w_itr+=1
            ind_itr+=1
        self.indexes=indexes

    def pickIndex(self) -> int:
        return random.choice(self.indexes)
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

import random
from bisect import bisect_left
class Solution:

    def __init__(self, w: List[int]):
        indexes=[]
        st=0
        for w_itr in range(len(w)):
            en=st+w[w_itr]
            indexes.append(en)
            st=en
        self.indexes=indexes
        self.total=sum(w)
        

    def pickIndex(self) -> int:
        num=random.randint(1,self.total)
        k=bisect_left(self.indexes,num)
        return k
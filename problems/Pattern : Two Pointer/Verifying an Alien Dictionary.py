from functools import cmp_to_key
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {c: pos for c, pos in zip(order, range(len(order)))}
        def alienCmp(word1,word2):
            ptr1,ptr2=0,0
            while(ptr1<len(word1) and ptr2< len(word2)):
                pos1 = mapping[word1[ptr1]]
                pos2 = mapping[word2[ptr2]]
                
                if pos1 < pos2:
                    return -1
                if pos2 < pos1:
                    return 1
                ptr1+=1
                ptr2+=1
                
            if ptr1==len(word1) and ptr2!= len(word2):
                return -1
            if ptr1!=len(word1) and ptr2== len(word2):
                return 1
            return 0
        
        alienSorted = sorted(words, key = cmp_to_key(alienCmp))
        for sw, w in zip(alienSorted,words):
            if sw!=w:
                return False
        return True
        
            
        
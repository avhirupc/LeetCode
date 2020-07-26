"""TLE"""
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.is_word=False
        self.children=defaultdict(TrieNode)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        trie=self.constructTrie(words)
        concat_words=[]
        for word in words:
            flg=[]
            if word=="":
                continue
            if self.is_concat(word,trie,flg):
                concat_words.append(word)
        return concat_words
    
    def constructTrie(self,words: List[str]):
        root=TrieNode()
        for word in words:
            curr=root
            for c in word:
                curr=curr.children[c]
            curr.is_word=True
        return root
    
    def is_concat(self,word,trie,flg):
        if word=="":
            return True
        curr=trie
        poss=[]
        for pos,c in enumerate(word):
            if curr.children[c].is_word and self.is_concat(word[pos+1:],trie,flg):
                flg.append(word[:pos])
            if c not in curr.children:
                break
            curr=curr.children[c]
        return True if len(flg)>1 else False
        
        
"""Accepted"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem = set(words)
        
        def isConcatDFS(word):
            #checks if concatenated by multilpe
            for pos in range(1,len(word)):
                prefix = word[:pos]
                suffix = word[pos:]
                if prefix in mem and suffix in mem:
                    return True
                if prefix in mem and isConcatDFS(suffix):
                    return True
            
            return False
            
            
            
        result_set=[]
        for word in words:
            if isConcatDFS(word):
                result_set.append(word)
        return result_set
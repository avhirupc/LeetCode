from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child=defaultdict(TrieNode)
        self.is_word=False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie=TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur=self.trie
        for c in word:
            cur=cur.child[c]
        cur.is_word=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        root=self.trie
        prefix=word
        return self.searchUtil(prefix,root)
    
    def searchUtil(self,prefix,root):
        if len(prefix)==1:
            if prefix=='.':
                if len(root.child.keys())==0:
                    return False
                for ch in root.child:
                    if root.child[ch].is_word:
                        return True
                return False
            return root.child[prefix].is_word if prefix in root.child else False
        if not prefix[0]=='.':
            if prefix[0] in root.child:
                return self.searchUtil(prefix[1:],root.child[prefix[0]])
            else: 
                return False
        for char in root.child.keys():
            if self.searchUtil(prefix[1:],root.child[char]):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
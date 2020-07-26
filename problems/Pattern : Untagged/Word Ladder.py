class Solution(object):
    def find_adjacent(self,word,wordList):
        char_set="qwertyuiopasdfghjklzxcvbnm"
        wordList=set(wordList)
        adjacent_words=[]
        for pos in range(len(word)):
            for char in char_set:
                val=word[:pos]+char+word[pos+1:]
                if val in wordList:
                    adjacent_words.append(val)
        return adjacent_words
    
    def remove_visited(self,adjacent_words,visited):
        return [word for word in adjacent_words if word not in visited]
                    

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord is None or endWord is None or wordList is None:
            return 0
        if len(beginWord)!=len(endWord):
            return 0
        if endWord not in wordList:
            return 0    
        queue=[(beginWord,0)]
        visited=set([beginWord])
        while(len(queue)!=0):
            word,level=queue.pop(0)
            if word==endWord:
                return level+1
            adjacent_words=self.find_adjacent(word,wordList)
            adjacent_words=self.remove_visited(adjacent_words,visited)
            for adj_word in adjacent_words:
                visited.add(adj_word)
                queue.append((adj_word,level+1))
        return 0

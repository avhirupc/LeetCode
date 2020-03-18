class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_map=["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result_set=[]
        for digit in digits:
            temp_result_set=[]
            if digit in ["0","1"]:
                continue
            for c in char_map[int(digit)]:
                temp_result_set+=self.letterCombinationsUtil(c,result_set)    
            result_set=temp_result_set[:]
        return result_set
    
    def letterCombinationsUtil(self,c,result_set):
        #each element in result add c
        if result_set ==[]:
            return [c]
        return [res+c for res in result_set]
                
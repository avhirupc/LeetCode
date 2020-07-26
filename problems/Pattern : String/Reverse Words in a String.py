class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        ind=0
        words=[]
        curr_word=""
        while(ind<len(s)):
            if s[ind]==" ":
                if curr_word!="":
                    words.append(curr_word)
                #add current word to list of words
                curr_word=""
                ind+=1
                continue
            curr_word+=s[ind]
            ind+=1
        if curr_word!="":
            words.append(curr_word)
        
        return " ".join(words[::-1])
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        string_min_len=min(map(lambda x:len(x),strs))
        num_of_strs=len(strs)
        lcp=""
        flg=0
        for i in range(0,string_min_len):
            c= strs[0][i]
            for str_ind in range(1,len(strs)):
                if strs[str_ind][i]!=c:
                    flg=1
                    break
            if flg==1:
                break
            lcp+=c
        return lcp
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping=[("M",1000),("CM",900),("DC",600),("D",500),("CD",400),("C",100),
                ("XC",90),("LX",60),("L",50),("XL",40),("X",10),("IX",9),("VI",6),("V",5),("IV",4),("I",1)]
        num=0
        m_ptr=0
        s_ptr=0
        while(s_ptr<len(s)):
            cmp_chr=len(mapping[m_ptr][0])
            if s[s_ptr:s_ptr+cmp_chr]!=mapping[m_ptr][0]:
                m_ptr+=1
            else:
                num+=mapping[m_ptr][1]
                s_ptr+=cmp_chr
        return num
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping=[("M",1000),("CM",900),("DC",600),("D",500),("CD",400),("C",100),
                ("XC",90),("LX",60),("L",50),("XL",40),("X",10),("IX",9),("VI",6),("V",5),("IV",4),("I",1)]
        mapping_itr=0
        result=""
        while(num!=0):
            mc,mn=mapping[mapping_itr]
            if num//mn!=0:
                result+=(mc*(num//mn))
                num=num%mn
                continue
            mapping_itr+=1
            
        return result
        
        
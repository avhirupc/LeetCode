class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res=""
        dividend,divisor=numerator,denominator
        R=-1
        while(dividend>=divisor):
            Q = dividend//divisor
            R = dividend%divisor
            res=res+str(Q)
            dividend=R
        R_set=set([])
        if R!=0:
            if len(res)==0:
                res="0"
            res=res+'.'
            while(R!=0):
                dividend=dividend*10
                while(dividend<divisor):
                    dividend=dividend*10
                    res+='0'
                Q=dividend//divisor
                R=dividend%divisor
                if R in R_set:
                    pos=res.rfind(str(Q))
                    if len(res)==1:
                        res=res[:pos]+"("+res[pos:]+")"
                    else:
                        #need to work on this condition
                        pos=pos
                        cnt=0
                        while(res[pos]=="0"):
                            pos=pos-1
                            cnt+=1
                        res=res[:pos]+"("+res[pos:-cnt]+")"
                    break
                R_set.add(R)
                res=res+str(Q)
                dividend=R
        return res
                    
            
        
"""
Learnings:
using dictionary to keep track of remainders and length /postion
divmod to calculate division and mod single line
negative case
"""    

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res=[""]
        num,den=numerator,denominator
        if num*den<0:
            res.append('-')
        num, den = abs(num), abs(den)
        q,rmd = divmod(num,den)
        res.append(str(q))
        if rmd==0:
            return "".join(res)
        res.append(".")
        dic={}
        num=rmd
        while(rmd!=0):
            if rmd in dic:
                res.insert(dic[rmd],"(")
                res.append(")")
                return "".join(res)
            dic[rmd]=len(res)
            q,rmd=divmod(num*10,den)
            res.append(str(q))
            num=rmd
        
        return "".join(res)
                
            
            
        
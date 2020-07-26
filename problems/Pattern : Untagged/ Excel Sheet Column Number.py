class Solution:
    def titleToNumber(self, s: str) -> int:
        num=0
        p=0
        for d in s[::-1]:
            num+=(math.pow(26,p)*(ord(d)-ord('A')+1))
            p+=1
        return int(num)
            
            
        
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        num="1"
        for i in range(1,n):
            num=self.get_next_num(num)
        return num
    
    def get_next_num(self,num):
        result=""
        itr=0
        while(itr<len(num)):
            j=itr+1
            counter=1
            while(j<len(num) and num[itr]==num[j]):
                j+=1
                counter+=1
            result+=f"{counter}{num[itr]}"
            itr=j
        return result
            
                        
        
    
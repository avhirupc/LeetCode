class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p=[]
        open_p=n
        close_p=0
        prefix=""
        def generateParenthesisUtil(prefix,open_p,close_p,p):
            if open_p==0 and close_p==0:
                p.append(prefix)
            if open_p>0:
                generateParenthesisUtil(prefix+"(",open_p-1,close_p+1,p)
            if close_p>0:
                generateParenthesisUtil(prefix+")",open_p,close_p-1,p)
        generateParenthesisUtil(prefix,open_p,close_p,p)       
        return p                
            
        
        
        
        
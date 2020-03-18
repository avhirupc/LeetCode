class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk=[]
        for c in s:
            if c in [")","}","]"]:
                if c == ')' and len(stk)>0 and stk[-1]=='(':
                    stk.pop()
                elif c == '}' and len(stk)>0 and stk[-1]=='{':
                    stk.pop()
                elif c==']' and len(stk)>0 and stk[-1]=='[':
                    stk.pop()
                else:
                    stk.append(c)
            else:
                stk.append(c)
        return True if len(stk)==0 else False
        
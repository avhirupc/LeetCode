class Solution:
    def simplifyPath(self, path: str) -> str:
        stk=[]
        sep="/"
        folders=path.split("/")
        for folder in folders:
            if folder =="." or folder == "":
                continue
            elif folder =="..":
                if len(stk)>0:
                    stk.pop()
            else:
                stk.append(folder)                
        return "/"+"/".join(stk)
        
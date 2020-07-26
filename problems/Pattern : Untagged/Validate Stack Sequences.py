class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # i keep a track of pushed elements in a stack
        stk=[]
        pushed_itr,popped_itr=0,0
        while(pushed_itr<len(pushed)):
            if len(stk)>0 and stk[-1]==popped[popped_itr]:
                stk.pop()
                popped_itr+=1
            else:
                stk.append(pushed[pushed_itr])
                pushed_itr+=1
        
        while(popped_itr<len(popped) and stk[-1]==popped[popped_itr]):
            stk.pop()
            popped_itr+=1
        
        return len(stk)==0
        
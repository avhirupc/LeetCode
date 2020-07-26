import functools 

def compare(item1,item2):
    XY=int(item1+item2)
    YX=int(item2+item1)
    return YX-XY

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        largest_number=""
        queue= [ str(e) for e in A]
        queue = sorted(queue,key=functools.cmp_to_key(compare))
        for e in queue:
            largest_number+=e
        l_n=""
        l_n=largest_number.lstrip("0")    
        if len(l_n)==0:
            return "0"
        return l_n
    

        
    
            
        

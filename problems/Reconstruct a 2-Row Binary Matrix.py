class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        l=len(colsum)
        result=[[0]*l,[0]*l]
        row_ptr=0
        for col_ptr in range(l):
            if upper>=lower:
                if  upper>0 and colsum[col_ptr]>0:
                    result[0][col_ptr]=1
                    upper=upper-1
                    colsum[col_ptr]-=1
                if lower>0 and colsum[col_ptr]>0:
                    result[1][col_ptr]=1
                    lower=lower-1
                    colsum[col_ptr]-=1
            else:
                if lower>0 and colsum[col_ptr]>0:
                    result[1][col_ptr]=1
                    lower=lower-1
                    colsum[col_ptr]-=1
                if  upper>0 and colsum[col_ptr]>0:
                    result[0][col_ptr]=1
                    upper=upper-1
                    colsum[col_ptr]-=1
            col_ptr+=1
        if not all([cs==0 for cs in colsum]) or upper >0 or lower>0 :
            return []
        return result

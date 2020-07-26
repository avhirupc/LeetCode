class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        J=set(J)
        for s in S:
            count+= 1 if s in J else 0
        return count
        
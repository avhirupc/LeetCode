import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            y=int(str(x)[::-1])
        else:
            y= -int(str(-x)[::-1])
        if not (math.pow(-2,31)< y < math.pow(2,31)):
            return 0
        return y
        
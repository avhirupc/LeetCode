"""TLE"""
class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient=0
        quotient_sign=(dividend>=0 and divisor>=0)or (dividend<0 and divisor<0)
        temp=0
        dividend,divisor=abs(dividend),abs(divisor)
        while(dividend>=(temp+divisor)):
            quotient+=1
            temp=temp+divisor
        if quotient_sign:
            return quotient
        else:
            return 0-quotient
        
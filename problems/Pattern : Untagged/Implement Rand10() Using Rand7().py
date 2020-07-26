# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num=11
        while(num>10):
            num = 7*(rand7()-1)+rand7()
        return num

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num=41
        while(num>40):
            num = 7*(rand7()-1)+rand7()
        return num%10+1
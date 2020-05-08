class Solution:
    def findComplement(self, num: int) -> int:
        bin_repr="{0:b}".format(num)
        complement="".join(["0" if c=='1' else "1" for c in bin_repr])
        return int(complement,2)
        
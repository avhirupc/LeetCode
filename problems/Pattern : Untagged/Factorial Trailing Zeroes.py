class Solution:
    def trailingZeroes(self, n: int) -> int:
        #find power of 5 in prime factorization
        num_to_divide=5
        power_of_5=0
        while(n >= num_to_divide):
            power_of_5+=(n//num_to_divide)
            num_to_divide=num_to_divide*5
        
        return power_of_5
        
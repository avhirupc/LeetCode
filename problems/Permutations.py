class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        def generate(p,nums,permutations):
            if len(nums)==0:
                permutations.append(p)
                return 
            for num in nums:
                temp=[n for n in nums if n!=num]
                generate(p+[num],temp,permutations) 
        
        generate([],nums,permutations)
        return permutations
            
            
        
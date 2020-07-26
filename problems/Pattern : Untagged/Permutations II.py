class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations={}
        def generate(p,nums,permutations):
            if len(nums)==0:
                permutations[str(p)]=p
                return 
            for ind in range(0,len(nums)):
                val=nums.pop(ind)
                generate(p+[val],nums,permutations)
                nums.insert(ind,val)
        
        generate([],nums,permutations)
        return list(permutations.values())
                

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        nums=sorted(nums)
        def generate(p,nums,permutations):
            if len(nums)==0:
                permutations.append(p)
                return 
            for ind in range(0,len(nums)):
                if ind!=0 and nums[ind]==nums[ind-1]:
                    continue
                val=nums.pop(ind)
                generate(p+[val],nums,permutations)
                nums.insert(ind,val)
        
        generate([],nums,permutations)
        return permutations
                
        
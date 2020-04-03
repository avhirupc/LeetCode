"""TLE"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets={}
        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums):
                for k,n3 in enumerate(nums):
                    if i<j<k:
                        if n1+n2+n3==0:
                            triplets[str(sorted([n1,n2,n3]))]=[n1,n2,n3]
        return list(triplets.values())
        

"""TLE"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set=[]
        unique_res=set([])
        for itr,val in enumerate(nums):
            tgt=0-val
            mem=set([])
            j=itr+1
            while(j<len(nums)):
                if nums[j] in mem:
                    triplet=sorted([val,nums[j],tgt-nums[j]])
                    if str(triplet) not in unique_res:
                        result_set.append(triplet)
                        unique_res.add(str(triplet))
                else:
                    mem.add(tgt-nums[j])
                j+=1
        return result_set



"""Correct Solution"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set=[]
        nums=sorted(nums)
        
        for ind,val in enumerate(nums):
        
            if ((ind==0 or (nums[ind]!=nums[ind-1])) and ind<len(nums)-2):
                sum=0-nums[ind]
                low_ind=ind+1
                high_ind=len(nums)-1
                while(low_ind<high_ind):
                    if (nums[low_ind]+nums[high_ind]==sum):
                        result_set.append([nums[ind],nums[low_ind],nums[high_ind]])
                        while(nums[low_ind]==nums[low_ind+1] and low_ind<len(nums)-2):
                            low_ind+=1
                        while(nums[high_ind]==nums[high_ind-1] and high_ind>=0):
                            high_ind-=1
                        low_ind+=1
                        high_ind-=1
                    elif (nums[low_ind]+nums[high_ind]<sum):
                        low_ind+=1
                    else:
                        high_ind-=1
        
        return result_set
                            
                
                
                
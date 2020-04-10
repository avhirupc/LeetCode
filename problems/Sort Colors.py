class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # I m looking to divide the array into three segments
        # 0 , 1 , 2
        # i have two variables with specify the boundary of 0-1 and 1-2
        # Iterating through the list i , move them in appropriate boundary and update boundary
        # when iteration reaches boundary 2 then done
        bound_1,bound_2=0,len(nums)
        itr=0
        while(itr<bound_2):
            if nums[itr]==0:
                del nums[itr]
                nums.insert(bound_1,0)
                bound_1+=1
                itr=bound_1
            elif nums[itr]==2:
                del nums[itr]
                nums.insert(bound_2,2)
                bound_2-=1
            elif nums[itr]==1:
                itr+=1
            #if num at itr 1 is 0 then insert at bound_1 and increment bound_1
            # if num at itr 2 is 2 then i insert at bound_2 and decrement bound_2
            # if num is 1 i move on as it is already in correct segment
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = 0,0
        while(ptr1< m and ptr2 < n):
            if nums1[ptr1] <= nums2[ptr2]:
                ptr1+=1
            else:
                tmpptr=len(nums1)-2
                while(tmpptr>= ptr1):
                    nums1[tmpptr+1]=nums1[tmpptr]
                    tmpptr-=1
                nums1[ptr1] = nums2[ptr2]
                ptr2+=1
                ptr1+=1
                m +=1
        
        while(ptr2< n):
            nums1[ptr1]=nums2[ptr2]
            ptr1+=1
            ptr2+=1
            
        
                
                
                
        
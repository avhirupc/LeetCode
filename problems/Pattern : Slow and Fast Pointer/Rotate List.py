# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # find the length of the list
        # k = k%len
        # take two pointers, fast and slow. 
        # start slow pointer when fast is at k distance
        # make slow ptr next as next head. slow ptr next as null, and fast ptr next as old head
        # done
        if not head:
            return 
        
        llen=0
        ptr=head
        while(ptr):
            ptr=ptr.next
            llen+=1
        
        k=k%llen
        if k==0:
            return head
        
        fptr,sptr=head,head
        dist_cntr=0
        while(dist_cntr<k and fptr):
            fptr=fptr.next
            dist_cntr+=1
        
        while(fptr.next):
            fptr=fptr.next
            sptr=sptr.next
            
        new_head=sptr.next
        sptr.next=None
        fptr.next=head
        return new_head
        
        
        
            
        
        
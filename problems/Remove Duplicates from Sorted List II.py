# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        counter=defaultdict(int)
        itr=head
        
        while(itr):
            counter[itr.val]+=1
            itr=itr.next
        
        while(head and counter[head.val]>1):
            head=head.next
        if not head:
            return head
        
        prev=head
        itr=head.next
        while(itr):
            while(itr and counter[itr.val]>1):
                itr=itr.next
            prev.next=itr
            prev=itr
            if itr:
                itr=itr.next 
        return head
                
            
        
        
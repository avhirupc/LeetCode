# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        itr=head
        while(itr):
            #if next element is same value to move to usaka next
            while(itr.next and itr.val == itr.next.val):
                itr.next=itr.next.next
            itr=itr.next
        return head
                
            
        
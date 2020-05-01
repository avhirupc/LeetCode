# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # swap the head, and move forth
        if not head:
            return head
        prev,next=head,head.next
        if not next:
            return head
        # swapping head
        prev.next= next.next
        next.next=prev
        head=next
        pprev=prev
        prev=prev.next
        if not prev:
            return head
        next=prev.next
        while(prev and next):
            prev.next= next.next
            next.next=prev
            pprev.next=next
            pprev=prev
            prev=prev.next
            if not prev:
                break
            next=prev.next
        
        return head
        
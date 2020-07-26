# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev=None
        fast_ptr=head
        slow_ptr=head
        while(n>0):
            fast_ptr=fast_ptr.next
            n=n-1
        if fast_ptr is None:
            head=head.next
            return head
        fast_ptr=fast_ptr.next
        slow_ptr=slow_ptr.next
        prev=head
        while(fast_ptr is not None):
            fast_ptr=fast_ptr.next
            slow_ptr=slow_ptr.next
            prev=prev.next
        prev.next=slow_ptr.next
        return head
        
"""Remove Nth Node From End of List"""
"Wrong Answer"
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast_ptr=head
        slow_ptr=head
        while(fast_ptr.next is not None and n>0):
            fast_ptr=fast_ptr.next
            n-=1
        while(fast_ptr.next is not None):
            fast_ptr=fast_ptr.next
            slow_ptr=slow_ptr.next
        if slow_ptr is not None :
            slow_ptr.next=slow_ptr.next.next if slow_ptr.next is not None else None
            return head
        else:
            head=head.next
            return head
            
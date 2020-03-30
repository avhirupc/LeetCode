# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val<=l2.val:
            head=ListNode(l1.val)
            prev=head
            l1=l1.next
        else :
            head=ListNode(l2.val)
            prev=head
            l2=l2.next
        while(l1 and l2):
            if l1.val<=l2.val:
                curr=ListNode(l1.val)
                l1=l1.next
                prev.next=curr
                prev=curr
            else:
                curr=ListNode(l2.val)
                l2=l2.next
                prev.next=curr
                prev=curr
        while(l1):
            curr=ListNode(l1.val)
            l1=l1.next
            prev.next=curr
            prev=curr
        while(l2):
            curr=ListNode(l2.val)
            l2=l2.next
            prev.next=curr
            prev=curr
        return head
                
            
        
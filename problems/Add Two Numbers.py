# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flg=0
        head=ListNode((l1.val+l2.val)%10)
        ptr=head
        c=(l1.val+l2.val)//10
        l1=l1.next
        l2=l2.next
        
        while(l1 is not None and l2 is not None):
            val=(l1.val+l2.val+c)%10
            c=(l1.val+l2.val+c)//10
            tmp=ListNode(val)
            ptr.next=tmp
            ptr=tmp
            l1=l1.next
            l2=l2.next
            
        while(l1 is not None):
            val=(l1.val+c)%10
            c=(l1.val+c)//10
            tmp=ListNode(val)
            ptr.next=tmp
            ptr=tmp
            l1=l1.next
            
        while(l2 is not None):
            val=(l2.val+c)%10
            c=(l2.val+c)//10
            tmp=ListNode(val)
            ptr.next=tmp
            ptr=tmp
            l2=l2.next
        if c!=0:
            tmp=ListNode(c)
            ptr.next=tmp
        return head
            
            
            
        
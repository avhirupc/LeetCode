# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val ==val and not head.next:
            return None
        #get the new head
        ptr=head
        while(ptr and ptr.val==val):
            ptr=ptr.next
        head = ptr
        
        if not head:
            return head
        
        prev=head
        ptr=head.next
            
        while(ptr):
            if ptr.val==val:
                prev.next=ptr.next
            else:
                prev=ptr
            ptr=ptr.next
        
        return head    

#Recursive solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        next = self.removeElements(head.next,val)
        if head.val == val : return next
        head.next = next
        return head
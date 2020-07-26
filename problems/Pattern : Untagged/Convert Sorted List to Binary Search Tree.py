# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        
        mid=self.find_mid(head)
        left_list=self.create_list(head,mid)
        right_list=mid.next
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(left_list)
        root.right=self.sortedListToBST(right_list)
        return root
    
    def find_mid(self,head: ListNode):
        if head is None or head.next is None:
            return head
        
        slw_ptr=head
        fst_ptr=head
        while(fst_ptr and fst_ptr.next):
            slw_ptr=slw_ptr.next
            fst_ptr=fst_ptr.next.next
        
        return slw_ptr
    
    def create_list(self, head: ListNode, mid: ListNode):
        itr=head
        while(itr.next!=mid):
            itr=itr.next
        itr.next=None
        return head
            
            
        
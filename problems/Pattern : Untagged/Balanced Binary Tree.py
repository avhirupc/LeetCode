# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        left_height=self.get_height(root.left)
        right_height=self.get_height(root.right)
        
        if abs(left_height-right_height)>1:
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    
    def get_height(self,node: TreeNode)-> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        
        return 1+ max(self.get_height(node.left),self.get_height(node.right))
        
        
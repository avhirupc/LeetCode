# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        if root is None:
            if sum==0:
                return True
            else:
                return False
        
        """
        if not root:
            return False
        if root.val ==sum and not(root.left or root.right):
            return True
        if root.val !=sum and not(root.left or root.right):
            return False
        
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val) 
        
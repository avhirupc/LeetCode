# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth=1
        return self.maxDepthUtil(root,depth)
    
    def maxDepthUtil(self,root,depth):
        if not root:
            return 0
        if not root.left and not root.right:
            return depth
        L,R=0,0
        if root.left:
            L= self.maxDepthUtil(root.left,depth+1)
        if root.right:
            R= self.maxDepthUtil(root.right,depth+1)
        return max(L,R)
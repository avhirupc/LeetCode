# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal=[]
        self.inorderTraversalUtil(root,traversal)
        return traversal
    
    def inorderTraversalUtil(self,root,traversal):
        if root is None:
            return 
        self.inorderTraversalUtil(root.left,traversal)
        traversal.append(root.val)
        self.inorderTraversalUtil(root.right,traversal)
        
        
        
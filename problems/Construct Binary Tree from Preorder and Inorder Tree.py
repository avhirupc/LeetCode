#Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        if isinstance(preorder,int):
            return TreeNode(preorder)

        root=preorder[0]
        pos_in_inorder=inorder.index(root)
        left_inorder=inorder[:pos_in_inorder]
        right_inorder=inorder[pos_in_inorder+1:]
        
        left_preorder=preorder[1:len(left_inorder)+1] 
        right_preorder=preorder[len(left_inorder)+1:] 
        
        # construct tree
        root=TreeNode(root)
        root.left=self.buildTree(left_preorder,left_inorder)
        root.right=self.buildTree(right_preorder,right_inorder)
        return root
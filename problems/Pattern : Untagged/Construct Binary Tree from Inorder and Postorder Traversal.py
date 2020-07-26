# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        tree = self.buildTreeUtil(inorder,postorder)
        return tree
    
    def buildTreeUtil(self,inorder,postorder):
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return TreeNode(inorder[0])
        
        root_val = postorder[-1] 
        root_pos = inorder.index(root_val)
        io_lst = inorder[:root_pos]
        io_rst = inorder[root_pos+1:]
        
        po_lst = postorder[:root_pos]
        po_rst = postorder[root_pos:-1]
        
        root = TreeNode(root_val)
        root.left = self.buildTreeUtil(io_lst,po_lst)
        root.right = self.buildTreeUtil(io_rst,po_rst)
        
        return root
        
        
        
        
        
        
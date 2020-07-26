# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum=[0]
        self.rangeSumBSTUtil(root,L,R,sum)
        return sum[0]
    
    def rangeSumBSTUtil(self, root: TreeNode, L: int, R: int, sum: List[int]) -> int:
        if not root:
            return
        if root.val< L :
            self.rangeSumBSTUtil(root.right,L,R,sum)
            return
        if root.val> R:
            self.rangeSumBSTUtil(root.left,L,R,sum)
            return
        
        sum[0]+=root.val
        
        self.rangeSumBSTUtil(root.left,L,R,sum)
        self.rangeSumBSTUtil(root.right,L,R,sum)
        
            
        
    
        
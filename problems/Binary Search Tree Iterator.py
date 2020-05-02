# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root):
    if not root:
        return []
    if not(root.left or root.right):
        return [root.val]
    return inorder(root.left)+[root.val]+inorder(root.right)

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder=inorder(root)
        self.curr_pos=0
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.curr_pos+=1
        return self.inorder[self.curr_pos-1]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.curr_pos<len(self.inorder):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
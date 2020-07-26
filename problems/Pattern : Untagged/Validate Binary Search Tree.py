"""Validate Binary Search Tree"""
""TLE""
class Solution(object):
    
    def findMax(self,root):
        if root.left is None and root.right is None:
            return root.val
        max_=root.val
        if root.left is not None and self.findMax(root.left)>max_:
            max_=self.findMax(root.left)
        if root.right is not None and self.findMax(root.right)>max_:
            max_=self.findMax(root.right)
        return max_
    
    def findMin(self,root):
        if root.left is None and root.right is None:
            return root.val
        min_=root.val
        if root.left is not None and self.findMin(root.left)<min_:
            min_=self.findMin(root.left)
        if root.right is not None and self.findMin(root.right)<min_:
            min_=self.findMin(root.right)
        return min_
    
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is not None and self.findMax(root.left)>=root.val:
            return False
        if root.right is not None and self.findMin(root.right)<=root.val:
            return False
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        return True


"""Correct Solution"""
INT_MAX = 4294967296
INT_MIN = -4294967296
class Solution(object):
    
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTUtil(root,INT_MIN,INT_MAX)
    
    def isValidBSTUtil(self,root,min_,max_):
        if root is None:
            return True
        if root.val<min_ or root.val>max_:
            return False
        if  not self.isValidBSTUtil(root.left,min_,root.val-1):
            return False
        if  not self.isValidBSTUtil(root.right,root.val+1,max_):
            return False
        return True
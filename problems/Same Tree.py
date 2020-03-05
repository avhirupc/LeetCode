class Solution(object):
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        
        if p is not None and q is not None:
            if p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
        return False
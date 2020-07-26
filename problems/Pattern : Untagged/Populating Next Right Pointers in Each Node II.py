"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return root
        if not(root.left or root.right):
            return root
        
        def helper(c):
            while(c and not(c.left or c.right)):
                c=c.next
            if c:
                return c.left or c.right
                
        
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = helper(root.next)
        if root.right:
            root.right.next = helper(root.next)
            
        self.connect(root.right)
        self.connect(root.left)
        
        return root
        
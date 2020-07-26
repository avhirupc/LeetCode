"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev=None
        queue=deque([(root,1)])
        curr_level=1
        while(queue):
            node,level=queue.popleft()
            if not node:
                break
            if level!=curr_level:
                curr_level=level
                prev=None
            node.next=prev
            prev=node
            if node.right:
                queue.append((node.right,curr_level+1))
            if node.left:
                queue.append((node.left,curr_level+1))
        return root
        
        
Recursive 
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return root
        if not(root.left or root.right):
            return root

        root.left.next=root.right
        if root.next:
            root.right.next=root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
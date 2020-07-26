# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue=deque()
        queue.append((root,1))
        curr_level=1
        result,tmp=[],[]
        while(queue):
            node,level=queue.popleft()
            if level==curr_level:
                tmp.append(node.val)
            else:
                curr_level+=1
                result.append(tmp)
                tmp=[node.val]
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        result.append(tmp)

        
        return result[::-1]
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=[root,"lc"]
        level_order,temp=[],[]
        while(len(queue)!=1):
            node = queue.pop(0)
            if node!='lc':
                if node is not None:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            else:
                level_order.append(temp)
                temp=[]
                queue.append("lc")
        return level_order
            
            
        
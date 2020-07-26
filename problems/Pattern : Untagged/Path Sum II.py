# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        results=[]
        path=[]
        def util(node,sum,path,results):
            if node is None:
                path=[]
                return
            if not(node.left or node.right):
                if node.val==sum:
                    path.append(node.val)
                    results.append(path)
                    path=[]
                else:
                    path=[]
            util(node.left,sum-node.val,path+[node.val],results)
            util(node.right,sum-node.val,path+[node.val],results)
            
        util(root,sum,path,results)
        return results
            
            
                
        
        
        
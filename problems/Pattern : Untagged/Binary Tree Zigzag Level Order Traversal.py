# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        zig_zag_order,temp=[],[]
        flg=0
        q1,q2=[root,"lc"],[]
        while(True):
            if len(q1)==1 and q1[0]=='lc' and len(q2)==0:
                break
            if len(q2)==1 and q2[0]=='lc' and len(q1)==0:
                break
            
            if flg==0:
                node=q1.pop(0)
                if node!='lc' and node is not None:
                    temp.append(node.val)
                    q2.insert(0,node.left)
                    q2.insert(0,node.right)
                elif node=='lc':
                    zig_zag_order.append(temp)
                    temp=[]
                    q2.append("lc")
                    flg= 1
            else:
                node=q2.pop(0)
                if node!='lc' and node is not None:
                    temp.append(node.val)
                    q1.insert(0,node.right)
                    q1.insert(0,node.left)
                elif node=='lc':
                    zig_zag_order.append(temp)
                    temp=[]
                    q1.append("lc")
                    flg= 0
        return zig_zag_order

        
        
        
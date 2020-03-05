class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_set = []
        if root==None:
            return result_set
        que = deque([root,"flg1"])
        tmp=[]
        cntr=0
        while(len(que)!=1):
            node=que.popleft()
            if node !="flg1" and cntr==0:
                if node.left!=None:
                    que.append(node.left)
                if node.right!=None:
                    que.append(node.right)
                tmp.append(node.val)
            if node !="flg1" and cntr==1:
                if node.right!=None:
                    que.append(node.right)
                if node.left!=None:
                    que.append(node.left)
                tmp.append(node.val)
            if node == "flg1":
                que = deque(reversed(que))
                que.append("flg1")
                cntr =0 if cntr==1 else 1
                result_set.append(tmp)
                tmp=[]
        result_set.append(tmp)
        return result_set        
        
        
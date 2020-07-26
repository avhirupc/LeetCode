"""TLE"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nodes=range(1,n+1)
        num_of_trees=self.numTreesUtil(nodes)
        return num_of_trees
    
    def numTreesUtil(self,nodes):
        num_of_trees=0
        if len(nodes) in [0,1]:
            return 1
        for root in nodes:
            left_nodes=nodes[:nodes.index(root)]
            right_nodes=nodes[nodes.index(root)+1:]
            possible_trees=self.numTreesUtil(left_nodes)*self.numTreesUtil(right_nodes)
            num_of_trees+=possible_trees
        return num_of_trees
            
"""Correct"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory=[0]*(n+1)
        memory[0]=1
        memory[1]=1
        for num_of_nodes in range(2,n+1):
            for root_node in range(num_of_nodes):
                left_count=root_node
                right_count=num_of_nodes-left_count-1
                memory[num_of_nodes]+=(memory[left_count]*memory[right_count])
        return memory[n] 
    
        

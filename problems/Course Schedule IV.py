from collections import defaultdict

def make_graph(numCourses,prerequisites):
    graph=defaultdict(list)
    for node in range(numCourses):
        for pair in prerequisites:
            if pair[0]==node:
                graph[node].append(pair[1])
    return graph

    
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = make_graph(n,prerequisites)
        for node in range(n):
            if node not in graph:
                graph[node]=[]
        mem={}
        for node in list(graph.keys()):
            mem[node]=self.dfs(node,graph,[False]*n)
        res=[]
        for query in queries:
            if query[1] in mem[query[0]]:
                res.append(True)
            else:
                res.append(False)
        return res
        #check all queries
        
    def dfs(self,start,graph,visited):
        if visited[start]:
            return []
        visited[start]=True
        k=[]
        for neighbour in graph[start]:
            k+=self.dfs(neighbour,graph,visited)
        return [start]+k
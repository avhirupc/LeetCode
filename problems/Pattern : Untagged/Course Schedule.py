from collections import defaultdict

def make_graph(numCourses,prerequisites):
    graph=defaultdict(list)
    for node in range(numCourses):
        for pair in prerequisites:
            if pair[1]==node:
                graph[node].append(pair[0])
    return graph
    
def detect_cycle(start,graph,visited,recstk):
    if visited[start] and recstk[start]:
        return True
    recstk[start]=True
    visited[start]=True
    for neighbour in graph[start]:
        if detect_cycle(neighbour,graph,visited,recstk):
            return True
    recstk[start]=False  
    return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=make_graph(numCourses,prerequisites)
        visited=[False]*numCourses
        recstk=[False]*numCourses
        for node in range(numCourses):
            
            if not visited[node] and detect_cycle(node,graph,visited,recstk):
                return False
        
        return True
        
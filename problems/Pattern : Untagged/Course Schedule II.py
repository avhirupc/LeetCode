from collections import defaultdict

def make_graph(numCourses,prerequisites):
    graph=defaultdict(list)
    for node in range(numCourses):
        for pair in prerequisites:
            if pair[1]==node:
                graph[node].append(pair[0])
    return graph

def topSort(start,graph,visited,recstk,stk):
    if start in visited:
        if recstk[start]:
            raise Exception("Cycle Detected")
        else:
            return
    
    visited.add(start)
    recstk[start]=True
    
    for neighbour in graph[start]:
        topSort(neighbour,graph,visited,recstk,stk)
    recstk[start]=False
    stk.append(start)
    

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = make_graph(numCourses,prerequisites)
        visited=set([])
        recstk=[False]*numCourses
        stk=[]
        try:
            for node in range(numCourses):
                if node not in visited:
                    topSort(node,graph,visited,recstk,stk)
        except:
            return []
        return stk[::-1]
                
        
        
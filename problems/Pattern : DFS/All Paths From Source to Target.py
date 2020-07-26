class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        all_paths = []
        src = 0
        target = len(graph)-1
        visited = [False]*len(graph)
        visited[src]=True
        path = [src]
    
        def allPathsSourceTargetUtil(graph,src, target,visited, path):
            
            if src == target :
                #nonlocal all_paths
                all_paths.append(path[:])
                #print(path,all_paths, src,target)
                return 

            for neighbour in graph[src]:
                if not visited[neighbour]:
                    path.append(neighbour)
                    visited[neighbour]=True
                    allPathsSourceTargetUtil(graph, neighbour, target, visited, path)
                    path.pop()
                    visited[neighbour]=False

            return 


    
        allPathsSourceTargetUtil(graph,src, target,visited, path)
        
        
        return all_paths
    
        
        
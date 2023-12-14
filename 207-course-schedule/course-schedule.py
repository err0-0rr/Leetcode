class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        
        for i,j in prerequisites:
            graph[i].append(j)
            
        def circle(v):
            visited[v]=True
            rec[v]=True
            for i in graph[v]:
                if not visited[i]:
                    if circle(i):
                        return True
                elif rec[i]:
                    return True
            rec[v]=False
            return False
        visited=[False]*numCourses
        rec=[False]*numCourses
        
        for i in graph.keys():
            if not visited[i]:
                if circle(i):
                    return False
        return True
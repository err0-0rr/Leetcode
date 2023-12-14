class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union find
        n=len(edges) #equal to number of nodes as there would be no repeating edges
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1) #length of subtree
        
        def findParent(v):
            p=parent[v]
            
            while p!=parent[p]:
                parent[p]=parent[parent[p]]
                p=parent[p]
            return p
        
        def union(a,b):
            p1,p2= findParent(a), findParent(b)
            if p1==p2:
                return True #circle formed
            
            elif rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                parent[p2]=p1
            else:
                rank[p2]+=rank[p1]
                parent[p1]=p2
                
            return False
        
        for a,b in edges:
            if union(a,b):
                return [a,b]
        return []
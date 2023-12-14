class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return x[0]*x[0]+x[1]*x[1]
        
        h=[]
        for i,a in enumerate(points):
            heapq.heappush(h, (-1*dist(a), i))
            if len(h)>k:
                heapq.heappop(h)
        for i,a in enumerate(h):
            h[i]=points[a[1]]
        return h
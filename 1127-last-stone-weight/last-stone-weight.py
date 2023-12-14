class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=list(map(lambda x:-1*x, stones))
        heapq.heapify(h)
        while len(h)>1:
            temp=heapq.heappop(h)-heapq.heappop(h)
            if temp<0:
                heapq.heappush(h, temp)
        if h:
            return -1*h[0]
        return 0
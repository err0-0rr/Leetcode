class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        self.ls=nums
        
    def add(self, val: int) -> int:
        heapq.heappush(self.ls, val)
        if len(self.ls)>self.k:
            heapq.heappop(self.ls)
        return self.ls[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
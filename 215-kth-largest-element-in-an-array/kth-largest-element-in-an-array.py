class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for i in range(k):
            heapq.heappush(h, nums[i])
        for i in range(k, len(nums)):
            heapq.heappush(h, nums[i])
            heapq.heappop(h)
            
        return heapq.heappop(h)
        
        
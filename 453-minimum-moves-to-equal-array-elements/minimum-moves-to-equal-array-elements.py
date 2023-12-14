class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mini=min(nums)
        ans=0
        for i in nums:
            ans+=(i-mini)
        return ans
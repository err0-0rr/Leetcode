class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = cur = 0
        for i in nums[::-1]:
            if i > cur:
                ans = max(ans, cur)
                cur = i
            else: cur += i
        return max(ans,cur)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans=0
        for i in range(1, len(height)-1):
            ans+=max(0, min(max(height[:i]), max(height[i+1:]))-height[i])
        return ans
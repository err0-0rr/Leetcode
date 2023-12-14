class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        ans=0
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i], 1+dp[j])
            ans=max(ans, dp[i])
        return ans
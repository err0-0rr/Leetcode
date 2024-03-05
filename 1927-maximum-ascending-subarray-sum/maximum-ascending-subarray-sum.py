class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=0
        temp_sum=nums[0]
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                temp_sum+=nums[i]
            else:
                ans=max(ans, temp_sum)
                temp_sum=nums[i]
                
        return max(ans, temp_sum)
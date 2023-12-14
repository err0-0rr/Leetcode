class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=max(nums)
        if ans<0:
            return ans
        c=0
        for i in nums:
            if c+i>=0:
                c+=i
            else:
                c=0
            ans=max(ans, c)
        return ans
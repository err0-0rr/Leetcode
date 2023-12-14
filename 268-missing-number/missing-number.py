class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t=0
        s=0
        for i in range(len(nums)):
            t^=(i+1)
            s^=nums[i]
        return t^s
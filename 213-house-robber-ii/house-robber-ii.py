class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        a,b=nums[0],max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            a,b=b,max(a+nums[i], b)
        temp=max(a,b)
        a,b=0,nums[1]
        for i in range(2, len(nums)):
            a,b=b,max(a+nums[i], b)
        return max(temp, a, b)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ans=nums.index(max(nums))
        for i in range(2):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        if nums[-1]>=(2*nums[-2]):
            return ans
        return -1
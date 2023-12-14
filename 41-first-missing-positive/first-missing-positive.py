class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp=set(nums)
        maxi=max(nums)
        for i in range(1, maxi):
            if i not in temp:
                return i
        if maxi<0:
            return 1
        return maxi+1
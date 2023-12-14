class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def util(a, i):
            if (a,i) in dp:
                return dp[(a,i)]
            if i ==len(nums):
                if a==target:
                    return 1
                return 0
            dp[(a,i)]=util(a-nums[i], i+1)+util(a+nums[i], i+1 )
            return dp[(a,i)]
        
        return util(0, 0)
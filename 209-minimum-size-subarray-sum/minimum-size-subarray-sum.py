class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        n=len(nums)
        l,r=0,0
        tot=0
        while r<n:
            if tot<target and r<n:
                tot+=nums[r]
                r+=1
            while tot>=target:
                #print(l,r)
                ans=min(ans, r-l)
                tot-=nums[l]
                l+=1
        if ans==float("inf"):
            return 0
        return ans
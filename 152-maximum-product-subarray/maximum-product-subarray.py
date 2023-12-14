class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=max(nums)
        mini=maxi=1
        for i in nums:
            if i==0:
                mini=maxi=1
                continue
            ls=[mini*i, maxi*i, i]
            mini,maxi=min(ls), max(ls)
            ans=max(ans, maxi)
            
        return ans
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(set(nums))
        tot=len(nums)
        ans=0
        
        for i in range(tot):
            s=set()
            for j in range(i, tot):
                s.add(nums[j])
                if len(s)==n:
                    ans+=(tot-j)
                    break
        
        return ans
            
        
        return util(0, set())
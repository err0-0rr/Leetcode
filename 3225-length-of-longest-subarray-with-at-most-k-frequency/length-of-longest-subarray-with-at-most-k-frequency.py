class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=0
        l=r=0
        dic={}
        while r<len(nums):
            if nums[r] in dic:
                if dic[nums[r]]<k:
                    dic[nums[r]]+=1
                    r+=1
                    ans=max(ans, r-l)
                    
                else:
                    while nums[l]!=nums[r]:
                        dic[nums[l]]-=1
                        l+=1
                        
                    l+=1
                    r+=1
            else:
                dic[nums[r]]=1
                r+=1
                ans=max(ans, r-l) 
        return ans
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        t,dic=0,{0:-1}
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                t+=-1
            else:
                t+=1
            
            try:
                diff=i-dic[t]
                ans=max(ans,diff)
            except:
                dic[t]=i
        return ans
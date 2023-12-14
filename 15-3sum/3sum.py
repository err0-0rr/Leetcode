class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        n=len(nums)
        #print(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            while k>j:
                tot=nums[i]+nums[j]+nums[k]
                if tot==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif tot>0:
                    k-=1
                else:
                    j+=1
        res=list(res)
        res=[list(i) for i in res]
        return res
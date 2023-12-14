class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        ans=(n+1)*(10**4)
        ret=4*(10**4)
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                tot=(nums[i]+nums[j]+nums[k])
                res=abs(tot-target)
                if tot<target:
                    j+=1
                else:
                    k-=1
                if res<=ans:
                    ret=tot
                    ans=res
        return ret
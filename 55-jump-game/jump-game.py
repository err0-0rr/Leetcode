class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        if n==0:
            return True
        maxi=nums[0]
        i=1
        while i<=maxi:
            if maxi>=n:
                return True
            maxi=max(maxi, i+nums[i])
            #print(maxi, i)
            i+=1
        return False
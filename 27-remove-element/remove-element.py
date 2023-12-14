class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        ans=0
        while i<j:
            if nums[i]==val:
                while j>=0 and nums[j]==val:
                    j-=1
                if i<j:
                    nums[i]=nums[j]
                else:
                    break
                i+=1
                j-=1
                ans+=1
            else:
                ans+=1
                i+=1
        if i==j and nums[i]!=val:
            ans+=1
        return ans
            
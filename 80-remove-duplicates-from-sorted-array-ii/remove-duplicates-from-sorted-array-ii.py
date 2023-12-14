class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        ans=0
        cur=10**5
        flag=False
        ls=[]
        while i<len(nums):
            if nums[i]!=cur:
                ans+=1
                cur=nums[i]
                ls.append(cur)
                flag=False
            else:
                if not flag:
                    ans+=1
                    ls.append(cur)
                    flag=True
            i+=1
        for i in range(ans):
            nums[i]=ls[i]
        return ans
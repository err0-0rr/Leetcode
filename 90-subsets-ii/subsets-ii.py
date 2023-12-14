class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def util(i=0, ls=[]):
            if i>len(nums):
                return
            if ls not in ans:
                ans.append(ls)
            for j in range(i, len(nums)):
                util(j+1, ls+[nums[i]])
                util(j+1, ls)
        ans=[]
        nums.sort()
        util()
        return ans
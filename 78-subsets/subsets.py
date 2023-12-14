class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def util(ls=[], i=0):
            ans.append(ls)
            for i in range(i, len(nums)):
                ls.append(nums[i])
                util(ls.copy(), i+1)
                ls.pop()
        util()
        return ans
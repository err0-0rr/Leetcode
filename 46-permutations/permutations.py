class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ls=[]
        def util(ans, rem):
            if not rem:
                ls.append(ans)
                return
            for i in range(len(rem)):
                util(ans+[rem[i]], rem[:i]+rem[i+1:])
        util([], nums.copy())
        return ls
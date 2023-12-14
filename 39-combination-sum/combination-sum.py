class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def util(n, l, j, ls):
            if n==0:
                ans.append(ls)
            if n<0:
                return
            for i in range(j, l):
                util(n-candidates[i], l, i, ls+[candidates[i]])
        util(target, len(candidates), 0, [])
        return ans
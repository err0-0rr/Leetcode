class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def util(n, l, j, ls):
            if n==0:
                ans.add(tuple(ls))
            if n<0:
                return
            i=j
            while i<l:
                flag=True
                util(n-candidates[i], l, i+1, ls+[(candidates[i])])
                while i+1<l-1 and candidates[i]==candidates[i+1]:
                    i+=1
                    flag=False
                if flag:
                    i+=1
                
        candidates.sort()
        util(target, len(candidates), 0, [])
        return list(list(i) for i in ans)
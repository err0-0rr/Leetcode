class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        def util(x):
            t=0
            while x:
                t+=x%2
                x>>=1
                if ans[x]!=0:
                    t+=ans[x]
                    break
            return t
        for i in range(n+1):
            ans[i]=util(i)
        return ans
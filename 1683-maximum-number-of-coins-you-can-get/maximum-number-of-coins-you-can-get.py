class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        n=len(piles)-2
        c=n//3
        ans=0
        while c>=0:
            ans+=piles[n]
            n-=2
            c-=1
        return ans
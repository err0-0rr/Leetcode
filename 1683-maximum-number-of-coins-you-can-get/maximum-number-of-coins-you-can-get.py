class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)-2
        c=n//3
        ans=0
        for _ in range(c+1):
            ans+=piles[n]
            n-=2
        return ans
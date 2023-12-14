class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)-2
        ans=0
        for i in range(n, (n//3)-1, -2):
            ans+=piles[i]
        return ans
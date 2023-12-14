class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)-2
        c=n//3
        ans=0
        for i in range(len(piles)-2, (n//3)-1, -2):
            ans+=piles[i]
        return ans
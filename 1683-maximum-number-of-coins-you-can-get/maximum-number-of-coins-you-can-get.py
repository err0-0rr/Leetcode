class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        for i in range(len(piles)-2, ((len(piles)-2)//3)-1, -2):
            ans+=piles[i]
        return ans
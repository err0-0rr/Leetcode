class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a=cost[0]
        b=cost[1]
        for i in range(2, len(cost)):
            a,b=b,min(a, b)+cost[i]
        return min(a,b)

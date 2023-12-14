class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for idx, val in enumerate(dp):
            for i in coins:
                if idx-i>=0:
                    dp[idx]=min(dp[idx], dp[idx-i]+1)
                    
        if dp[amount]==float("inf"):
            return -1
        return dp[amount]
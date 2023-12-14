class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for i in range(n)]for j in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    continue
                if i>0 and j>0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                elif i>0:
                    dp[i][j]=dp[i-1][j]
                elif j>0:
                    dp[i][j]=+dp[i][j-1]
        return dp[m-1][n-1]
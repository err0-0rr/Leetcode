class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        s=set()
        m=len(grid)
        n=len(grid[0])
        ans=0
        
        def dfs(i,j):
            nonlocal s
            if not (0<=i<m and 0<=j<n) or grid[i][j]==0 or (i,j) in s:
                return 0
                
            s.add((i,j))
            return 1+dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in s and grid[i][j]==1:
                    ans=max(ans, dfs(i,j))
        return ans
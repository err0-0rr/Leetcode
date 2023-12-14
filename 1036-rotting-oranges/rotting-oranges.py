class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid), len(grid[0])
        ls=[]
        for i in grid:
            temp=[]
            for j in i:
                if j==1:
                    temp.append(float("inf"))
                else:
                    temp.append(0)
            ls.append(temp)
        def bfs(i, j):
            nonlocal ls
            q=deque()
            q.append([i,j, 0])
            visited=set()
            while q:
                x,y,t=q.popleft()
                visited.add((x,y))
                if ls[x][y]<=t and grid[x][y]==1:
                    continue
                else:
                    ls[x][y]=t

                temp=[[x-1, y, t+1], [x+1, y, t+1], [x, y-1, t+1], [x,y+1, t+1]]
                for x,y,t in temp:
                    if (x,y) not in visited and 0<=x<m and 0<=y<n and grid[x][y]==1:
                        q.append([x,y,t])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    bfs(i,j)
        ans=0
        for i in ls:
            ans=max(ans, max(i))
            if ans==float("inf"):
                return -1
        return ans
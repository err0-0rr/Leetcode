class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        s=set()
        ans=0
        def bfs(x, y):
            q=deque()
            q.append((x, y))
            #print(q)
            nonlocal s
            visited=set()
            while q:
                i,j=q.popleft()
                s.add((i,j))
                a,b=i-1,j
                if (a,b) not in visited and 0<=a<m and 0<=b<n and grid[a][b]=='1':
                    q.append((a,b))
                    visited.add((a, b))
                a,b=i,j-1
                if (a,b) not in visited and 0<=a<m and 0<=b<n and grid[a][b]=='1':
                    q.append((a,b))
                    visited.add((a, b))
                a,b=i+1,j
                if (a,b) not in visited and 0<=a<m and 0<=b<n and grid[a][b]=='1':
                    q.append((a,b))
                    visited.add((a, b))
                a,b=i,j+1
                if (a,b) not in visited and 0<=a<m and 0<=b<n and grid[a][b]=='1':
                    q.append((a,b))
                    visited.add((a, b))
                
        for i in range(m):
            for j in range(n):
                if (i,j) not in s and grid[i][j]=='1':
                    ans+=1
                    bfs(i,j)
        #print(s)
        return ans